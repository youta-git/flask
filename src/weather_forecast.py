# -*- coding: utf-8 -*-
"""天気予報"""

# ライブラリのインポート
import logging
import unicodedata
from dataclasses import dataclass
from enum import Enum
from typing import Optional

import requests
from requests.exceptions import RequestException

# ロギングの設定
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Prefecture(Enum):
    """関西の地域コード"""

    SHIGA = "250000"  # 滋賀県
    KYOTO = "260000"  # 京都府
    OSAKA = "270000"  # 大阪府
    HYOGO = "280000"  # 兵庫県
    NARA = "290000"  # 奈良県
    WAKAYAMA = "300000"  # 和歌山県


@dataclass
class WeatherForecast:
    """天気予報データクラス"""

    today: str  # 今日の天気
    tomorrow: str  # 明日の天気
    day_after_tomorrow: Optional[str] = None  # 明後日の天気（取得できない場合はNone）


class WeatherAPI:
    """気象庁天気予報APIクライアント"""

    BASE_URL = "https://www.jma.go.jp/bosai/forecast/data/forecast"
    TIMEOUT = 10

    @staticmethod
    def normalize_text(text: str) -> str:
        """テキストの正規化"""
        return unicodedata.normalize("NFKC", text)

    def get_weather_forecast(self, prefecture: Prefecture) -> Optional[WeatherForecast]:
        """天気予報を取得する

        Args:
            prefecture (Prefecture): 地域コード

        Returns:
            Optional[WeatherForecast]: 天気予報
        """
        url = f"{self.BASE_URL}/{prefecture.value}.json"

        try:
            response = requests.get(url, timeout=self.TIMEOUT)
            response.raise_for_status()
            data = response.json()

            weathers = [self.normalize_text(weather) for weather in data[0]["timeSeries"][0]["areas"][0]["weathers"]]

            return WeatherForecast(
                today=weathers[0], tomorrow=weathers[1], day_after_tomorrow=weathers[2] if len(weathers) > 2 else None
            )

        except RequestException as e:
            logger.error(f"API接続エラー: {e}")
            return None
        except (KeyError, IndexError) as e:
            logger.error(f"データ解析エラー: {e}")
            return None
        except Exception as e:
            logger.error(f"予期せぬエラー: {e}")
            return None


def get_osaka_tomorrow_weather() -> str:
    """明日の大阪の天気を取得する

    Returns:
        str: 明日の大阪の天気
    """
    api = WeatherAPI()
    forecast = api.get_weather_forecast(Prefecture.OSAKA)

    if forecast is None:
        return "天気予報の取得に失敗しました"

    return forecast.tomorrow


if __name__ == "__main__":
    weather = get_osaka_tomorrow_weather()
    print(f"明日の大阪の天気: {weather}")
