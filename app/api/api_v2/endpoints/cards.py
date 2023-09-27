from fastapi import APIRouter

# Create an APIRouter instance with a specified prefix, tags, and responses
router = APIRouter(
    prefix="/ok",  # The base path for all endpoints under this router
    tags=["ok"],  # Tags for grouping and organizing endpoints
    responses={200: {"message": "Ok!"}}
)


@router.get("/", response_model=dict)  # DELETE method
def root():
    """
    Root endpoint for the "/ok" path.

    Returns:
        dict: A dictionary response with a message indicating "Ok!".
    """
    return router.responses.get(200)
