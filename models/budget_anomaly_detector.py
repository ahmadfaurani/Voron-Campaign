#!/usr/bin/env python3
"""
Budget Anomaly Detector — HOI Intelligence Module
Classification: TLP:AMBER — Internal Operational Use

Purpose: Detect anomalies in government budget allocations using Isolation Forest
Integration: AIL Framework output parser → Pandas DataFrame → Scikit-learn model

Owner: HOI-ANA-01 (Intelligence Analyst)
Deployment: /home/p62operator/.openclaw/workspace-hoi/models/
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import json
import os
from datetime import datetime

# Configuration
MODEL_PATH = "/home/p62operator/.openclaw/workspace-hoi/models/"
CONTAMINATION_RATE = 0.05  # Expected 5% anomalies
RANDOM_STATE = 42
N_ESTIMATORS = 100


class BudgetAnomalyDetector:
    """
    Anomaly detection for government budget data.
    
    Features:
    - Sector allocation amounts
    - Year-over-year changes
    - Project cost distributions
    - Agency spending patterns
    
    Output: Anomaly scores + flags for flagged records
    """
    
    def __init__(self, contamination=CONTAMINATION_RATE, n_estimators=N_ESTIMATORS):
        self.model = IsolationForest(
            n_estimators=n_estimators,
            contamination=contamination,
            random_state=RANDOM_STATE,
            n_jobs=-1,
            verbose=0
        )
        self.scaler = StandardScaler()
        self.is_fitted = False
        self.feature_columns = []
        
    def prepare_features(self, df):
        """
        Extract numerical features for anomaly detection.
        
        Expected columns:
        - amount: Budget amount (RM)
        - sector_code: Numeric sector identifier
        - agency_code: Numeric agency identifier
        - fiscal_year: Year (e.g., 2024)
        - project_type: Numeric project category
        
        Returns: Scaled feature matrix
        """
        required_cols = ['amount', 'sector_code', 'agency_code', 'fiscal_year']
        
        # Check required columns
        missing = [col for col in required_cols if col not in df.columns]
        if missing:
            raise ValueError(f"Missing required columns: {missing}")
        
        # Select features
        self.feature_columns = required_cols
        X = df[self.feature_columns].copy()
        
        # Handle missing values
        X = X.fillna(X.median())
        
        # Scale features
        X_scaled = self.scaler.fit_transform(X)
        
        return X_scaled
    
    def fit(self, df):
        """
        Train the anomaly detection model on historical budget data.
        
        Args:
            df: pandas DataFrame with budget records
        """
        print(f"[{datetime.now().isoformat()}] Training anomaly detector on {len(df)} records...")
        
        X_scaled = self.prepare_features(df)
        self.model.fit(X_scaled)
        self.is_fitted = True
        
        print(f"[{datetime.now().isoformat()}] Model trained successfully.")
        return self
    
    def predict(self, df):
        """
        Predict anomalies in budget data.
        
        Args:
            df: pandas DataFrame with budget records
            
        Returns:
            DataFrame with anomaly scores and flags
        """
        if not self.is_fitted:
            raise RuntimeError("Model must be fitted before prediction")
        
        X_scaled = self.scaler.transform(df[self.feature_columns])
        
        # Get predictions (-1 = anomaly, 1 = normal)
        predictions = self.model.predict(X_scaled)
        
        # Get anomaly scores (more negative = more anomalous)
        scores = self.model.score_samples(X_scaled)
        
        # Create results
        results = df.copy()
        results['anomaly_flag'] = predictions == -1
        results['anomaly_score'] = scores
        results['anomaly_rank'] = results['anomaly_score'].rank(ascending=True)
        
        return results
    
    def save_model(self, filepath=None):
        """Save trained model to disk."""
        if not self.is_fitted:
            raise RuntimeError("No model to save")
        
        if filepath is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filepath = os.path.join(MODEL_PATH, f"isolation_forest_{timestamp}.pkl")
        
        import pickle
        with open(filepath, 'wb') as f:
            pickle.dump({
                'model': self.model,
                'scaler': self.scaler,
                'feature_columns': self.feature_columns
            }, f)
        
        print(f"[{datetime.now().isoformat()}] Model saved to {filepath}")
        return filepath
    
    def load_model(self, filepath):
        """Load trained model from disk."""
        import pickle
        with open(filepath, 'rb') as f:
            data = pickle.load(f)
            self.model = data['model']
            self.scaler = data['scaler']
            self.feature_columns = data['feature_columns']
            self.is_fitted = True
        
        print(f"[{datetime.now().isoformat()}] Model loaded from {filepath}")
        return self


def load_budget_data_from_json(filepath):
    """
    Load budget data from AIL JSON output.
    
    Expected JSON structure:
    {
        "records": [
            {
                "title": "Project Name",
                "amount": 5000000,
                "sector": "Education",
                "sector_code": 1,
                "agency": "Ministry of Education",
                "agency_code": 101,
                "fiscal_year": 2024,
                "project_type": "Infrastructure",
                "source_url": "https://...",
                "timestamp": "2026-04-29T03:55:00Z",
                "trust_score": 0.95
            }
        ]
    }
    """
    with open(filepath, 'r') as f:
        data = json.load(f)
    
    df = pd.DataFrame(data['records'])
    print(f"Loaded {len(df)} budget records from {filepath}")
    return df


def generate_sample_budget_data(n_records=1000):
    """
    Generate synthetic budget data for testing.
    Includes 5% injected anomalies.
    """
    np.random.seed(RANDOM_STATE)
    
    # Normal budget patterns
    sectors = {
        1: ('Education', 5000000, 2000000),
        2: ('Infrastructure', 10000000, 5000000),
        3: ('Healthcare', 8000000, 3000000),
        4: ('Defense', 15000000, 7000000),
        5: ('Agriculture', 3000000, 1000000)
    }
    
    agencies = {
        101: 'Ministry of Education',
        102: 'Ministry of Works',
        103: 'Ministry of Health',
        104: 'Ministry of Defence',
        105: 'Ministry of Agriculture'
    }
    
    records = []
    n_anomalies = int(n_records * CONTAMINATION_RATE)
    n_normal = n_records - n_anomalies
    
    # Generate normal records
    for i in range(n_normal):
        sector_code = np.random.choice(list(sectors.keys()))
        sector_name, mean_amt, std_amt = sectors[sector_code]
        
        amount = np.random.normal(mean_amt, std_amt)
        amount = max(100000, amount)  # Minimum RM 100K
        
        agency_code = 100 + sector_code
        
        records.append({
            'title': f'Normal Project {i+1}',
            'amount': amount,
            'sector': sector_name,
            'sector_code': sector_code,
            'agency': agencies[agency_code],
            'agency_code': agency_code,
            'fiscal_year': np.random.choice([2023, 2024, 2025]),
            'project_type': np.random.choice(['Infrastructure', 'Operations', 'R&D']),
            'source_url': f'https://example.gov.my/project/{i+1}',
            'timestamp': datetime.now().isoformat(),
            'trust_score': np.random.uniform(0.85, 1.0),
            'is_anomaly': False
        })
    
    # Generate anomalous records (unusual patterns)
    for i in range(n_anomalies):
        anomaly_type = np.random.choice(['amount_spike', 'sector_mismatch', 'new_agency'])
        
        if anomaly_type == 'amount_spike':
            # Unusually high amount
            sector_code = np.random.choice(list(sectors.keys()))
            sector_name, mean_amt, _ = sectors[sector_code]
            amount = mean_amt * np.random.uniform(5, 20)  # 5-20x normal
            agency_code = 100 + sector_code
            
        elif anomaly_type == 'sector_mismatch':
            # Agency spending in wrong sector
            sector_code = np.random.choice(list(sectors.keys()))
            agency_code = np.random.choice([101, 102, 103, 104, 105])
            amount = np.random.uniform(1000000, 50000000)
            sector_name = sectors[sector_code][0]
            
        else:  # new_agency
            # Unknown agency code
            sector_code = np.random.choice(list(sectors.keys()))
            sector_name, mean_amt, std_amt = sectors[sector_code]
            amount = np.random.normal(mean_amt, std_amt)
            agency_code = 999  # Unknown agency
            
        records.append({
            'title': f'Anomaly Project {i+1} ({anomaly_type})',
            'amount': amount,
            'sector': sector_name,
            'sector_code': sector_code,
            'agency': f'Unknown Agency {agency_code}',
            'agency_code': agency_code,
            'fiscal_year': np.random.choice([2023, 2024, 2025]),
            'project_type': np.random.choice(['Infrastructure', 'Operations', 'R&D']),
            'source_url': f'https://example.gov.my/project/anomaly_{i+1}',
            'timestamp': datetime.now().isoformat(),
            'trust_score': np.random.uniform(0.5, 0.8),
            'is_anomaly': True
        })
    
    df = pd.DataFrame(records)
    print(f"Generated {len(df)} synthetic budget records ({n_anomalies} anomalies)")
    return df


def main():
    """Test the anomaly detector with synthetic data."""
    print("=" * 60)
    print("Budget Anomaly Detector — Test Run")
    print("=" * 60)
    
    # Generate sample data
    df = generate_sample_budget_data(1000)
    
    # Initialize detector
    detector = BudgetAnomalyDetector()
    
    # Train model
    detector.fit(df)
    
    # Predict anomalies
    results = detector.predict(df)
    
    # Analyze results
    flagged = results[results['anomaly_flag'] == True]
    
    print(f"\n{'=' * 60}")
    print("Results Summary")
    print("=" * 60)
    print(f"Total records: {len(df)}")
    print(f"Flagged anomalies: {len(flagged)} ({len(flagged)/len(df)*100:.1f}%)")
    print(f"Actual anomalies (ground truth): {df['is_anomaly'].sum()}")
    
    # Calculate detection accuracy
    true_positives = len(flagged[flagged['is_anomaly'] == True])
    false_positives = len(flagged[flagged['is_anomaly'] == False])
    false_negatives = len(results[(results['is_anomaly'] == True) & (results['anomaly_flag'] == False)])
    
    precision = true_positives / (true_positives + false_positives) if (true_positives + false_positives) > 0 else 0
    recall = true_positives / (true_positives + false_negatives) if (true_positives + false_negatives) > 0 else 0
    
    print(f"\nDetection Performance:")
    print(f"  True Positives: {true_positives}")
    print(f"  False Positives: {false_positives}")
    print(f"  False Negatives: {false_negatives}")
    print(f"  Precision: {precision:.2f}")
    print(f"  Recall: {recall:.2f}")
    
    # Save model
    model_path = detector.save_model()
    
    # Export results
    output_path = os.path.join(MODEL_PATH, "anomaly_results.csv")
    results.to_csv(output_path, index=False)
    print(f"\nResults exported to {output_path}")
    
    # Show top 10 anomalies
    print(f"\n{'=' * 60}")
    print("Top 10 Flagged Anomalies")
    print("=" * 60)
    top_anomalies = flagged.nsmallest(10, 'anomaly_score')[['title', 'amount', 'sector', 'agency', 'anomaly_score']]
    print(top_anomalies.to_string(index=False))
    
    return results


if __name__ == "__main__":
    main()
