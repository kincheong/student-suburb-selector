# Attributes

The following document gives the specifications for the data attributes, the front-end user form inputs, how the attributes are derived from the user inputs, and any special validation rules which apply to the user form.

## Importance

The following rules apply to all 'themes' and their corresponding attributes.

- When the user inputs a valid form (specific validation rules are stated below in the respective 'theme' section), the user has also selected an 'importance' value for each 'theme'.
  - The possible values to be taken are 'None' = 0, 'Low' = 1, 'Medium' = 2, 'High' = 3.
- Each attribute which is True (see below specifications) is transformed into the value of the corresponding importance of that 'theme'.
  - For example, if the user has stated that the 'commute' theme is 'High' importance, then the value for the selected university campus is not simply 1, but is 3 since the value for 'High' is 3.

## Accomodation theme

The accomodation attributes follow the most complex business rules of all 'themes' of preference attributes we are using.

- Users will indicate the type of accomodation they would like to find, house and/or apartment.
- Users will indicate the number of bedrooms they would like to find, one and/or two and/or three and/or four plus.
- The system will automatically incorporate the relative number of rented houses/apartments in the suburb (under the logic that students will be renting and not buying).
- Users will input their "maximum rent" amount as a number, this number will be used by the system with the average rent price of each suburb and recommend suburbs whose average rent price is below this.
  - The system will store the number of people whose rent is in a given range (e.g., 1-74, 75-99, etc.).
  - The system assigns **weights** to these attributes such that the columns in lower (or equal to input) ranges are included (i.e., 1 or priority given) and the attributes which indicate prices above that are not included (i.e., 0).
  - The model then captures the suburbs who has higher densities of number of renters at the input amount or below.

### Form structure

It is useful to first understand the basic structure of this section of the form:

<form style="display: grid; background-color: white; color: black; border-radius: 8px; padding: 16px; margin: 32px 0; box-shadow: 0 0 16px grey;">
  <h2 style="color: black; margin-top: 0;">Accomodation</h2>
  <div>
    How important is accomodation for you?
    <input type="radio" name="importance" checked>None</input>
    <input type="radio" name="importance">Low</input>
    <input type="radio" name="importance">Medium</input>
    <input type="radio" name="importance">High</input>
  </div>
  <div>
    Maximum rent (R):
    <input type="number" min="0">
  </div>
  <div>
    House (H):
    <input type="checkbox" checked>
    <span style="width:8px;display:inline-block;"></span>
    Apartment (A):
    <input type="checkbox" checked>
  </div>
  <div>
    1 bed (1B):
    <input type="checkbox" checked>
    <span style="width:8px;display:inline-block;"></span>
    2 bed (2B):
    <input type="checkbox">
    <span style="width:8px;display:inline-block;"></span>
    3 bed (3B):
    <input type="checkbox">
    <span style="width:8px;display:inline-block;"></span>
    4+ bed (4pB):
    <input type="checkbox">
  </div>
  <div>
    Shared (S):
    <input type="checkbox">
  </div>
</form>

This form has the following validation rules:

- The maximum rent can be empty (server treats this as 'inf', i.e., user can afford any rent/rent price is irrelevant to them).
- At least one box in the 'house/apartment' row must be selected (default both selected).
- At least one box in the 'bed' row must be selected (default one-bed is selected).
- The 'shared' box may be left empty.

### Attributes

The following is a list of the attributes and a detailed description of the values they take according to the selections made in the form.

- House attributes
  - `acc_rented_house_relative`
    If (H): True, else False.
  - `acc_house_onebed`
    If (H) AND (1B): True, else False.
  - `acc_house_twobed`
    If (H) AND (2B): True, else False.
  - `acc_house_threebed`
    If (H) AND (3B): True, else False.
  - `acc_house_fourplusbed`
    If (H) AND (4pB): True, else False.
- Apartment attributes
  - `acc_rented_apartment_relative`
    If (A): True, else False.
  - `acc_apartment_onebed`
    If (A) AND (1B): True, else False.
  - `acc_apartment_twobed`
    If (A) AND (2B): True, else False.
  - `acc_apartment_threebed`
    If (A) AND (3B): True, else False.
  - `acc_apartment_fourplusbed`
    If (A) AND (4pB): True, else False.
- Group/shared attributes
  - `acc_shared_relative`
    If (S): True, else False.
