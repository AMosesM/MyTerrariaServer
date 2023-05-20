import os
import sys
import subprocess
import re

SERVER_INSTALL = "{APP_HOME}/server/{TERRARIA_VERSION}".format(**os.environ) + f"/{os.environ.get('TERRARIA_VERSION').replace('.','')}"
WORLD_PATH = "{APP_HOME}/Worlds/".format(**os.environ)
WORLD_FILE = "{WORLD_PATH}/MyTerrariaServer.wld".format(**locals())
PORT = os.environ.get("PORT", "7777")
SERVER_CONFIG = "{APP_HOME}/server.cfg".format(**os.environ)
SERVER_RUNTIME_CONFIG = "{APP_HOME}/server-runtime.cfg".format(**os.environ)

def create_runtime_config():
    with open(SERVER_CONFIG, "r") as cfg:
        cfg_text = cfg.read()
        cfg_text = re.sub("worldpath=.*",f"worldpath={WORLD_PATH}", cfg_text)
        cfg_text = re.sub("world=.*",f"world={WORLD_FILE}", cfg_text)
        cfg_text = re.sub("port=.*",f"port={PORT}", cfg_text)
        with open(SERVER_RUNTIME_CONFIG, "w") as runtime_cfg:
            runtime_cfg.write(cfg_text)

create_runtime_config()

if sys.platform == "linux" or sys.platform == "linux2":
    # linux
    subprocess.call([
        f"{SERVER_INSTALL}/Linux/TerrariaServer",
        "-config", SERVER_RUNTIME_CONFIG
    ])
    
elif sys.platform == "darwin":
    print("starting server for mac")
    print(os.environ.get("APP_HOME"))
    # OS X
    subprocess.call([
        f"{SERVER_INSTALL}/Mac/Terraria Server.app/Contents/MacOS/TerrariaServer",
       "-config", SERVER_RUNTIME_CONFIG
    ])
elif sys.platform == "win32":
    # Windows...
    pass
else:
    pass