import os
from dotenv import load_dotenv
from fastapi.responses import JSONResponse
from database.databaseConnection import engine, SessionLocal, Base



from fastapi import FastAPI, HTTPException, Request, status, Response, Depends
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware



from schema import authenticationSchema
from model import authenticationModel
from controller import authenticationController












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




app.include_router(authenticationController.router, tags=["Authentication"])


