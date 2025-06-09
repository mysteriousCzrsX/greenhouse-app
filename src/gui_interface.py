"""
@file tkinter_dashboard.py
@brief Tkinter GUI for greenhouse monitoring.

This application corresponds to a web dashboard,
showing sensor data, target parameters, and report generation.
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from db_ctrl import Database

target_parameters = {
    "temperature": 25.0,
    "humidity": 50,
    "co2": 400,
    "nitrates": 2.0
}


class GreenhouseDashboard(tk.Tk):
    def __init__(self):
        """
        @brief Main app window constructor.
        """
        super().__init__()
        self.title("Greenhouse Dashboard")
        self.geometry("700x400")
        self.configure(bg="#f0f5f1")

        self.create_navbar()
        self.content_frame = tk.Frame(self, bg="#f0f5f1")
        self.content_frame.pack(fill="both", expand=True)
        self.db = Database()
        self.display_data()

    def create_navbar(self):
        """
        @brief Top navigation bar initialization.
        """
        nav = tk.Frame(self, bg="#f0f5f1")
        nav.pack(pady=10)

        btn_data = tk.Button(nav, text="Display Data", command=self.display_data, bg="#4CAF50", fg="white")
        btn_params = tk.Button(nav, text="Target Parameters", command=self.display_parameters, bg="#4CAF50", fg="white")
        btn_report = tk.Button(nav, text="Generate Report", command=self.generate_report, bg="#4CAF50", fg="white")

        for btn in [btn_data, btn_params, btn_report]:
            btn.pack(side="left", padx=5)

    def clear_content(self):
        """
        @brief Clears the content of the main window.
        """
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def display_data(self):
        """
        @brief Displays historical measurement data in a table.
        """

        self.clear_content()
        label = tk.Label(self.content_frame, text="Measurement Data", font=("Arial", 16), bg="#f0f5f1", fg="#2e8b57")
        label.pack(pady=10)

        columns = ("timestamp", "temperature", "humidity", "co2", "nitrates")
        tree = ttk.Treeview(self.content_frame, columns=columns, show="headings")
        tree.pack(expand=True, fill="both", padx=10, pady=10)

        for col in columns:
            tree.heading(col, text=col.title())
            tree.column(col, anchor="center")
        greenhouse_records = self.db.get_all_data()
        for row in greenhouse_records:
            tree.insert("", "end", values=(
                row.timestamp, row.temperature, row.humidity, row.co2, row.n2
            ))

    def display_parameters(self):
        """
        @brief Displays current target parameters for greenhouse control.
        """

        self.clear_content()
        label = tk.Label(self.content_frame, text="Target Parameters", font=("Arial", 16), bg="#f0f5f1", fg="#2e8b57")
        label.pack(pady=10)

        for key, value in target_parameters.items():
            line = f"{key.title()}: {value} {'°C' if key == 'temperature' else 'ppm' if key == 'co2' else '%'}"
            param_label = tk.Label(self.content_frame, text=line, bg="#f0f5f1", font=("Arial", 12))
            param_label.pack(anchor="w", padx=20)

    def generate_report(self):
        """
        @brief Generates a textual report from all historical data and saves it as a file.
        """
        self.clear_content()
        label = tk.Label(self.content_frame, text="Report Generation", font=("Arial", 16), bg="#f0f5f1", fg="#2e8b57")
        label.pack(pady=10)
        greenhouse_records = self.db.get_all_data()
        if not greenhouse_records:
            tk.Label(self.content_frame, text="No data available to generate report.", bg="#f0f5f1").pack()
            return

        report_lines = ["=== Greenhouse Report ==="]
        
        for m in greenhouse_records:
            report_lines.append(
                f"Time: {m.timestamp} | Temp: {m.temperature} °C | "
                f"Humidity: {m.humidity} % | CO₂: {m.co2} ppm | Nitrates: {m.n2} mg/L"
            )
        report_text = "\n".join(report_lines)

        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt")],
            title="Save Report As"
        )

        if file_path:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(report_text)
            messagebox.showinfo("Report Saved", f"Report saved to:\n{file_path}")
        else:
            messagebox.showinfo("Cancelled", "Report generation cancelled.")


if __name__ == "__main__":
    app = GreenhouseDashboard()
    app.mainloop()
