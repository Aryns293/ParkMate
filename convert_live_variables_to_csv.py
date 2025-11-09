import json, csv

with open("docs/live-variables-unused.json") as f:
    data = json.load(f)

with open("docs/live-variables-unused.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["File", "Line", "Message", "Type"])
    for item in data:
        writer.writerow([
            item.get("path"),
            item.get("line"),
            item.get("message"),
            item.get("type")
        ])

print("Converted JSON → CSV at docs/live-variables-unused.csv")
