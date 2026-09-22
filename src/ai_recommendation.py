# Fixed disease-specific treatment information
# No AI API or Hugging Face model is used.

TREATMENTS = {

    # =========================
    # APPLE
    # =========================

    "Apple___Apple_scab": {
        "description": "A fungal disease affecting apple leaves and fruit.",
        "symptoms": [
            "Olive-green or brown spots on leaves",
            "Dark lesions may develop on fruit",
            "Severe infections can cause premature leaf drop"
        ],
        "treatment": [
            "Remove severely infected leaves and fruit",
            "Remove fallen leaves and infected plant debris",
            "Improve air circulation through pruning",
            "Use an appropriate fungicide according to its label and local guidance"
        ],
        "prevention": [
            "Keep the area around trees clean",
            "Remove fallen infected leaves",
            "Prune dense branches",
            "Monitor plants regularly during favorable disease conditions"
        ]
    },

    "Apple___Black_rot": {
        "description": "A fungal disease that can affect apple leaves, branches and fruit.",
        "symptoms": [
            "Purple or brown leaf spots",
            "Dark lesions on fruit",
            "Fruit may become shriveled or mummified"
        ],
        "treatment": [
            "Remove infected fruit and plant material",
            "Prune severely affected branches",
            "Remove mummified fruit from the tree and ground",
            "Use an appropriate fungicide according to its label"
        ],
        "prevention": [
            "Maintain good orchard sanitation",
            "Remove dead or infected wood",
            "Improve air circulation",
            "Monitor plants regularly"
        ]
    },

    "Apple___Cedar_apple_rust": {
        "description": "A fungal disease that can cause characteristic rust-colored symptoms on apple leaves.",
        "symptoms": [
            "Yellow-orange spots on leaves",
            "Orange or rust-colored structures on the underside of leaves",
            "Premature leaf damage in severe infections"
        ],
        "treatment": [
            "Remove severely affected plant material where practical",
            "Improve air circulation",
            "Remove nearby alternate hosts where appropriate",
            "Use an appropriate fungicide according to its label"
        ],
        "prevention": [
            "Monitor plants during the growing season",
            "Maintain good orchard sanitation",
            "Improve air circulation through pruning",
            "Use disease-resistant varieties where available"
        ]
    },

    "Apple___healthy": {
        "description": "No visible disease was detected by the model.",
        "symptoms": [
            "No major disease symptoms detected"
        ],
        "treatment": [
            "No disease treatment is required based on this prediction",
            "Continue normal plant care",
            "Monitor the plant regularly"
        ],
        "prevention": [
            "Provide adequate sunlight and water",
            "Maintain good soil and plant nutrition",
            "Remove damaged plant material",
            "Monitor regularly for new symptoms"
        ]
    },

    # =========================
    # BLUEBERRY
    # =========================

    "Blueberry___healthy": {
        "description": "No visible disease was detected by the model.",
        "symptoms": [
            "No major disease symptoms detected"
        ],
        "treatment": [
            "No disease treatment is required based on this prediction",
            "Continue normal plant care"
        ],
        "prevention": [
            "Maintain suitable soil moisture",
            "Provide adequate sunlight",
            "Maintain good air circulation",
            "Monitor plants regularly"
        ]
    },

    # =========================
    # CHERRY
    # =========================

    "Cherry_(including_sour)___Powdery_mildew": {
        "description": "A fungal disease characterized by powdery growth on leaves and shoots.",
        "symptoms": [
            "White powdery growth on leaves",
            "Distorted or curled leaves",
            "Reduced plant vigor"
        ],
        "treatment": [
            "Remove severely affected plant material",
            "Improve air circulation",
            "Avoid excessive nitrogen fertilization",
            "Use an appropriate fungicide according to its label"
        ],
        "prevention": [
            "Maintain adequate spacing",
            "Prune dense growth",
            "Monitor new leaves regularly",
            "Avoid conditions that promote excessive humidity"
        ]
    },

    "Cherry_(including_sour)___healthy": {
        "description": "No visible disease was detected by the model.",
        "symptoms": [
            "No major disease symptoms detected"
        ],
        "treatment": [
            "No disease treatment is required",
            "Continue regular plant care"
        ],
        "prevention": [
            "Maintain good air circulation",
            "Provide adequate sunlight and water",
            "Remove damaged plant material",
            "Monitor regularly"
        ]
    },

    # =========================
    # CORN
    # =========================

    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": {
        "description": "A fungal disease that produces gray or brown leaf lesions.",
        "symptoms": [
            "Long rectangular gray or brown lesions",
            "Lesions commonly appear on leaves",
            "Severe infections can reduce healthy leaf area"
        ],
        "treatment": [
            "Remove heavily infected plant debris after harvest",
            "Improve field sanitation",
            "Use disease-management products when appropriate",
            "Follow local agricultural recommendations"
        ],
        "prevention": [
            "Practice crop rotation",
            "Use resistant varieties where available",
            "Maintain appropriate plant spacing",
            "Monitor fields regularly"
        ]
    },

    "Corn_(maize)___Common_rust_": {
        "description": "A fungal disease producing reddish-brown rust pustules on corn leaves.",
        "symptoms": [
            "Small reddish-brown pustules",
            "Rust-colored spots on leaves",
            "Premature drying of severely affected leaves"
        ],
        "treatment": [
            "Monitor disease development",
            "Remove severely affected plant material where practical",
            "Use appropriate disease-management products when recommended",
            "Follow local agricultural guidance"
        ],
        "prevention": [
            "Use resistant varieties when available",
            "Maintain appropriate plant density",
            "Practice good field sanitation",
            "Monitor crops regularly"
        ]
    },

    "Corn_(maize)___Northern_Leaf_Blight": {
        "description": "A fungal disease that produces elongated lesions on corn leaves.",
        "symptoms": [
            "Long gray-green or brown lesions",
            "Lesions may enlarge and merge",
            "Reduced healthy leaf area in severe infections"
        ],
        "treatment": [
            "Remove infected crop debris after harvest",
            "Use resistant varieties where available",
            "Use appropriate fungicide management when recommended",
            "Follow local agricultural guidance"
        ],
        "prevention": [
            "Practice crop rotation",
            "Use resistant hybrids where available",
            "Maintain field sanitation",
            "Monitor crops during humid conditions"
        ]
    },

    "Corn_(maize)___healthy": {
        "description": "No visible disease was detected by the model.",
        "symptoms": [
            "No major disease symptoms detected"
        ],
        "treatment": [
            "No disease treatment is required",
            "Continue normal crop management"
        ],
        "prevention": [
            "Maintain adequate plant nutrition",
            "Provide appropriate irrigation",
            "Keep fields clean",
            "Monitor crops regularly"
        ]
    },

    # =========================
    # GRAPE
    # =========================

    "Grape___Black_rot": {
        "description": "A fungal disease affecting grape leaves, shoots and berries.",
        "symptoms": [
            "Brown circular leaf spots",
            "Dark lesions on berries",
            "Infected berries may shrivel and become mummified"
        ],
        "treatment": [
            "Remove infected berries and leaves",
            "Remove mummified fruit",
            "Improve air circulation within the canopy",
            "Use an appropriate fungicide according to its label"
        ],
        "prevention": [
            "Maintain vineyard sanitation",
            "Prune dense growth",
            "Remove infected plant material",
            "Monitor plants regularly"
        ]
    },

    "Grape___Esca_(Black_Measles)": {
        "description": "A complex grapevine disease associated with fungal infection and internal wood damage.",
        "symptoms": [
            "Leaf discoloration",
            "Interveinal spotting or streaking",
            "Fruit may develop dark spots",
            "Affected vines may show reduced vigor"
        ],
        "treatment": [
            "Remove severely affected plant material where appropriate",
            "Prune carefully and remove infected wood",
            "Avoid spreading contaminated pruning equipment",
            "Seek local vineyard disease-management guidance"
        ],
        "prevention": [
            "Use healthy planting material",
            "Disinfect pruning tools",
            "Protect pruning wounds where recommended",
            "Remove severely affected vines when necessary"
        ]
    },

    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
        "description": "A fungal leaf disease that causes spots and blight symptoms on grape foliage.",
        "symptoms": [
            "Dark leaf spots",
            "Brown or necrotic areas",
            "Progressive leaf damage"
        ],
        "treatment": [
            "Remove severely affected leaves",
            "Improve canopy ventilation",
            "Remove infected plant debris",
            "Use an appropriate fungicide according to its label"
        ],
        "prevention": [
            "Maintain good vineyard sanitation",
            "Prune dense foliage",
            "Avoid prolonged leaf wetness",
            "Monitor plants regularly"
        ]
    },

    "Grape___healthy": {
        "description": "No visible disease was detected by the model.",
        "symptoms": [
            "No major disease symptoms detected"
        ],
        "treatment": [
            "No disease treatment is required",
            "Continue regular vineyard management"
        ],
        "prevention": [
            "Maintain good canopy management",
            "Provide adequate nutrition",
            "Maintain good sanitation",
            "Monitor vines regularly"
        ]
    },

    # =========================
    # ORANGE
    # =========================

    "Orange___Haunglongbing_(Citrus_greening)": {
        "description": "A serious citrus disease that affects plant health and fruit production.",
        "symptoms": [
            "Uneven yellowing of leaves",
            "Blotchy leaf patterns",
            "Reduced plant vigor",
            "Small or poorly developed fruit may occur"
        ],
        "treatment": [
            "There is no simple curative treatment for an infected tree",
            "Remove severely affected trees according to local guidance",
            "Control the insect vector according to integrated pest-management recommendations",
            "Consult a local citrus specialist or agricultural extension service"
        ],
        "prevention": [
            "Use certified healthy planting material",
            "Monitor for insect vectors",
            "Remove infected trees when recommended",
            "Follow local citrus disease-management programs"
        ]
    },

    # =========================
    # PEACH
    # =========================

    "Peach___Bacterial_spot": {
        "description": "A bacterial disease that can affect peach leaves and fruit.",
        "symptoms": [
            "Small dark spots on leaves",
            "Yellowing around leaf lesions",
            "Spots or lesions on fruit"
        ],
        "treatment": [
            "Remove severely affected plant material where practical",
            "Improve air circulation",
            "Avoid unnecessary overhead irrigation",
            "Use disease-management products according to local recommendations"
        ],
        "prevention": [
            "Maintain orchard sanitation",
            "Use healthy planting material",
            "Avoid prolonged leaf wetness",
            "Monitor plants regularly"
        ]
    },

    "Peach___healthy": {
        "description": "No visible disease was detected by the model.",
        "symptoms": [
            "No major disease symptoms detected"
        ],
        "treatment": [
            "No disease treatment is required",
            "Continue normal orchard care"
        ],
        "prevention": [
            "Maintain good air circulation",
            "Provide appropriate irrigation",
            "Maintain orchard sanitation",
            "Monitor plants regularly"
        ]
    },

    # =========================
    # PEPPER
    # =========================

    "Pepper,_bell___Bacterial_spot": {
        "description": "A bacterial disease affecting pepper leaves and fruit.",
        "symptoms": [
            "Small dark spots on leaves",
            "Yellow halos around lesions",
            "Raised or scabby spots on fruit"
        ],
        "treatment": [
            "Remove severely infected plant material",
            "Avoid overhead watering",
            "Improve air circulation",
            "Use appropriate disease-management products according to local guidance"
        ],
        "prevention": [
            "Use healthy seed and planting material",
            "Avoid working with wet plants",
            "Maintain adequate spacing",
            "Practice crop rotation"
        ]
    },

    "Pepper,_bell___healthy": {
        "description": "No visible disease was detected by the model.",
        "symptoms": [
            "No major disease symptoms detected"
        ],
        "treatment": [
            "No disease treatment is required",
            "Continue normal plant care"
        ],
        "prevention": [
            "Maintain good soil moisture",
            "Provide adequate sunlight",
            "Maintain plant spacing",
            "Monitor plants regularly"
        ]
    },

    # =========================
    # POTATO
    # =========================

    "Potato___Early_blight": {
        "description": "A fungal disease that commonly affects potato foliage.",
        "symptoms": [
            "Dark circular spots on leaves",
            "Concentric rings within lesions",
            "Yellowing around infected areas"
        ],
        "treatment": [
            "Remove severely affected foliage where practical",
            "Improve field sanitation",
            "Avoid prolonged leaf wetness",
            "Use an appropriate fungicide according to its label"
        ],
        "prevention": [
            "Practice crop rotation",
            "Use healthy planting material",
            "Remove infected crop debris",
            "Monitor crops regularly"
        ]
    },

    "Potato___Late_blight": {
        "description": "A serious disease that can rapidly damage potato foliage and tubers.",
        "symptoms": [
            "Dark water-soaked leaf lesions",
            "Rapid browning of foliage",
            "Dark lesions may occur on tubers"
        ],
        "treatment": [
            "Remove severely affected plant material where practical",
            "Improve field sanitation",
            "Avoid prolonged leaf wetness",
            "Use appropriate fungicide management according to local recommendations"
        ],
        "prevention": [
            "Use certified healthy seed potatoes",
            "Monitor crops frequently",
            "Avoid excessive leaf wetness",
            "Remove infected plant debris"
        ]
    },

    "Potato___healthy": {
        "description": "No visible disease was detected by the model.",
        "symptoms": [
            "No major disease symptoms detected"
        ],
        "treatment": [
            "No disease treatment is required",
            "Continue normal crop management"
        ],
        "prevention": [
            "Use healthy planting material",
            "Maintain appropriate irrigation",
            "Practice crop rotation",
            "Monitor plants regularly"
        ]
    },

    # =========================
    # RASPBERRY
    # =========================

    "Raspberry___healthy": {
        "description": "No visible disease was detected by the model.",
        "symptoms": [
            "No major disease symptoms detected"
        ],
        "treatment": [
            "No disease treatment is required",
            "Continue normal plant care"
        ],
        "prevention": [
            "Maintain good air circulation",
            "Remove damaged plant material",
            "Provide appropriate water and nutrition",
            "Monitor plants regularly"
        ]
    },

    # =========================
    # SOYBEAN
    # =========================

    "Soybean___healthy": {
        "description": "No visible disease was detected by the model.",
        "symptoms": [
            "No major disease symptoms detected"
        ],
        "treatment": [
            "No disease treatment is required",
            "Continue normal crop management"
        ],
        "prevention": [
            "Maintain appropriate soil moisture",
            "Provide balanced plant nutrition",
            "Maintain field sanitation",
            "Monitor crops regularly"
        ]
    },

    # =========================
    # SQUASH
    # =========================

    "Squash___Powdery_mildew": {
        "description": "A fungal disease producing white powdery growth on squash leaves.",
        "symptoms": [
            "White powdery patches on leaves",
            "Yellowing or browning of affected foliage",
            "Reduced plant vigor"
        ],
        "treatment": [
            "Remove severely affected leaves",
            "Improve air circulation",
            "Avoid excessive nitrogen fertilization",
            "Use an appropriate fungicide according to its label"
        ],
        "prevention": [
            "Provide adequate plant spacing",
            "Avoid prolonged humidity around foliage",
            "Monitor plants regularly",
            "Use resistant varieties when available"
        ]
    },

    # =========================
    # STRAWBERRY
    # =========================

    "Strawberry___Leaf_scorch": {
        "description": "A fungal leaf disease that causes dark lesions and scorched-looking foliage.",
        "symptoms": [
            "Small dark purple or brown spots",
            "Spots may merge into larger damaged areas",
            "Leaves can appear scorched"
        ],
        "treatment": [
            "Remove severely affected leaves",
            "Remove infected plant debris",
            "Improve air circulation",
            "Use appropriate disease-management products according to local guidance"
        ],
        "prevention": [
            "Maintain plant spacing",
            "Avoid prolonged leaf wetness",
            "Remove old infected leaves",
            "Monitor plants regularly"
        ]
    },

    "Strawberry___healthy": {
        "description": "No visible disease was detected by the model.",
        "symptoms": [
            "No major disease symptoms detected"
        ],
        "treatment": [
            "No disease treatment is required",
            "Continue normal plant care"
        ],
        "prevention": [
            "Maintain good air circulation",
            "Provide appropriate irrigation",
            "Remove damaged leaves",
            "Monitor plants regularly"
        ]
    },

    # =========================
    # TOMATO
    # =========================

    "Tomato___Bacterial_spot": {
        "description": "A bacterial disease affecting tomato leaves, stems and fruit.",
        "symptoms": [
            "Small dark spots on leaves",
            "Yellow halos around lesions",
            "Dark spots may develop on fruit"
        ],
        "treatment": [
            "Remove severely infected plant material",
            "Avoid overhead watering",
            "Improve air circulation",
            "Use appropriate disease-management products according to local guidance"
        ],
        "prevention": [
            "Use healthy seed and planting material",
            "Avoid handling wet plants",
            "Maintain adequate spacing",
            "Practice crop rotation"
        ]
    },

    "Tomato___Early_blight": {
        "description": "A fungal disease commonly affecting tomato leaves and stems.",
        "symptoms": [
            "Dark circular leaf spots",
            "Concentric ring patterns",
            "Yellowing around lesions"
        ],
        "treatment": [
            "Remove severely infected leaves",
            "Remove infected plant debris",
            "Avoid overhead watering",
            "Use an appropriate fungicide according to its label"
        ],
        "prevention": [
            "Maintain adequate plant spacing",
            "Keep foliage dry where practical",
            "Practice crop rotation",
            "Monitor plants regularly"
        ]
    },

    "Tomato___Late_blight": {
        "description": "A disease that can rapidly damage tomato foliage and fruit.",
        "symptoms": [
            "Dark water-soaked lesions",
            "Rapid browning of leaves",
            "Dark lesions may appear on fruit"
        ],
        "treatment": [
            "Remove severely affected plant material",
            "Improve air circulation",
            "Avoid prolonged leaf wetness",
            "Use appropriate disease-management products according to local guidance"
        ],
        "prevention": [
            "Monitor plants frequently",
            "Avoid overhead irrigation",
            "Remove infected plant debris",
            "Maintain adequate plant spacing"
        ]
    },

    "Tomato___Leaf_Mold": {
        "description": "A fungal disease that commonly develops under humid conditions.",
        "symptoms": [
            "Yellow patches on upper leaf surfaces",
            "Olive-green or grayish fungal growth underneath leaves",
            "Leaf yellowing and drying"
        ],
        "treatment": [
            "Remove severely affected leaves",
            "Improve ventilation",
            "Reduce excessive humidity",
            "Use an appropriate fungicide according to its label"
        ],
        "prevention": [
            "Improve greenhouse or field ventilation",
            "Avoid excessive humidity",
            "Provide adequate plant spacing",
            "Remove infected plant debris"
        ]
    },

    "Tomato___Septoria_leaf_spot": {
        "description": "A fungal disease that causes numerous small spots on tomato leaves.",
        "symptoms": [
            "Small circular leaf spots",
            "Dark margins around lesions",
            "Tiny dark structures may occur inside spots"
        ],
        "treatment": [
            "Remove infected lower leaves",
            "Remove plant debris",
            "Avoid overhead watering",
            "Use an appropriate fungicide according to its label"
        ],
        "prevention": [
            "Maintain good sanitation",
            "Keep foliage dry where possible",
            "Use adequate plant spacing",
            "Practice crop rotation"
        ]
    },

    "Tomato___Spider_mites Two-spotted_spider_mite": {
        "description": "Damage caused by spider mites feeding on tomato foliage.",
        "symptoms": [
            "Fine yellow or pale speckling on leaves",
            "Leaf bronzing or drying",
            "Fine webbing may appear in severe infestations"
        ],
        "treatment": [
            "Remove heavily infested leaves where practical",
            "Use a suitable mite-management product according to its label",
            "Monitor the underside of leaves",
            "Avoid unnecessary broad-spectrum pesticide use where it may harm beneficial organisms"
        ],
        "prevention": [
            "Monitor plants regularly",
            "Maintain appropriate plant hydration",
            "Control weeds that may harbor mites",
            "Encourage beneficial predatory organisms where practical"
        ]
    },

    "Tomato___Target_Spot": {
        "description": "A fungal disease that causes target-like spots on tomato leaves and fruit.",
        "symptoms": [
            "Circular brown leaf lesions",
            "Concentric rings within lesions",
            "Fruit lesions may also develop"
        ],
        "treatment": [
            "Remove severely infected leaves",
            "Improve air circulation",
            "Remove infected plant debris",
            "Use an appropriate fungicide according to its label"
        ],
        "prevention": [
            "Maintain adequate plant spacing",
            "Avoid prolonged leaf wetness",
            "Practice crop rotation",
            "Monitor plants regularly"
        ]
    },

    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "description": "A viral disease that causes leaf curling and yellowing and is commonly spread by whiteflies.",
        "symptoms": [
            "Upward curling of leaves",
            "Yellowing of leaves",
            "Stunted plant growth",
            "Reduced fruit production"
        ],
        "treatment": [
            "There is no simple curative treatment for an infected plant",
            "Remove severely infected plants where appropriate",
            "Manage insect vectors according to integrated pest-management guidance",
            "Consult local agricultural guidance for disease management"
        ],
        "prevention": [
            "Use healthy planting material",
            "Monitor and manage whiteflies",
            "Remove infected plants when recommended",
            "Control weeds that may harbor vectors"
        ]
    },

    "Tomato___Tomato_mosaic_virus": {
        "description": "A viral disease that can cause mottled leaves and reduced plant growth.",
        "symptoms": [
            "Mottled light and dark green leaf patterns",
            "Leaf distortion",
            "Reduced plant growth",
            "Reduced fruit quality or yield"
        ],
        "treatment": [
            "There is no simple curative treatment for an infected plant",
            "Remove severely infected plants where appropriate",
            "Clean tools after handling infected plants",
            "Follow local agricultural disease-management guidance"
        ],
        "prevention": [
            "Use healthy planting material",
            "Disinfect tools regularly",
            "Wash hands after handling infected plants",
            "Remove infected plant debris"
        ]
    },

    "Tomato___healthy": {
        "description": "No visible disease was detected by the model.",
        "symptoms": [
            "No major disease symptoms detected"
        ],
        "treatment": [
            "No disease treatment is required",
            "Continue normal tomato plant care"
        ],
        "prevention": [
            "Maintain adequate sunlight",
            "Provide appropriate irrigation",
            "Maintain good plant spacing",
            "Monitor plants regularly"
        ]
    }
}


