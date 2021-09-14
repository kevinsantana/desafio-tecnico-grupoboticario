from fastapi import APIRouter


router = APIRouter()


@router.post(
    "/",
    status_code=201,
    summary="Cadastra um revendedor",
    response_model="",
    responses=""
)
def criar_revendedor():
    pass
