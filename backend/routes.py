from fastapi import APIRouter
from fastapi.responses import FileResponse

from schemas import Agreement
from ai.llm import generate_agreement
from database import agreement_collection
from services.pdf_service import create_pdf

router = APIRouter()


@router.post("/generate")

def generate(data: Agreement):

    user_data = data.model_dump()

    agreement = generate_agreement(user_data)

    document = {

        "landlord_name": user_data["landlord_name"],
        "tenant_name": user_data["tenant_name"],
        "property_address": user_data["property_address"],
        "monthly_rent": user_data["monthly_rent"],
        "security_deposit": user_data["security_deposit"],
        "start_date": user_data["start_date"],
        "end_date": user_data["end_date"],
        "agreement_text": agreement

    }

    result = agreement_collection.insert_one(document)

    pdf_path = create_pdf(

        f"{result.inserted_id}.pdf",

        agreement

    )

    return FileResponse(

        path=pdf_path,

        filename=f"{result.inserted_id}.pdf",

        media_type="application/pdf"

    )