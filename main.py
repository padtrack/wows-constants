import glob
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

manifest = {}
for file in glob.iglob(os.path.join(os.path.dirname(__file__), "data", "versions", "*.json")):
    with open(file) as fp:
        data = json.load(fp)
        version = data["VERSION"]
        manifest[version["BUILD"]] = {"version": version["VERSION"], "patch": version["PATCH"]}

with open("manifest.json", "w") as fp:
    json.dump(dict(sorted(manifest.items(), key=lambda i: int(i[0]))), fp, indent=4)
