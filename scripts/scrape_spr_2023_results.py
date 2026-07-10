#!/usr/bin/env python3
"""
SPR 2023 Election Results Scraper for PRN Negeri Sembilan
==========================================================
Purpose: Scrape complete election results for all 36 DUN seats from PRN Negeri Sembilan 2023
Source: electiondata.my API (canonical data source)
Output: JSON and CSV formats with full ballot breakdown and statistics
Classification: TLP:AMBER

Usage:
    python3 scrape_spr_2023_results.py

API Key: edmy_bd1e69207f3b1ab81dbef4fb1acabf3392535bb1

API Endpoints (from electiondata.my docs):
  Step 1: GET /seats/dropdown - Get list of all seats with slugs
  Step 2: GET /seats/results?slug={slug}&lineage=false - Get election history for a seat
  Step 3: GET /results?seat={seat}&state={state}&date={date} - Get detailed ballot results
"""

import requests
import json
import csv
from datetime import datetime
import os
import sys

# Configuration
API_KEY="edmy_bd1e69207f3b1ab81dbef4fb1acabf3392535bb1"
API_BASE_URL = "https://api.electiondata.my/v1"
OUTPUT_DIR = "/home/p62operator/.openclaw/workspace-hoi/intelligence/prn-johor-2026/spr-data"
OUTPUT_JSON = f"{OUTPUT_DIR}/spr-n9-2023-complete-results.json"
OUTPUT_CSV = f"{OUTPUT_DIR}/spr-n9-2023-complete-results.csv"
LOG_FILE = f"{OUTPUT_DIR}/scraper-log.txt"

# PRN Negeri Sembilan 2023 election date
ELECTION_DATE = "2023-08-12"
STATE = "Negeri Sembilan"


