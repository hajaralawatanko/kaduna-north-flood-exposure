
import csv

with open("wards.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    rows = list(reader)

areas = [int(row["area"]) for row in rows]

ward_summary = {
    "count": len(rows),
    "wards": [row["ward"] for row in rows]
}

area_summary = {
    "count": len(areas),
    "minimum": min(areas),
    "maximum": max(areas),
    "total": sum(areas),
    "average": sum(areas) / len(areas)
}

print("Ward summary:")
print(ward_summary)

print("Area summary:")
print(area_summary)
