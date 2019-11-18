import csv
from collections import defaultdict, Counter

with open("Data/survey_results_public.csv") as f:
    csv_reader = csv.DictReader(f)

    dev_type_info = {}

    for i, line in enumerate(csv_reader):

        dev_types = line["DevType"].split(";")

        for dev_type in dev_types:
            dev_type_info.setdefault(dev_type,
            {
                "total": 0,
                "language_counter": Counter()
            })
            
            languages = line["LanguageWorkedWith"].split(";")
            dev_type_info[dev_type]["language_counter"].update(languages)
            dev_type_info[dev_type]["total"] += 1

for devtype, info in dev_type_info.items():
    print(devtype)
    total = info["total"]
    for language, value in info["language_counter"].most_common(3):
        print(f"\t{language}: {round((value/total*100),2)}%")
