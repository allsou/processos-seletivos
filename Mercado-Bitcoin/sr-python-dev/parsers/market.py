from entities.market import Market
from settings import LOGGER
DISTINCT_NUMBERS = [
    "S/N",
    "15-A",
    "14A",
    "12E",
    "1236A"
]
MAX_PARAMS_ALLOWED = 4
PARAMS_ALLOWED = {
    'distrito',
    'regiao5',
    'nome_feira',
    'bairro'
}


class MarketParser:
    @staticmethod
    def number_from_csv_to_int(number):
        number_parsed = number
        if number == '':
            number_parsed = "S/N"
        elif number not in DISTINCT_NUMBERS:
            if len(number) > 4:
                number_parsed = str(int(float(number)))
        return number_parsed

    @staticmethod
    def params_to_query(params: list, params_allowed: set = PARAMS_ALLOWED) -> str:
        if len(params) > MAX_PARAMS_ALLOWED:
            LOGGER.warning(f'Too many params. Only {MAX_PARAMS_ALLOWED} are allowed')
            raise Exception
        query = ''
        for param_key, param_value in params:
            if not {param_key}.issubset(params_allowed):
                continue
            if param_key == 'distrito':
                query = f'"distrito" = \'{param_value}\''
            elif param_key == 'regiao5':
                query = f'"regiao5" = \'{param_value}\''
            elif param_key == 'nome_feira':
                query = f'"nome_feira" = \'{param_value}\''
            elif param_key == 'bairro':
                query = f'"bairro" = \'{param_value}\''

        return query

    @staticmethod
    def object_to_json(market: Market):
        return {
            "id": market.id,
            "long": market.long,
            "lat": market.long,
            "setcens": market.setcens,
            "areap": market.areap,
            "coddist": market.coddist,
            "distrito": market.distrito,
            "codsubpref": market.codsubpref,
            "subprefe": market.subprefe,
            "regiao5": market.regiao5,
            "regiao8": market.regiao8,
            "nome_feira": market.nome_feira,
            "registro": market.registro,
            "logradouro": market.logradouro,
            "numero": market.numero,
            "bairro": market.bairro,
            "referencia": market.referencia
        }

    @staticmethod
    def markets_to_json(markets: list):
        markets_parsed = []
        for market in markets:
            markets_parsed.append({
                "id": market[0],
                "long": market[1],
                "lat": market[2],
                "setcens": market[3],
                "areap": market[4],
                "coddist": market[5],
                "distrito": market[6],
                "codsubpref": market[7],
                "subprefe": market[8],
                "regiao5": market[9],
                "regiao8": market[10],
                "nome_feira": market[11],
                "registro": market[12],
                "logradouro": market[13],
                "numero": market[14],
                "bairro": market[15],
                "referencia": market[16]
            })
        return markets_parsed
