from fastapi import FastAPI
from fastapi import Depends, FastAPI, HTTPException, status, Security
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import pyrebase

app = FastAPI()


firebaseConfig = {
  'apiKey': "AIzaSyCLdvVPekIctUds2mBM-xLfIkEDbFfkt6Q",
  'authDomain': "authentication-ad9c1.firebaseapp.com",
  'databaseURL': 'https://authentication-ad9c1-default-rtdb.firebaseio.com',
  'projectId': "authentication-ad9c1",
  'storageBucket': "authentication-ad9c1.appspot.com",
  'messagingSenderId' : "866294106237",
  'appId' : "1:866294106237:web:bc4b3fa1aa0ff72936c914",
  'measurementId' : "G-RWNW0EZPHN"
};

firebase=pyrebase.initialize_app(firebaseConfig)

securityBasic = HTTPBasic()
securityBearer = HTTPBearer()

@app.get("/")
async def index():
    return {"message": "API-REST"}


@app.get(
    "/users/token",
    status_code = status.HTTP_202_ACCEPTED,
    summary="Get atoken for user",
    description="Get atoken for user",
    tags=["auth"]
)
async def get_token(credentials:HTTPBasicCredentials = Depends(securityBasic)):
    try:
        email = credentials.username
        password = credentials.password
        auth = firebase.auth()
        user = auth.sign_in_with_email_and_password(email, password)
        response ={
            "token": user['idToken'],
            "uid": user['localId']
        }
        return response
    except Exception as error:
        print(f"ERROR: {error}")
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED)

@app.get(
    "/users/",
    status_code = status.HTTP_202_ACCEPTED,
    summary="Get a user",
    description="Get a user",
    tags=["auth"]
)
async def get_user(credentials:HTTPAuthorizationCredentials = Depends(securityBearer)):
    try:
        auth = firebase.auth()
        user = auth.get_account_info(credentials.credentials)
        uid =user['users'][0]['localId']
        db = firebase.database()
        user_data = db.child("user").child(uid).get().val()
        response = {
            "user_data": user_data
        }
        return response
    except Exception as error:
         print(f"ERROR: {error}")
    raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED)
