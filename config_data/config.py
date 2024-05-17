from pydantic import SecretStr, RedisDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class BotSettings(BaseSettings):
    bot_token: SecretStr
    redis_dsn: RedisDsn

    model_config = SettingsConfigDict(env_file=".env")