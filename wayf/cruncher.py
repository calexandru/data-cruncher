import logging
from typing import List
from typing import Optional
from typing import Tuple

logger = logging.getLogger(__name__)


class NumbersCruncher:
    def __init__(self, numbers: List[int], target_sum: int = 0):
        self.numbers = numbers
        self.target_sum = target_sum

    def find_pair(self) -> Optional[Tuple[int, int]]:
        """Find first pair of numbers that add up to the target sum.

        Returns
            Optional[Tuple[int, int]]: pair of numbers found or None

        """
        missing_pair_number = set()
        for number in self.numbers:
            if number in missing_pair_number:
                # we just found the missing amount for a previous processed number
                return self.target_sum - number, number
            else:
                missing_pair_number.add(self.target_sum - number)
        return None

    def find_trio(self) -> Optional[Tuple[int, int, int]]:
        """Find first group of three numbers that add up to the target sum.

        Returns
            Optional[Tuple[int, int, int]]: tuple with the three numbers found

        """
        for i, number in enumerate(self.numbers):
            pair_target_sum = self.target_sum - number
            next = i + 1
            if pair := NumbersCruncher(self.numbers[next:], pair_target_sum).find_pair():
                return number, *pair
        return None

    @classmethod
    def from_file(cls, file_path: str, target_sum: int):
        """Extract all numbers from a given input file and initialize a new cruncher instance.

        Args:
            file_path (str): relative path to the numbers input file
            target_sum (int): Sum amount

        Returns
            [type]: Instance of NumberCruncher

        """
        try:
            with open(file_path, "r") as f:
                numbers = list(map(int, filter(lambda x: x.strip(), f.readlines())))
            return cls(numbers, target_sum)
        except ValueError as ex_number:
            logger.warning(f"Input file contains invalid numbers: {ex_number}")
        except FileNotFoundError as ex_file:
            logger.error(f"File not found: {ex_file}")
