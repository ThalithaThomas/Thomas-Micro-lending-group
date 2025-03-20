import os
from flask import Flask,render_template,request,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError,SQLAlchemyError,DataError
from datetime import datetime,date
app = Flask(__name__, static_url_path='/static', static_folder='static')

app.secret_key=os.environ.get('FLASK_SECRET_KEY','default_secret_key')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['ENV']= 'development'
app.config['DEBUG']= True
db = SQLAlchemy(app)

class Applicant(db.Model):
    __tablename__='applicant'
    id=db.Column(db.Integer, primary_key=True,autoincrement=True)
    title=db.Column(db.String(100), nullable=False)
    southAfricanId = db.Column(db.String(13),nullable=False)
    firstName=db.Column(db.String(100), nullable=False)
    lastName=db.Column(db.String(100), nullable=False)
    phoneNumber = db.Column(db.String(12),nullable=False )
    applicant_email=db.Column(db.String(100), nullable=False)
    employmentStatus=db.Column(db.String(100), nullable=False)
    employmentStartDate=db.Column(db.Date)
    salaryFrequency=db.Column(db.String(100))
    grossSalary=db.Column(db.Integer, nullable=False)
    NetIncome=db.Column(db.Integer, nullable=False)
    livingEXpenses=db.Column(db.Integer, nullable=False)
    
with app.app_context():
        db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contacts')
def contact():
    return render_template("contact.html")

@app.route('/personal')
def personal():
    return render_template("personal.html")

@app.route('/submit-loan-request',methods=['POST'])
def submit_loan_request():
    title=request.form.get('title')
    southAfricanId = request.form.get('ID')
    firstName=request.form.get('Firstname')
    lastName=request.form.get('lastname')
    phoneNumber = request.form.get('phone-number')
    applicant_email=request.form.get('email')
    employmentStatus=request.form.get('employmentStatus')
    employmentStartDate=request.form.get('startDate')
    salaryFrequency=request.form.get('salaryFrequency')
    grossSalary=request.form.get('salary')
    NetIncome=request.form.get('netIncome')
    livingEXpenses=request.form.get('livingExpense')
    requiredFields= [title, southAfricanId,firstName,lastName,phoneNumber,applicant_email,employmentStatus,
   grossSalary,NetIncome,livingEXpenses
    ]
    print(requiredFields)
  
    if any(field is None or field.strip() == '' for field in requiredFields):
        flash('Please fill in all required fields.', 'error')
        return redirect(url_for('personal'))
    try:

        new_applicant=Applicant(title=title,
                                    southAfricanId=southAfricanId,
                                    firstName=firstName,
                                    lastName=lastName,
                                    phoneNumber=phoneNumber,
                                    applicant_email=applicant_email,
                                    employmentStatus=employmentStatus,
                                    employmentStartDate=datetime.strptime(employmentStartDate,'%Y-%m-%d') ,
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
    except Exception as e:
            db.session.rollback()
            flash(f'An unexpected error occurred: {str(e)}', 'error')
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run( debug=True)