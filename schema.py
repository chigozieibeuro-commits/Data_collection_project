from pydantic import BaseModel

class Register(BaseModel):
    first_name:str
    second_name:str
    mail:str
    age:int
    department:str
    address:str
    next_of_kin:str
    next_of_kin_phone:int
