from git import Object
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import pickle


st.title("Car Price Prediction", "<h1 style='text-align: left; color: grey;'>Big headline</h1>")
image = Image.open('car1.jpg')
st.sidebar.image(image, caption='Enter Specifications')


final_scaler = pickle.load(open("final_auto", 'rb'))
model = pickle.load(open('final_as', 'rb'))
columns_name = pickle.load(open("columns", 'rb'))

#select box
make_model = st.sidebar.selectbox('Model', ('Audi A1', 'Audi A2', 'Audi A3', 'Opel Astra', 'Opel Corsa','Opel Insignia', 'Renault Clio', 'Renault Duster', 'Renault Espace'))


   
Gearing_Type=st.sidebar.selectbox('Gearing_Type', ('Automatic', 'Manual', 'Semi-automatic'))
hp_kW = st.sidebar.number_input("hp:", step=1)
age = st.sidebar.number_input("age:", step=1)
km = st.sidebar.number_input("km:", step=1)
my_dict = {
    "hp": hp_kW,
    "age": age,
    "km": km,
    "Model": make_model,
    "Gearing_Type": Gearing_Type
}
if 'Audi A1' in make_model:
    image = Image.open('audia1.jpg')
    st.image(image, caption='Audi A1')
elif 'Audi A2' in make_model:
    image = Image.open('audia2.jpg')
    st.image(image, caption='Audi A2')
elif 'Audi A3' in make_model:
    image = Image.open('audia3.jpg')
    st.image(image, caption='Audi A3')
elif 'Opel Astra' in make_model:
    image = Image.open('astra.jpg')
    st.image(image, caption='Opel Astra')
elif 'Opel Corsa' in make_model:
    image = Image.open('corsa.jpg')
    st.image(image, caption='Opel Corsa')
elif 'Opel Insignia' in make_model:
    image = Image.open('insignia.jpg')
    st.image(image, caption='Opel Insignia')
elif 'Renault Clio' in make_model:
    image = Image.open('clio.jpg')
    st.image(image, caption='Renault Clio')
elif 'Renault Duster' in make_model:
    image = Image.open('duster.jpg')
    st.image(image, caption='Renault Duster')
elif 'Renault Espace' in make_model:
    image = Image.open('espace.jpg')
    st.image(image, caption='Renault Espace')    
else:
    image = Image.open('car1.jpg')
df=pd.DataFrame([my_dict])

dum = pd.get_dummies(df)

my_dict = dum.reindex(columns=columns_name, fill_value=0)

my_dict = final_scaler.transform(my_dict)

if st.button("Estimated Price"):
    pred = model.predict(my_dict)
    st.write("%.f" % pred[0],"€")