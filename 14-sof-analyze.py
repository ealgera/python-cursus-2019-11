import csv
from collections import defaultdict, Counter

'''
{
    <dev_type>: {
        "total": 0,
        "language_counter: {
            <language>: 0
        }
    } 
}
'''

with open("Data/survey_results_public.csv", "r") as f:
    csv_reader = csv.DictReader(f)

    dev_type_info_dict = {}

    for i, line in enumerate(csv_reader):
        if i < 1000:
            dev_types_list = line.get("DevType").split(";")
            for dev_type in dev_types_list:
                dev_type_info_dict.setdefault(dev_type, {
                    "Total": 0,
                    "language_counter": Counter()
                })

                dev_type_info_dict[dev_type]["Total"] += 1
                
                dev_languages_list = line.get("LanguageWorkedWith").split(";")
                dev_type_info_dict[dev_type]["language_counter"].update(dev_languages_list)

        else:
            break

for dev_type, info in dev_type_info_dict.items():  
    print(dev_type)
    total = info["Total"]
    for language, counter in info["language_counter"].most_common(5):
        print(f"\t{language} - {(counter/total)*100:.1f}")
    print()
