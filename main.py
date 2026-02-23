from fastapi import FastAPI, HTTPException
import requests
from fastapi import Body
app = FastAPI()

URL_USERS = "https://jsonplaceholder.typicode.com/users"

#Obtener todos los datos del usuario
@app.get("/users")
def get_users():
    try :
        response = requests.get(URL_USERS)
        response.raise_for_status()
        return response.json() # Devueleve la respuesta en formato JSON
        
    except requests.exceptions.RequestException :
        raise HTTPException(status_code=500, detail="Error externo")
    
#Obtener un usuario por su ID
@app.get("/users/{user_id}")
async def get_user(user_id: str):
    try:
        user_id = int(user_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="El ID debe ser un numero")

    try:
        response = requests.get(f"{URL_USERS}/{user_id}")
        if response.status_code == 404:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")

        data = response.json()
        if not data:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return data

    except requests.exceptions.RequestException:
        raise HTTPException(status_code=500, detail="Error externo")
    
@app.post("/users")
def create_user(user: dict = Body (...)):
    try:
        response = requests.post(URL_USERS, json=user)
        response.raise_for_status()
        return response.json() # Devuelve la respuesta en formato JSON

    except requests.exceptions.RequestException:
        raise HTTPException(status_code=500, detail="Error externo")

@app.put("/users/{user_id}")
def update_user(user_id: str, user: dict = Body(...)):
    try:
        user_id = int(user_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="El ID debe ser un numero")

    try:
        response = requests.put(f"{URL_USERS}/{user_id}", json=user)
        if response.status_code == 404:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        response.raise_for_status()
        return response.json() # Devuelve la respuesta en formato JSON

    except requests.exceptions.RequestException:
        raise HTTPException(status_code=500, detail="Error externo")
    
@app.patch("/users/{user_id}")
def patch_user(user_id: str, user: dict = Body(...)):
    try:
        user_id = int(user_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="El ID debe ser un numero")

    try:
        response = requests.patch(f"{URL_USERS}/{user_id}", json=user)
        if response.status_code == 404:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        response.raise_for_status()
        return response.json() # Devuelve la respuesta en formato JSON

    except requests.exceptions.RequestException:
        raise HTTPException(status_code=500, detail="Error externo")
    
@app.delete("/users/{user_id}")
def delete_user(user_id: str):
    try:
        user_id = int(user_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="El ID debe ser un numero")

    try:
        response = requests.delete(f"{URL_USERS}/{user_id}")
        if response.status_code == 404:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        response.raise_for_status()
        return {"message": "Usuario eliminado exitosamente"}

    except requests.exceptions.RequestException:
        raise HTTPException(status_code=500, detail="Error externo")