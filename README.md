# 🌿 AI-Powered Plant Disease Detection System

<p align="center">

<img src="https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python">

<img src="https://img.shields.io/badge/TensorFlow-2.18-orange?style=for-the-badge&logo=tensorflow">

<img src="https://img.shields.io/badge/Keras-DeepLearning-red?style=for-the-badge&logo=keras">

<img src="https://img.shields.io/badge/Streamlit-WebApp-FF4B4B?style=for-the-badge&logo=streamlit">

<img src="https://img.shields.io/badge/Classes-38-green?style=for-the-badge">

</p>

---

## 📌 Project Overview

The **AI-Powered Plant Disease Detection System** is a deep learning-based web application designed to detect plant diseases from leaf images.

The system uses a **Convolutional Neural Network (CNN)** to classify plant leaf images into **38 different plant health and disease categories**.

Users can upload a plant leaf image through the interactive **Streamlit** web application and receive:

- 🌱 Predicted plant disease
- 🎯 Prediction confidence
- 🔍 Disease symptoms
- 💊 Disease-specific treatment information
- 🛡️ Prevention guidelines

The application uses a predefined disease-treatment database to provide treatment and prevention information.

---

## 🎯 Project Objectives

- Detect plant diseases from leaf images using deep learning
- Classify images into 38 plant disease and healthy categories
- Provide prediction confidence
- Provide disease-specific treatment information
- Provide prevention guidelines
- Develop an interactive web application using Streamlit
- Demonstrate an end-to-end deep learning inference system

---

## ✨ Features

### 🌿 Plant Disease Detection

- Upload JPG, JPEG, or PNG leaf images
- Automatic image preprocessing
- CNN-based disease classification
- 38 supported classes
- 224 × 224 input image size

### 🎯 Prediction

The application displays:

- Predicted disease
- Plant name
- Prediction confidence
- Confidence indicator

### 💊 Disease Treatment Information

The application provides predefined disease-specific information including:

- 🔍 Symptoms
- 💊 Treatment
- 🛡️ Prevention

The treatment information is stored locally in:

```text
src/ai_recommendation.py
```

The application does not require an external AI or language model to generate treatment information.

### 🖥️ Interactive Web Interface

The Streamlit application provides:

- Project information sidebar
- Image upload interface
- Prediction results
- Confidence display
- Disease treatment information
- Prevention guidelines
- Developer information

---

## 🧠 Model Information

| Property | Value |
|---|---|
| Model | Convolutional Neural Network (CNN) |
| Framework | TensorFlow / Keras |
| Input Size | 224 × 224 × 3 |
| Number of Classes | 38 |
| Activation | ReLU + Softmax |
| Optimizer | Adam |
| Loss Function | Sparse Categorical Crossentropy |
| Application Framework | Streamlit |

---

## 📊 Model Performance

| Metric | Score |
|---|---:|
| Validation Accuracy | **93.06%** |
| Validation Loss | **0.2726** |

> The confidence displayed for an individual prediction represents the model's prediction probability and does not guarantee that the prediction is correct.

---

## 🌱 Supported Plant Categories

The model supports 38 classes covering the following plant categories:

- 🍎 Apple
- 🫐 Blueberry
- 🍒 Cherry
- 🌽 Corn (Maize)
- 🍇 Grape
- 🍊 Orange
- 🍑 Peach
- 🌶️ Pepper Bell
- 🥔 Potato
- 🫐 Raspberry
- 🌱 Soybean
- 🎃 Squash
- 🍓 Strawberry
- 🍅 Tomato

The exact class labels are maintained in:

```text
src/class_names.py
```

---

## 🛠️ Technology Stack

### Programming Language

- Python 3.10

### Deep Learning

- TensorFlow 2.18
- Keras
- Convolutional Neural Network

### Image Processing

- Pillow
- NumPy

### Web Application

- Streamlit

### Development Tools

- Visual Studio Code
- Git
- GitHub
- Jupyter Notebook
- Google Colab

---

## 📂 Project Structure

```text
AI-Plant-Disease-Detection-System/
│
├── .venv/
│
├── app/
│   └── app.py
│
├── models/
│   ├── best_plant_disease_model.keras
│   └── best_plant_disease_model_fixed.keras
│
├── notebooks/
│
├── outputs/
│
├── src/
│   ├── __init__.py
│   ├── ai_recommendation.py
│   └── class_names.py
│
├── fix_model.py
├── requirements.txt
├── runtime.txt
└── README.md
```

