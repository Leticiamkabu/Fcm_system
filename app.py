import os
from dotenv import load_dotenv
from fastapi.responses import JSONResponse
from database.databaseConnection import engine, SessionLocal, Base



from fastapi import FastAPI, HTTPException, Request, status, Response, Depends
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware



from schemas import formsSchema, authenticationSchema
from models import formModel, authenticationModel
from controllers import formsController, authenticationController,formSubmissionController,dashboardController,fileController
from fastapi_login import LoginManager


from fastapi.security import OAuth2PasswordRequestForm

from fastapi_login.exceptions import InvalidCredentialsException
from middleWare import *


SECRET = "super-secret-key"
manager = LoginManager(SECRET, '/login')




load_dotenv()



app = FastAPI(
    title= "MySay Form Service",
    version="0.0.1",
    description="FastAPI Forms creation",
    openapi_tags=[
        {
            "name": "Home",
            "description": "Check health of the API"
        }
    ]
)





app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

async def authenticate_user():
    return TemporaryAuthMiddleware()

# app.add_middleware(TemporaryAuthMiddleware)

app.include_router(authenticationController.router, tags=["Authentication"])
app.include_router(formsController.router, prefix="", tags=["Forms"])
app.include_router(formSubmissionController.router, prefix="", tags=["Form_submissions"])
app.include_router(dashboardController.router, prefix="", tags=["Dashboard"])
app.include_router(fileController.router, prefix="", tags=["Upload"])

