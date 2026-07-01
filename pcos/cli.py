import argparse

from pcos.engine import Engine


def main():
    parser = argparse.ArgumentParser(prog="pcos")

    sub = parser.add_subparsers(dest="command")

    sub.add_parser("list")

    args = parser.parse_args()

    engine = Engine()

    if args.command == "list":
        print("Available services:\n")

        for service in engine.list_services():
            print(f"✓ {service}")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()