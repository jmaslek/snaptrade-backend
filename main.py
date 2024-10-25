import json
from pathlib import Path
import os
from contextlib import asynccontextmanager
from typing import Optional
from fastapi import FastAPI, Depends, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
from loguru import logger
from utils import *
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:1420",
    "http://localhost:5050",
    "https://pro.openbb.dev",
    "https://pro.openbb.co",
    "https://excel.openbb.co",
    "https://excel.openbb.dev",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/widgets.json")
def get_widgets():
    """Widgets configuration file for the OpenBB Terminal Pro"""
    return JSONResponse(
        content=json.load((Path(__file__).parent.resolve() / "widgets.json").open())
    )

@app.get("/")
def hello_world():
    return {"Hello":"Snaptrade Example Custom Backend"}

@app.get("/accounts")
def get_user_accounts(snaptrade_client=Depends(get_snaptrade_client)):
    return JSONResponse(content=show_accounts(snaptrade_client))

@app.get("/holdings")
def get_user_holdings(account_id:str,
                      snaptrade_client=Depends(get_snaptrade_client)):
    return JSONResponse(
        content=return_holdings(snaptrade_client, account_id)
    )