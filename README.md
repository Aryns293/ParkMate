🚗 ParkMate — Smart Parking Management System
🧠 About the Project

ParkMate is a smart parking management system developed using Python (Flask) that automates the process of slot allocation, vehicle entry, exit tracking, and revenue calculation.
It integrates Software Quality Metrics analysis (Halstead, Information Flow, Live Variables, and Measure of Dispersion) to evaluate and improve software maintainability, reliability, and performance.

🌟 Key Features

🔐 User & Vehicle Management — Register and track vehicles with timestamps.

🎯 Smart Slot Allocation — Automatically assigns random free slots among 10 available ones.

🕒 Real-Time Parking Status — Displays occupied and available slots dynamically.

💰 Revenue & Duration Tracking — Calculates parking time and cost efficiently.

📊 Integrated Metrics Dashboard — Displays Halstead, Information Flow, and Live Variable metrics visually.

💾 SQLite Database Support — Lightweight, easy-to-manage backend database.

🏗️ Tech Stack
Layer	Technology Used
Frontend	HTML, CSS, JavaScript
Backend	Python (Flask Framework)
Database	SQLite
Code Quality Tools	Radon, Pylint
Metrics Computation	Custom Python scripts (info_flow_metrics.py, calculate_dispersion_metrics.py)
Visualization	Chart.js in HTML dashboard
⚙️ Project Architecture
ParkMate/
│
├── app.py                        # Main Flask app entry point
│
├── models/                       # Data Models
│   ├── parking_lot.py
│   ├── user.py
│   └── vehicle.py
│
├── services/                     # Business Logic Layer
│   ├── db_service.py
│   ├── metrics_service.py
│   └── parking_service.py
│
├── templates/                    # Frontend Templates
│   ├── index.html
│   └── history.html
│
├── static/                       # CSS & JS files
│   └── style.css
│
├── database/                     # Database Folder
│   └── parkmate.db
│
├── docs/                         # Analysis Reports
│   ├── halstead.json
│   ├── information-metrics.json
│   ├── live-variables-summary.txt
│   ├── dispersion-metrics-simplified.csv
│   └── halstead-metrics-summary.txt
│
└── README.md                     # This file

🧮 Software Quality Metrics
Metric Type	Tool / Script	Purpose
Halstead Metrics	radon hal	Measures code complexity, effort, and maintainability
Information Flow Metrics	info_flow_metrics.py	Calculates Fan-In, Fan-Out, and Information Flow Value
Live Variable Metrics	pylint	Detects unused and unreachable code segments
Measure of Dispersion	calculate_dispersion_metrics.py	Evaluates consistency and variance in code metrics
🚀 How to Run
1️⃣ Clone the Repository
git clone https://github.com/Aryns293/ParkMate.git
cd ParkMate

2️⃣ Install Dependencies
pip install flask radon pylint networkx

3️⃣ Run the Flask App
python3 app.py


Visit your app at: http://127.0.0.1:5000/

📈 Running Metric Analyses
🧩 Halstead Metrics
radon hal models services -j > docs/halstead.json

🧩 Information Flow Metrics
python3 info_flow_metrics.py

🧩 Live Variable Metrics
pylint models services --disable=all --enable=W0612,W0611,W0101 > docs/live-variables-summary.txt

🧩 Measure of Dispersion
python3 calculate_dispersion_metrics.py


All results are stored in the /docs folder for visualization and reporting.

📊 Sample Dashboard Preview

System Metrics Overview — total classes, methods, attributes, inheritance relations, and vehicles parked.

Charts (via Chart.js) visualize metrics like total effort, code volume, and revenue.

🧠 Learning Outcomes

Practical understanding of Software Quality Metrics.

Experience in Flask-based backend architecture.

Exposure to code analysis and visualization tools.

Improved skills in structured project documentation and version control (Git).

🧑‍💻 Author

Aryan Sharma
📍 Developer | Software Quality Analyst | B.Tech CSE
🔗 GitHub: Aryns293

🏁 License

This project is licensed under the MIT License — feel free to modify and reuse with credits.
