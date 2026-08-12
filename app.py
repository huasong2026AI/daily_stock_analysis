# -*- coding: utf-8 -*-
"""
Hugging Face Spaces Entry Point for Daily Stock Analysis
"""
import os
import uvicorn
from api.app import create_app
from src.config import setup_env
from src.logging_config import setup_logging

setup_env()
setup_logging(log_prefix="web_server")

app = create_app()

if __name__ == "__main__":
    port = int(os.getenv("PORT", os.getenv("WEBUI_PORT", 7860)))
    uvicorn.run("app:app", host="0.0.0.0", port=port, log_level="info")
