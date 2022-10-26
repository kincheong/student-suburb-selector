import random
import csv

Acc = ['acc_house_onebed',
      'acc_house_twobed',
      'acc_house_threebed',
      'acc_house_fourplusbed',
      'acc_apartment_onebed',
      'acc_apartment_twobed',
      'acc_apartment_threebed',
      'acc_apartment_fourplusbed',
      'acc_rented_house_relative',
      'acc_rented_apartment_relative',
      'acc_shared_relative']
Acc_price = ['acc_rent_1_74',
            'acc_rent_75_99',
            'acc_rent_100_149',
            'acc_rent_150_199',
            'acc_rent_200_224',
            'acc_rent_225_274',
            'acc_rent_275_349',
            'acc_rent_350_449',
            'acc_rent_450_549',
            'acc_rent_550_649',
            'acc_rent_650_749',
            'acc_rent_750_849',
            'acc_rent_850_949',
            'acc_rent_950_plus']

Env = ['env_retail',
        'env_accomodation_food',
        'env_public_admin',
        'env_healthcare_social_assist',
        'env_arts_recreation',
        'env_rental_hiring_realestate',
        'env_parks']

Dem = ['dem_students_relative']

Tra = ['tra_train',
        'tra_bus',
        'tra_tram']

Saf = ['saf_crime_person',
        'saf_crime_property',
        'saf_drug_offences',
        'saf_order_security',
        'saf_justice_procedure',
        'saf_other']

Com = ["com_swinbourne_hawthorn",
  "com_swinbourne_croydon",
  "com_swinbourne_wantirna",
  "com_deakin_burwood",
  "com_deakin_geelong",
  "com_deakin_warrnambool",
  "com_federation_ballarat",
  "com_federation_churchill",
  "com_federation_berwick",
  "com_federation_wimmera",
  "com_latrobe_melbourne",
  "com_latrobe_bendigo",
  "com_latrobe_shepparton",
  "com_latrobe_wodonga",
  "com_latrobe_mildura",
  "com_monash_clayton",
  "com_monash_caulfield",
  "com_monash_peninsula",
  "com_monash_parkville",
  "com_rmit_melbourne",
  "com_swinburne_hawthorne",
  "com_swinburne_croydon",
  "com_swinburne_wantirna",
  "com_unimelb_parkville",
  "com_unimelb_southbank",
  "com_unimelb_burnley",
  "com_unimelb_dookie",
  "com_unimelb_creswick",
  "com_unimelb_werribee",
  "com_unimelb_shepparton",
  "com_vicuni_melbourne",
  "com_vicuni_footscray",
  "com_vicuni_stalbans",
  "com_vicuni_sunshine",
  "com_vicuni_werribee",
  "com_catholic_ballarat",
  "com_catholic_melbourne",
  "com_torrens_melbourne"
]


def acc_generator(Header):
    result = []
    multiplier = random.randint(0,3)
    house = random.randint(0,1)
    apt = random.randint(0,1)

    a = 0
    rentHouse = 0
    rentApt = 0
    temp = []

    zero = True
    for a in range(4):
        x = random.randint(0, 1)
        x = x*multiplier
        temp.append(x)

    for item in temp:
        x = item*house
        if x > 0:
            rentHouse = x
        result.append(x)

    for item in temp:
        x = item*apt
        if x > 0:
            rentApt = x
        result.append(x)

    result.append(rentHouse)
    result.append(rentApt)

    x = random.randint(0, 1)
    x = x * multiplier
    result.append(x)

    result2 = acc_generator_2(multiplier)
    result = result + result2

    return result

def acc_generator_2(multiplier):
    result = []
    # min = False
    # max = False
    # for i in range(14):
    #     if max == True:
    #         x = 0
    #     elif min == True:
    #         x = 1
    #         count -= 1
    #         if count == 0:
    #             min = False
    #             max = True
    #     elif max == False:
    #         x = random.randint(0, 1)
    #         if x == 1:
    #             min = True
    #             count = random.randint(0, 14-len(result))
    #             count -= 1
    #
    #     x = x * multiplier
    #     result.append(x)


    range_num = random.randint(1,41)
    i = 0
    for i in range(range_num):
        result.append(multiplier)
        i += 1
    j = 0
    for j in range(41 - range_num):
        result.append(0)

    return result

def generator(Header):
    result = []
    multiplier = random.randint(0,3)
    for item in Header:
        x = random.randint(0, 1)
        x = x*multiplier
        result.append(x)
    return result

def com_generator():
    result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    rand = random.randint(0, 10)
    multiplier = random.randint(0,3)
    result[rand] = multiplier
    return result

i = 0
end_csv = []
header = Acc + Acc_price + Env + Dem + Tra + Saf + Com
end_csv.append (header)
for i in range(100000):
    lst1 = acc_generator(Acc)
    lst2 = generator(Env)
    lst3 = generator(Dem)
    lst4 = generator(Tra)
    lst5 = generator(Saf)
    lst6 = com_generator()
    end = lst1 + lst2 + lst3 + lst4 + lst5 + lst6
    end_csv.append(end)
    i += 1

with open('generatedPref.csv', 'w+', newline ='') as f:
     write = csv.writer(f)
     write.writerows(end_csv)