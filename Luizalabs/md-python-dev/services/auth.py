import json

from jose import jwt
from six.moves.urllib.request import urlopen
from starlette.requests import Request

from exceptions.auth import AuthError
from settings import AUTH0_DOMAIN, API_AUDIENCE
from utils.response_generator import generate_response

ALGORITHMS = ["RS256"]


def get_token_auth_header(request):
    """Obtains the Access Token from the Authorization Header
    """
    auth = request.headers.get("Authorization", None)
    if not auth:
        raise AuthError(
            error={"code": "authorization_header_missing", "description": "Authorization header is expected"},
            status_code=401
        )
    parts = auth.split()
    if parts[0].lower() != "bearer":
        raise AuthError({"code": "invalid_header",
                         "description":
                             "Authorization header must start with"
                             " Bearer"}, 401)
    elif len(parts) == 1:
        raise AuthError({"code": "invalid_header",
                         "description": "Token not found"}, 401)
    elif len(parts) > 2:
        raise AuthError({"code": "invalid_header",
                         "description":
                             "Authorization header must be"
                             " Bearer token"}, 401)

    token = parts[1]
    return token


def requires_auth(function):
    """Determines if the Access Token is valid
    """

    async def decorated(*args, **kwargs):
        for arg in args:
            if isinstance(arg, Request):
                request = arg
        try:
            token = get_token_auth_header(request)
        except AuthError as exception:
            return generate_response(message=exception.error, status_code=exception.status_code)
        jsonurl = urlopen("https://" + AUTH0_DOMAIN + "/.well-known/jwks.json")
        jwks = json.loads(jsonurl.read())
        unverified_header = jwt.get_unverified_header(token)
        rsa_key = {}
        for key in jwks["keys"]:
            if key["kid"] == unverified_header["kid"]:
                rsa_key = {
                    "kty": key["kty"],
                    "kid": key["kid"],
                    "use": key["use"],
                    "n": key["n"],
                    "e": key["e"]
                }
        if rsa_key:
            try:
                jwt.decode(
                    token,
                    rsa_key,
                    algorithms=ALGORITHMS,
                    audience=API_AUDIENCE,
                    issuer="https://" + AUTH0_DOMAIN + "/"
                )
            except jwt.ExpiredSignatureError:
                return generate_response(
                    message={"code": "token_expired", "description": "token is expired"}, status_code=401
                )
            except jwt.JWTClaimsError:
                return generate_response(message={"code": "invalid_claims",
                                                  "description":
                                                      "incorrect claims,"
                                                      "please check the audience and issuer"}, status_code=401)
            except Exception:
                raise generate_response(message={"code": "invalid_header",
                                                 "description":
                                                     "Unable to parse authentication"
                                                     " token."}, status_code=401)

            return await function(*args, **kwargs)
        raise generate_response(message={"code": "invalid_header",
                                         "description": "Unable to find appropriate key"}, status_code=401)

    return decorated
