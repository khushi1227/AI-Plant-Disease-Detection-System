import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient


# Loading Environment Variables:

load_dotenv()

# Read Hugging Face Token:

HF_TOKEN = os.getenv('HF_TOKEN')

# Create Hugging Face Client:

client = InferenceClient(
    provider='together',
    api_key=HF_TOKEN
)

def get_treatment_recommendation(disease_name):
    """
    Generate AI-powered treatment recommendation
    for a predicted plant disease.
    """

    response = client.chat.completions.create(
        model="Qwen/Qwen2.5-7B-Instruct",
        messages=[
            {
                "role": "user",
                "content": f"""
The predicted plant disease is: {disease_name}.

Provide the following in simple language:

1. Disease Description
2. Symptoms
3. Causes
4. Organic Treatment
5. Chemical Treatment
6. Prevention Tips

Keep the response well-structured.
"""
            }
        ],
        max_tokens=500
    )

    return response.choices[0].message.content