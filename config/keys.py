from config.settings import (
    OPENWEATHER_API_KEY,
    POSITIONSTACK_API_KEY,
)

def get_openweather_key() -> str:
    if not OPENWEATHER_API_KEY:
        raise RuntimeError("OPENWEATHER_API_KEY not configured")
    return OPENWEATHER_API_KEY

def get_positionstack_key() -> str:
    if not POSITIONSTACK_API_KEY:
        raise RuntimeError("POSITIONSTACK_API_KEY not configured")
    return POSITIONSTACK_API_KEY
