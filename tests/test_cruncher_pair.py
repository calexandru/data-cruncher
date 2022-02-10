import pytest

from cruncher import NumbersCruncher


class TestCruncher:

    pair_input_output = [
        ([1721, 979, 366, 299, 675, 1456], 2020, (1721, 299)),
        ([1, 2, 3, 4, 5], 9, (4, 5)),
        ([1, 2, 3, 4, 5], 10, None),
        ([1, 2, 3, 4, 5], 2, None),
        ([1, 2, 3, 4, 5], 3, (1, 2)),
        ([1, 2, 3, 6, 5], 6, (1, 5)),
        ([], 100, None),
        ([100], 100, None),
    ]

    @pytest.mark.parametrize("pair_input, pair_sum, pair_output", pair_input_output)
    def test_find_pair(self, pair_input, pair_sum, pair_output):
        assert NumbersCruncher(pair_input, pair_sum).find_pair() == pair_output

    trio_input_output = [
        ([1721, 979, 366, 299, 675, 1456], 2020, (979, 366, 675)),
        ([1, 2, 3, 8, 5], 10, (2, 3, 5)),
        ([1, 2, 3, 4, 5], 3, None),
        ([1, 2, 3, 4, 5], 2000, None),
        ([1, 2, 3, 6, 5], 6, (1, 2, 3)),
        ([], 100, None),
        ([100], 100, None),
        ([50, 50], 100, None),
    ]

    @pytest.mark.parametrize("trio_input, trio_sum, trio_output", trio_input_output)
    def test_find_trio(self, trio_input, trio_sum, trio_output):
        assert NumbersCruncher(trio_input, trio_sum).find_trio() == trio_output
