from starlette.responses import JSONResponse


def response(message: str = None, data: dict = None, status_code: int = 200):
    """

    Args:
        message: information
        data: data from model
        status_code: http status code

    Returns: JSONResponse

    """
    return JSONResponse(
        {
            "message": message,
            "data": data,
        },
        status_code
    )
