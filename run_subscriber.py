"""
Subscriber driver script
"""
import argparse
from pathlib import Path
import sys
import traceback

from src.configuration import SubscriberConfiguration
from src.subscriber import Subscriber


def main(args: argparse.Namespace) -> int:
    """
    Read the configuration from the specified file, create a `Subscriber` object with the configuration, and run the
    `Subscriber`.
    """
    return_value: int = 0

    try:
        config_path = Path(args.config).resolve()
        config = SubscriberConfiguration.from_yaml(config_path)

        Subscriber(config).run()
    except KeyboardInterrupt:
        print("Terminating subscriber")
    except Exception:
        print("Abnormal termination")
        if args.verbose:
            print(traceback.format_exc())
        return_value = 1

    return return_value


if __name__ == "__main__":

    PARSER = argparse.ArgumentParser()
    PARSER.add_argument("-c", "--config", type=str, help="Path to server configuration file")
    PARSER.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")
    ARGS: argparse.Namespace = PARSER.parse_args()

    RETURN_VALUE: int = main(ARGS)

    sys.exit(RETURN_VALUE)
