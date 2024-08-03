# Project Name

This project called "Classify Species Butterfly from Image using Neural Network and Computer Vision". This project is part of my personal portofolio in Data Science. My other personal project can be found at the [Nyoman Yudis Developer](https://github.com/nyomanyudisdeveloper)

#### -- Project Status: On-Hold

## Project Intro/Objective

The purpose of this project is to classify species butterfly from image using method computer vision and neuron neural network. This project will make benefit to make identify species easier in order for conservation, understand distribution and population species butterfly can help to make better decision related their habitat preservation.

### Methods Used

- Computer vision
- Neuron Neural Network
- Data Visualization
- Data Image Augmentation

### Technologies

- Python
- Pandas
- Numpy
- Matplotlib
- Seaborn
- Sklearn
- cv2
- Tensorflow
- Streamlit

## Project Description

The dataset i use to create this model is from [here](https://www.kaggle.com/datasets/phucthaiv02/butterfly-image-classification/data) where contain two folder image, folder train contain file csv with column filename and species label That will used for model training. and folder test contain file csv with only column filename for model inference.
After do exploratory data analysis (EDA) i found that this dataset has inbalance label which is give bad impact on process model training, every image has same size which is good and save effort to resize image. And because the goal of this project is to identufy species butterfly that color is important part, so i dont need to modify Color Channel anymore.
In feature engineer i have split data train and test , and try to make balance my label dataset by using method data image augmentation and balancing. And for modelling i used pre trained model MobileNetV2 because to save resource and have many usage for classify image.

## Getting Started

1. Clone this repo (for help see this [tutorial](https://help.github.com/articles/cloning-a-repository/)).
2. For process Feature Engineer, Exploratory Data Analysis (EDA), Image Data Augmentation, Model Training, Model Evaluation, and Model Improvement is being kept in file P2G7_yudis_aditya.ipynb
3. Model inference script is being kept in file P2G7_yudis_aditya_inference.ipynb
4. Streamlit for deployment to hunggigface script are being kepy in folder deployment
5. Raw data is being kept [here](https://www.kaggle.com/datasets/phucthaiv02/butterfly-image-classification/data)

## Featured Notebooks/Analysis/Deliverables

- [Hungging Face for model usage demonstration](https://huggingface.co/spaces/nyomanyudisdeveloper/ButterflySpeciesClassifyCV)

## Contact

- If you have any question or want to contribute with this project, feel free to ask me in [linkedin](https://www.linkedin.com/in/yudit-a-9941ab318/) or my partners.
