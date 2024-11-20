import json
import os
import shutil


GAME_PATH = r"C:\Games\World_of_Warships"
DUMP_PATH = os.path.join(GAME_PATH, "profile", "constants.json")

with open(DUMP_PATH) as fp:
    constants = json.load(fp)
    version = constants["VERSION"]
    shutil.copy(DUMP_PATH, os.path.join(os.path.dirname(__file__), "data", "versions", f"{version['BUILD']}.json"))
    shutil.copy(DUMP_PATH, os.path.join(os.path.dirname(__file__), "data", f"latest.json"))
