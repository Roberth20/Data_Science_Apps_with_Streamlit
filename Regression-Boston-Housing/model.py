import pandas as pd
import pickle
from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor

# Load California house price dataset
housing = fetch_california_housing()
X = pd.DataFrame(housing['data'], columns = housing.feature_names)
Y = housing['target']

# Build Regression Model
model = RandomForestRegressor()
model.fit(X, Y)

pickle.dump(model, open('price_regression.pkl', 'wb'))