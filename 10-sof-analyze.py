import csv
from collections import defaultdict, Counter

with open("Data/survey_results_public.csv", "r") as f:
    csv_reader = csv.DictReader(f)

    language_counter = Counter()

    for i, line in enumerate(csv_reader):
        if i < 10:
            language_counter["Total"] += 1
            language_list = line.get("LanguageWorkedWith").split(";")
            for language in language_list:
                language_counter[language] += 1
        else:
            break

total = language_counter.get('Total')
print(f"Verwerkt: {total}")

for k, v in language_counter.items():
    print(f"Taal: {k}, {v/total*100:.1f}%")
