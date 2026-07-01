from __future__ import annotations

import threading
import time
from typing import Callable, Optional


class Watchdog:
    def __init__(self, callback: Callable[[], None], interval_seconds: float = 10.0) -> None:
        self.callback = callback
        self.interval_seconds = interval_seconds
        self._thread: Optional[threading.Thread] = None
        self._stop_event = threading.Event()

    def _run(self) -> None:
        while not self._stop_event.wait(self.interval_seconds):
            self.callback()

    def start(self) -> None:
        if self._thread and self._thread.is_alive():
            return
        self._stop_event.clear()
        self._thread = threading.Thread(target=self._run, daemon=True)
        self._thread.start()

    def stop(self) -> None:
        self._stop_event.set()
        if self._thread is not None:
            self._thread.join(timeout=1.0)
            self._thread = None
