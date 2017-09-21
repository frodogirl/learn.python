import json
import os
from collections import Counter

def load_data(path_to_file):
    with open(path_to_file, 'r') as f:
        return json.load(f)


def get_top_regions(data, top_size=5):
    # TODO: тут должен быть код, который по данным возвращает словарь вида {'название региона': количество заведений в нём}
    all_regions = [data[i]['Cells']['rayon'] for i in range(len(data))]
    count_regions = Counter(all_regions)
    return dict(count_regions.most_common()[0:5])


if __name__ == '__main__':
    data = load_data(os.path.join('data', 'technical_education_moscow.json'))
    top_regions = get_top_regions(data)
    for region, universities_amount in top_regions.items():
        print('%s: %s' % (region, universities_amount))
