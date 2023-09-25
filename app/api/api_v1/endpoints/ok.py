from fastapi import APIRouter


router = APIRouter(
    prefix="/ok",
    tags=["ok"],
    responses={200: {"message": "Ok!"}}
)


@router.delete("/", response_model=dict)
@router.post("/", response_model=dict)
@router.put("/", response_model=dict)
@router.get("/", response_model=dict)
def root():
    return router.responses.get(200)
