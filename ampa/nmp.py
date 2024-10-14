# nmp.py

from datetime import datetime

NLMP_DATE = datetime(year=2025, month=1, day=2, hour=14)
nlmp = NLMP_DATE - datetime.now()
print(f"NLMP:  {nlmp}")