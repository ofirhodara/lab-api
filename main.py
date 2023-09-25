from starlette.middleware.cors import CORSMiddleware
from app.managers.config_manager import ConfigurationManager
from app.api.api_v1.api import api_router
from app.managers.facade import Facade
from fastapi import FastAPI


def main():
    init_config = ConfigurationManager().get_config()
    app = FastAPI(title=init_config["project_name"])
    facade = Facade(config=init_config,
                    app=app)
    facade.run()


if __name__ == '__main__':
    main()
