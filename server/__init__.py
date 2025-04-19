from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from server.extensions import LOGGER
from server.core import LoggerMiddleWare




def create_app() -> FastAPI:
    LOGGER.info("Creating App")
    app = FastAPI()
    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
        allow_credentials=True,
    )
    
    app.add_middleware(LoggerMiddleWare)

    return app
