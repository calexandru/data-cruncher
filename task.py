import argparse
import math
import sys

from cruncher import NumbersCruncher

DEFAULT_TARGET_SUM = 2020


class PairMode:
    PAIR = "pair"
    TRIO = "trio"


def cli():
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
        default="input/default.txt",
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
            sys.exit(1)
    else:
        # failed to initialize cruncher
        sys.exit(1)


if __name__ == "__main__":
    cli()
