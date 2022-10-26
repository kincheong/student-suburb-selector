
import random
import pandas as pd

from app.tests import client
from app import app, db
from app.data.models import Suburb


def test_query():
    # suburb_metadata = pd.read_csv("../../../data/derived/SuburbMetadata.csv")
    # suburb_names = suburb_metadata.locality.to_list()
    # suburb_names = random.choices(suburb_names, k=50)
    suburb_names = ['Laverton', 'Balmattum', 'Beeac', 'Winlaton', 'Montmorency', 'Bridge Creek', 'Yalla-Y-Poora', 'Walkerville', 'Drouin West', 'Clematis', 'Tooradin', 'Glenrowan West', 'Rosebery', 'Milltown', 'Wallaloo East', 'Normanville', 'Tamleugh North', 'Mount Richmond', 'Berwick', 'Traynors Lagoon']

    with app.app_context():
        for suburb in suburb_names:
            assert suburb == Suburb.query.get(suburb).name


if __name__ == "__main__":
    suburb_metadata = pd.read_csv("../../../data/derived/SuburbMetadata.csv")
    suburb_names = suburb_metadata.locality.to_list()
    print(suburb_names)
