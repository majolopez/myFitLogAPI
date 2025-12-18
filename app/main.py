import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routers.hello import router as hello_router
from app.api.routers.users import router as user_router
from app.api.routers.meal import router as meal_router

load_dotenv()  

app = FastAPI(title="Hello World API")

cors_origins = os.getenv("CORS_ORIGINS", "")
cors_origin_regex = os.getenv("CORS_ORIGIN_REGEX", None)

allowed_origins = [
    origin.strip()
    for origin in cors_origins.split(",")
    if origin.strip()
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_origin_regex=cors_origin_regex,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(hello_router)
app.include_router(user_router)
app.include_router(meal_router)