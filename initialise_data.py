
import random
import pandas as pd

from app import app
from app import db
from app.data.models import Suburb


db.drop_all()
db.create_all()


suburb_data = pd.read_csv("../data/derived/SuburbData.csv")
suburb_metadata = pd.read_csv("../data/derived/SuburbMetadata.csv")
suburb_rawdata = pd.read_csv(f"../data/derived/SuburbRawdata.csv")

all_suburbs_names = suburb_data["locality"]


def get_detail(suburb_name: str, detail_name: str):
    res = suburb_rawdata[suburb_rawdata["locality"] == suburb_name][detail_name].to_list()
    if len(res) > 0:
        return res[0]
    return None


def get_metadata(suburb_name, metadata_name: str):
    return suburb_metadata[suburb_metadata["locality"] == suburb_name][metadata_name].to_list()[0]


def main():
    with app.app_context():
        for suburb_name in all_suburbs_names:
            db.session.add(Suburb(
                name=suburb_name, 
                postcode=get_metadata(suburb_name, "postcode"), 
                lga=get_metadata(suburb_name, "lgaregion"),
                population=get_detail(suburb_name, "Tot_P_P"),
                median_age=get_detail(suburb_name, "Median_age_persons"),
                avg_household_size=get_detail(suburb_name, "Average_household_size"),
                num_uni_students=get_detail(suburb_name, "Tert_Tot_Tert_P"),
                median_weekly_rent=get_detail(suburb_name, "Median_rent_weekly"),
                num_houses=get_detail(suburb_name, "Separate_house_Total") + get_detail(suburb_name, "Se_d_r_or_t_h_t_Tot_Total"),
                num_apartments=get_detail(suburb_name, "Flt_apart_Tot_Total"),
                num_shared=get_detail(suburb_name, "Tot_Group_H")
            ))
        db.session.commit()


if __name__ == "__main__":
    main()
