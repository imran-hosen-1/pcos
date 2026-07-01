import json
import subprocess
import sys
from pathlib import Path

REGISTRY_PATH = Path(__file__).resolve().parent / "registry.json"

def load_registry():
    if not REGISTRY_PATH.exists():
        print("Registry not found")
        sys.exit(1)
    return json.loads(REGISTRY_PATH.read_text())

def run(cmd):
    return subprocess.run(cmd, shell=True)

def start_service(name, registry):
    svc = registry.get(name)
    if not svc:
        print(f"[ERROR] Service '{name}' not found")
        return

    print(f"[PCOS] Starting {name}...")
    run(svc["start"])

def stop_service(name, registry):
    svc = registry.get(name)
    if not svc:
        print(f"[ERROR] Service '{name}' not found")
        return

    print(f"[PCOS] Stopping {name}...")
    run(svc["stop"])

def status(registry):
    print("\n[PCOS STATUS]")
    for name, svc in registry.items():
        print(f"- {name}: {svc.get('type')}")

def main():
    registry = load_registry()

    if len(sys.argv) < 2:
        print("Usage: pcos <start|stop|status> [service]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "start":
        start_service(sys.argv[2], registry)

    elif command == "stop":
        stop_service(sys.argv[2], registry)

    elif command == "status":
        status(registry)

    else:
        print("Unknown command")

if __name__ == "__main__":
    main()