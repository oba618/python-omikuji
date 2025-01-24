from src import main


class TestMain:
    def test_main(self):
        """正常終了すること
        """
        assert main.run() == 0
