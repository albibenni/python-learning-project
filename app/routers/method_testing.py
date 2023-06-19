from fastapi import APIRouter

router = APIRouter(
    prefix="/tests",
    tags=["tests"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def read_root():
    return {"Hello": "World"}


@router.get("/list-comprehension")
def read_item():
    x = [[j for j in range(5) if j % 2 == 1] for i in range(10)]
    return x


@router.get("/file-conditional")
def read_item():
    if __name__ == "__main__":
        return "Main"
    if __name__ == "__method_testing__":
        return "__method_testing__"
    else:
        return "Not main"
