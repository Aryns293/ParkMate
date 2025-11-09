🚗 ParkMate – Smart Parking Management System
🧩 A Flask-based Parking Automation App with Integrated Software Quality Metrics
🌟 Overview

ParkMate is a Flask web application designed to manage parking slots automatically —
assigning, tracking, and calculating fares for vehicles in real time.
It also includes software quality metric analysis tools (Halstead, Live Variables, Information Flow, and Dispersion)
to evaluate and enhance software performance, reliability, and maintainability.

⚙️ Tech Stack
Layer	Technologies
Frontend	HTML, CSS, JavaScript, Chart.js
Backend	Python (Flask)
Database	SQLite
Metrics Tools	Radon, Pylint, NetworkX
Reports	JSON, CSV visualized in /docs/
🚀 Features

✅ Smart Slot Allocation – Randomly assigns one of 10 available slots.
✅ Driver Details Logging – Captures driver name, phone number, and entry time.
✅ Automated Fare Calculation – ₹100/hr (4-wheeler), ₹50/hr (2-wheeler).
✅ Real-Time Parking Table – View occupied and free slots instantly.
✅ No Space Warning – Displays “No Space Available” when all slots are full.
✅ Integrated Metrics Dashboard – Displays Halstead, Information Flow, and Revenue stats.

🗂️ Project Structure
ParkMate/
├── app.py                         # Main Flask app
├── models/
│   ├── user.py
│   ├── vehicle.py
│   └── parking_lot.py
├── services/
│   ├── db_service.py
│   ├── metrics_service.py
│   └── parking_service.py
├── templates/
│   ├── index.html
│   └── history.html
├── static/
│   └── style.css
├── database/
│   └── parkmate.db
├── docs/
│   ├── halstead.json
│   ├── information-metrics.json
│   ├── live-variables-summary.txt
│   ├── dispersion-metrics-simplified.csv
│   └── halstead-metrics-summary.txt
└── README.md

🧮 Software Quality Metrics
Metric                    Tool Used                              Description
Halstead Metrics          radon hal                              Measures complexity, effort, and maintainability
Information Flow          info_flow_metrics.py                   Calculates Fan-In, Fan-Out, and Information Flow Value
Live Variable Analysis     pylint                                Detects unused or unreachable variables
Measure of Dispersion      calculate_dispersion_metrics.py       Calculates variance and code stability metrics

🧑‍💻 How to Run the Project
1️⃣ Clone Repository
git clone https://github.com/Aryns293/ParkMate.git
cd ParkMate

2️⃣ Install Requirements
pip install flask radon pylint networkx

3️⃣ Run the App
python3 app.py


Then visit 👉 http://127.0.0.1:5000

📊 Generating Metrics

Halstead Metrics
radon hal models services -j > docs/halstead.json


Information Flow
python3 info_flow_metrics.py


Live Variable Metrics
pylint models services --disable=all --enable=W0612,W0611,W0101 > docs/live-variables-summary.txt


Measure of Dispersion
python3 calculate_dispersion_metrics.py

📸 Dashboard Preview
Displays live slot status, driver details, total vehicles, and real-time metrics using Chart.js.

🧠 Learning Outcomes
Implemented real-world software metrics on a live Python project.
Learned Flask app structure and database integration.
Applied static code analysis tools for software quality improvement.
Built a complete end-to-end system with UI + metrics reporting.

👤 Developed By

Aryan Sharma
🎓 B.Tech Software Engineering | DTU
🔗 GitHub: Aryns293

🪪 License
This project is licensed under the MIT License — free to modify and use with attribution.

💡 Short Repo Tagline for GitHub
“Smart Parking + Smart Metrics — A Flask-based Parking Management System with Real-Time Quality Analysis”
