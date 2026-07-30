from pydantic import BaseModel

class Agreement(BaseModel):
    landlord_name:str
    tenant_name:str
    property_address:str
    monthly_rent:int
    security_deposit:int
    start_date:str
    end_date:str

