from pydantic import BaseModel, Field, field_validator
from typing import Optional
from datetime import date
import uuid

class Doctor(BaseModel):
    patient_id:int=Field(...,examples="XXXXXX",description="enter patients ID number")
    Doctor_id:int=Field(...,examples="XXXXXX",description="enter doctors ID number")
    symptoms:str=Field(...,examples="cold,cough...etc",description="enter the patients symptoms")
    diagnosis_date:date=Field(...,examples="10-10-1999",description="enter Diagnosis date in DD-MM-YYYY")
    
    