- Rent attributes
  Whatever value (R) is inputted, the corresponding attribute below is True, and so is every attribute 'less' (above) also (since a person is specifying their MAXIMUM rent, and can therefore of course afford rent which is less than that which they specify).
  - `acc_rent_1_74`
  - `acc_rent_75_99`
  - `acc_rent_100_149`
  - `acc_rent_150_199`
  - `acc_rent_200_224`
  - `acc_rent_225_274`
  - `acc_rent_275_349`
  - `acc_rent_350_449`
  - `acc_rent_450_549`
  - `acc_rent_550_649`
  - `acc_rent_650_749`
  - `acc_rent_750_849`
  - `acc_rent_850_949`
  - `acc_rent_950_plus`

### Example

For example, the user indicated that they want only an apartment-style accomodation with either one or two bedrooms, and their max-rent is $500. They also indicated that the priority of these accomodation variables is "High" = 3, hence the multipliers are 3 rather that 1 (i.e., not bool). They did not check "Shared" so no impact is made due to this variable.

```json
{
  "acc_house_onebed": 0,
  "acc_house_twobed": 0,
  "acc_house_threebed": 0,
  "acc_house_fourplusbed": 0,
  "acc_apartment_onebed": 3,
  "acc_apartment_twobed": 3,
  "acc_apartment_threebed": 0,
  "acc_apartment_fourplusbed": 0,
  "acc_rented_house_relative": 0,
  "acc_rented_apartment_relative": 3,
  "acc_shared_relative": 0,
  "acc_rent_1_74": 3,
  "acc_rent_75_99": 3,
  "acc_rent_100_149": 3,
  "acc_rent_150_199": 3,
  "acc_rent_200_224": 3,
  "acc_rent_225_274": 3,
  "acc_rent_275_349": 3,
  "acc_rent_350_449": 3,
  "acc_rent_450_549": 3,
  "acc_rent_550_649": 0,
  "acc_rent_650_749": 0,
  "acc_rent_750_849": 0,
  "acc_rent_850_949": 0,
  "acc_rent_950_plus": 0
}
```

### Derivations from raw data

``` text
acc_house_onebed = 
    Separate_house_Number_of_bedrooms_One_bedroom
  + Semi_detached_row_or_terrace_house_townhouse_etc_with_Total_Number_of_bedrooms_One_bedroom
acc_house_twobed = 
    Separate_house_Number_of_bedrooms_Two_bedrooms
  + Semi_detached_row_or_terrace_house_townhouse_etc_with_Total_Number_of_bedrooms_Two_bedrooms
acc_house_threebed = 
    Semi_detached_row_or_terrace_house_townhouse_etc_with_One_storey_Number_of_bedrooms_Three_bedrooms
  + Semi_detached_row_or_terrace_house_townhouse_etc_with_Two_or_more_storeys_Number_of_bedrooms_Three_bedrooms
acc_house_fourplusbed = 
    Semi_detached_row_or_terrace_house_townhouse_etc_with_One_storey_Number_of_bedrooms_Four_bedrooms
  + Semi_detached_row_or_terrace_house_townhouse_etc_with_One_storey_Number_of_bedrooms_Five_bedrooms
  + Semi_detached_row_or_terrace_house_townhouse_etc_with_One_storey_Number_of_bedrooms_Six_bedrooms_or_more
  + Semi_detached_row_or_terrace_house_townhouse_etc_with_Total_Number_of_bedrooms_Four_bedrooms
  + Semi_detached_row_or_terrace_house_townhouse_etc_with_Total_Number_of_bedrooms_Five_bedrooms
  + Semi_detached_row_or_terrace_house_townhouse_etc_with_Total_Number_of_bedrooms_Six_bedrooms_or_more

acc_apartment_onebed = 
    Flat_or_apartment_Total_Number_of_bedrooms_One_bedroom
acc_apartment_twobed =
    Flat_or_apartment_Total_Number_of_bedrooms_Two_bedrooms
acc_apartment_threebed =
    Flat_or_apartment_Total_Number_of_bedrooms_Three_bedrooms
acc_apartment_fourplusbed =
    Flat_or_apartment_Total_Number_of_bedrooms_Four_bedrooms
  + Flat_or_apartment_Total_Number_of_bedrooms_Five_bedrooms
  + Flat_or_apartment_Total_Number_of_bedrooms_Six_bedrooms_or_more

acc_rented_house_relative = 
  ( Rented_Total_Dwelling_structure_Separate_house
  + Rented_Total_Dwelling_structure_Semi_detached_row_or_terrace_house_townhouse_etc )
  / ( Total_Dwelling_structure_Separate_house
    Total_Dwelling_structure_Semi_detached_row_or_terrace_house_townhouse_etc )

acc_rented_apartment_relative = 
    Rented_Total_Dwelling_structure_Flat_or_apartment
  / Total_Dwelling_structure_Flat_or_apartment

acc_shared_relative = 
    Total_Group_households (2021Census:G42)
  / Total_Total (2021Census:G42)

acc_rent_1_74 = 
    1_74_Total
acc_rent_75_99 = 
    75_99_Total
acc_rent_100_149 = 
    100_149_Total
acc_rent_150_199 = 
    150_199_Total
acc_rent_200_224 = 
    200_224_Total
acc_rent_225_274 = 
    225_274_Total
acc_rent_275_349 = 
    275_349_Total
acc_rent_350_449 = 
    350_449_Total
acc_rent_450_549 = 
    450_549_Total
acc_rent_550_649 = 
    550_649_Total
acc_rent_650_749 = 
    650_and_749_Total
acc_rent_750_849 = 
    750_and_849_Total
acc_rent_850_949 = 
    850_and_949_Total
acc_rent_950_plus = 
    950_and_over_Total
```

