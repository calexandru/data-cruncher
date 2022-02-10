import argparse
import logging
import math
import os

from .cruncher import NumbersCruncher

logger = logging.getLogger(__name__)


DEFAULT_TARGET_SUM = 2020
CURRENT_DIR = os.path.dirname(__file__)
a = os.path.join(CURRENT_DIR, "input/default.txt")
print(f"x: {CURRENT_DIR}")
print(f"x: {a}")


class PairMode:
    PAIR = "pair"
    TRIO = "trio"


def main():
    parser = argparse.ArgumentParser(description="CLI tool")
    parser.add_argument(
        "-s",
        "--target_sum",
        type=int,
        default=DEFAULT_TARGET_SUM,
        help="Target sum for received numbers (defaults to 2020).",
    )
    parser.add_argument(
        "-f",
        "--input_file",
        type=str,
        default=os.path.join(CURRENT_DIR, "input/default.txt"),
        help="Path to input file with numbers (defaults to local file).",
    )
    parser.add_argument(
        "-m",
        "--work_mode",
        type=str,
        default=PairMode.PAIR,
        choices=[PairMode.PAIR, PairMode.TRIO],
        help="Work mode - pair or trio (defaults to 'pair')",
    )

    args = parser.parse_args()
    if cruncher := NumbersCruncher.from_file(args.input_file, args.target_sum):
        # call appropriate cruncher find_x method based on the current work mode
        if found_numbers := getattr(cruncher, f"find_{args.work_mode}")():
            print(math.prod(found_numbers))
        else:
            print("No group found")
    else:
        # failed to initialize cruncher
        logger.error("Failed to initialize Cruncher")
        return 1
    return 0
