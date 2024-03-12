import pandas as pd
import pickle
from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor
import bz2file as bz2

def compress_pickle(title, data):
    with bz2.BZ2File(title+'.pbz2', 'w') as f:
        pickle.dump(data, f)

# Load California house price dataset
housing = fetch_california_housing()
X = pd.DataFrame(housing['data'], columns = housing.feature_names)
Y = housing['target']

# Build Regression Model
model = RandomForestRegressor()
model.fit(X, Y)

#pickle.dump(model, open('price_regression.pkl', 'wb'))
compress_pickle('price_regression', model)
