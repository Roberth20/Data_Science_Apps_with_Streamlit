import streamlit as st
import numpy as np
import pandas as pd
import pickle
from PIL import Image
from rdkit import Chem
from rdkit.Chem import Descriptors
from rdkit.Chem import rdMolDescriptors

#---------------------------#
# Custom functions
#---------------------------#
## Calculate molecular descriptors
def AromaticProportion(m):
    aromatic_atoms = [m.GetAtomWithIdx(i).GetIsAromatic() for i in range(m.GetNumAtoms())]
    aa_count = []
    for i in aromatic_atoms:
        if i == True:
            aa_count.append(1)
            
    AromaticAtom = sum(aa_count)
    HeavyAtom = Descriptors.HeavyAtomCount(m)
    AR = AromaticAtom / HeavyAtom
    return AR

def generate(smiles):
    moldata = []
    for elem in smiles:
        mol = Chem.rdmolfiles.MolFromSmiles(elem)
        moldata.append(mol)

    baseData = np.arange(1,1)
    i = 0
    for mol in moldata:
        desc_MolLogP = Descriptors.MolLogP(mol)
        desc_MolWt = Descriptors.MolWt(mol)
        desc_NumRotableBonds = rdMolDescriptors.CalcNumRotatableBonds(mol)
        desc_AromaticProportion = AromaticProportion(mol)

        row = np.array([desc_MolLogP,
                       desc_MolWt,
                       desc_NumRotableBonds,
                       desc_AromaticProportion])

        if i == 0:
            baseData = row
        else:
            baseData = np.vstack([baseData, row])

        i += 1

    columnNames = ["MolLogP","MolWt","NumRotatableBonds","AromaticProportion"]
    descriptors = pd.DataFrame(data = baseData, columns = columnNames)

    return descriptors

#---------------------------#
# Page title
#---------------------------#
## Header
st.image(Image.open('picture.jpg'), width=300)
st.title('Molecular Solubility Prediction App')
st.write('''This app predicts the **Solubility (LogS)** values of molecules!

Data obtained from the John S. Delaney. [ESOL:  Estimating Aqueous Solubility Directly from Molecular Structure](https://pubs.acs.org/doi/10.1021/ci034243x). ***J. Chem. Inf. Comput. Sci.*** 2004, 44, 3, 1000-1005.
***
''')

#---------------------------#
# Input molecules (Side panel)
#---------------------------#
st.sidebar.header('User Input Features')

## Read SMILES input
SMILE_input = "NCCCC\nCCC\nCN"

SMILES = st.sidebar.text_area('SMILES input', SMILE_input)
SMILES = "C\n" + SMILES # Adding C as a dummy, first item
SMILES = SMILES.split('\n')

st.header('Input SMILES')
SMILES[1:] # Skip first dummy item

# Calculate molecular descriptors
st.header('Computed molecular descriptors')
X = generate(SMILES)
X[1:] # Skip the dummy first

#---------------------------#
# Pre-built model
#---------------------------#
## Reads saved model
load_model = pickle.load(open('solubility_model.pkl', 'rb'))

# Apply model to make prediction
prediction = load_model.predict(X)
#prediction_proba = load_model.predict_proba(X)

st.header('Predicted LogS values')
prediction[1:] # Skips the dummy first item
#prediction_proba[1:]







