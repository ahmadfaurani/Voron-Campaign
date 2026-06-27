#!/usr/bin/env python3
"""
Sector Classification Pipeline for Malaysian Budget Intelligence
Classifies budget line items into 10 predefined sectors
"""

import pandas as pd
import re
from typing import Dict, List, Tuple
from pathlib import Path

class SectorClassifier:
    """Classify budget records into government sectors"""
    
    # Sector keyword mappings (bilingual)
    SECTOR_KEYWORDS = {
        'SEC-01': {
            'en': ['defence', 'defense', 'military', 'army', 'navy', 'air force', 'police', 'security', 'border', 'immigration'],
            'ms': ['pertahanan', 'ketenteraan', 'tentera', 'polisi', 'keselamatan', 'sempadan', 'imigresen']
        },
        'SEC-02': {
            'en': ['education', 'school', 'university', 'college', 'student', 'teacher', 'curriculum'],
            'ms': ['pendidikan', 'sekolah', 'universiti', 'kolej', 'pelajar', 'guru', 'kurikulum']
        },
        'SEC-03': {
            'en': ['health', 'hospital', 'clinic', 'medical', 'doctor', 'nurse', 'medicine', 'vaccine'],
            'ms': ['kesihatan', 'hospital', 'klinik', 'perubatan', 'doktor', 'jururawat', 'ubat', 'vaksin']
        },
        'SEC-04': {
            'en': ['infrastructure', 'road', 'bridge', 'highway', 'railway', 'airport', 'port', 'construction'],
            'ms': ['infrastruktur', 'jalan', 'jambatan', 'lebuh raya', 'kereta api', 'lapangan terbang', 'pelabuhan', 'pembinaan']
        },
        'SEC-05': {
            'en': ['economy', 'trade', 'industry', 'investment', 'export', 'import', 'commerce', 'manufacturing'],
            'ms': ['ekonomi', 'perdagangan', 'industri', 'pelaburan', 'eksport', 'import', 'perniagaan', 'pembuatan']
        },
        'SEC-06': {
            'en': ['digital', 'technology', 'IT', 'software', 'hardware', 'cyber', 'telecom', 'broadband', 'AI', 'artificial intelligence'],
            'ms': ['digital', 'teknologi', 'IT', 'perisian', 'perkakasan', 'siber', 'telekom', 'jalur lebar', 'AI', 'kecerdasan buatan']
        },
        'SEC-07': {
            'en': ['agriculture', 'farming', 'fishery', 'livestock', 'crop', 'palm oil', 'rubber', 'paddy'],
            'ms': ['pertanian', 'perikanan', 'ternakan', 'tanaman', 'sawit', 'getah', 'padi']
        },
        'SEC-08': {
            'en': ['welfare', 'social', 'poverty', 'aid', 'assistance', 'housing', 'community'],
            'ms': ['kebajikan', 'sosial', 'kemiskinan', 'bantuan', 'bantuan', 'perumahan', 'komuniti']
        },
        'SEC-09': {
            'en': ['environment', 'climate', 'forest', 'conservation', 'pollution', 'waste', 'sustainability'],
            'ms': ['alam sekitar', 'iklim', 'hutan', 'pemuliharaan', 'pencemaran', 'sisa', 'kelestarian']
        },
        'SEC-10': {
            'en': ['administration', 'government', 'public service', 'parliament', 'ministry', 'department'],
            'ms': ['pentadbiran', 'kerajaan', 'perkhidmatan awam', 'parlimen', 'kementerian', 'jabatan']
        }
    }
    
    # Agency code to sector mapping
    AGENCY_SECTOR_MAP = {
        'MINDEF': 'SEC-01', 'PDRM': 'SEC-01', 'APM': 'SEC-01', 'NACSA': 'SEC-01',
        'KPM': 'SEC-02', 'IPTA': 'SEC-02', 'IPTS': 'SEC-02',
        'KKM': 'SEC-03', 'HOSPITAL': 'SEC-03',
        'KLK': 'SEC-04', 'JKR': 'SEC-04', 'MOT': 'SEC-04',
        'MITI': 'SEC-05', 'MOF': 'SEC-05', 'MIDA': 'SEC-05',
        'MCMC': 'SEC-06', 'MAMPU': 'SEC-06', 'MYDIGITAL': 'SEC-06',
        'KPKM': 'SEC-07', 'LPP': 'SEC-07', 'FAMA': 'SEC-07',
        'KPWKM': 'SEC-08', 'JKM': 'SEC-08',
        'NRE': 'SEC-09', 'DOE': 'SEC-09',
        'JPM': 'SEC-10', 'ESA': 'SEC-10'
    }
    
    def __init__(self):
        self.sector_names = {
            'SEC-01': 'Security & Defence',
            'SEC-02': 'Education',
            'SEC-03': 'Healthcare',
            'SEC-04': 'Infrastructure',
            'SEC-05': 'Economy & Trade',
            'SEC-06': 'Digital & Technology',
            'SEC-07': 'Agriculture',
            'SEC-08': 'Social Welfare',
            'SEC-09': 'Environment',
            'SEC-10': 'General Administration'
        }
    
    def classify_by_keywords(self, text: str) -> Tuple[str, float]:
        """Classify text based on keyword matching"""
        text_lower = text.lower()
        scores = {}
        
        for sector, keywords in self.SECTOR_KEYWORDS.items():
            en_matches = sum(1 for kw in keywords['en'] if kw in text_lower)
            ms_matches = sum(1 for kw in keywords['ms'] if kw in text_lower)
            scores[sector] = en_matches + ms_matches
        
        if max(scores.values()) == 0:
            return 'SEC-10', 0.0  # Default to General Administration
        
        best_sector = max(scores, key=scores.get)
        confidence = scores[best_sector] / max(1, sum(scores.values()))
        
        return best_sector, confidence
    
    def classify_by_agency(self, agency_code: str) -> str:
        """Classify by agency code"""
        agency_upper = agency_code.upper()
        
        # Direct match
        if agency_upper in self.AGENCY_SECTOR_MAP:
            return self.AGENCY_SECTOR_MAP[agency_upper]
        
        # Partial match
        for code, sector in self.AGENCY_SECTOR_MAP.items():
            if code in agency_upper or agency_upper in code:
                return sector
        
        return 'SEC-10'  # Default
    
    def classify_record(self, record: Dict) -> Dict:
        """Classify a single budget record"""
        # Extract fields
        title = record.get('title', '') or record.get('description', '')
        agency = record.get('agency', '') or record.get('agency_code', '')
        
        # Classify by agency (higher priority)
        if agency:
            sector = self.classify_by_agency(agency)
            method = 'agency'
        else:
            sector, confidence = self.classify_by_keywords(title)
            method = 'keyword'
        
        return {
            **record,
            'sector_code': sector,
            'sector_name': self.sector_names[sector],
            'classification_method': method,
        }
    
    def classify_batch(self, records: List[Dict]) -> pd.DataFrame:
        """Classify multiple records and return DataFrame"""
        classified = [self.classify_record(r) for r in records]
        df = pd.DataFrame(classified)
        
        return df
    
    def aggregate_by_sector(self, df: pd.DataFrame) -> pd.DataFrame:
        """Aggregate budget amounts by sector"""
        if 'amount' not in df.columns:
            raise ValueError("DataFrame must have 'amount' column")
        
        aggregation = df.groupby(['sector_code', 'sector_name']).agg({
            'amount': ['sum', 'mean', 'count']
        }).round(2)
        
        aggregation.columns = ['total_amount', 'avg_amount', 'record_count']
        aggregation = aggregation.reset_index()
        
        return aggregation
    
    def aggregate_by_agency(self, df: pd.DataFrame) -> pd.DataFrame:
        """Aggregate budget amounts by agency"""
        if 'amount' not in df.columns or 'agency' not in df.columns:
            raise ValueError("DataFrame must have 'amount' and 'agency' columns")
        
        aggregation = df.groupby('agency').agg({
            'amount': ['sum', 'mean', 'count'],
            'sector_code': 'first'
        }).round(2)
        
        aggregation.columns = ['total_amount', 'avg_amount', 'record_count', 'sector_code']
        aggregation = aggregation.reset_index()
        aggregation = aggregation.sort_values('total_amount', ascending=False)
        
        return aggregation


