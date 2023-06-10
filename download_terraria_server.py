import os
import subprocess

TERRARIA_VERSION = os.environ.get("TERRARIA_VERSION")
SERVER_ZIP = f"terraria-server-{TERRARIA_VERSION.replace('.','')}.zip"
DOWNLOAD_URL = f"https://terraria.org/api/download/pc-dedicated-server/{SERVER_ZIP}"
ROOT = "server"
SERVER_INSTALL = f"{ROOT}/{TERRARIA_VERSION}"

if not os.path.exists(SERVER_ZIP):
    subprocess.call(["wget", DOWNLOAD_URL])

if not os.path.exists(SERVER_INSTALL):
    os.makedirs(ROOT, exist_ok=True)
    subprocess.call(["unzip", SERVER_ZIP, "-d", SERVER_INSTALL])
