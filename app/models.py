from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime, date

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(20))  # 'doctor', 'nurse', 'admin'
    prescriptions = db.relationship('Prescription', backref='doctor', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=False)
    gender = db.Column(db.String(10))
    age = db.Column(db.Integer)
    contact = db.Column(db.String(15))
    address = db.Column(db.String(200))
    registration_date = db.Column(db.Date, default=date.today)
    
    # Leprosy specific fields
    leprosy_type = db.Column(db.String(50))  # MB/PB
    disability_grade = db.Column(db.Integer)  # 0, 1, 2
    treatment_status = db.Column(db.String(20))  # active, completed, defaulted
    notes = db.Column(db.Text)
    
    prescriptions = db.relationship('Prescription', backref='patient', lazy='dynamic')
    
    def __repr__(self):
        return f'<Patient {self.first_name} {self.last_name}>'

class Prescription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, default=date.today)
    diagnosis = db.Column(db.String(200))
    medications = db.Column(db.Text)
    instructions = db.Column(db.Text)
    doctor_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))

    def __repr__(self):
        return f'<Prescription {self.id}>'

class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50))  # medication, equipment, supplies
    quantity = db.Column(db.Integer, default=0)
    unit = db.Column(db.String(20))  # tablets, bottles, pieces
    expiry_date = db.Column(db.Date)
    last_updated = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Inventory {self.name}>'