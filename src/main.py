import json
from random import choice


def run() -> int:
    """「おみくじ」実行ハンドラ

    Returns:
        int: 実行結果
    """
    try:
        # 運勢一覧取得
        fortunes = get_fortunes()

        # 運勢選択
        fortune = choice(fortunes)

        # 運勢出力
        print_fortune(fortune)

    # 異常終了
    except Exception as e:
        print(e)
        return 1

    # 正常終了
    return 0


def get_fortunes() -> list:
    """運勢一覧取得

    Returns:
        list: 運勢一覧
    """
    with open('src/fortunes.json', encoding='UTF-8') as file:
        file_dict = json.load(file)

    return file_dict.get('fortunes')


def print_fortune(fortune: dict):
    """運勢出力

    Args:
        fortune (dict): 運勢
    """
    for result, description in fortune.items():
        print(f'| === {result} === |: {description}')


# 実行判定
if __name__ == '__main__':
    run()
