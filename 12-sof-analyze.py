import csv
from collections import defaultdict, Counter

with open("Data/survey_results_public.csv", "r") as f:
    csv_reader = csv.DictReader(f)

    language_counter = Counter()
    total = 0

    for line in csv_reader:
        total += 1
        language_list = line.get("LanguageWorkedWith").split(";")
        language_counter.update(language_list)

print(f"Verwerkt: {total}")
print()

for taal, aantal in language_counter.most_common(5):
    print(f"{taal.rjust(10)}, {aantal/total*100:.1f}%")

print()
#print(f"Meest voorkomende talen: {language_counter.most_common(5)}")