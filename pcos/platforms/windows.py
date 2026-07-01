import subprocess

from pcos.platforms.base import Platform


class WindowsPlatform(Platform):

    def run(self, command: str):
        return subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
        )