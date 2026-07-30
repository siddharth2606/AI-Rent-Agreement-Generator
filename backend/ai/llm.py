import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def generate_agreement(data):

    prompt = f"""
You are an Indian legal assistant.

Generate a professional Rent Agreement.

Landlord Name : {data["landlord_name"]}

Tenant Name : {data["tenant_name"]}

Property Address : {data["property_address"]}

Monthly Rent : ₹{data["monthly_rent"]}

Security Deposit : ₹{data["security_deposit"]}

Start Date : {data["start_date"]}

End Date : {data["end_date"]}

Return only the agreement.
"""

    response = model.generate_content(prompt)

    return response.text