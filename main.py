import json
from datetime import datetime

with open("testdata.json", "r") as file:
    data = json.load(file)

sorted_data = sorted(data, key=lambda x: x['aikaleima_suomi'])

max_price = max(float(entry["hinta"]) for entry in sorted_data)
min_price = min(float(entry["hinta"]) for entry in sorted_data)
price_range = max_price - min_price

graph_width = 50

current_date = datetime.now().strftime("%d-%m-%y")
current_hour = datetime.now().hour

print(f"\n {current_date}")
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

