import sys
from unittest.mock import patch

import pytest

from wayf.cli import main


class TestCli:
    @patch("wayf.cli.NumbersCruncher")
    def test_cli_params(self, mocked_cruncher):
        testargs = ["prog", "-f", "/input/fake_file.txt", "-s", "100", "-m", "trio"]
        with patch.object(sys, "argv", testargs):
            main()
            mocked_cruncher.from_file.assert_called_once_with("/input/fake_file.txt", 100)
            mocked_instance = mocked_cruncher.from_file.return_value
            mocked_instance.find_trio.assert_called_once()

    @patch("wayf.cli.NumbersCruncher")
    def test_cli_default(self, mocked_cruncher):
        testargs = ["prog", "-f", "/input/fake_file.txt"]
        with patch.object(sys, "argv", testargs):
            main()
            mocked_cruncher.from_file.assert_called_once_with("/input/fake_file.txt", 2020)
            mocked_instance = mocked_cruncher.from_file.return_value
            mocked_instance.find_pair.assert_called_once()

    @patch("wayf.cli.NumbersCruncher")
    def test_cli_wrong_params(self, mocked_cruncher):
        with patch.object(sys, "argv", ["prog", "-f", "/input/fake_file.txt", "-s", "abc"]):
            with pytest.raises(SystemExit) as ex:
                main()
            assert ex.value.code == 2

        with patch.object(sys, "argv", ["prog", "-f", "/input/fake_file.txt", "-m", "penta"]):
            with pytest.raises(SystemExit) as ex:
                main()
            assert ex.value.code == 2
