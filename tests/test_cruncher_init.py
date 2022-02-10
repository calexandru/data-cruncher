from unittest.mock import mock_open
from unittest.mock import patch

import pytest

from wayf.cruncher import NumbersCruncher


class TestCruncherInit:

    cruncher_file_input_output = [
        ("1721\n979\n366\n299\n675\n1456", [1721, 979, 366, 299, 675, 1456], False),
        ("   1721\n 979 \n   366 \n299 \n\n", [1721, 979, 366, 299], False),
        ("", [], False),
        ("asd\nbcd", None, True),
    ]

    @pytest.mark.parametrize("file_input, numbers_output, should_fail", cruncher_file_input_output)
    def test_from_file(self, file_input, numbers_output, should_fail):
        with patch("builtins.open", mock_open(read_data=file_input)):
            cruncher = NumbersCruncher.from_file("fake_file", 2020)
            if should_fail:
                assert cruncher is None
            else:
                assert cruncher
                assert cruncher.numbers == numbers_output
