# -*- coding: utf-8 -*-
"""おみくじ"""

# ライブラリのインポート
import random
from dataclasses import dataclass


@dataclass
class Fortune:
    result: str
    advice: str


class Omikuji:
    FORTUNES = {
        "大吉": "明日は非常に良い日です。\n自信を持って行動しましょう！",
        "中吉": "明日は良い日ですが、\n慎重さも忘れずに。",
        "小吉": "まあまあの運勢です。\nちょっとしたラッキーがあります。",
        "吉": "運勢は良いですが、\n油断は禁物。",
        "凶": "明日は気をつけて行動しましょう。\n無理をしないのが吉。",
        "大凶": "注意が必要な日です。\n心も体も休めて。",
    }

    @staticmethod
    def draw() -> Fortune:
        """おみくじを引く

        Returns:
            Fortune: 運勢と助言を含むFortuneオブジェクト
        """
        result = random.choice(list(Omikuji.FORTUNES.keys()))
        return Fortune(result, Omikuji.FORTUNES[result])


if __name__ == "__main__":
    fortune = Omikuji.draw()
    print(f"結果: {fortune.result}")
    print(f"アドバイス: {fortune.advice}")
