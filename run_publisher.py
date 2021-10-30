"""
Publisher driver script
"""
import argparse
from pathlib import Path
import sys
import traceback

from src.configuration import PublisherConfiguration
from src.publisher import Publisher


def main(args: argparse.Namespace) -> int:
    """
    Read the configuration from the specified file, create a `Publisher` object with the configuration, and run the
    `Publisher`.
    """
    return_value: int = 0

    try:
        config_path = Path(args.config).resolve()
        config = PublisherConfiguration.from_yaml(config_path)

        Publisher(config).run()
    except KeyboardInterrupt:
        print("Terminating publisher")
    except Exception:
        print("Abnormal termination")
        if args.verbose:
            print(traceback.format_exc())
        return_value = 1

    return return_value


if __name__ == "__main__":

    PARSER = argparse.ArgumentParser()
    PARSER.add_argument("-c", "--config", type=str, help="Path to publisher configuration file")
    PARSER.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")
    ARGS: argparse.Namespace = PARSER.parse_args()

    RETURN_VALUE: int = main(ARGS)

    sys.exit(RETURN_VALUE)
