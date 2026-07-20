#!/usr/bin/env python3
"""
VoronDRQ Stakeholder Collection - Enrichment Script v1.4
Adds newly collected stakeholders from:
- Agrobank Malaysia (Development Finance)
- Great Eastern Life Malaysia (Insurance)
- ICBC Malaysia (Tier 1 Foreign)
- Citibank Malaysia (Tier 1 Foreign)
- SME Bank (Development Finance)
- EXIM Bank (Development Finance)
- OCBC Malaysia (Tier 1 Foreign)

Updates:
- prospect-database-enriched-v1.4.csv (row-per-contact schema)
- prospect-database-7stakeholders.csv (role-column schema)
"""

import csv
from datetime import datetime

# New stakeholder data collected today
NEW_STAKEHOLDERS = [
    # Agrobank Malaysia (Development Finance) - 100% coverage
    {"id": "36", "name": "YM Dato' Tengku Ahmad Badli Shah Raja Hussin", "role_normalized": "CEO", "company_normalized": "Agrobank", "company_legal_entity": "Agrobank Malaysia", "confidence_score": "95", "source_url": "https://www.agrobank.com.my/home/corporate-info/senior-leadership/", "country": "Malaysia", "region": "Kuala Lumpur", "notes": "Group President/CEO; leads Islamic development finance institution", "date_collected": "2026-07-10"},
    {"id": "37", "name": "Encik Zulkeefli Mad Karim", "role_normalized": "CFO", "company_normalized": "Agrobank", "company_legal_entity": "Agrobank Malaysia", "confidence_score": "95", "source_url": "https://www.agrobank.com.my/home/corporate-info/senior-leadership/", "country": "Malaysia", "region": "Kuala Lumpur", "notes": "Group Chief Finance Officer", "date_collected": "2026-07-10"},
    {"id": "38", "name": "Encik Hussien Mullar", "role_normalized": "CRO", "company_normalized": "Agrobank", "company_legal_entity": "Agrobank Malaysia", "confidence_score": "95", "source_url": "https://www.agrobank.com.my/home/corporate-info/senior-leadership/", "country": "Malaysia", "region": "Kuala Lumpur", "notes": "Group Chief Risk Officer", "date_collected": "2026-07-10"},
    {"id": "39", "name": "Encik Nolan Jeffrey A/L Abdul Hai", "role_normalized": "CIO", "company_normalized": "Agrobank", "company_legal_entity": "Agrobank Malaysia", "confidence_score": "95", "source_url": "https://www.agrobank.com.my/home/corporate-info/senior-leadership/", "country": "Malaysia", "region": "Kuala Lumpur", "notes": "Group Chief Information Technology Officer", "date_collected": "2026-07-10"},
    {"id": "40", "name": "Encik Fairoshawal Idrus", "role_normalized": "Compliance", "company_normalized": "Agrobank", "company_legal_entity": "Agrobank Malaysia", "confidence_score": "95", "source_url": "https://www.agrobank.com.my/home/corporate-info/senior-leadership/", "country": "Malaysia", "region": "Kuala Lumpur", "notes": "Group Chief Compliance & Integrity Officer", "date_collected": "2026-07-10"},
    {"id": "41", "name": "Encik Kamarudin Samsudin", "role_normalized": "Audit", "company_normalized": "Agrobank", "company_legal_entity": "Agrobank Malaysia", "confidence_score": "95", "source_url": "https://www.agrobank.com.my/home/corporate-info/senior-leadership/", "country": "Malaysia", "region": "Kuala Lumpur", "notes": "Group Chief Internal Audit", "date_collected": "2026-07-10"},
    {"id": "42", "name": "Encik Zahid Ahmad Zawawi", "role_normalized": "COO", "company_normalized": "Agrobank", "company_legal_entity": "Agrobank Malaysia", "confidence_score": "90", "source_url": "https://www.agrobank.com.my/home/corporate-info/senior-leadership/", "country": "Malaysia", "region": "Kuala Lumpur", "notes": "Group Chief Operations Officer; additional executive", "date_collected": "2026-07-10"},
    
    # Great Eastern Life Malaysia (Insurance) - 85.7% coverage
    {"id": "43", "name": "Dato Koh Yaw Hui", "role_normalized": "CEO", "company_normalized": "Great Eastern", "company_legal_entity": "Great Eastern Life Assurance (Malaysia) Berhad", "confidence_score": "95", "source_url": "https://www.greateasternlife.com/my/en/about-us/company-profile/our-leaders/key-executive.html", "country": "Malaysia", "region": "Kuala Lumpur", "notes": "CEO since 21 Jan 2008; 20+ years insurance experience", "date_collected": "2026-07-10"},
    {"id": "44", "name": "Loke Chang Yueh", "role_normalized": "CFO", "company_normalized": "Great Eastern", "company_legal_entity": "Great Eastern Life Assurance (Malaysia) Berhad", "confidence_score": "95", "source_url": "https://www.greateasternlife.com/my/en/about-us/company-profile/our-leaders/key-executive.html", "country": "Malaysia", "region": "Kuala Lumpur", "notes": "CFO; joined 2013; BSc Actuarial Science (City University London)", "date_collected": "2026-07-10"},
    {"id": "45", "name": "Vincent Chin", "role_normalized": "CIO", "company_normalized": "Great Eastern", "company_legal_entity": "Great Eastern Life Assurance (Malaysia) Berhad", "confidence_score": "90", "source_url": "https://www.greateasternlife.com/my/en/about-us/company-profile/our-leaders/key-executive.html", "country": "Malaysia", "region": "Kuala Lumpur", "notes": "Division Head, IT; joined 2007; Bachelor of Business (RMIT)", "date_collected": "2026-07-10"},
    {"id": "46", "name": "Liza Hanim Zainal Abidin", "role_normalized": "Compliance", "company_normalized": "Great Eastern", "company_legal_entity": "Great Eastern Life Assurance (Malaysia) Berhad", "confidence_score": "85", "source_url": "https://www.greateasternlife.com/my/en/about-us/company-profile/our-leaders/key-executive.html", "country": "Malaysia", "region": "Kuala Lumpur", "notes": "Division Head, Company Secretary and Legal; LLB (Hons) Aberystwyth", "date_collected": "2026-07-10"},
    {"id": "47", "name": "Audra Chung Kit Li", "role_normalized": "Audit", "company_normalized": "Great Eastern", "company_legal_entity": "Great Eastern Life Assurance (Malaysia) Berhad", "confidence_score": "95", "source_url": "https://www.greateasternlife.com/my/en/about-us/company-profile/our-leaders/key-executive.html", "country": "Malaysia", "region": "Kuala Lumpur", "notes": "Chief Internal Auditor; since 2005; BCommerce Accounting (Canberra)", "date_collected": "2026-07-10"},
    {"id": "48", "name": "Yvonne Gan Pek Yi", "role_normalized": "COO", "company_normalized": "Great Eastern", "company_legal_entity": "Great Eastern Life Assurance (Malaysia) Berhad", "confidence_score": "90", "source_url": "https://www.greateasternlife.com/my/en/about-us/company-profile/our-leaders/key-executive.html", "country": "Malaysia", "region": "Kuala Lumpur", "notes": "COO appointed 1 Jan 2025; BSc Statistics (UM)", "date_collected": "2026-07-10"},
    
    # ICBC Malaysia (Tier 1 Foreign) - CEO confirmed
    {"id": "49", "name": "Geng Hao", "role_normalized": "CEO", "company_normalized": "ICBC Malaysia", "company_legal_entity": "Industrial and Commercial Bank of China (Malaysia) Berhad", "confidence_score": "95", "source_url": "https://malaysia.icbc.com.cn/en/column/1438058793782362235.html", "country": "Malaysia", "region": "Kuala Lumpur", "notes": "MD/CEO appointed 26 Sep 2024; former Deputy GM ICBC Singapore; MBA Renmin University", "date_collected": "2026-07-10"},
    {"id": "50", "name": "Wei Quanhong", "role_normalized": "Chairman", "company_normalized": "ICBC Malaysia", "company_legal_entity": "Industrial and Commercial Bank of China (Malaysia) Berhad", "confidence_score": "90", "source_url": "https://malaysia.icbc.com.cn/en/column/1438058793782362235.html", "country": "Malaysia", "region": "Kuala Lumpur", "notes": "Non-Independent Non-Executive Director and Chairperson; appointed 8 Feb 2023", "date_collected": "2026-07-10"},
    {"id": "51", "name": "Chin Chee Kong", "role_normalized": "Audit", "company_normalized": "ICBC Malaysia", "company_legal_entity": "Industrial and Commercial Bank of China (Malaysia) Berhad", "confidence_score": "90", "source_url": "https://malaysia.icbc.com.cn/en/column/1438058793782362235.html", "country": "Malaysia", "region": "Kuala Lumpur", "notes": "Independent Non-Executive Director; Chairman Audit Committee; former KPMG Partner", "date_collected": "2026-07-10"},
    
    # Citibank Malaysia (Tier 1 Foreign) - CEO confirmed
    {"id": "52", "name": "Vikram Singh", "role_normalized": "CEO", "company_normalized": "Citibank Malaysia", "company_legal_entity": "Citibank Berhad", "confidence_score": "95", "source_url": "https://theedgemalaysia.com/node/664448", "country": "Malaysia", "region": "Kuala Lumpur", "notes": "CEO effective May 1, 2023; joined Citi 1999; former Head Asia-Pacific regional account management", "date_collected": "2026-07-10"},
    
    # SME Bank (Development Finance) - CEO confirmed
    {"id": "53", "name": "En. Samad Majid Zain Abdul Majid", "role_normalized": "CEO", "company_normalized": "SME Bank", "company_legal_entity": "SME Bank Malaysia", "confidence_score": "95", "source_url": "https://www.smebank.com.my/senior-management", "country": "Malaysia", "region": "Kuala Lumpur", "notes": "CEO; promoted from acting CEO role", "date_collected": "2026-07-10"},
    {"id": "54", "name": "En. Zabidi Abdullah", "role_normalized": "CBO", "company_normalized": "SME Bank", "company_legal_entity": "SME Bank Malaysia", "confidence_score": "90", "source_url": "https://www.smebank.com.my/senior-management", "country": "Malaysia", "region": "Kuala Lumpur", "notes": "Chief Business Officer", "date_collected": "2026-07-10"},
    {"id": "55", "name": "Pn. Zarina Nor Ismail", "role_normalized": "COO", "company_normalized": "SME Bank", "company_legal_entity": "SME Bank Malaysia", "confidence_score": "90", "source_url": "https://www.smebank.com.my/senior-management", "country": "Malaysia", "region": "Kuala Lumpur", "notes": "Chief Operating Officer", "date_collected": "2026-07-10"},
    {"id": "56", "name": "Pn. Shuhaibahtulaslamiah Hurmuzan", "role_normalized": "CHRO", "company_normalized": "SME Bank", "company_legal_entity": "SME Bank Malaysia", "confidence_score": "90", "source_url": "https://www.smebank.com.my/senior-management", "country": "Malaysia", "region": "Kuala Lumpur", "notes": "Chief Human Capital Officer", "date_collected": "2026-07-10"},
    
    # EXIM Bank (Development Finance) - CEO confirmed
    {"id": "57", "name": "Nurbayu Kasim Chang", "role_normalized": "CEO", "company_normalized": "EXIM Bank", "company_legal_entity": "Export-Import Bank of Malaysia Berhad", "confidence_score": "95", "source_url": "https://www.exim.com.my/press_release/nurbayu-kasim-chang-appointed-as-president-and-chief-executive-officer-of-exim-bank-malaysia/", "country": "Malaysia", "region": "Kuala Lumpur", "notes": "President and CEO appointed 17 Feb 2025; former Chief Business Officer; ACCA 1999", "date_collected": "2026-07-10"},
    
    # OCBC Malaysia (Tier 1 Foreign) - Chairman confirmed
    {"id": "58", "name": "Mr George Lee Lap Wah", "role_normalized": "Chairman", "company_normalized": "OCBC Malaysia", "company_legal_entity": "OCBC Bank (Malaysia) Berhad", "confidence_score": "95", "source_url": "https://www.ocbc.com.my/group/about-us/our-leadership", "country": "Malaysia", "region": "Kuala Lumpur", "notes": "Independent Non-Executive Chairman since 1 Oct 2024; former EVP OCBC Ltd", "date_collected": "2026-07-10"},
    {"id": "59", "name": "Mr Tan Chor Sen", "role_normalized": "CEO", "company_normalized": "OCBC Malaysia", "company_legal_entity": "OCBC Bank (Malaysia) Berhad", "confidence_score": "90", "source_url": "https://www.ocbc.com/group/investors/annual-reports/2024-annual-report/our-management.page", "country": "Malaysia", "region": "Kuala Lumpur", "notes": "CEO Malaysia; confirmed via OCBC Group Annual Report 2024", "date_collected": "2026-07-10"},
]

