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
def get_user(user_id: int):
    try :
        response = requests.get(f"{URL_USERS}/{user_id}")
        response.raise_for_status()
        return response.json()

    except requests.exceptions.HTTPError:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error externo: {str(e)}")
    
    
 # Buscar usuario por username
@app.get("/users/search/")
def search_user(username: str):
    try:
        response = requests.get(URL_USERS)
        response.raise_for_status()
        users = response.json()

        # Buscar el usuario en la lista
        for user in users:
            if user["username"].lower() == username.lower():
                return user

        # Si no encuentra ninguno
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error externo: {str(e)}")   