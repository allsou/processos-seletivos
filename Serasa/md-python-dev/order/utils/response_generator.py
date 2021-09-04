from starlette.responses import JSONResponse


def response(message: str = None, data: dict = None, status_code: int = 200):
    """
    Response generator
    :param message: message to inform user
    :param data: data of request
    :param status_code: http status code
    :return: JSONRsponse
    """
    return JSONResponse(
        {
            "message": message,
            "data": data,
        },
        status_code
    )
