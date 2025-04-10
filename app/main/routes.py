from flask import render_template, redirect, url_for
from app.main import bp
from app.models import Patient, Inventory

@bp.route('/')
def index():
    # Get counts for dashboard
    patient_count = Patient.query.count()
    inventory_count = Inventory.query.count()
    treatment_count = Patient.query.filter_by(treatment_status='active').count()
    
    return render_template('index.html', title='Home',
                          patient_count=patient_count,
                          inventory_count=inventory_count,
                          treatment_count=treatment_count)

@bp.route('/about')
def about():
    return render_template('about.html', title='About Anandwan')