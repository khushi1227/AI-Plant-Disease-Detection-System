import streamlit as st

import numpy as np
from PIL import Image
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
from src.ai_recommendation import get_treatment_recommendation

import os
import sys

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.class_names import CLASS_NAMES


# -------------------------------
# Page Configuration
# -------------------------------

st.set_page_config(
    page_title="🌿 Plant Disease Detection",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------
# Load Trained CNN Model
# -------------------------------

MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "models",
    "best_plant_disease_model.keras"
)

@st.cache_resource
def load_cnn_model():
    return load_model(MODEL_PATH)

cnn_model = load_cnn_model()

# -------------------------------
# Sidebar
# -------------------------------

st.sidebar.title("🌿 Project Information")

st.sidebar.markdown("""
### 🌱 AI Plant Disease Detection

🤖 **Model:** CNN

📊 **Classes:** 38

🖼️ **Input Size:** 224 × 224

🎯 **Validation Accuracy:** 93.06%

⚙️ **Framework:** TensorFlow + Streamlit
""")

st.sidebar.divider()

st.sidebar.success("Developed by\n\n**Mukul Chakravorty**")

# -------------------------------
# Load Class Names
# -------------------------------

from src.class_names import CLASS_NAMES

class_names = CLASS_NAMES

# -------------------------------
# Prediction Function
# -------------------------------

def predict_disease(img):

    # Resize Image
    img = img.resize((224, 224))

    # Convert to Array
    img_array = image.img_to_array(img)

    # Add Batch Dimension
    img_array = np.expand_dims(img_array, axis=0)

    # Prediction
    prediction = cnn_model.predict(img_array, verbose=0)

    predicted_class = class_names[np.argmax(prediction)]
    confidence = float(np.max(prediction))
    display_name = (
    predicted_class
    .replace("___", " - ")
    .replace("_", " ")
    .title()
)


    return predicted_class, display_name, confidence

# -------------------------------
# Main Title
# -------------------------------

st.title("🌿 AI-Powered Plant Disease Detection System")

st.markdown("""
Detect plant diseases instantly using a trained Convolutional Neural Network (CNN).  
Upload a clear leaf image to receive the predicted disease and confidence score.
""")

st.divider()

# -------------------------------
# File Upload
# -------------------------------

uploaded_file = st.file_uploader(
    "📤 Upload a Leaf Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    img = Image.open(uploaded_file)

    st.image(
        img,
        caption="📷 Uploaded Leaf Image",
        use_container_width=False,
        width=400
    )
    st.write("")
    

    # -------------------------------
    # Predict Button
    # -------------------------------

    if st.button("🔍 Predict Disease", use_container_width=True):

        with st.spinner("Analyzing leaf image..."):

            predicted_class, display_name, confidence = predict_disease(img)

        st.success("Prediction Completed ✅")

        st.subheader("Prediction Result")

        st.markdown("## 🌿 Predicted Disease")

        st.success(display_name)
        if "healthy" in predicted_class.lower():

            st.success("🌿 Plant appears Healthy.")

        else:

            st.error("⚠ Disease Detected. Please inspect the plant carefully.")

        st.markdown("## 🎯 Prediction Confidence")
        st.metric(
            label="Model Confidence",
            value=f"{confidence:.2%}"
        )

        st.progress(confidence)
        if confidence >= 0.95:

            st.success("✅ High Confidence Prediction")

        elif confidence >= 0.80:

            st.warning("⚠ Medium Confidence Prediction")

        else:

            st.error("❌ Low Confidence Prediction")

        # Integrating with AI for Recommendation after forming a test file in SRC folder with name ai_recommendation.py

        if "healthy" not in predicted_class.lower():
            st.divider()

            st.subheader("🤖 AI Treatment Recommendation")

            with st.spinner("Generating AI recommendation...."):

                try:

                    recommendation = get_treatment_recommendation(display_name)

                    st.markdown(recommendation)

                except Exception as e:

                    st.error(f"Failed to generate AI recommendation.\n\n{e}")
                


            st.divider()

        st.caption(
        "🌱 Built with TensorFlow • Keras • Streamlit | © Mukul Chakravorty"
        )