def update_enriched_csv():
    """Update the enriched CSV with new stakeholder records."""
    enriched_path = "/home/p62operator/.openclaw/workspace-hoi/voron-stakeholders/prospect-database-enriched-v1.4.csv"
    
    # CSV header for enriched format (row-per-contact)
    fieldnames = ["id", "name", "role_normalized", "company_normalized", "company_legal_entity", 
                  "confidence_score", "source_url", "country", "region", "notes", "date_collected"]
    
    with open(enriched_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(NEW_STAKEHOLDERS)
    
    print(f"✓ Written {len(NEW_STAKEHOLDERS)} stakeholder records to enriched CSV v1.4")
    return len(NEW_STAKEHOLDERS)

def update_master_csv():
    """Update the master database CSV with role-column schema."""
    master_path = "/home/p62operator/.openclaw/workspace-hoi/voron-prospects/prospect-database-7stakeholders.csv"
    
    # Read existing master CSV
    existing_rows = []
    fieldnames = None
    with open(master_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames if reader.fieldnames else []
        for row in reader:
            existing_rows.append(row)
    
    # Map company names to CSV row identifiers
    company_updates = {
        "Agrobank Malaysia": {
            "Chief Information Security Officer": "",
            "Head of Governance Risk & Compliance": "Encik Hussien Mullar (CRO) + Encik Fairoshawal Idrus (Compliance)",
            "Chief Financial Officer": "Encik Zulkeefli Mad Karim",
            "Chief Risk Officer": "Encik Hussien Mullar",
            "Head of Compliance": "Encik Fairoshawal Idrus",
            "Chief Information Officer": "Encik Nolan Jeffrey A/L Abdul Hai",
            "Head of Internal Audit": "Encik Kamarudin Samsudin"
        },
        "Great Eastern General Insurance (Malaysia) Berhad": {
            "Chief Information Security Officer": "",
            "Head of Governance Risk & Compliance": "Liza Hanim Zainal Abidin (Legal/Compliance) + Audra Chung Kit Li (Audit)",
            "Chief Financial Officer": "Loke Chang Yueh",
            "Chief Risk Officer": "",
            "Head of Compliance": "Liza Hanim Zainal Abidin",
            "Chief Information Officer": "Vincent Chin",
            "Head of Internal Audit": "Audra Chung Kit Li"
        },
        "Great Eastern Life Assurance (Malaysia) Berhad": {
            "Chief Information Security Officer": "",
            "Head of Governance Risk & Compliance": "Liza Hanim Zainal Abidin (Legal/Compliance) + Audra Chung Kit Li (Audit)",
            "Chief Financial Officer": "Loke Chang Yueh",
            "Chief Risk Officer": "",
            "Head of Compliance": "Liza Hanim Zainal Abidin",
            "Chief Information Officer": "Vincent Chin",
            "Head of Internal Audit": "Audra Chung Kit Li"
        },
        "ICBC (Malaysia) Berhad": {
            "Chief Information Security Officer": "",
            "Head of Governance Risk & Compliance": "",
            "Chief Financial Officer": "",
            "Chief Risk Officer": "",
            "Head of Compliance": "",
            "Chief Information Officer": "",
            "Head of Internal Audit": "Chin Chee Kong (Audit Committee Chair)"
        },
        "Citibank Berhad": {
            "Chief Information Security Officer": "",
            "Head of Governance Risk & Compliance": "",
            "Chief Financial Officer": "",
            "Chief Risk Officer": "",
            "Head of Compliance": "",
            "Chief Information Officer": "",
            "Head of Internal Audit": ""
        },
        "SME Bank Berhad": {
            "Chief Information Security Officer": "",
            "Head of Governance Risk & Compliance": "",
            "Chief Financial Officer": "",
            "Chief Risk Officer": "",
            "Head of Compliance": "Rosehamidi Kamaruddin (per RocketReach)",
            "Chief Information Officer": "",
            "Head of Internal Audit": ""
        },
        "EXIM Bank Malaysia": {
            "Chief Information Security Officer": "",
            "Head of Governance Risk & Compliance": "",
            "Chief Financial Officer": "",
            "Chief Risk Officer": "",
            "Head of Compliance": "",
            "Chief Information Officer": "",
            "Head of Internal Audit": ""
        },
        "OCBC Bank (Malaysia) Berhad": {
            "Chief Information Security Officer": "",
            "Head of Governance Risk & Compliance": "",
            "Chief Financial Officer": "",
            "Chief Risk Officer": "",
            "Head of Compliance": "",
            "Chief Information Officer": "",
            "Head of Internal Audit": ""
        }
    }
    
    # Update rows
    updated_count = 0
    for row in existing_rows:
        company = row.get("Institution_Name", "")
        if company in company_updates:
            updates = company_updates[company]
            # CEO goes in a separate pass - for now update 7 stakeholder columns
            for role, value in updates.items():
                if role in row and value:
                    row[role] = value
            updated_count += 1
    
    # Write updated master CSV
    with open(master_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(existing_rows)
    
    print(f"✓ Updated {updated_count} institution rows in master CSV")
    return updated_count

if __name__ == "__main__":
    print("=" * 70)
    print("VoronDRQ Stakeholder Collection - Database Update v1.4")
    print("=" * 70)
    print()
    
    enriched_count = update_enriched_csv()
    master_count = update_master_csv()
    
    print()
    print("=" * 70)
    print(f"Summary: {enriched_count} new stakeholder contacts added")
    print(f"         {master_count} institution rows updated in master database")
    print("=" * 70)
