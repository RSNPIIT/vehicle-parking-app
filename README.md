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

📂 https://drive.google.com/file/d/1OAGhlKo35PAy1-pzfxdsMS8PLH9ng2GY/view?usp=drive_link

NOTE : To open this all must have a valid iitm.ac.in email id 
Learners outside the system of IIT Madras need to ask for permission via gmail.


## 📚 Project Report :

The Link of the project report is :

📂 https://docs.google.com/document/d/1AZfhAa69oYk5N_B3m-0ZITWaK6j97USM/edit?usp=drive_link&ouid=106565817420713086394&rtpof=true&sd=true

NOTE : All learners having a valid iitm.ac.in email id can view and comment
However Those without are mere viewers .

## 🗃️ Directory Structure :

$ tree -a -I 'venv|.git'
.
├── app.py
├── .gitignore
├── instance
│   └── parking.db
├── models
│   └── db_init.sql
├── README.md
├── requirements.txt
├── static
│   ├── images
│   │   ├── adm001.jpg
│   │   ├── adm002.jpg
│   │   ├── adm003.jpg
│   │   ├── adm004.jpg
│   │   ├── adm005.jpg
│   │   ├── adm006.jpg
│   │   ├── adm007.jpg
│   │   ├── adm008.jpg
│   │   ├── adm009.jpg
│   │   ├── adm010.jpg
│   │   ├── banjara.jpg
│   │   ├── commstreet.jpg
│   │   ├── connaught.jpg
│   │   ├── howrah.jpg
│   │   ├── jlnstadium.jpg
│   │   ├── marinedrive.jpg
│   │   ├── mgroad.jpg
│   │   ├── parkstreet.jpg
│   │   ├── phoenix.jpg
│   │   └── sector17.jpg
│   └── style.css
├── templates
│   ├── about.html
│   ├── admin_dashboard.html
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── logout.html
│   ├── register.html
│   └── user_dashboard.html
└── utils
    ├── db.py
    ├── __init__.py
    └── __pycache__
        ├── db.cpython-313.pyc
        └── __init__.cpython-313.pyc

8 directories, 39 files

