from fastapi import APIRouter
from app.services.hello_service import HelloService

router = APIRouter(prefix="/hello", tags=["Hello"])

@router.get("")
def hello():
    print("Hello endpoint called")
    return HelloService.get_hello()
