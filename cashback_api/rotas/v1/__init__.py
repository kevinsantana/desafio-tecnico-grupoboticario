from math import ceil


def paginacao(data: list, qtd: int, offset: int, total: int, url: str) -> dict:
    total = ceil(total / qtd)
    paginacao = {
        "data": data,
        "paginacao": {
            "proximo": "",
            "anterior": "",
            "primeiro": "",
            "ultimo": "",
            "total": total,
        },
    }
    endpoint, params = url.split("?")
    _, _, *others = params.split("&")
    if len(data) == qtd and offset < total:
        next_params = "&".join([f"qtd={qtd}", f"offset={offset+1}", *others])
        paginacao["paginacao"]["proximo"] = f"{endpoint}?{next_params}"
    if offset > 1 and offset <= total:
        previous_parms = "&".join([f"qtd={qtd}", f"offset={offset-1}", *others])
        paginacao["paginacao"]["anterior"] = f"{endpoint}?{previous_parms}"
    last_params = "&".join([f"qtd={qtd}", f"offset={total}", *others])
    first_params = "&".join([f"qtd={qtd}", "offset=1", *others])
    if offset > 1:
        paginacao["paginacao"]["primeiro"] = f"{endpoint}?{first_params}"
    if offset < total:
        paginacao["paginacao"]["ultimo"] = f"{endpoint}?{last_params}"
    return paginacao
