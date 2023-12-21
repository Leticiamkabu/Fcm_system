import os
from dotenv import load_dotenv
from fastapi.responses import JSONResponse
from database.databaseConnection import engine, SessionLocal, Base



from fastapi import FastAPI, HTTPException, Request, status, Response, Depends
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware



from schema import authenticationSchema, vehicleSchema
from model import authenticationModel, vehicleModel
from controller import authenticationController, vehicleController, userController













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



app.include_router(userController.router, tags=["User"])
app.include_router(authenticationController.router, tags=["Authentication"]),
app.include_router(vehicleController.router, tags=["Vehicle"])


