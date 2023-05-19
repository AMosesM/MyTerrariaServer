import os
import sys
import subprocess

SERVER_INSTALL = "{APP_HOME}/server/{TERRARIA_VERSION}".format(**os.environ) + f"/{os.environ.get('TERRARIA_VERSION').replace('.','')}"
print(f"{sys.platform}")
if sys.platform == "linux" or sys.platform == "linux2":
    # linux
    pass
elif sys.platform == "darwin":
    print("starting server for mac")
    print(os.environ.get("APP_HOME"))
    # OS X
    subprocess.call([
        f"{SERVER_INSTALL}/Mac/Terraria Server.app/Contents/MacOS/TerrariaServer",
        "-world", "~/world.wld".format(**os.environ),
        "-autocreate", "1"
        
    ])
elif sys.platform == "win32":
    # Windows...
    pass
else:
    pass