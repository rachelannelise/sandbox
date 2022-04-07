# %%
import csv
import statistics

abs_path = '/Users/annelise/sandbox/co_real_estate'
residence = 'Neighborhood_Zhvi_SingleFamilyResidence.csv'
rentals = 'Neighborhood_Zri_SingleFamilyResidenceRental.csv'


def get_data(type: str, state: str='CO', county: str=None) -> tuple[dict, dict, dict]:
    # setting
    temp_data = []
    data = {}
    metadata = {}
    iloc_dict = {}

    assert type in ['residence', 'rentals']

    # read file
    with open(f'{abs_path}/data/{eval(type)}', 'r') as file:
        csv_reader = csv.DictReader(file, delimiter=',')
        for row in csv_reader:
            temp_data.append(row)

    # rows to clean
    string_rows = ['RegionID', 'RegionName', 'City', 'State', 'Metro', 'CountyName']
    rank_rows = ['SizeRank']
    # make default empty list for each "column"
    keys = string_rows + rank_rows
    for key in keys:
        metadata.setdefault(key, [])

    # merge dictionaries into 1 dictionary with structure {key1: [value1, value2, value3], key2: [a1, a2, a3]}
    # assuming zeroes for missing data
    # filter out for appropriate state/county data
    iloc_count = 0
    for dictionary in temp_data:
        if dictionary['State'] != state:
            continue
        if county:
            if dictionary['CountyName'] != county:
                continue
        iloc_dict[iloc_count] = dictionary['RegionID'] + ' ' + dictionary['RegionName'] +' ' + dictionary['City']+' '+dictionary['Metro']
        iloc_count += 1
        data[dictionary['RegionID']] = []
        for k, v in dictionary.items():
            if k not in string_rows and k not in rank_rows:
                v = int(v) if v else 0
                data[dictionary['RegionID']] = data[dictionary['RegionID']] + [v]
            if k in keys:
                metadata[k] = metadata[k] + [v]

    return metadata, data, iloc_dict

# %% analyze

colorado_residence_metadata, colorado_residence_data, colorado_residence_iloc = get_data('residence', 'CO')

# 1. Using the most recent data available in these csv files, what neighborhoods in Colorado have the highest median home value?

# Assuming most recent data = 3 years, 36 months
months_lookback = 36
medians = {}
for k, v in colorado_residence_data.items():
    medians[k] = statistics.median(v[-months_lookback:])

# top five medians
find_medians = list(medians.values())
find_medians.sort(reverse=True)
max_medians = find_medians[0:5]

max_median_regions = []
print('The top 5 neighborhoods in Colorado have the highest median home value in the last 3 years are: ')
for i in max_medians:
    n = list(medians.values()).index(i)
    print(f'{colorado_residence_iloc[n]} with median value ${i}')


# %%
# 2. What are the top 5 neighborhoods in Colorado, ranked by how much the home price has increased (%) over the last two years.

# 3. What neighborhoods (top 5 again) in Colorado have the highest ratio of rental income to home value.
#
# 4. A real-estate investor has come to you with money to invest in Boulder County. What neighborhood would you suggest she invest in? Use the data to justify your answer and provide a quick estimate of her ROI after 3 years.
#
# 5. How much more money could this investor make if she were willing to invest in other markets in Colorado?