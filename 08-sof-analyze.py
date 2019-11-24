import csv
from collections import defaultdict

with open("Data/survey_results_public.csv", "r") as f:
    csv_reader = csv.DictReader(f)

    counter = defaultdict(int)

    for line in csv_reader:
        counter[line["Hobbyist"]] += 1

total = (counter["Yes"] + counter["No"])
yes_pct = counter["Yes"] /  total * 100
no_pct  = counter["No"] /  total  * 100
#
print(f"Yes: {yes_pct:.1f}%")
print(f"No : {no_pct:.1f}%")