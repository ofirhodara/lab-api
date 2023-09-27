from app.managers.config_manager import ConfigurationManager

from fastapi import FastAPI, UploadFile

from app.managers.facade import Facade


def main():
    init_config = ConfigurationManager().get_config()
    app = FastAPI(title=init_config["project_name"])
    facade = Facade(config=init_config,
                    app=app)
    facade.run()


if __name__ == '__main__':
    main()
