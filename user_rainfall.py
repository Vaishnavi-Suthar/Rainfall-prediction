import tkinter as tk
from tkinter import messagebox, ttk
import joblib
from sklearn.preprocessing import StandardScaler  # ✅ Correct import
import numpy as np
import csv
from datetime import datetime
import os

# Load trained model and scaler
model = joblib.load("rainfall_predictor_model.pkl")
scaler = joblib.load("scaler.pkl")  # ✅ Load the saved scaler

# Parameters with actual min, max, and units
parameters = [
    ("Day", 1, 365, "day"),
    ("Pressure", 999.0, 1034.6, "hPa"),
    ("Max Temp", 10.4, 36.0, "°C"),
    ("Temperature", 7.4, 31.5, "°C"),
    ("Min Temp", 4.0, 29.8, "°C"),
    ("Dew Point", -0.3, 26.7, "°C"),
    ("Humidity", 39.0, 98.0, "%"),
    ("Cloud", 2.0, 100.0, "%"),
    ("Sunshine", 0.0, 12.1, "hours"),
    ("Wind Direction", 10.0, 300.0, "°"),
    ("Wind Speed", 4.4, 59.5, "km/h")
]

# Predict rainfall
def predict_rainfall():
    inputs = []
    try:
        for i, (label, min_val, max_val, unit) in enumerate(parameters):
            value = float(entries[i].get())
            if not (min_val <= value <= max_val):
                messagebox.showerror("Input Error",
                    f"{label} must be between {min_val} and {max_val} {unit}.")
                return
            inputs.append(value)

        # ✅ Corrected scaling
        inputs_scaled = scaler.transform([inputs])
        prediction = model.predict(inputs_scaled)
        
        result_text = "🌧️ Rainfall Expected!" if prediction[0] == 1 else "☀️ No Rainfall"
        result_label.config(text=result_text, fg="green" if prediction[0] == 0 else "blue")

        # Log prediction to audit_trail.csv
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        prediction_label = "Rainfall" if prediction[0] == 1 else "No Rainfall"
        row = [timestamp] + inputs + [prediction_label]

        file_exists = os.path.exists("audit_trail.csv")
        with open("audit_trail.csv", mode='a', newline='') as file:
            writer = csv.writer(file)
            if not file_exists:
                headers = ["Timestamp"] + [p[0] for p in parameters] + ["Prediction"]
                writer.writerow(headers)
            writer.writerow(row)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")
        


# Reset fields
def reset_fields():
    for entry in entries:
        entry.delete(0, tk.END)
    result_label.config(text="")

# Show prediction history from audit_trail.csv
def show_history():
    history_window = tk.Toplevel(window)
    history_window.title("Prediction History")
    history_window.geometry("1000x400")

    tree = ttk.Treeview(history_window)
    cols = ["Timestamp"] + [p[0] for p in parameters] + ["Prediction"]
    tree["columns"] = cols
    tree["show"] = "headings"

    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=100)

    try:
        with open("audit_trail.csv", newline="") as f:
            reader = csv.reader(f)
            for row in reader:
                tree.insert("", tk.END, values=row)
    except FileNotFoundError:
        messagebox.showinfo("Info", "No prediction history found.")

    tree.pack(fill=tk.BOTH, expand=True)

# Show user audit trail from user_audit.csv
def show_user_audit():
    audit_window = tk.Toplevel(window)
    audit_window.title("User Audit Trail")
    audit_window.geometry("600x400")

    tree = ttk.Treeview(audit_window)
    cols = ["Username", "Login Time", "Logout Time"]
    tree["columns"] = cols
    tree["show"] = "headings"

    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=180)

    try:
        with open("user_audit.csv", newline="") as f:
            reader = csv.reader(f)
            for row in reader:
                tree.insert("", tk.END, values=row)
    except FileNotFoundError:
        messagebox.showinfo("Info", "No user audit history found.")

    tree.pack(fill=tk.BOTH, expand=True)

# Log logout time when window closes
def log_logout_time():
    username = os.environ.get("CURRENT_USER")
    login_time = os.environ.get("CURRENT_LOGIN_TIME")

    if username and login_time:
        logout_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        updated_rows = []

        try:
            with open("user_audit.csv", mode='r', newline='') as file:
                reader = csv.reader(file)
                header = next(reader)
                for row in reader:
                    if row[0] == username and row[1] == login_time and row[2] == "":
                        row[2] = logout_time
                    updated_rows.append(row)

            with open("user_audit.csv", mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Username", "Login Time", "Logout Time"])
                writer.writerows(updated_rows)
        except FileNotFoundError:
            pass


# Logout handler to update logout time
def on_logout():
    username = os.environ.get("CURRENT_USER")
    login_time = os.environ.get("CURRENT_LOGIN_TIME")
    logout_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if username and login_time:
        rows = []
        try:
            with open("user_audit.csv", newline="") as f:
                reader = csv.reader(f)
                rows = list(reader)

            # Update the correct row
            for i in range(1, len(rows)):
                if rows[i][0] == username and rows[i][1] == login_time and rows[i][2] == "":
                    rows[i][2] = logout_time
                    break

            # Rewrite file
            with open("user_audit.csv", mode="w", newline="") as f:
                writer = csv.writer(f)
                writer.writerows(rows)

        except FileNotFoundError:
            pass

    window.destroy()

# Override close event
#window.protocol("WM_DELETE_WINDOW", on_logout)


# GUI setup
window = tk.Tk()
window.title("Rainfall Prediction System")
window.geometry('700x700+400+50')
window.configure(bg='white')
window.resizable(False, False)

# Handle logout on close
window.protocol("WM_DELETE_WINDOW", lambda: (log_logout_time(), window.destroy()))

# Menu bar
'''menubar = tk.Menu(window)
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="History", command=show_history)
file_menu.add_command(label="User Audit Trail", command=show_user_audit)
file_menu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="Menu", menu=file_menu)
window.config(menu=menubar)'''

# Title
title = tk.Label(window, text="Rainfall Prediction System", font=("Helvetica", 20, "bold"), fg="#1e90ff", bg="white")
title.pack(pady=20)

# Frame for inputs
form_frame = tk.LabelFrame(window, text="Input Weather Data", font=("Helvetica", 14), bg="white", padx=20, pady=20)
form_frame.pack(padx=20, pady=10)

entries = []

# Form fields
for i, (label_text, min_val, max_val, unit) in enumerate(parameters):
    label = tk.Label(form_frame, text=f"{label_text} ({min_val}-{max_val} {unit})", font=("Helvetica", 10), bg="white")
    label.grid(row=i, column=0, sticky='e', padx=10, pady=5)
    entry = tk.Entry(form_frame, width=25, font=("Helvetica", 10))
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)

# Predict and Reset Buttons
button_frame = tk.Frame(window, bg="white")
button_frame.pack(pady=15)

predict_button = tk.Button(button_frame, text="Predict Rainfall", command=predict_rainfall,
                           font=("Helvetica", 12), bg="#4CAF50", fg="white", width=18)
predict_button.grid(row=0, column=0, padx=10)

reset_button = tk.Button(button_frame, text="Reset", command=reset_fields,
                         font=("Helvetica", 12), bg="#f44336", fg="white", width=10)
reset_button.grid(row=0, column=1, padx=10)

# Result display
result_label = tk.Label(window, text="", font=("Helvetica", 16, "bold"), bg="white")
result_label.pack(pady=20)

# Start GUI loop
window.mainloop()
