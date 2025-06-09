"""
@file web_server.py
@brief Web interface for greenhouse monitoring using Flask.

This application displays sensor data, target parameters,
and allows the user to generate a report as a downloadable file.

All functions are documented with Doxygen-style comments to facilitate
HTML documentation generation and ensure maintainability.
"""

from flask import Flask, render_template_string, redirect, url_for, send_file
import os
from db_ctrl import Database

app = Flask(__name__)
db = Database()

target_parameters = {
    "temperature": 25.0,
    "humidity": 50,
    "co2": 400,
    "nitrates": 2.0
}

# === HTML TEMPLATE ===
layout = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Greenhouse Dashboard</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f0f5f1; padding: 30px; }
        h2 { color: #2e8b57; }
        table { border-collapse: collapse; width: 100%; background-color: #fff; }
        th, td { border: 1px solid #ccc; padding: 10px; text-align: center; }
        th { background-color: #e0f8e0; }
        .nav { margin-bottom: 20px; }
        .nav button {
            background-color: #4CAF50; color: white;
            padding: 10px 20px; border: none; cursor: pointer;
            margin-right: 10px; border-radius: 4px;
        }
        .nav button:hover { background-color: #45a049; }
        .download-link {
            margin-top: 20px;
            display: inline-block;
            background: #2e8b57;
            color: white;
            padding: 10px 15px;
            text-decoration: none;
            border-radius: 4px;
        }
    </style>
</head>
<body>
    <div class="nav">
        <form action="{{ url_for('DisplayData') }}" method="get" style="display:inline;">
            <button type="submit">Display Data</button>
        </form>
        <form action="{{ url_for('GetParameters') }}" method="get" style="display:inline;">
            <button type="submit">Target Parameters</button>
        </form>
        <form action="{{ url_for('GenerateReport') }}" method="get" style="display:inline;">
            <button type="submit">Generate Report</button>
        </form>
    </div>
    {{ content|safe }}
</body>
</html>
"""

@app.route('/')
def home():
    """
    @brief Redirects to the main data display page.
    """
    return redirect(url_for('DisplayData'))

@app.route('/data')
def DisplayData():
    """
    @brief Displays historical measurement data in a table.
    """
    table_html = """
    <h2>Measurement Data</h2>
    <table>
        <tr>
            <th>Timestamp</th><th>Temperature (°C)</th><th>Humidity (%)</th><th>CO₂ (ppm)</th><th>Nitrates (mg/L)</th>
        </tr>
    """
    greenhouse_records = db.get_all_data()
    for entry in greenhouse_records:
        table_html += f"""
        <tr>
            <td>{entry.timestamp}</td>
            <td>{entry.temperature}</td>
            <td>{entry.humidity}</td>
            <td>{entry.co2}</td>    
            <td>{entry.n2}</td>
        </tr>
        """
    table_html += "</table>"
    return render_template_string(layout, content=table_html)

@app.route('/parameters')
def GetParameters():
    """
    @brief Displays current target parameters for greenhouse control.
    """
    p = target_parameters
    content = f"""
    <h2>Target Parameters</h2>
    <ul>
        <li>Temperature: {p['temperature']} °C</li>
        <li>Humidity: {p['humidity']} %</li>
        <li>CO₂: {p['co2']} ppm</li>
        <li>Nitrates: {p['nitrates']} mg/L</li>
    </ul>
    """
    return render_template_string(layout, content=content)

@app.route('/report')
def GenerateReport():
    """
    @brief Generates a textual report from all historical data and provides a download link.
    """
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    REPORT_PATH = os.path.join(BASE_DIR, "greenhouse_report.txt")
    greenhouse_records = db.get_all_data()
    if not greenhouse_records:
        content = "<p>No data available to generate report.</p>"
    else:
        report_lines = ["=== Greenhouse Report ==="]
        for m in greenhouse_records:
            report_lines.append(
                f"Time: {m.timestamp} | Temp: {m.temperature} °C | "
                f"Humidity: {m.humidity} % | CO₂: {m.co2} ppm | Nitrates: {m.n2} mg/L"
            )
        report_text = "\n".join(report_lines)

        with open(REPORT_PATH, "w", encoding="utf-8") as f:
            f.write(report_text)

        content = """
        <h2>Report Generated</h2>
        <a class="download-link" href="/download" download>Download Report</a>
        """
    return render_template_string(layout, content=content)

@app.route('/download')
def DownloadReport():
    """
    @brief Sends the generated report file for download.
    @return Flask file response
    """
    return send_file("greenhouse_report.txt", as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
