import pytest
import pandas as pd
import joblib

MODEL = joblib.load('../../dtree_model.pkl')
preference_data = pd.read_csv('../../../data/derived/GeneratedPref.csv')

# preference_data = pd.read_csv('data/derived/GeneratedPref.csv')
# list(preference_data.iloc[1010])

def test_1():
    preference = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    preference_df = pd.DataFrame([preference], columns=MODEL.feature_names_in_)
    recommended_suburb = MODEL.predict(preference_df)[0]
    assert recommended_suburb in MODEL.classes_

def test_2():
    preference = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    preference_df = pd.DataFrame([preference], columns=MODEL.feature_names_in_)
    recommended_suburb = MODEL.predict(preference_df)[0]
    assert recommended_suburb in MODEL.classes_

def test_3():
    preference = [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 0, 0, 0, 0, 3, 0, 3, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    preference_df = pd.DataFrame([preference], columns=MODEL.feature_names_in_)
    recommended_suburb = MODEL.predict(preference_df)[0]
    assert recommended_suburb in MODEL.classes_

def test_4():
    preference = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 2, 2, 0, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    preference_df = pd.DataFrame([preference], columns=MODEL.feature_names_in_)
    recommended_suburb = MODEL.predict(preference_df)[0]
    assert recommended_suburb in MODEL.classes_

def test_5():
    preference = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
    preference_df = pd.DataFrame([preference], columns=MODEL.feature_names_in_)
    recommended_suburb = MODEL.predict(preference_df)[0]
    assert recommended_suburb in MODEL.classes_
