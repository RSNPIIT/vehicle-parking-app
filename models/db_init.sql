-- users table: stores user info
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- parking_lots table: each parking lot
CREATE TABLE IF NOT EXISTS parking_lots (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    rows INTEGER NOT NULL,      -- e.g. 5 rows
    columns INTEGER NOT NULL,   -- e.g. 5 columns
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- parking_spots table: spots inside lots, named like A1, B3 etc
CREATE TABLE IF NOT EXISTS parking_spots (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    lot_id INTEGER NOT NULL,
    spot_label TEXT NOT NULL,   -- e.g. A1, B5
    is_occupied INTEGER NOT NULL DEFAULT 0,
    FOREIGN KEY (lot_id) REFERENCES parking_lots(id) ON DELETE CASCADE,
    UNIQUE (lot_id, spot_label)
);

-- bookings table: track user bookings
CREATE TABLE IF NOT EXISTS bookings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    spot TEXT NOT NULL,
    timestamp TEXT DEFAULT CURRENT_TIMESTAMP
);
