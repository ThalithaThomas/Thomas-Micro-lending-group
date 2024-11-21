# apis/db.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Applicant(db.Model):
    __tablename__ = 'applicant'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    southAfricanId = db.Column(db.String(13), nullable=False)
    firstName = db.Column(db.String(100), nullable=False)
    lastName = db.Column(db.String(100), nullable=False)
    phoneNumber = db.Column(db.String(12), nullable=False)
    applicant_email = db.Column(db.String(100), nullable=False)
    employmentStatus = db.Column(db.String(100), nullable=False)
    employmentStartDate = db.Column(db.Date)
    salaryFrequency = db.Column(db.String(100))
    grossSalary = db.Column(db.Integer, nullable=False)
    NetIncome = db.Column(db.Integer, nullable=False)
    livingEXpenses = db.Column(db.Integer, nullable=False)
