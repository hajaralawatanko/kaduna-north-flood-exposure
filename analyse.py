import csv

with open("wards.csv", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        area = int(row["area"])

        if area >= 1000:
            classification = "large"
        else:
            classification = "small"

        print(row["ward"], classification)