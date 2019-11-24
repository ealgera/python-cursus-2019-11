import csv
from collections import defaultdict, Counter

with open("Data/survey_results_public.csv", "r") as f:
    csv_reader = csv.DictReader(f)

    language_counter = Counter()
    total = 0

    for i, line in enumerate(csv_reader):
        if i < 1000:
            total += 1
            language_list = line.get("LanguageWorkedWith").split(";")
            language_counter.update(language_list)
        else:
            break

print(f"Verwerkt: {total}")
print()

for k, v in language_counter.most_common(5):
    print(f"Taal: {k}, {v/total*100:.1f}%")

#print()
#print(f"Meest voorkomende talen: {language_counter.most_common(5)}")