import streamlit as st
import pandas as pd 
import json 
import pickle 
import numpy as np
import tensorflow as tf
from keras.models import load_model

model = load_model("model_after.h5")

with open('dict_butterfly_index.json','r') as file_2:
    dict_butterfly_index = json.load(file_2)

def run():
    with st.form('prediction_form'):
        st.write('Personal Information')
        uploaded = st.file_uploader(label='Input File Image',type=['png','jpg'])

        
        submitted = st.form_submit_button()
    
    st.write("Result Prediction")
    if submitted:
        img = tf.keras.utils.load_img(uploaded, target_size=(224, 224))
        x = tf.keras.utils.img_to_array(img)/255
        

        x = np.expand_dims(x, axis=0)
        images = np.vstack((x,x))
        classes = model.predict(images, batch_size=10)
        idx = np.argmax(classes[0])
        st.write(f"The predictions is = {dict_butterfly_index[str(idx)]}")
        st.image(img,caption="Uploaded Image", use_column_width=True)
            


if __name__ == '__main__':
    run()