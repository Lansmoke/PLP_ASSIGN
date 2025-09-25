-- clinic_db.sql
-- Clinic Booking System database
-- Run: mysql -u root -p < clinic_db.sql

DROP DATABASE IF EXISTS clinic_db;
CREATE DATABASE clinic_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE clinic_db;

-- Users table (for authentication / staff)
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    role ENUM('admin','reception','doctor') NOT NULL DEFAULT 'reception',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Patients
CREATE TABLE patients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    date_of_birth DATE,
    gender ENUM('male','female','other') DEFAULT 'other',
    phone VARCHAR(30),
    email VARCHAR(255),
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(email)
);

-- Doctors
CREATE TABLE doctors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    speciality VARCHAR(100),
    phone VARCHAR(30),
    email VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(email)
);

-- Services (what a clinic offers)
CREATE TABLE services (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    description TEXT,
    duration_minutes INT NOT NULL CHECK (duration_minutes > 0),
    price DECIMAL(10,2) DEFAULT 0.00,
    UNIQUE(name)
);

-- Appointment statuses
CREATE TABLE appointment_status (
    id INT AUTO_INCREMENT PRIMARY KEY,
    code VARCHAR(30) NOT NULL UNIQUE, -- e.g., SCHEDULED, COMPLETED, CANCELLED, NO_SHOW
    description VARCHAR(255)
);

INSERT INTO appointment_status (code, description) VALUES
('SCHEDULED','Appointment scheduled'),
('COMPLETED','Appointment completed'),
('CANCELLED','Appointment cancelled'),
('NO_SHOW','Patient did not show up');

-- Appointments
CREATE TABLE appointments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    doctor_id INT NOT NULL,
    service_id INT NOT NULL,
    appointment_start DATETIME NOT NULL,
    appointment_end DATETIME NOT NULL,
    status_id INT NOT NULL DEFAULT 1, -- SCHEDULED
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_appointment_patient FOREIGN KEY (patient_id) REFERENCES patients(id) ON DELETE CASCADE,
    CONSTRAINT fk_appointment_doctor FOREIGN KEY (doctor_id) REFERENCES doctors(id) ON DELETE RESTRICT,
    CONSTRAINT fk_appointment_service FOREIGN KEY (service_id) REFERENCES services(id) ON DELETE RESTRICT,
    CONSTRAINT fk_appointment_status FOREIGN KEY (status_id) REFERENCES appointment_status(id) ON DELETE RESTRICT,
    CONSTRAINT chk_end_after_start CHECK (appointment_end > appointment_start)
);

-- Prevent duplicate identical appointment slots for the same doctor at the same time (coarse)
-- Note: This does not prevent overlapping intervals; more complex checks require triggers / application logic.
CREATE UNIQUE INDEX ux_doctor_slot ON appointments (doctor_id, appointment_start);

-- Many-to-many: doctors can have multiple specialties (string list alternative), or we can track doctor availabilities
CREATE TABLE doctor_availability (
    id INT AUTO_INCREMENT PRIMARY KEY,
    doctor_id INT NOT NULL,
    weekday TINYINT NOT NULL CHECK (weekday BETWEEN 0 AND 6), -- 0=Sunday .. 6=Saturday
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    CONSTRAINT fk_avail_doctor FOREIGN KEY (doctor_id) REFERENCES doctors(id) ON DELETE CASCADE,
    CONSTRAINT chk_avail_times CHECK (end_time > start_time)
);

-- Prescriptions (linked to appointment)
CREATE TABLE prescriptions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    appointment_id INT NOT NULL,
    prescribed_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    notes TEXT,
    CONSTRAINT fk_presc_appointment FOREIGN KEY (appointment_id) REFERENCES appointments(id) ON DELETE CASCADE
);

-- Medications for prescriptions (1 prescription -> many medication rows)
CREATE TABLE prescription_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    prescription_id INT NOT NULL,
    medication_name VARCHAR(200) NOT NULL,
    dosage VARCHAR(100),
    frequency VARCHAR(100),
    duration_days INT,
    CONSTRAINT fk_presc_item_prescription FOREIGN KEY (prescription_id) REFERENCES prescriptions(id) ON DELETE CASCADE
);

-- Optional: create some helpful indexes
CREATE INDEX idx_appointments_patient ON appointments(patient_id);
CREATE INDEX idx_appointments_doctor ON appointments(doctor_id);
CREATE INDEX idx_appointments_date ON appointments(appointment_start);

-- Sample admin user insertion (password_hash should be replaced with a real bcrypt hash)
INSERT INTO users (username, password_hash, role) VALUES ('admin', '$2b$12$EXAMPLEBCRYPTHASHSHOULDBEREPLACED', 'admin');

-- Done
