
import csv


def read_rows(filename):
    with open(filename, newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def clean_values(values):
    cleaned = []

    for value in values:
        try:
            cleaned.append(float(value))
        except (ValueError, TypeError):
            continue

    return cleaned


def summarise(values):
    if not values:
        return {
            "count": 0,
            "smallest": None,
            "largest": None,
            "average": None,
        }

    return {
        "count": len(values),
        "smallest": min(values),
        "largest": max(values),
        "average": sum(values) / len(values),
    }


def summarise_all(rows):
    if not rows:
        print("No data found.")
        return

    for column in rows[0]:
        values = clean_values([row[column] for row in rows])

        if not values:
            continue

        result = summarise(values)

        print(
            f"{column}: count={result['count']}, "
            f"smallest={result['smallest']:g}, "
            f"largest={result['largest']:g}, "
            f"average={result['average']:g}"
        )


data = read_rows("wards.csv")
summarise_all(data)
