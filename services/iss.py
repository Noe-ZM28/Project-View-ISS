from datetime import datetime
from utils.responseAPI import API_reponse

class ISSData():
    URL = "http://api.open-notify.org/iss-now.json"
    
    def __init__(self) -> None:
        self._client = API_reponse()

    def get_ISS_position(self) -> tuple[str, str, str] | None:
        self.response_api = self._client.get_response_api(self.URL)

        if self.response_api is None:
            return None

        lon = self.response_api["iss_position"]["longitude"]
        lat = self.response_api["iss_position"]["latitude"]

        date = datetime.fromtimestamp(self.response_api["timestamp"]).strftime("%Y-%m-%d %H:%M:%S")

        return lon, lat, date
