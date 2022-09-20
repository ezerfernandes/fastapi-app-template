# -*- coding: utf-8 -*-
import uvicorn
from fastapi import FastAPI
from mangum import Mangum
from settings import Settings, get_settings


def create_app():
    settings: Settings = get_settings()
    app = FastAPI()

    @app.get("/")
    def read_root():
        return {
            "detail": (
                f"An example app based on the Clean Architecture "
                "using FastAPI  "
                "that can be easily deployed on AWS Lambda "
                "- {settings.environment_name}"
                ),
            }

    handler = Mangum(app)
    return app, settings, handler


app, settings, handler = create_app()


def run():
    uvicorn.run(
        'main:app',
        host="0.0.0.0",
        port=settings.port,
        reload=not settings.is_production,
    )


if __name__ == "__main__":
    run()