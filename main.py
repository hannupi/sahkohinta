#!/usr/bin/env python3
import requests
from datetime import datetime

current_date = datetime.now().strftime("%y-%m-%d")
URL =  f"https://www.sahkohinta-api.fi/api/v1/halpa?tunnit=24&tulos=haja&aikaraja={current_date}"
res = requests.get(URL)

sorted_data = sorted(res.json(), key=lambda x: x['aikaleima_suomi'])

max_price = max(float(entry["hinta"]) for entry in sorted_data)
min_price = min(float(entry["hinta"]) for entry in sorted_data)
price_range = max_price - min_price

graph_width = 50
current_date = datetime.now().strftime("%d-%m-%y")
current_hour = datetime.now().hour

print(f"{current_date}")
print("-" * 20 + "-" * graph_width)

for entry in sorted_data:
    date_time = entry["aikaleima_suomi"]
    dt = datetime.strptime(date_time, "%Y-%m-%dT%H:%M")
    hinta = float(entry["hinta"])

    scaled_position = int((hinta - min_price) / price_range * (graph_width - 1))
    line = " " * scaled_position + "*"

    hour_label = f"{dt.strftime('%H')}:00"
    if int(dt.strftime("%H")) == current_hour:
        hour_label = f"* {dt.strftime('%H')}:00"  
    else:
        hour_label = f"  {dt.strftime('%H')}:00"
    print(f"{hour_label} | {line} ({hinta:.2f})")
