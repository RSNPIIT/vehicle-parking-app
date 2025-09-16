from flask import Flask, render_template, request, redirect, url_for, session, flash
from utils.db import get_connection
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_super_secret_key'

@app.route("/")
def home():
    return render_template("index.html", name="Ramrup")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Admin login check
        if username == 'admin' and password == 'admin123':
            session['username'] = 'admin'
            session['role'] = 'admin'  
            flash("Logged in as admin.")
            return redirect(url_for('admin_dashboard'))

        # User login check in DB
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        conn.close()

        if user and password == user['password_hash']:  
            session['username'] = username
            session['role'] = 'user' 
            flash("Logged in successfully.")
            return redirect(url_for('user_dashboard'))

        flash("Invalid credentials.")
        return redirect(url_for('login'))

    return render_template('login.html')

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            conn.close()
            flash("Username already taken. Please choose a different one.")
            return redirect(url_for("register"))

        cursor.execute("INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)",
                       (username, email, password))
        conn.commit()
        conn.close()

        session['username'] = username
        session['role'] = 'user'
        flash("Registered successfully.")
        return redirect(url_for("user_dashboard"))

    return render_template("register.html")

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.clear()
    flash("Logged out successfully.")
    return redirect(url_for('home'))

@app.route("/admin")
def admin_dashboard():
    if session.get("username") != "admin":
        return redirect(url_for("login"))

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM bookings ORDER BY timestamp DESC")
    bookings = cursor.fetchall()

    cursor.execute("SELECT * FROM parking_lots ORDER BY id")
    lots = cursor.fetchall()

    conn.close()

    return render_template("admin_dashboard.html", bookings=bookings, lots=lots)


@app.route('/user_dashboard')
def user_dashboard():
    username = session.get("username", "Guest")

    parking_lots = [
        {"id": 1, "name": "Connaught Place Lot", "address": "Block A, CP, New Delhi", "image": "connaught.jpg", "price": 50},
        {"id": 2, "name": "Phoenix Mall Lot", "address": "Velachery, Chennai", "image": "phoenix.jpg", "price": 40},
        {"id": 3, "name": "Howrah Station Lot", "address": "Howrah Railway Station, Kolkata", "image": "howrah.jpg", "price": 30},
        {"id": 4, "name": "MG Road Parking", "address": "MG Road, Bangalore", "image": "mgroad.jpg", "price": 45},
        {"id": 5, "name": "Marine Drive Parking", "address": "Marine Drive, Mumbai", "image": "marinedrive.jpg", "price": 55},
        {"id": 6, "name": "Banjara Hills Lot", "address": "Banjara Hills, Hyderabad", "image": "banjara.jpg", "price": 35},
        {"id": 7, "name": "Sector 17 Parking", "address": "Sector 17, Chandigarh", "image": "sector17.jpg", "price": 25},
        {"id": 8, "name": "Park Street Lot", "address": "Park Street, Kolkata", "image": "parkstreet.jpg", "price": 40},
        {"id": 9, "name": "Commercial Street Parking", "address": "Commercial Street, Bangalore", "image": "commstreet.jpg", "price": 45},
        {"id": 10, "name": "JLN Stadium Lot", "address": "JLN Stadium, New Delhi", "image": "jlnstadium.jpg", "price": 50}
    ]

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT spot FROM bookings WHERE username = ?", (username,))
    result = cursor.fetchone()
    user_booked_spot = result[0] if result else None
    conn.close()

    return render_template(
        'user_dashboard.html',
        username=username,
        parking_lots=parking_lots,
        user_booked_spot=user_booked_spot
    )

@app.route('/book_spot', methods=['POST'])
def book_spot():
    username = session.get("username")
    spot = request.form.get("spot")

    if not username or username == "admin":
        return redirect(url_for("login", msg="access_denied"))

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM bookings WHERE username = ?", (username,))
    user_booking = cursor.fetchone()
    if user_booking:
        conn.close()
        return redirect(url_for("user_dashboard", msg="already_booked"))

    cursor.execute("SELECT * FROM bookings WHERE spot = ?", (spot,))
    spot_taken = cursor.fetchone()
    if spot_taken:
        conn.close()
        return redirect(url_for("user_dashboard", msg="spot_taken"))

    cursor.execute(
        "INSERT INTO bookings (username, spot, timestamp) VALUES (?, ?, CURRENT_TIMESTAMP)",
        (username, spot)
    )
    conn.commit()
    conn.close()
    return redirect(url_for("user_dashboard", msg="booked"))

@app.route('/release_spot', methods=['POST'])
def release_spot():
    username = session.get("username")

    if not username or username == "admin":
        return redirect(url_for("login", msg="access_denied"))

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM bookings WHERE username = ?", (username,))
    conn.commit()
    conn.close()

    return redirect(url_for("user_dashboard", msg="released"))

@app.route("/admin/add_lot", methods=["POST"])
def add_parking_lot():
    if session.get("username") != "admin":
        return redirect(url_for("login"))

    name = request.form.get("name")
    location = request.form.get("location")
    price = request.form.get("price")

    if name and location and price:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO parking_lots (name, location, price)
            VALUES (?, ?, ?)
        """, (name, location, price))
        conn.commit()
        conn.close()
    
    return redirect(url_for("admin_dashboard"))


@app.route("/admin/remove_lot/<int:lot_id>", methods=["POST"])
def remove_parking_lot(lot_id):
    if session.get("username") != "admin":
        return redirect(url_for("login"))

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM parking_lots WHERE id = ?", (lot_id,))
    conn.commit()
    conn.close()

    return redirect(url_for("admin_dashboard"))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
