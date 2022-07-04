from starlette.responses import JSONResponse


def generate_response(data=None, message=None, status_code=200):
    """HTTP response pattern design function
    | default status code is 200
    | default notice arg  is an empty array"""

    if message is None:
        message = []
    if data is None:
        data = {}
    return JSONResponse({
        "message": message,
        "data": data
    }, status_code=status_code)
