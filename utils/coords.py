class Coords:
    @staticmethod
    def validate_coords(lat:float|int, lon:float|int) -> bool:
        """
            Latitud:

            La latitud varía de -90° (para el Polo Sur) a +90° (para el Polo Norte).
            Una latitud válida estará dentro de este rango.

            Longitud:

            La longitud varía de -180° (para la longitud occidental) a +180° (para la longitud oriental).
        """
        return True if -90 <= lat <= 90 and -180 <= lon <= 180 else False
