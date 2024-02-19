import pandas as pd
import streamlit as st
from PIL import Image
import altair as alt

image = Image.open('dna-logo.jpg')

st.image(image, use_column_width=True)

st.write("""
         # DNA Nucleotide Count Web App
         
         This App counts the nucleotide composition of query DNA
         
         ***
         """)
    
st.header('Enter DNA sequence')

sequence_input = ">DNA Query \nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

sequence = st.text_area("Sequence input", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:] # Skip the first line
sequence = ''.join(sequence) # Re-join list of strings

st.write("***")

# Print input DNA sequence
st.header("INPUT (DNA Query)")
sequence

# DNA nucleotide count
st.header('OUTPUT (DNA Nucleotide Count)')

### 1. Print dictionary
st.subheader('1. Print dictionary')
def DNA_nucleotide_count(seq):
    d = dict([
            ('A', seq.count('A')),
            ('T', seq.count('T')),
            ('G', seq.count('G')),
            ('C', seq.count('C'))
        ])
    return d

X = DNA_nucleotide_count(sequence)
X_label = list(X)
X_values = list(X.values())

X

### 2. Print text
st.subheader("2. Print text")
st.write(f"There are {X['A']} adenine (A)")
st.write(f"There are {X['T']} thymine (T)")
st.write(f"There are {X['G']} guanine (G)")
st.write(f"There are {X['C']} cytosine (C)")

### 3. Display DataFrame
st.subheader("3. Display DataFrame")
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis=1)
df.reset_index(inplace=True)
df = df.rename(columns={'index':'nucleotide'})
st.write(df)

### 4. Display Bar chart using Altair
st.subheader('4. Display Bar Chart')
p = alt.Chart(df).mark_bar(size=50).encode(x = 'nucleotide', 
                                    y = 'count')

p.properties(width = 800) # width of the bar

st.altair_chart(p, use_container_width=True)







