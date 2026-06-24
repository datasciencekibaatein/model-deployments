from pydantic import BaseModel

class BankNote(BaseModel):
    variance:float
    skewness:float
    curtosis:float
    entropy:float
    
    model_config={
        "json_schema_extra":{
            "examples":[
                {"variance":3.6216,"skewness":8.6661,
                 "curtosis":-2.8073,"entropy":-0.44699}
            ]
        }
    }