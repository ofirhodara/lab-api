
from starlette.middleware.cors import CORSMiddleware

from app.api.api_v1.api import api_router

local_config = ConfigurationManager().get_config()
app = FastAPI(title=local_config["project_name"])

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
)

app.include_router(api_router, prefix=local_config["api"]["api_endpoint_str"])

if __name__ == '__main__':
    print("ofir")
