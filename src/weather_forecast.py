# -*- coding: utf-8 -*-
"""天気予報"""

# ライブラリのインポート
import unicodedata

import requests

# 定数
AREA_SHIGA = "250000"  # 滋賀県
AREA_KYOTO = "260000"  # 京都部
AREA_OSAKA = "270000"  # 大阪府
AREA_HYOGO = "280000"  # 兵庫県
AREA_NARA = "290000"  # 奈良県
AREA_WAKAYAMA = "300000"  # 和歌山県


def get_weather_forecast(area_code: str) -> list:
    """天気予報を取得する

    Args:
        area_code (str): エリアコード

    Returns:
        list: [0]今日の天気, [1]明日の天気予報, [2]明後日の天気予報 ※取得時刻によっては明後日の予報が無い場合あり

    Note:
        処理簡略化の為、ひとつのエリアコードに複数の地域情報（例：南部と北部）が含まれる場合は、ひとつめの地域のみを抽出する
    """
    # 明日の天気予報
    URL = f"https://www.jma.go.jp/bosai/forecast/data/forecast/{area_code}.json"  # 天気予報API

    try:
        res = requests.get(URL, timeout=10)
        res.raise_for_status()
        data = res.json()
        weathers = [
            unicodedata.normalize("NFKC", weather) for weather in data[0]["timeSeries"][0]["areas"][0]["weathers"]
        ]
    except requests.exceptions.RequestException:
        weathers = []
    except (KeyError, IndexError):
        weathers = []

    return weathers


def weather_in_osaka_tomorrow() -> str:
    """明日の大阪の天気を取得する

    Returns:
        str: 明日の大阪の天気
    """
    return get_weather_forecast(AREA_OSAKA)[1]


if __name__ == "__main__":
    print(weather_in_osaka_tomorrow())
