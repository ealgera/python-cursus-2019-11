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
        if i < 10:
            dev_types_list = line.get("DevType").split(";")
            for dev_type in dev_types_list:
                dev_type_info_dict[dev_type] = {}
        else:
            break

for k, v in dev_type_info_dict.items():
    print(k, v)
