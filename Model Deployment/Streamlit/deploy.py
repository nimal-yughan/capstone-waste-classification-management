import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
from PIL import Image

model_path = 'vgg16_b32_f.h5'
sample_data = 'test1.jpg'
class_subset=['cardboard', 'ewaste', 'glass', 'metal','organic', 'paper', 'plastic']

def load_models():
    model=load_model(model_path,compile=False)
    return model

def check_type(a):
    if(a=='organic'):
        return 'Bio-degradable'
    elif(a=='ewaste'):
        return 'E-Waste'
    else:
        return 'Recyclable'

st.title('Waste Classification GUI')
st.markdown('The CNN model will classify the image into its corresponding class and map to the broad category!!')
st.markdown('To view prdiction result you may use the sample data provided or upload your own image.')

st.sidebar.title('Your Choice:')
user_choice = st.sidebar.selectbox("Choose an option:", ["Sample Data", "Upload Image"])
if user_choice == "Sample Data":
    st.header("Sample prediction for waste")
    if st.checkbox('View Sample Image'):
        st.info("Sample image")
        img = Image.open(sample_data)
        img = img.resize((224, 224))
        st.image(img, caption='Sample Data')
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        img_array2 = tf.keras.applications.vgg16.preprocess_input(img_array)
        img_array2 = tf.expand_dims(img_array2, 0)
        st.subheader("Check prediction result")
        if st.checkbox('Sample image Result'):
            model=load_models()
            result=model.predict(img_array2)
            predicted_class = class_subset[np.argmax(result[0])]
            confidence = round(100 * (np.max(result[0])), 2)
            category= check_type(predicted_class)
            st.write(confidence, predicted_class, category)
            st.success("Here is the prediction!")

if user_choice == "Upload Image":
    st.header("Upload the image for prediction below:")
    uploaded_file = st.file_uploader("Choose your image", type=["jpg", "png"])
    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        st.info("View your image:")
        img = img.resize((224, 224))
        st.image(img, caption="Uploaded image")
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        img_array2 = tf.keras.applications.vgg16.preprocess_input(img_array)
        img_array2 = tf.expand_dims(img_array2, 0)
        st.subheader("Check prediction result")
        if st.checkbox('View Prediction Result'):
            model=load_models()
            result=model.predict(img_array2)
            predicted_class = class_subset[np.argmax(result[0])]
            confidence = round(100 * (np.max(result[0])), 2)
            category= check_type(predicted_class)
            st.write(confidence, predicted_class, category)
            st.success("Here is the prediction!")

        
            
        
