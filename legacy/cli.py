import sys

from engine import Engine


def status():

    engine = Engine()

    services = engine.load_services()

    print()

    print("========== PCOS ==========")

    for name, svc in services.items():

        print(f"{name:<12} {svc.status()}")

    print()


def start(service):

    engine = Engine()

    services = engine.load_services()

    if service not in services:

        print("Unknown service")

        return

    services[service].start()


def stop(service):

    engine = Engine()

    services = engine.load_services()

    if service not in services:

        print("Unknown service")

        return

    services[service].stop()


def main():

    if len(sys.argv) < 2:

        print("Usage:")

        print(" status")

        print(" start SERVICE")

        print(" stop SERVICE")

        return

    cmd = sys.argv[1]

    if cmd == "status":

        status()

    elif cmd == "start":

        start(sys.argv[2])

    elif cmd == "stop":

        stop(sys.argv[2])

    else:

        print("Unknown command")


if __name__ == "__main__":
    main()