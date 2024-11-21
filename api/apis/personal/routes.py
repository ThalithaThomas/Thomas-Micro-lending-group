# apis/personal/routes.py
from flask import Blueprint, render_template, request, redirect, url_for, flash
from apis.db import db
from apis.db import Applicant
from datetime import datetime
from sqlalchemy.exc import IntegrityError, SQLAlchemyError, DataError

personal_bp = Blueprint('personal', __name__)

@personal_bp.route('/personal')
def personal():
    return render_template("personal.html")

@personal_bp.route('/submit-loan-request', methods=['POST'])
def submit_loan_request():
    title = request.form.get('title')
    southAfricanId = request.form.get('ID')
    firstName = request.form.get('Firstname')
    lastName = request.form.get('lastname')
    phoneNumber = request.form.get('phone-number')
    applicant_email = request.form.get('email')
    employmentStatus = request.form.get('employmentStatus')
    employmentStartDate = request.form.get('startDate')
    salaryFrequency = request.form.get('salaryFrequency')
    grossSalary = request.form.get('salary')
    NetIncome = request.form.get('netIncome')
    livingEXpenses = request.form.get('livingExpense')

    requiredFields = [
        title, southAfricanId, firstName, lastName, phoneNumber,
        applicant_email, employmentStatus, grossSalary, NetIncome, livingEXpenses
    ]

    if any(field is None or field.strip() == '' for field in requiredFields):
        flash('Please fill in all required fields.', 'error')
        return redirect(url_for('personal.personal'))

    try:
        new_applicant = Applicant(
            title=title,
            southAfricanId=southAfricanId,
            firstName=firstName,
            lastName=lastName,
            phoneNumber=phoneNumber,
            applicant_email=applicant_email,
            employmentStatus=employmentStatus,
            employmentStartDate=datetime.strptime(employmentStartDate, '%Y-%m-%d'),
            salaryFrequency=salaryFrequency,
            grossSalary=int(grossSalary),
            NetIncome=int(NetIncome),
            livingEXpenses=int(livingEXpenses)
        )
        db.session.add(new_applicant)
        db.session.commit()
        flash('Your loan request has been successfully submitted!', 'success')
    except IntegrityError:
        db.session.rollback()
        flash('There was an integrity error. Please check your input.', 'error')
    except DataError:
        db.session.rollback()
        flash('There was an error with the data provided. Please check that all fields are correct.', 'error')
    except SQLAlchemyError as e:
        db.session.rollback()
        flash(f'An error occurred: {str(e)}', 'error')

    return redirect(url_for('personal.personal'))
