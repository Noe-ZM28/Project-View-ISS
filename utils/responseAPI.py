from requests import get
from requests.models import Response
from requests.exceptions import RequestException

class API_reponse:
    def construc_url(self, **kwars)->str: ...

    def get_response_api(self, url:str, to_JSON:bool= True) -> Response | dict | None:
        try:
            print(url)
            response = get(url)
            response.raise_for_status()

            return response.json() if to_JSON else response

        except RequestException as e:
            print(e)
            print(f"Error en la petición: {e}")
            return None