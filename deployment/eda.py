import streamlit as st

def run():
    # Note : For EDA I Only use Image from notebook EDA because it will too large to upload all image 
    st.title('Classify Species Butterfly(EDA)')
    st.image('https://t3.ftcdn.net/jpg/04/85/05/98/360_F_485059889_IxZNo1zBe86JC6SBfz8e1AT8fpCACilB.jpg')
    st.write('This page is made by Yudis Aditya')
    st.markdown('---')

    st.write('In this page, I want to show visualization about my dataset image so i can make better plan to create my model')
    st.link_button('Link dataset','https://www.kaggle.com/datasets/phucthaiv02/butterfly-image-classification')

    st.write('## 1. Identify Class Balance')
    st.image('eda1.jpg')
    st.write("From here we know that label in folder image train has 75 label/class. And from graph 'Top 5 Species' we can know that my dataset image is not balance because has different size for each class. I must do data balancing before model training")

    st.write('## 2. Visualize Image Size')
    st.image('eda2.jpg')
    st.write("From analyze above we can know that my dataset image has same size (224 x 224). It's already good for model training for classify image.")

    st.write('## 3.Visualize Sampling of Images')
    st.image('eda3.jpeg')
    st.write("These list image above are sample for every class/label. From my first impression to clasify species butterfly it's already good because to do that color is important indergredients. And filter image on edge will not work because it depend on colors.")
    
    
if __name__ == '__main__':
    run()
