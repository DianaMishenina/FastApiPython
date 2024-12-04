from fastapi import FastAPI, HTTPException
import uvicorn
from models import *
from config import *
from response_models import *

app = FastAPI(
    title="yourtitle",
    description="pracAPI",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

@app.get("/users/select/{user_id}")
async def get_users(user_id:int):
    try:
        with DBSettings.get_session() as conn:
            user = conn.query(User).filter(User.id == user_id).first()
            return user
    except: 
        raise HTTPException(status_code=404, detail="User not found")
    
@app.post("/users/add", response_model=UserCreate)
async def add_users(user_name:str, user_role:str):
    user = UserCreate(name=user_name, role=user_role)
    with DBSettings.get_session() as conn:
        roleDB = conn.query(Role).filter(Role.name == user.role).first()
        if (roleDB == None):
            raise HTTPException(status_code=404, detail="We haven't this role")
        else:
            new_user = User(name = user.name, role_id = roleDB.id)
            conn.add(new_user)
            conn.commit()
            print("Успешно")
            return(user)
        
@app.delete("/users/delete/{users_id}")
async def delete_users(user_id:int):
    with DBSettings.get_session() as conn:
        user = conn.query(User).filter(User.id == user_id).first()
        if (user == None):
            raise HTTPException(status_code=404, detail="We haven't this user")
        else:
            conn.delete(user)
            conn.commit()
            print("Успешно")


@app.put("/users/update/{users_id}")
async def update_users(user_id:int, name:str, role_id:int):
    userUpd = UserUpdate(name=name, role_id=role_id)

    with DBSettings.get_session() as conn:
        user = conn.query(User).filter(User.id == user_id).first()
        if (user == None):
            raise HTTPException(status_code=404, detail="We haven't this user")
        else:
            if userUpd.name is not None:
                user.name = userUpd.name
            if userUpd.role_id is not None:
                user.role_id = userUpd.role_id

        conn.commit()

uvicorn.run(app, host="127.0.0.1", port=8000)