## Commute theme

The commute attributes very simple in implementation since it is a single input from the user form.

### Form structure

Here is the structure of this section of the form:

<form style="display: grid; background-color: white; color: black; border-radius: 8px; padding: 16px; margin: 32px 0; box-shadow: 0 0 16px grey;">
  <h2 style="color: black; margin-top: 0;">Commute</h2>
  <div>
    How important is commute for you?
    <input type="radio" name="importance" checked>None</input>
    <input type="radio" name="importance">Low</input>
    <input type="radio" name="importance">Medium</input>
    <input type="radio" name="importance">High</input>
  </div>
  <div>
    University campus (U):
    <input list="unis"><datalist id="unis"><option value="Australian Institute of Music"><option value="Australian Catholic University"><option value="Deakin University"><option value="La Trobe University"><option value="Monash University"><option value="Royal Melbourne Institute of Technology"><option value="Swinburne University of Technology"><option value="University of Melbourne"><option value="University of Divinity"><option value="Victoria University"><option value="Royal Gurkhas Institute of Technology"></datalist>
  </div>
</form>

This form has the following validation rules:

- If the priority is not 'None', then (U) cannot be empty.

### Attributes

The following is a list of the attributes and a detailed description of the values they take according to the selections made in the form.

- Campus
  Whatever value (U) is selected, the corresponding attribute below is True and all others are False.
  - `com_swinbourne_hawthorn`
  - `com_swinbourne_croydon`
  - `com_swinbourne_wantirna`
  - `com_deakin_burwood`
  - `com_deakin_geelong`
  - `com_deakin_warrnambool`
  - `com_federation_ballarat`
  - `com_federation_churchill`
  - `com_federation_berwick`
  - `com_federation_wimmera`
  - `com_latrobe_melbourne`
  - `com_latrobe_bendigo`
  - `com_latrobe_shepparton`
  - `com_latrobe_wodonga`
  - `com_latrobe_mildura`
  - `com_monash_clayton`
  - `com_monash_caulfield`
  - `com_monash_peninsula`
  - `com_monash_parkville`
  - `com_rmit_melbourne`
  - `com_swinburne_hawthorne`
  - `com_swinburne_croydon`
  - `com_swinburne_wantirna`
  - `com_unimelb_parkville`
  - `com_unimelb_southbank`
  - `com_unimelb_burnley`
  - `com_unimelb_dookie`
  - `com_unimelb_creswick`
  - `com_unimelb_werribee`
  - `com_unimelb_shepparton`
  - `com_vicuni_melbourne`
  - `com_vicuni_footscray`
  - `com_vicuni_stalbans`
  - `com_vicuni_sunshine`
  - `com_vicuni_werribee`
  - `com_catholic_ballarat`
  - `com_catholic_melbourne`
  - `com_torrens_melbourne`

### Example

For example, the user has selected their commute to be "Monash University Clayton Campus" with an importance of "Low" = 1.

