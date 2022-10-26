import os
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import joblib


def get_suburb_data(suburb_data_csv_path):
    suburb_data = pd.read_csv(suburb_data_csv_path)
    return suburb_data


# NEED HELP ON THIS (TAKING FROM GeneratedPref.csv ATM)
def get_generated_preferences(generated_preferences_csv_path):
    preference_data = pd.read_csv(generated_preferences_csv_path)
    return preference_data
   

def _linear_combination(pref_row, suburbs_df, weights: dict = None):
    # default weights are all ones, i.e., all 
    if weights is None:
        weights = {colname: 1 for colname in pref_row.index}
    # copy suburbs dataframe
    score_df = suburbs_df.copy()
    # save localities and then drop non-attribute columns from scores_df
    localities = score_df["locality"]
    score_df = score_df.drop(columns=["postcode", "locality", "coordinates"])
    # compute linear combination of preferences with suburb attribute values and custom weights
    score_df = (score_df * pref_row * pd.Series(weights))
    # condense results into single summation (sum of products)
    score_df = score_df.sum(axis=1)
    # get the index of the largest value (i.e., the best suburb score)
    index = score_df.nlargest(n=1).index[0]
    # return the suburb name
    return localities.get(index)


def generate_training_data(suburb_data, preference_data):
    # Accomodation, Commute, Transport, Demographics, Environment, and Safety columns
    columns = list(suburb_data.columns[3:])

    # Normalize column values
    normalised_suburb_data = suburb_data.copy()
    ## iterate over columns and replace/create column with normalised
    for col in columns:
        normalise_col = (suburb_data[col] - suburb_data[col].min()) / (suburb_data[col].max() - suburb_data[col].min())
        normalised_suburb_data[col] = normalise_col    
    
    # Inverse safety and commute columns
    invertable_columns = [i for i in list(normalised_suburb_data.columns) if i.split("_", maxsplit=1)[0] in ["saf", "com"]]
    inv_norm_suburb_data = normalised_suburb_data.copy()
    ## iterate over columns and replace/create column with inverted
    for col in columns:
        inv_norm_suburb_data[col] = 1 - inv_norm_suburb_data[col]

    # Generate training data
    training_data = preference_data.assign(suburb = (
        preference_data
            .apply(lambda row: _linear_combination(row, inv_norm_suburb_data), axis=1)
    ))

    return training_data


def create_decision_tree(training_data): 
    # X -> features, y -> label
    X = training_data.loc[:, training_data.columns != 'suburb']
    y = training_data['suburb']
    
    # Dividing X, y into train and test data
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0)
    
    # Training a DecisionTreeClassifier
    dtree_model = DecisionTreeClassifier(max_depth=2).fit(X_train, y_train)
    # Save the model
    joblib.dump(dtree_model, 'src/dtree_model.pkl')
    print(f'Decision tree model saved in "src/dtree_model.pkl"')
    

def predict_suburb(user_preference):
    # Load the decision tree model
    dtree_model = joblib.load('src/dtree_model.pkl')

    # Convert user_preference from a List to a DataFrame
    user_preference_df = pd.DataFrame([user_preference], columns=dtree_model.feature_names_in_)

    # Predicted suburb with highest probability
    predicted_suburb = dtree_model.predict(user_preference_df)
    print("Recommended Suburb:", predicted_suburb[0])


if __name__=="__main__":
    # Load the suburb data
    suburb_data = get_suburb_data(suburb_data_csv_path = 'data/derived/SuburbData.csv')
    
    # Load the simulated user preference data
    preference_data = get_generated_preferences(generated_preferences_csv_path = 'data/derived/GeneratedPref.csv')
    
    # Generate the training data using suburb data and simulated user preference data
    training_data = generate_training_data(suburb_data = suburb_data, preference_data = preference_data)
    
    # Create the decision tree model, train it on the training data, and save the model in a .pkl file
    create_decision_tree(training_data = training_data)
    
    # Load the decision tree model and make a prediction on the best suburb to live in given a set of user preference
    predict_suburb([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])

