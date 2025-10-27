from pydantic import BaseModel, Field, field_validator
from typing import Optional
from datetime import date
import uuid

class Doctor(BaseModel):
    diagnosis_id:int=Field(...,examples="XXXXXX",description="enter patients ID number")
    report_type:str=Field(...,examples="XXXX",description="enter the type of report")
    results:str=Field(...,examples="XXXX",description="enter the result of report")
    report_date:str=Field(...,examples="XXXX",description="enter the date of report created")
    
    
    
    