def get_treatment_recommendation(disease_name):

    def normalize_name(name):
        return (
            name.lower()
            .replace("___", " ")
            .replace("_", " ")
            .replace("-", " ")
            .replace("(", " ")
            .replace(")", " ")
            .replace(",", " ")
        ).split()

    # Normalize the predicted disease name
    predicted_name = normalize_name(disease_name)

    treatment = None

    # Match the predicted name with the database
    for database_name, data in TREATMENTS.items():

        database_normalized = normalize_name(database_name)

        if predicted_name == database_normalized:
            treatment = data
            break

    if treatment is None:
        return f"""
### 🌿 {disease_name}

Disease-specific information is not available in the current database.

### General Care

- Monitor the plant regularly.
- Remove severely damaged plant material where appropriate.
- Maintain good air circulation.
- Avoid unnecessary overhead watering.
- Consult a local agricultural expert for disease-specific guidance.
"""

    symptoms = "\n".join(
        f"- {item}" for item in treatment["symptoms"]
    )

    treatment_steps = "\n".join(
        f"- {item}" for item in treatment["treatment"]
    )

    prevention = "\n".join(
        f"- {item}" for item in treatment["prevention"]
    )

    display_name = disease_name.replace("___", " — ").replace("_", " ")

    return f"""
### 🌿 Disease Information

**{display_name}**

### 🔍 Symptoms

{symptoms}

### 💊 Treatment

{treatment_steps}

### 🛡️ Prevention

{prevention}

> **Note:** Treatment recommendations are general information. Follow
> product labels and applicable local agricultural guidance before using
> any pesticide or fungicide.
"""