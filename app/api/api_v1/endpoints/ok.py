from fastapi import APIRouter

# Create an APIRouter instance with a specified prefix, tags, and responses
router = APIRouter(
    prefix="/ok",  # The base path for all endpoints under this router
    tags=["ok"],  # Tags for grouping and organizing endpoints
    responses={200: {"message": "Ok!"}}
)


@router.delete("/", response_model=dict)  # DELETE method
@router.post("/", response_model=dict)  # POST method
@router.put("/", response_model=dict)  # PUT method
@router.get("/", response_model=dict)  # GET method
def root():
    """
    Root endpoint for the "/ok" path.

    Returns:
        dict: A dictionary response with a message indicating "Ok!".
    """
    return router.responses.get(200)