def main():
    """Test sector classifier with sample data"""
    classifier = SectorClassifier()
    
    # Sample budget records
    test_records = [
        {'title': 'NACSA Threat Intelligence Platform', 'agency': 'NACSA', 'amount': 500000},
        {'title': 'KPM Sekolah Digital Initiative', 'agency': 'KPM', 'amount': 2000000},
        {'title': 'KKM Hospital Equipment Upgrade', 'agency': 'KKM', 'amount': 1500000},
        {'title': 'JKR Jalan Raya Construction', 'agency': 'JKR', 'amount': 5000000},
        {'title': 'MCMC 5G Infrastructure Rollout', 'agency': 'MCMC', 'amount': 3000000},
        {'title': 'Pertahanan Sistem Radar', 'agency': 'MINDEF', 'amount': 8000000},
        {'title': 'Pendidikan Universiti Penyelidikan', 'agency': 'IPTA', 'amount': 1200000},
    ]
    
    # Classify
    df = classifier.classify_batch(test_records)
    
    print("=== Classified Records ===")
    print(df[['title', 'agency', 'sector_code', 'sector_name', 'amount']].to_string(index=False))
    
    print("\n=== Aggregation by Sector ===")
    sector_agg = classifier.aggregate_by_sector(df)
    print(sector_agg.to_string(index=False))
    
    print("\n=== Aggregation by Agency ===")
    agency_agg = classifier.aggregate_by_agency(df)
    print(agency_agg.to_string(index=False))
    
    # Save results
    df.to_csv('/home/p62operator/.openclaw/workspace-hoi/models/sector_classification_test.csv', index=False)
    sector_agg.to_csv('/home/p62operator/.openclaw/workspace-hoi/models/sector_aggregation_test.csv', index=False)
    
    print("\n✅ Test complete. Results saved to models/")


if __name__ == '__main__':
    main()
