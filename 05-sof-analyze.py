import csv

with open("Data/survey_results_public.csv", "r") as f:
    csv_reader = csv.DictReader(f)

    for i, line in enumerate(csv_reader):
        #print(line)
        if i < 10:
            print(line)
            print()
        else:
            break