``` json
{
  "com_swinbourne_hawthorn": 0,
  "com_swinbourne_croydon": 0,
  "com_swinbourne_wantirna": 0,
  "com_deakin_burwood": 0,
  "com_deakin_geelong": 0,
  "com_deakin_warrnambool": 0,
  "com_federation_ballarat": 0,
  "com_federation_churchill": 0,
  "com_federation_berwick": 0,
  "com_federation_wimmera": 0,
  "com_latrobe_melbourne": 0,
  "com_latrobe_bendigo": 0,
  "com_latrobe_shepparton": 0,
  "com_latrobe_wodonga": 0,
  "com_latrobe_mildura": 0,
  "com_monash_clayton": 1,
  "com_monash_caulfield": 0,
  "com_monash_peninsula": 0,
  "com_monash_parkville": 0,
  "com_rmit_melbourne": 0,
  "com_swinburne_hawthorne": 0,
  "com_swinburne_croydon": 0,
  "com_swinburne_wantirna": 0,
  "com_unimelb_parkville": 0,
  "com_unimelb_southbank": 0,
  "com_unimelb_burnley": 0,
  "com_unimelb_dookie": 0,
  "com_unimelb_creswick": 0,
  "com_unimelb_werribee": 0,
  "com_unimelb_shepparton": 0,
  "com_vicuni_melbourne": 0,
  "com_vicuni_footscray": 0,
  "com_vicuni_stalbans": 0,
  "com_vicuni_sunshine": 0,
  "com_vicuni_werribee": 0,
  "com_catholic_ballarat": 0,
  "com_catholic_melbourne": 0,
  "com_torrens_melbourne": 0
}
```

### Derivations from raw data

These attributes are derived programmatically from coordinates/addresses in Python directly as the as-the-crow-flies distance between suburb centre and the campus centre. See [1.1-CommuteAttributes.ipynb](1.1-CommuteAttributes.ipynb) for details.

## Industry and environment theme

The commute attributes very simple in implementation since it is a single input from the user form.

### Form structure

Here is the structure of this section of the form:

<form style="display: grid; background-color: white; color: black; border-radius: 8px; padding: 16px; margin: 32px 0; box-shadow: 0 0 16px grey;">
  <h2 style="color: black; margin-top: 0;">Industry and environment</h2>
  <div>
    How important is industry and environment for you?
    <input type="radio" name="importance" checked>None</input>
    <input type="radio" name="importance">Low</input>
    <input type="radio" name="importance">Medium</input>
    <input type="radio" name="importance">High</input>
  </div>
  <div>
    Retail (R):
    <input type="checkbox" checked>
  </div>
  <div>
    Accomodation and food (A):
    <input type="checkbox" checked>
  </div>
  <div>
    Public administration (P):
    <input type="checkbox" checked>
  </div>
  <div>
    Heathcare and social assistance (H):
    <input type="checkbox" checked>
  </div>
  <div>
    Arts and recreation (T):
    <input type="checkbox" checked>
  </div>
  <div>
    Rental, hiring, and real estate (E):
    <input type="checkbox" checked>
  </div>
  <div>
    Parks (K):
    <input type="checkbox" checked>
  </div>
</form>

This form has no special validation rules.

