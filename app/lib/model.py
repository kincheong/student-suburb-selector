
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

training_data = pd.read_csv('data/derived/TrainingData.csv')

# X -> features, y -> label
X = training_data.loc[:, training_data.columns != 'suburb']
y = training_data['suburb']
  
# Dividing X, y into train and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0)
  
# Training a DecisionTreeClassifier
MODEL = DecisionTreeClassifier()
MODEL.fit(X_train, y_train)

# read model from file
# the model is read outside the function to ensure it is 'pre-loaded'
#MODEL = joblib.load("dtree_model.pkl")


def get_suburb_from_prefs(prefs: dict):

    # Convert prefs to a DataFrame
    user_preference = pd.DataFrame(prefs, index=[0])
    
    # Ensure order of columns in user preference data is same as training data
    user_preference = user_preference[MODEL.feature_names_in_]

    # Predict recommended suburb using model
    recommended_suburb = MODEL.predict(user_preference)[0]
    
    # Return the recommended suburb
    return recommended_suburb


if __name__ == "__main__":
    get_suburb_from_prefs({})
