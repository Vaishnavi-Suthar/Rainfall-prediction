import tkinter as tk
from tkinter import messagebox, ttk
import joblib
from sklearn.preprocessing import StandardScaler
import numpy as np
import csv
from datetime import datetime
import os

# Load trained model and scaler
model = joblib.load("rainfall_predictor_model.pkl")
scaler = joblib.load("scaler.pkl")

# Parameters with min, max, units
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

# Show prediction history with Clear button
def show_history():
    history_window = tk.Toplevel(window)
    history_window.title("Prediction History")
    history_window.geometry("1000x450")

    tree = ttk.Treeview(history_window)
    cols = ["Timestamp"] + [p[0] for p in parameters] + ["Prediction"]
    tree["columns"] = cols
    tree["show"] = "headings"

    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=100)

    # Load history data
    def load_history_data():
        for row in tree.get_children():
            tree.delete(row)
        try:
            with open("audit_trail.csv", newline="") as f:
                reader = csv.reader(f)
                headers = next(reader)
                for row in reader:
                    tree.insert("", tk.END, values=row)
        except FileNotFoundError:
            messagebox.showinfo("Info", "No prediction history found.")

    # Clear prediction history
    def clear_history():
        if messagebox.askyesno("Confirm", "Are you sure you want to clear the prediction history?"):
            with open("audit_trail.csv", mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Timestamp"] + [p[0] for p in parameters] + ["Prediction"])
            load_history_data()
            messagebox.showinfo("Success", "Prediction history has been cleared.")

    load_history_data()
    tree.pack(fill=tk.BOTH, expand=True)

    clear_button = tk.Button(history_window, text="🧹 Clear History", font=("Helvetica", 12),
                             bg="#f44336", fg="white", command=clear_history)
    clear_button.pack(pady=10)

# Show user audit trail with "Clear History" button
def show_user_audit():
    audit_window = tk.Toplevel(window)
    audit_window.title("User Audit Trail")
    audit_window.geometry("600x450")

    tree = ttk.Treeview(audit_window)
    cols = ["Username", "Login Time", "Logout Time"]
    tree["columns"] = cols
    tree["show"] = "headings"

    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=180)

    # Load audit data
    def load_user_audit_data():
        for row in tree.get_children():
            tree.delete(row)
        try:
            with open("user_audit.csv", newline="") as f:
                reader = csv.reader(f)
                next(reader)  # Skip header
                for row in reader:
                    tree.insert("", tk.END, values=row)
        except FileNotFoundError:
            messagebox.showinfo("Info", "No user audit history found.")

    # Clear audit data
    def clear_user_audit():
        if messagebox.askyesno("Confirm", "Are you sure you want to clear the User Audit Trail?"):
            with open("user_audit.csv", mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Username", "Login Time", "Logout Time"])
            load_user_audit_data()
            messagebox.showinfo("Success", "User audit trail has been cleared.")

    load_user_audit_data()
    tree.pack(fill=tk.BOTH, expand=True)

    clear_button = tk.Button(audit_window, text="🧹 Clear History", font=("Helvetica", 12),
                             bg="#f44336", fg="white", command=clear_user_audit)
    clear_button.pack(pady=10)

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

# Logout and close
def on_logout():
    log_logout_time()
    window.destroy()

# GUI setup
window = tk.Tk()
window.title("Rainfall Prediction System")
window.geometry('700x700+400+50')
window.configure(bg='white')
window.resizable(False, False)
window.protocol("WM_DELETE_WINDOW", on_logout)

# Menu bar
menubar = tk.Menu(window)
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Rainfall Prediction History", command=show_history)
file_menu.add_command(label="User Audit Trail", command=show_user_audit)
file_menu.add_command(label="Exit", command=on_logout)
menubar.add_cascade(label="Menu", menu=file_menu)
window.config(menu=menubar)

# Title
title = tk.Label(window, text="Rainfall Prediction System", font=("Helvetica", 20, "bold"), fg="#1e90ff", bg="white")
title.pack(pady=20)

# Input Frame
form_frame = tk.LabelFrame(window, text="Input Weather Data", font=("Helvetica", 14), bg="white", padx=20, pady=20)
form_frame.pack(padx=20, pady=10)

entries = []
for i, (label_text, min_val, max_val, unit) in enumerate(parameters):
    label = tk.Label(form_frame, text=f"{label_text} ({min_val}-{max_val} {unit})", font=("Helvetica", 10), bg="white")
    label.grid(row=i, column=0, sticky='e', padx=10, pady=5)
    entry = tk.Entry(form_frame, width=25, font=("Helvetica", 10))
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)

# Buttons
button_frame = tk.Frame(window, bg="white")
button_frame.pack(pady=15)

predict_button = tk.Button(button_frame, text="Predict Rainfall", command=predict_rainfall,
                           font=("Helvetica", 12), bg="#4CAF50", fg="white", width=18)
predict_button.grid(row=0, column=0, padx=10)

reset_button = tk.Button(button_frame, text="Reset", command=reset_fields,
                         font=("Helvetica", 12), bg="#f44336", fg="white", width=10)
reset_button.grid(row=0, column=1, padx=10)

# Result label
result_label = tk.Label(window, text="", font=("Helvetica", 16, "bold"), bg="white")
result_label.pack(pady=20)

# Start GUI loop
window.mainloop()
