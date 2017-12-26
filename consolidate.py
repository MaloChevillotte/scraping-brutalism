import json
import os

files = os.listdir("json_files")
table = []

for filename in files:
    if ".json" not in filename:
        continue
    print(filename)
    with open("json_files/" + filename) as f:
        table.append(json.load(f))

with open("data.json", "wb") as f:
    json.dump(table, f)
