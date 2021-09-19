from math import ceil

from loguru import logger


def paginacao(data: list, qtd: int, offset: int, total: int, url: str) -> dict:
    registros = ceil(total / qtd)
    logger.debug(total)
    logger.debug(qtd)
    logger.debug(registros)
    paginacao = {
        "data": data,
        "paginacao": {
            "proximo": "",
            "anterior": "",
            "primeiro": "",
            "ultimo": "",
            "registros": registros,
        },
    }
    endpoint, params = url.split("?")
    _, _, *outros = params.split("&")
    logger.debug(outros)
    if len(data) == qtd and offset < registros:
        next_params = "&".join([f"qtd={qtd}", f"offset={offset+1}", *outros])
        paginacao["paginacao"]["proximo"] = f"{endpoint}?{next_params}"
        logger.debug(next_params)
    if offset > 1 and offset <= registros:
        previous_parms = "&".join([f"qtd={qtd}", f"offset={offset-1}", *outros])
        paginacao["paginacao"]["anterior"] = f"{endpoint}?{previous_parms}"
        logger.debug(previous_parms)
    last_params = "&".join([f"qtd={qtd}", f"offset={registros}", *outros])
    first_params = "&".join([f"qtd={qtd}", "offset=1", *outros])
    logger.debug(last_params)
    logger.debug(first_params)
    if offset > 1:
        paginacao["paginacao"]["primeiro"] = f"{endpoint}?{first_params}"
        logger.debug(paginacao["paginacao"]["primeiro"])
    if offset < registros:
        paginacao["paginacao"]["ultimo"] = f"{endpoint}?{last_params}"
        logger.debug(paginacao["paginacao"]["ultimo"])
    return paginacao
