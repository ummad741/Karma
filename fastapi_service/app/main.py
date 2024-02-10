from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

# local folders and files



app = FastAPI(
    title='Ecommerce'
)


