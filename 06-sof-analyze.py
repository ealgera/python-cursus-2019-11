import csv

with open("Data/survey_results_public.csv", "r") as f:
    csv_reader = csv.DictReader(f)

    yes_counter = 0
    no_counter = 0

    for line in csv_reader:
        if line.get("Hobbyist") == "Yes":
            yes_counter += 1
        elif line.get("Hobbyist") == "No":
            no_counter += 1

yes_pct = yes_counter / (yes_counter + no_counter) * 100
no_pct  = no_counter / (yes_counter + no_counter) * 100

print(f"Yes: {yes_pct:.1f}%")
print(f"No : {no_pct:.1f}%")