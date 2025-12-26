from utils.coords import Coords
from config.keys import get_positionstack_key
from utils.responseAPI import API_reponse

class GeoDataLocation():
    BASE_URL = "http://api.positionstack.com/v1/reverse"

    def __init__(self) -> None:
        self.__API_KEY__ = get_positionstack_key()
        self._client = API_reponse()

    def construct_url(
        self,
        lat: float | int,
        lon: float | int,
        limit: int = 1
    ) -> str | None:
        
        if not Coords.validate_coords(lat=lat, lon=lon):
            return None
        
        return (
            f"{self.BASE_URL}"
            f"?access_key={self.__API_KEY__}"
            f"&query={lat},{lon}"
            f"&limit={limit}"
        )

    def get_location(self, lat:float|int, lon:float|int) -> str | None:
        url = self.construct_url(lat, lon)
        if not url:
            return None

        return self._client.get_response_api(url)

