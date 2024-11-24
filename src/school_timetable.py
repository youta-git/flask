# -*- coding: utf-8 -*-
# ライブラリのインポート
import csv
import os
from datetime import datetime, timedelta

# 定数
CSV_PASS = "./school_timetable.csv"  # 時間割csvファイルのパス


def get_school_timetable(file_path: str) -> list:
    """時間割csvファイルを取り込む

    Args:
        file_path (str): 時間割csvファイルのパス

    Returns:
        list: 時間割[日付, 時限, 科目, 教室, 先生]
    """
    if not os.path.isfile(file_path):
        return []

    with open(file_path, encoding="utf-8", newline="") as f:
        items = [[s.strip() for s in row] for row in csv.reader(f) if row]

    return items


def tomorrow_school_timetable() -> list:
    """明日の時間割

    Returns:
        list: 時間割[時限, 科目, 教室, 先生]
    """
    school_timetable = get_school_timetable(CSV_PASS)

    tomorrow_dt = datetime.now() + timedelta(days=1)
    yyyymmdd = tomorrow_dt.strftime("%Y%m%d")
    items = [item[1:] for item in school_timetable if item and item[0] == yyyymmdd]

    return items


if __name__ == "__main__":
    print(tomorrow_school_timetable())
