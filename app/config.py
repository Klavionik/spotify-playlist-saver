from pydantic import BaseSettings


class Config(BaseSettings):
    DEBUG: bool = False
    CLIENT_ID: str = ''
    CLIENT_SECRET: str = ''
    BASE_API_URL: str = 'https://api.spotify.com/v1'
    SECRET_KEY: str = ''
    STATE_KEY: str = '_spotify_state'
    TOKEN_KEY: str = '_spotify-token'
    REFRESH_TOKEN_KEY: str = '_spotify-refresh-token'

    class Config:
        env_file = '.env'


config = Config()


def get_config():
    return config
