from io import BytesIO

from app.core.serializer_methods.data_formats import DataFormat
from app.managers.config_manager import ConfigurationManager

init_config = ConfigurationManager(None).get_config()

from pathlib import Path

from starlette.middleware.cors import CORSMiddleware

from app.core.data_sources.file_source import ReadFileSource
from app.core.lab.items import Component


from app.api.api_v1.api import api_router
from app.managers.facade import Facade
from fastapi import FastAPI, UploadFile


def main():
    # Create a mock UploadFile object
    # mock_file = UploadFile(filename="mock.txt", content_type="text/plain")
    # # Simulate uploading content by setting the file's content
    # content = b"Mock file content"
    # mock_file.file = BytesIO(content)

    # You can set other attributes as needed, such as content_type, filename, etc.


    format_type = DataFormat.CSV
    file_path = Path("app/data/Components.csv")
    lab_object = Component

    data_service = ReadFileSource(
        file_path=file_path,
        data_format=format_type,
        lab_class=lab_object
    )
    data_service.parse_data()



    # app = FastAPI(title=init_config["project_name"])
    # facade = Facade(config=init_config,
    #                 app=app)
    # facade.run()


if __name__ == '__main__':
    main()
