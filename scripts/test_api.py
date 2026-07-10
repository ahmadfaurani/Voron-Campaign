#!/usr/bin/env python3
import requests

API_KEY = "edmy_bd1e69207f3b1ab81dbef4fb1acabf3392535bb1"
BASE_URL = "https://api.electiondata.my/v1"

headers = {"Authorization": f"Bearer {API_KEY}"}

# Test 1: Get seats dropdown
print("Test 1: GET /seats/dropdown")
resp = requests.get(f"{BASE_URL}/seats/dropdown", headers=headers, timeout=10)
print(f"Status: {resp.status_code}")
if resp.status_code == 200:
    data = resp.json()
    print(f"Total seats: {len(data.get('seats', []))}")
    # Find first N9 seat
    for seat in data.get('seats', []):
        if 'Negeri Sembilan' in seat.get('seat', '') and seat.get('type') == 'dun':
            print(f"First N9 seat: {seat}")
            break
else:
    print(f"Error: {resp.text}")

print("\n" + "="*60 + "\n")

# Test 2: Get seat results for N.01 Chennah
print("Test 2: GET /seats/results for N.01 Chennah")
slug = "n01-chennah-negeri-sembilan"
resp = requests.get(f"{BASE_URL}/seats/results", headers=headers, params={'slug': slug, 'lineage': False}, timeout=10)
print(f"Status: {resp.status_code}")
if resp.status_code == 200:
    data = resp.json()
    print(f"Response: {data}")
else:
    print(f"Error: {resp.text}")

print("\n" + "="*60 + "\n")

# Test 3: Get detailed results
print("Test 3: GET /results for N.01 Chennah, 2023-08-12")
resp = requests.get(f"{BASE_URL}/results", headers=headers, params={
    'seat': 'N.01 Chennah',
    'state': 'Negeri Sembilan',
    'date': '2023-08-12'
}, timeout=10)
print(f"Status: {resp.status_code}")
if resp.status_code == 200:
    data = resp.json()
    print(f"Response: {data}")
else:
    print(f"Error: {resp.text}")
