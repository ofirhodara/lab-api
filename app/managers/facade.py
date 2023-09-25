from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.api.api_v1.api import api_router
from app.managers.config_manager import ConfigurationManager
import uvicorn

from app.managers.logger_manager import create_logger

logger = create_logger(__name__)


class Facade:
    """
    A Facade class for configuring and running the FastAPI app.
    """

    def __init__(self,
                 *,
                 config: ConfigurationManager,
                 app: FastAPI):
        """
        Initialize the Facade with configuration and the FastAPI app instance.

        Args:
            config (ConfigurationManager): An instance of ConfigurationManager for configuration settings.
            app (FastAPI): The FastAPI app instance.
        """
        self.local_config = config
        self.app = app
        self._configure_app()

    def _configure_app(self):
        """
        Configure the FastAPI app with CORS middleware and include the router.
        """
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins="*",
            allow_credentials=True,
            allow_methods=["GET", "POST", "PUT", "DELETE"],
            allow_headers="*",
        )

        self.app.include_router(api_router, prefix=self.local_config["api"]["api_endpoint_str"])

    def run(self):
        """
        Run the FastAPI app using uvicorn with specified host and port.
        """
        uvicorn.run(self.app,
                    host=self.local_config["api"]["server_host"],
                    port=int(self.local_config["api"]["port"]))