- If the user does not select any checkboxes and has the importance as any value not 'None', this is logically incorrect; however, is ignored by the system for simplicity and better user experience (i.e., they don't need to intentionally select 'None' when unchecked everything else).

### Attributes

The following is a list of the attributes and a detailed description of the values they take according to the selections made in the form.

- `env_retail` If (R): True, else False.
- `env_accomodation_food` If (A): True, else False.
- `env_public_admin` If (P): True, else False.
- `env_healthcare_social_assist` If (H): True, else False.
- `env_arts_recreation` If (T): True, else False.
- `env_rental_hiring_realestate` If (E): True, else False.
- `env_parks` If (K): True, else False.

### Example

The user has checked all boxes and stated the importance as 'Low'.

``` json
{
  "env_retail": 1,
  "env_accomodation_food": 1,
  "env_public_admin": 1,
  "env_healthcare_social_assist": 1,
  "env_arts_recreation": 1,
  "env_rental_hiring_realestate": 1,
  "env_parks": 1
}
```

### Derivations from raw data

``` text
env_retail =
    Retail trade (no.)

env_accomodation_food =
    Accommodation and food services (no.)

env_public_admin =
    Public administration and safety (no.)

env_healthcare_social_assist =
    Health care and social assistance (no.)

env_arts_recreation =
    Arts and recreation services (no.)

env_rental_hiring_realestate =
    Rental, hiring and real estate services (no.)

env_parks =
    Protected land area (%)
```

## Demographics theme

### Form structure

Here is the structure of this section of the form:

<form style="display: grid; background-color: white; color: black; border-radius: 8px; padding: 16px; margin: 32px 0; box-shadow: 0 0 16px grey;">
  <h2 style="color: black; margin-top: 0;">Demographics</h2>
  <div>
    How important is demographics for you?
    <input type="radio" name="importance" checked>None</input>
    <input type="radio" name="importance">Low</input>
    <input type="radio" name="importance">Medium</input>
    <input type="radio" name="importance">High</input>
  </div>
  <div>
    High student population (S):
    <input type="checkbox" checked>
  </div>
</form>

This form has no special validation rules.

### Attributes

The following is a list of the attributes and a detailed description of the values they take according to the selections made in the form.

- `dem_students_relative` If (S): True, else False.

### Example

For example, the user indicated that they would like to consider the student population of the suburb with an importance level of "Medium" = 2.

```json
{
  "dem_students_relative": 2
}
```

### Derivations from raw data

``` text
dem_students_relative =
    Tertiary_Total_Tertiary_Persons (2021Census:G15)
  / Total_Persons_Persons (2021Census:G01)
```

## Safety theme

### Form structure

Here is the structure of this section of the form:

<form style="display: grid; background-color: white; color: black; border-radius: 8px; padding: 16px; margin: 32px 0; box-shadow: 0 0 16px grey;">
  <h2 style="color: black; margin-top: 0;">Safety</h2>
  <div>
    How important is safety for you?
    <input type="radio" name="importance" checked>None</input>
    <input type="radio" name="importance">Low</input>
    <input type="radio" name="importance">Medium</input>
    <input type="radio" name="importance">High</input>
  </div>
  <div>
    Crimes against the person (C):
    <input type="checkbox" checked>
  </div>
  <div>
    Property and deception offences (P):
    <input type="checkbox" checked>
  </div>
  <div>
    Drug offences (D):
    <input type="checkbox" checked>
  </div>
  <div>
    Public order and security offences (S):
    <input type="checkbox" checked>
  </div>
  <div>
    Justice procedures offences (J):
    <input type="checkbox" checked>
  </div>
  <div>
    Other offences (O):
    <input type="checkbox" checked>
  </div>
</form>

### Attributes

The following is a list of the attributes and a detailed description of the values they take according to the selections made in the form.

- `saf_crime_person` If (C): True, else False.
- `saf_crime_property` If (P): True, else False.
- `saf_drug_offences` If (D): True, else False.
- `saf_order_security` If (S): True, else False.
- `saf_justice_procedure` If (J): True, else False.
- `saf_other` If (O): True, else False.

### Example

For example, the user has indicated that they are concerned about "Crimes against the person" and "Property and deception offences", but none of the others matter. The importance of the 'safety' attributes is "Medium" = 2.

``` json
{
  "saf_crime_person": 2,
  "saf_crime_property": 2,
  "saf_drug_offences": 0,
  "saf_order_security": 0,
  "saf_justice_procedure": 0,
  "saf_other": 0
}
```

### Derivations from raw data

``` txt
saf_crime_person =
    A Crimes against the person
  / population
saf_crime_property =
    B Property and deception offences
  / population
saf_drug_offences =
    C Drug offences
  / population
saf_order_security =
    D Public order and security offences
  / population
saf_justice_procedure =
    E Justice procedures offences
  / population
saf_other =
    F Other offences
  / population
```

## Transport theme

### Form structure

Here is the structure of this section of the form:

<form style="display: grid; background-color: white; color: black; border-radius: 8px; padding: 16px; margin: 32px 0; box-shadow: 0 0 16px grey;">
  <h2 style="color: black; margin-top: 0;">Transport</h2>
  <div>
    How important is transport for you?
    <input type="radio" name="importance" checked>None</input>
    <input type="radio" name="importance">Low</input>
    <input type="radio" name="importance">Medium</input>
    <input type="radio" name="importance">High</input>
  </div>
  <div>
    Trains (T):
    <input type="checkbox" checked>
  </div>
  <div>
    Buses (B):
    <input type="checkbox" checked>
  </div>
  <div>
    Trams (R):
    <input type="checkbox" checked>
  </div>
</form>

### Attributes

The following is a list of the attributes and a detailed description of the values they take according to the selections made in the form.

- `tra_train` If (T): True, else False.
- `tra_bus` If (B): True, else False.
- `tra_tram` If (R): True, else False.

### Example

The user has indicated that all transport types are 'Medium' importance.

``` json
{
  "tra_train": 2,
  "tra_bus": 2,
  "tra_tram": 2,
}
```

### Derivations from raw data

See [1.2-TransportAttributes.ipynb](1.2-TransportAttributes.ipynb) for detailed descriptions and the code used to derive the transport attribute scores from the GTFS dataset.
