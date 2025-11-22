from pydantic_settings import BaseSettings
from pydantic import ConfigDict


class Settings(BaseSettings):
    # BrowserStack credentials
    browserstack_username: str
    browserstack_access_key: str
    browserstack_url: str = "hub.browserstack.com/wd/hub"

    # Android capabilities
    android_device: str = "Samsung Galaxy S22"
    android_platform_version: str = "12.0"
    android_app: str = "bs://sample.app"

    # iOS capabilities
    ios_device: str = "iPhone 14"
    ios_platform_version: str = "16"
    ios_app: str = "bs://sample.app"

    # ИСПРАВЛЕНИЕ для Pydantic v2
    model_config = ConfigDict(env_file=".env")


settings = Settings()