from fastapi import FastAPI , HTTPException
import requests

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

        
        
