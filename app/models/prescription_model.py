from pydantic import BaseModel, Field, field_validator
from typing import Optional
from datetime import date
import uuid

class Doctor(BaseModel):
    diagnosis_id:int=Field(...,examples="XXXXXX",description="enter patients ID number")
    mediaction_name:str=Field(...,examples="XXXX",description="enter the mediactioon name patient")
    dosage:str=Field(...,examples="XXXX",description="enter the dosage of mediaction patient")
    duration:str=Field(...,examples="XXXX",description="enter the duration opf medication")
    
    
    