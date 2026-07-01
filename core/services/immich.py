from __future__ import annotations

import shutil
import subprocess

from .base import BaseService
from ..registry import ServiceConfig


class ImmichService(BaseService):
    def __init__(self, config: ServiceConfig) -> None:
        super().__init__(config)
        self.url = config.metadata.get("url", "http://localhost:3001") if config.metadata else "http://localhost:3001"

    def validate(self) -> bool:
        """Check if Immich can be started (minimal validation)."""
        self.logger.info("Immich service validation passed.")
        return True

    def is_healthy(self) -> bool:
        """Check if Immich is responding to HTTP requests."""
        try:
            import urllib.request
            response = urllib.request.urlopen(f"{self.url}/api/server/ping", timeout=5)
            return response.status == 200
        except Exception:
            return False
