#!/usr/bin/env python3
"""Create enriched CSV with CIMB stakeholders for version control"""

import csv
from datetime import datetime

# Create versioned enriched CSV
output_file = f"/home/p62operator/.openclaw/workspace-hoi/prospect-database-enriched-v1.2.csv"

# CIMB stakeholders data (from collection)
cimb_data = [
    {
        "id": "1",
        "company_name": "CIMB Bank Berhad",
        "legal_entity_name": "CIMB Group Holdings Berhad",
        "role": "Group Chief Executive Officer",
        "name": "Novan Amirudin",
        "confidence_score": "95",
        "source_url": "https://www.cimb.com/en/who-we-are/leadership/board-of-directors/cimb-group/novan-amirudin.html",
        "country": "Malaysia",
        "verified_date": "2026-07-10",
        "database_version": "v1.2"
    },
    {
        "id": "2",
        "company_name": "CIMB Bank Berhad",
        "legal_entity_name": "CIMB Group Holdings Berhad",
        "role": "Group Chief Financial & Strategy Officer",
        "name": "Khairul Rifaie",
        "confidence_score": "95",
        "source_url": "https://www.cimb.com/en/who-we-are/leadership/senior-management-team/senior-management-team/khairul-rifaie.html",
        "country": "Malaysia",
        "verified_date": "2026-07-10",
        "database_version": "v1.2"
    },
    {
        "id": "3",
        "company_name": "CIMB Bank Berhad",
        "legal_entity_name": "CIMB Group Holdings Berhad",
        "role": "Group Chief Risk Officer",
        "name": "Vera Handajani",
        "confidence_score": "95",
        "source_url": "https://www.cimb.com/en/who-we-are/leadership/senior-management-team/senior-management-team/vera-handajani.html",
        "country": "Malaysia",
        "verified_date": "2026-07-10",
        "database_version": "v1.2"
    },
    {
        "id": "4",
        "company_name": "CIMB Bank Berhad",
        "legal_entity_name": "CIMB Group Holdings Berhad",
        "role": "Group Chief Technology Officer",
        "name": "Ros Aziah Mohd Yusoff",
        "confidence_score": "95",
        "source_url": "https://www.cimb.com/en/who-we-are/leadership/senior-management-team/senior-management-team/ros-aziah.html",
        "country": "Malaysia",
        "verified_date": "2026-07-10",
        "database_version": "v1.2"
    },
    {
        "id": "5",
        "company_name": "CIMB Bank Berhad",
        "legal_entity_name": "CIMB Group Holdings Berhad",
        "role": "Group Chief Information Security Officer",
        "name": "Charles Samuel",
        "confidence_score": "85",
        "source_url": "https://www.zoominfo.com/p/Charles-Samuel/2399253080",
        "country": "Malaysia",
        "verified_date": "2026-07-10",
        "database_version": "v1.2"
    },
    {
        "id": "6",
        "company_name": "CIMB Bank Berhad",
        "legal_entity_name": "CIMB Group Holdings Berhad",
        "role": "Group Chief Legal & Compliance Officer",
        "name": "Kwan Keen Yew",
        "confidence_score": "95",
        "source_url": "https://www.cimb.com/en/who-we-are/leadership/senior-management-team/senior-management-team/kwan-keen-yew.html",
        "country": "Malaysia",
        "verified_date": "2026-07-10",
        "database_version": "v1.2"
    },
    {
        "id": "7",
        "company_name": "CIMB Bank Berhad",
        "legal_entity_name": "CIMB Group Holdings Berhad",
        "role": "Group Chief Internal Auditor",
        "name": "Amran Mohamad",
        "confidence_score": "90",
        "source_url": "https://my.linkedin.com/in/amran-mohamad-393ba517",
        "country": "Malaysia",
        "verified_date": "2026-07-10",
        "database_version": "v1.2"
    },
]

# Write CSV
fieldnames = ["id", "company_name", "legal_entity_name", "role", "name", "confidence_score", "source_url", "country", "verified_date", "database_version"]

with open(output_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(cimb_data)

print(f"✅ Created {output_file}")
print(f"   Records: {len(cimb_data)}")
print(f"   Coverage: 7/7 roles (100%)")
print(f"   HIGH confidence (80-100): {len([r for r in cimb_data if int(r['confidence_score']) >= 80])}")
