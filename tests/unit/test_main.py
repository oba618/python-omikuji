from unittest import mock

from src import main


class TestMain:
    def test_main(self):
        """正常終了すること
        """
        assert main.run() == 0

    def test_main_except_exception(self):
        """異常終了すること
        """
        # 運勢取得でエラー発生
        with mock.patch('src.main.get_fortunes') as m:
            m.side_effect = Exception()

            result = main.run()

        assert result == 1

    def test_get_fortune(self):
        """おみくじが取得できること
        """
        fortunes = main.get_fortunes()

        assert len(fortunes) == 4
        assert fortunes[0] == {"大吉": "とても良い運勢です"}
        assert fortunes[1] == {"吉": "良い運勢です"}
        assert fortunes[2] == {"凶": "悪い運勢です"}
        assert fortunes[3] == {"大凶": "とても悪い運勢です"}

    def test_print_fortune(self):
        """正常終了すること
        """
        assert main.print_fortune({"TEST": "IS OK"}) is None
