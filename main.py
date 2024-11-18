from openai import OpenAI
from dotenv import load_dotenv
import json


load_dotenv()
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def create_medical_professional(prompt):
    print("Running create_medical_professional")
    response = client.chat.completions.create(
        response_format={
            "type": "json_object",
        },
        messages=[

            {
              "role": "system",
              "type": "json_object",
              "content": "Create a medical professional with a unique name, bio and category."
                         "Name - The name of the medical professional."
                         "Bio - A brief description of who the person is"
                         "Category - What kind of medical professional are they (within mental health) ex: clinical psychologist, psychiatrist, licensed counselor, or social worker."
                         "return it in json format: "
                         "{"
                            "'name': name,"
                            "'bio': bio,"
                            "'category': category"
                         "}",
            },

            {
                "role": "user",
                "content": f"{prompt}",
            }],
        model="gpt-4o-mini", # gpt-4o-mini is return similar results. gpt-4 is recommended for production
    )
    response = json.loads(response.choices[0].message.content)
    return response




response = create_medical_professional(
    "Create a profile for a mental health professional, including the following details: Name, Bio and Category."
)


