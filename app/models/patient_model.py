from pydantic import BaseModel, Field, field_validator
from typing import Optional
from datetime import date
import uuid

class Doctor(BaseModel):
    name:str=Field(...,examples="XXXX",description="enter name of the patient")
    DOB:date=Field(...,examples="10-10-1999",description="enter Date of birth in DD-MM-YYYY")
    gender:str=Field(...,examples="XXXX",description="enter the gender of patient")
    contact:int=Field(...,examples="0000000000",description="enter your mobile number")
    

    