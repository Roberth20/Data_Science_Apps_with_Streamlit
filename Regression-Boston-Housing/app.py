import streamlit as st
import pandas as pd
import shap
from sklearn.datasets import fetch_california_housing
import matplotlib.pyplot as pl
import pickle
import bz2file as bz2

def decompress_pickle(file):
    data = bz2.BZ2File(file, 'rb')
    data = pickle.load(data)
    return data
    
model = decompress_pickle('Regression-Boston-Housing/price_regression.pbz2')

st.title('California House Price Prediction App')

st.write('This app predicts **California House Price**!')
st.write('---')

# Load California house price dataset
housing = fetch_california_housing()
X = pd.DataFrame(housing['data'], columns = housing.feature_names)


# Sidebar
# Header to specify input parameters
st.sidebar.header('Specify Input Parameters')

def user_input_parameters():
    MI = st.sidebar.slider('MedInc', X.MedInc.max(), X.MedInc.min(), X.MedInc.mean())
    HA = st.sidebar.slider('HouseAge', X.HouseAge.max(), X.HouseAge.min(), X.HouseAge.mean())
    AR = st.sidebar.slider('AveRooms', X.AveRooms.max(), X.AveRooms.min(), X.AveRooms.mean())
    AB = st.sidebar.slider('AveBedrms', X.AveBedrms.max(), X.AveBedrms.min(), X.AveBedrms.mean())
    P = st.sidebar.slider('Population', X.Population.max(), X.Population.min(), X.Population.mean())
    AO = st.sidebar.slider('AveOccup', X.AveOccup.max(), X.AveOccup.min(), X.AveOccup.mean())
    LA = st.sidebar.slider('Latitude', X.Latitude.max(), X.Latitude.min(), X.Latitude.mean())
    LO = st.sidebar.slider('Longitude', X.Longitude.max(), X.Longitude.min(), X.Longitude.mean())
    data = {'MedInc':MI, 'HouseAge':HA, 'AveRooms':AR, 'AveBedrms':AB, 'Population':P, 
            'AveOccup':AO, 'Latitude':LA, 'Longitude':LO}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_parameters()

# Main Panel

# Print specified input parameters
st.header('Specified Input Parameters')
st.write(df)
st.write('---')

# Apply model to make predictions
prediction = model.predict(df)

st.header('Prediction of MedHouseVal')
st.write('The value is expressed in hundreds of thousands of dollars ($100,000)')
st.write(prediction)
st.write('---')

# Explaining the model's predictions using SHAP values
# https://github.com/slundberg/shap
#explainer = shap.TreeExplainer(model)
#shap_values = explainer.shap_values(X)

#st.header('Feature Importance')
#plt.title('Feature importance based on SHAP values')
#shap.summary_plot(shap_values, X)
#st.pyplot(bbox_inches='tight')
#st.write('---')

#plt.title('Feature importance based on SHAP values (Bar)')
#shap.summary_plot(shap_values, X, plot_type='bar')
#st.pyplot(bbox_inches='tight')







