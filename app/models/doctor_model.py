from pydantic import BaseModel, Field, field_validator
from typing import Optional
from datetime import date
import uuid

class Doctor(BaseModel):
    name:str=Field(...,examples="DR.XXXX",description="enter name of the doctor")
    specialization:str=Field(...,example="dematologist...etc",description="enter doctors specializations")
    experiance:int=Field(...,examples="XX years",description="enter doctors experiance")
