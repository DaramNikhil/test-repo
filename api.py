from fastapi import FastAPI
from pydantic import BaseModel
from hashlib import sha256


app = FastAPI()


class Item(BaseModel):
    uname: str
    email: str
    password: str

data = []

@app.get('/get_data')
def get_data():
    if data:
        cleaned_data = [[record["uname"], record["password"]] for record in data]
        return {"data": cleaned_data}

    else:
        return {"message": "No data found"}

@app.post('/add_data')
def add_data(item: Item):
    new_data = item.dict()
    # name = item.get('name')
    # email = item.get('email')
    # password = item.get('password')
    # hashed_password = sha256(password.encode()).hexdigest()
    # user_data = {"name": name, "email": email, "hashed_password": hashed_password}
    data.append(new_data)
    return {"message": "Data added successfully"}
    