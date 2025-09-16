# 🚗 Vehicle Parking App

A simple multi-user Vehicle Parking Management Web App built using **Flask**, **SQLite**, and **Bootstrap**.

## 📌 Features

### 👤 User
- Register and login
- Book a parking slot
- Release the booked slot
- View current bookings with timestamps

### 🛠️ Admin
- View all bookings
- Add or remove parking lots
- Remove bookings manually
- Dashboard with slot, user, time info

## 🧠 Technologies Used

| Category       | Tools / Frameworks         |
|----------------|-----------------------------|
| Backend        | Python 3, Flask             |
| Templating     | Jinja2                      |
| Database       | SQLite                      |
| Frontend       | HTML5, CSS3, Bootstrap 5    |
| Others         | Git, GitHub (for version control) |

## ⚠️ Challenges Faced

- **Image loading failures**: Original design included images for parking slots which broke due to path/db issues. Removed to simplify.
- **SQLite query errors**: Needed strict handling of cursor rows and error checking.
- **Flask session issues**: Resolved by ensuring proper app secret key and session usage.
- **Form handling bugs**: Fixed with method checks and CSRF-safe forms.
- **Cleanup for submission**: Removed all unnecessary files like `venv/`, `__pycache__/`, scripts.

## 📚 What I Learned

- Structuring a Flask app with routes, templates, and database logic.
- Using SQLite with Python via `sqlite3` and organizing DB utility functions.
- Bootstrap integration for responsive UI.
- Version control basics (clean commits, `.gitignore`, and organizing code).
- Debugging real-world template and backend integration issues.

## 🎥 Video Demo

📂 [Watch Explanation Video on Google Drive](https://drive.google.com/your-video-link)

> *(Replace with your actual video link once uploaded)*

---

## 🗃️ Directory Structure