### Important Files

#### `app/app.py`

Contains the Streamlit web application and handles:

- Image upload
- Image preprocessing
- Model prediction
- Confidence calculation
- Treatment information display

#### `models/best_plant_disease_model_fixed.keras`

The compatibility-fixed trained CNN model used by the application.

#### `src/class_names.py`

Contains the 38 class names used by the model.

#### `src/ai_recommendation.py`

Contains the predefined disease-specific:

- Symptoms
- Treatment
- Prevention

information.

#### `fix_model.py`

Utility script used to create a compatible version of the trained `.keras` model.

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/khushi1227/AI-Plant-Disease-Detection-System.git
```

## 2. Move into the Project Directory

```bash
cd AI-Plant-Disease-Detection-System
```

## 3. Create a Virtual Environment

Python 3.10 is recommended.

```bash
py -3.10 -m venv .venv
```

## 4. Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

You should see:

```text
(.venv)
```

before the terminal path.

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

## 6. Run the Application

```bash
streamlit run app/app.py
```

The application will open at:

```text
http://localhost:8501
```

---

# 🚀 Application Workflow

```text
             Leaf Image
                 │
                 ▼
       Image Preprocessing
                 │
                 ▼
         Resize to 224×224
                 │
                 ▼
             CNN Model
                 │
                 ▼
        Disease Prediction
                 │
                 ▼
         Confidence Score
                 │
                 ▼
     Disease Treatment Database
                 │
        ┌────────┼────────┐
        ▼        ▼        ▼
    Symptoms  Treatment Prevention
        │        │        │
        └────────┴────────┘
                 │
                 ▼
          Streamlit Web App
```

---

# 🔬 How the Prediction Works

1. The user uploads a plant leaf image.
2. The application reads the uploaded image.
3. The image is preprocessed.
4. The image is resized to **224 × 224 pixels**.
5. The processed image is passed to the trained CNN model.
6. The CNN generates prediction probabilities for all 38 classes.
7. The class with the highest probability is selected.
8. The application displays the predicted disease.
9. The prediction confidence is displayed.
10. The predicted disease is matched with the local treatment database.
11. The application displays symptoms, treatment, and prevention information.

---

# 💊 Disease Treatment System

The application uses a **fixed disease-specific treatment database**.

The database is stored in:

```text
src/ai_recommendation.py
```

The process is:

```text
Predicted Disease
       ↓
Disease Name Matching
       ↓
Treatment Database
       ↓
Symptoms
       ↓
Treatment
       ↓
Prevention
```

This approach provides deterministic information for supported diseases.

> Treatment information is provided for educational purposes. Users should follow applicable product labels and local agricultural guidance before using pesticides or fungicides.

---

# 🖥️ Application Interface

## Home Page

Users can upload a plant leaf image for analysis.

## Prediction Result

The application displays:

- 🌱 Predicted disease
- 🎯 Prediction confidence
- 📊 Prediction result

## Disease Treatment

The application displays:

- 🔍 Symptoms
- 💊 Treatment
- 🛡️ Prevention

## Developer Information

The application displays:

```text
Developed by

Khushi Gupta
```

---

# 📈 Future Improvements

Possible future improvements include:

- 📄 PDF disease report generation
- 📊 Prediction history
- 📱 Improved mobile interface
- 🌍 Multi-language support
- 🌱 Disease severity estimation
- 🔬 Explainable AI using Grad-CAM
- 📈 Model performance dashboard
- 🗺️ Region-specific agricultural guidance
- ☁️ Docker deployment
- 🚀 Cloud deployment

---

# 👩‍💻 Project Development

### Khushi Gupta


The current implementation includes:

- CNN-based plant disease classification
- 38 plant disease and healthy-leaf classes
- Model compatibility improvements
- Streamlit web application
- Prediction confidence display
- Disease-specific treatment database
- Symptoms and prevention information
- Customized application interface
- Developer information customization

---

# 🙏 Acknowledgements

This project uses open-source technologies and resources including:

- TensorFlow
- Keras
- Streamlit
- Python
- Plant disease image datasets
- GitHub

---

# ⚠️ Disclaimer

This application is intended for educational and demonstration purposes.

Model predictions may be incorrect, particularly for images that differ significantly from the training data.

Treatment information is general educational guidance and should not replace advice from qualified agricultural professionals.

---

## ⭐ Project

Thank you for exploring the **AI-Powered Plant Disease Detection System**.