class SPR2023Scraper:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': f'Bearer {API_KEY}',
            'User-Agent': 'Mozilla/5.0 (PRN Johor Intelligence Bot)',
            'Accept': 'application/json'
        })
        self.results = []
        self.errors = []
        self.log_messages = []
        
    def log(self, message, level="INFO"):
        """Log messages with timestamp"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [{level}] {message}"
        self.log_messages.append(log_entry)
        print(log_entry)
        
    def get_seats_list(self):
        """
        Get list of all seats in Johor from the API
        Endpoint: GET /seats/dropdown
        Returns list of seats with slugs for filtering
        """
        self.log("Fetching seats dropdown from electiondata.my API...")
        
        try:
            response = self.session.get(
                f"{API_BASE_URL}/seats/dropdown",
                timeout=30
            )
            
            if response.status_code == 200:
                data = response.json()
                seats = data.get('seats', [])
                
                # Filter for Negeri Sembilan state seats (DUN)
                # State is embedded in the seat name: "N.01 Chennah, Negeri Sembilan"
                ns_dun = [s for s in seats if s.get('type') == 'dun' and ', Negeri Sembilan' in s.get('seat', '')]
                
                self.log(f"Found {len(ns_dun)} DUN seats in {STATE}", "SUCCESS")
                return ns_dun
            else:
                self.log(f"Failed to retrieve seats: HTTP {response.status_code}", "ERROR")
                self.errors.append(f"Seats API error: {response.status_code}")
                return None
                
        except Exception as e:
            self.log(f"Error fetching seats: {str(e)}", "ERROR")
            self.errors.append(f"Seats API exception: {str(e)}")
            return None
    
    def get_election_results(self, seat, state, date):
        """
        Get detailed election results for a specific seat
        Endpoint: GET /results?seat={seat}&state={state}&date={date}
        
        Returns: dict with ballot and stats
        """
        try:
            response = self.session.get(
                f"{API_BASE_URL}/results",
                params={
                    'seat': seat,
                    'state': state,
                    'date': date
                },
                timeout=30
            )
            
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 404:
                self.log(f"No results found for {seat}", "WARNING")
                return None
            else:
                self.log(f"API error for {seat}: HTTP {response.status_code}", "ERROR")
                return None
                
        except Exception as e:
            self.log(f"Error fetching results for {seat}: {str(e)}", "ERROR")
            return None
    
    def scrape_all_results(self, seats_list):
        """
        Scrape results for all DUN seats in Johor 2023
        Uses two-step process:
          1. Get seat results summary from /seats/results
          2. Get detailed ballot from /results
        """
        self.log("=" * 60)
        self.log("SCRAPE PHASE: Fetching results for all DUN seats")
        self.log("=" * 60)
        
        successful = 0
        failed = 0
        
        for idx, seat_info in enumerate(seats_list, 1):
            seat_name_full = seat_info.get('seat')  # e.g., "N.01 Chennah, Negeri Sembilan"
            seat_slug = seat_info.get('slug')
            
            # Extract just the seat name without state suffix
            # "N.01 Chennah, Negeri Sembilan" -> "N.01 Chennah"
            seat_name = seat_name_full.split(',')[0].strip()
            
            self.log(f"[{idx}/{len(seats_list)}] Processing {seat_name_full}...")
            
            # Step 1: Get seat history to find the 2023 election
            try:
                response = self.session.get(
                    f"{API_BASE_URL}/seats/results",
                    params={'slug': seat_slug, 'lineage': False},
                    timeout=30
                )
                
                if response.status_code != 200:
                    self.log(f"  ✗ Failed to get seat history: HTTP {response.status_code}", "ERROR")
                    failed += 1
                    continue
                
                seat_data = response.json()
                results_list = seat_data.get('results', [])
                
                # Find 2023 election result
                election_2023 = None
                for result in results_list:
                    if result.get('date') == ELECTION_DATE:
                        election_2023 = result
                        break
                
                if not election_2023:
                    self.log(f"  ✗ No 2023 election found for {seat_name}", "WARNING")
                    failed += 1
                    continue
                
                # Step 2: Get detailed ballot results
                ballot_results = self.get_election_results(
                    seat_name, 
                    STATE, 
                    ELECTION_DATE
                )
                
                if ballot_results:
                    # Enrich with metadata
                    enriched_result = {
                        'seat_slug': seat_slug,
                        'seat_name': seat_name,
                        'state': STATE,
                        'election_date': ELECTION_DATE,
                        'summary': election_2023,
                        'ballot': ballot_results.get('ballot', []),
                        'stats': ballot_results.get('stats', [{}])[0] if ballot_results.get('stats') else {}
                    }
                    
                    self.results.append(enriched_result)
                    successful += 1
                    
                    # Extract winner info for logging
                    if enriched_result['ballot']:
                        winner = enriched_result['ballot'][0]
                        self.log(f"  ✓ Winner: {winner['name']} ({winner['party']}/{winner.get('coalition', 'N/A')}) - {winner['votes']:,} votes", "SUCCESS")
                else:
                    failed += 1
                    self.errors.append(f"Failed to get ballot for {seat_name}")
                    
            except Exception as e:
                self.log(f"  ✗ Error processing {seat_name}: {str(e)}", "ERROR")
                failed += 1
                self.errors.append(f"Exception for {seat_name}: {str(e)}")
                
        self.log(f"Scraping complete: {successful} successful, {failed} failed", "SUCCESS")
        return successful, failed
    
    def generate_summary(self):
        """Generate summary statistics"""
        summary = {
            'total_seats': len(self.results),
            'coalition_wins': {},
            'total_voters': 0,
            'total_votes_cast': 0,
            'average_turnout': 0,
            'closest_margins': [],
            'biggest_majorities': []
        }
        
        margins = []
        
        for result in self.results:
            stats = result.get('stats', {})
            ballot = result.get('ballot', [])
            
            # Count coalition wins
            if ballot:
                winner_coalition = ballot[0].get('coalition', 'Unknown')
                summary['coalition_wins'][winner_coalition] = summary['coalition_wins'].get(winner_coalition, 0) + 1
            
            # Aggregate voter stats
            if stats:
                summary['total_voters'] += stats.get('voters_total', 0)
                summary['total_votes_cast'] += stats.get('voter_turnout', 0)
                
                # Track margins
                majority = stats.get('majority', 0)
                majority_perc = stats.get('majority_perc', 0)
                margins.append({
                    'seat': result['seat_name'],
                    'majority': majority,
                    'majority_perc': majority_perc,
                    'winner': ballot[0]['name'] if ballot else 'N/A'
                })
        
        # Calculate average turnout
        if summary['total_voters'] > 0:
            summary['average_turnout'] = (summary['total_votes_cast'] / summary['total_voters']) * 100
        
        # Sort margins
        margins_sorted = sorted(margins, key=lambda x: x['majority_perc'])
        summary['closest_margins'] = margins_sorted[:5]  # Top 5 closest
        summary['biggest_majorities'] = list(reversed(margins_sorted))[:5]  # Top 5 biggest
        
        return summary
    
    def save_json(self):
        """Save complete results to JSON"""
        output = {
            'metadata': {
                'generated_at': datetime.now().isoformat(),
                'classification': 'TLP:AMBER',
                'source': 'electiondata.my API',
                'election': 'PRN Johor 2023',
                'election_date': ELECTION_DATE,
                'state': STATE,
                'api_key_used': API_KEY[:20] + '...'
            },
            'summary': self.generate_summary(),
            'results': self.results,
            'errors': self.errors if self.errors else None
        }
        
        try:
            with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
                json.dump(output, f, indent=2, ensure_ascii=False)
            self.log(f"JSON output saved to: {OUTPUT_JSON}", "SUCCESS")
            return True
        except Exception as e:
            self.log(f"Error saving JSON: {str(e)}", "ERROR")
            return False
    
    def save_csv(self):
        """Save results to CSV format"""
        try:
            with open(OUTPUT_CSV, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                
                # Header
                writer.writerow([
                    'Seat', 'Seat UID', 'State', 'Election Date',
                    'Candidate Name', 'Party', 'Coalition', 'Votes', 'Votes %', 'Result',
                    'Total Voters', 'Turnout', 'Turnout %', 'Rejected Votes', 'Majority', 'Majority %'
                ])
                
                # Data rows
                for result in self.results:
                    stats = result.get('stats', {})
                    for candidate in result.get('ballot', []):
                        writer.writerow([
                            result['seat_name'],
                            result.get('seat_uid', ''),
                            result['state'],
                            result['election_date'],
                            candidate.get('name', ''),
                            candidate.get('party', ''),
                            candidate.get('coalition', ''),
                            candidate.get('votes', 0),
                            candidate.get('votes_perc', 0),
                            candidate.get('result', ''),
                            stats.get('voters_total', 0),
                            stats.get('voter_turnout', 0),
                            stats.get('voter_turnout_perc', 0),
                            stats.get('votes_rejected', 0),
                            stats.get('majority', 0),
                            stats.get('majority_perc', 0)
                        ])
            
            self.log(f"CSV output saved to: {OUTPUT_CSV}", "SUCCESS")
            return True
        except Exception as e:
            self.log(f"Error saving CSV: {str(e)}", "ERROR")
            return False
    
    def save_log(self):
        """Save log to file"""
        try:
            with open(LOG_FILE, 'w', encoding='utf-8') as f:
                f.write('\n'.join(self.log_messages))
            print(f"Log saved to: {LOG_FILE}")
            return True
        except Exception as e:
            print(f"Error saving log: {str(e)}")
            return False
    
    def run(self):
        """Main execution"""
        self.log("=" * 60)
        self.log("SPR 2023 ELECTION RESULTS SCRAPER - PRN NEGERI SEMBILAN", "INFO")
        self.log("Source: electiondata.my API", "INFO")
        self.log("=" * 60)
        
        # Step 1: Get seats list
        seats_list = self.get_seats_list()
        
        if not seats_list:
            self.log("Failed to retrieve seats list. Exiting.", "ERROR")
            return False
        
        # Step 2: Scrape all results
        successful, failed = self.scrape_all_results(seats_list)
        
        if successful == 0:
            self.log("No results scraped. Exiting.", "ERROR")
            return False
        
        # Step 3: Save outputs
        self.save_json()
        self.save_csv()
        self.save_log()
        
        # Final summary
        self.log("=" * 60)
        self.log("SCRAPER EXECUTION COMPLETE")
        self.log(f"Total DUN seats processed: {len(self.results)}")
        self.log(f"Successful: {successful}, Failed: {failed}")
        
        summary = self.generate_summary()
        self.log(f"Total registered voters: {summary['total_voters']:,}")
        self.log(f"Average turnout: {summary['average_turnout']:.2f}%")
        self.log(f"Coalition breakdown: {summary['coalition_wins']}")
        self.log("=" * 60)
        
        return True


if __name__ == "__main__":
    # Ensure output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    scraper = SPR2023Scraper()
    success = scraper.run()
    
    sys.exit(0 if success else 1)
