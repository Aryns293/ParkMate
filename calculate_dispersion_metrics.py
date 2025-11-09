import json
import csv
import math
import statistics as stats
import os

input_file = "halstead.json"
if not os.path.exists(input_file):
    print("halstead.json not found! Please run:")
    print("radon hal models services -j > halstead.json")
    exit()

with open(input_file) as f:
    data = json.load(f)

#  Metrics to extract from the 'total' section of each file
metrics_data = {
    "volume": [],
    "difficulty": [],
    "effort": [],
    "estimated_bugs": [],
    "time_to_program_hours": [],
    "N1": [],
    "N2": [],
    "vocabulary": [],
}

#  Extract only the "total" metrics from each file
for file, details in data.items():
    if "total" in details:
        total = details["total"]
        metrics_data["volume"].append(total.get("volume", 0))
        metrics_data["difficulty"].append(total.get("difficulty", 0))
        metrics_data["effort"].append(total.get("effort", 0))
        metrics_data["estimated_bugs"].append(total.get("bugs", 0))
        metrics_data["time_to_program_hours"].append(total.get("time", 0))
        metrics_data["N1"].append(total.get("N1", 0))
        metrics_data["N2"].append(total.get("N2", 0))
        metrics_data["vocabulary"].append(total.get("vocabulary", 0))

# Compute dispersion stats for each metric
output_rows = []
for metric, values in metrics_data.items():
    # Remove all-zero metrics
    values = [v for v in values if v != 0]
    if not values:
        continue

    N = len(values)
    min_v = min(values)
    max_v = max(values)
    rng = max_v - min_v
    mean = stats.mean(values)
    mean_dev = sum(abs(x - mean) for x in values) / N
    variance = stats.variance(values) if N > 1 else 0
    std_dev = math.sqrt(variance)
    cv = (std_dev / mean * 100) if mean else 0

    output_rows.append([
        metric, N, round(min_v, 3), round(max_v, 3), round(rng, 3),
        round(mean, 3), round(mean_dev, 3), round(variance, 3),
        round(std_dev, 3), round(cv, 2)
    ])

# Save as CSV
os.makedirs("docs", exist_ok=True)
output_path = "docs/dispersion-metrics-simplified.csv"

header = ["Metric", "N", "Min", "Max", "Range", "Mean", "Mean Deviation", "Variance", "Std Dev", "CV%"]

with open(output_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(output_rows)

print(f"Dispersion metrics saved → {output_path}")
