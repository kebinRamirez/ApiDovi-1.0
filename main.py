import uvicorn
from typing import Optional
from fastapi import Depends, FastAPI, Header, HTTPException
#Import paquetes
from configurations.functions import *
from models.places import *
from models.sort import *
from models.dictionaries import *
from distribution import *
from distribution import Neigh
from distribution import Colombia, States, Town
from distribution.Colombia import datasets
#from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
#app.add_middleware(                                
#    CORSMiddleware,                                       
#    allow_origins=["*"],
#    allow_credentials=True,                             
#    allow_methods=["*"],                               
#    allow_headers=["*"]          
#)
app.include_router(Colombia.router)
app.include_router(States.router)
app.include_router(Neigh.router)
app.include_router(Town.router)
@app.get("/")
def main():
    var = "This DOVI-API is running..."
    return var


