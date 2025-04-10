from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.patients import bp
from app.models import Patient, Prescription
from app.patients.forms import PatientForm, PrescriptionForm
from app import db
from datetime import date

@bp.route('/')
@bp.route('/index')
@login_required
def index():
    patients = Patient.query.all()
    return render_template('patients/index.html', title='Patients', patients=patients)

@bp.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = PatientForm()
    if form.validate_on_submit():
        patient = Patient(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            gender=form.gender.data,
            age=form.age.data,
            contact=form.contact.data,
            address=form.address.data,
            leprosy_type=form.leprosy_type.data,
            disability_grade=form.disability_grade.data,
            treatment_status=form.treatment_status.data,
            notes=form.notes.data,
            registration_date=date.today()
        )
        db.session.add(patient)
        db.session.commit()
        flash('Patient added successfully!', 'success')
        return redirect(url_for('patients.index'))
    return render_template('patients/add.html', title='Add Patient', form=form)

@bp.route('/<int:id>/view')
@login_required
def view(id):
    patient = Patient.query.get_or_404(id)
    prescriptions = patient.prescriptions.all()
    return render_template('patients/view.html', title=f'Patient: {patient.first_name}',
                          patient=patient, prescriptions=prescriptions)

@bp.route('/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit(id):
    patient = Patient.query.get_or_404(id)
    form = PatientForm(obj=patient)
    if form.validate_on_submit():
        patient.first_name = form.first_name.data
        patient.last_name = form.last_name.data
        patient.gender = form.gender.data
        patient.age = form.age.data
        patient.contact = form.contact.data
        patient.address = form.address.data
        patient.leprosy_type = form.leprosy_type.data
        patient.disability_grade = form.disability_grade.data
        patient.treatment_status = form.treatment_status.data
        patient.notes = form.notes.data
        db.session.commit()
        flash('Patient updated successfully!', 'success')
        return redirect(url_for('patients.view', id=patient.id))
    return render_template('patients/edit.html', title='Edit Patient', form=form, patient=patient)

@bp.route('/<int:id>/prescribe', methods=['GET', 'POST'])
@login_required
def prescribe(id):
    if current_user.role != 'doctor':
        flash('Only doctors can create prescriptions', 'danger')
        return redirect(url_for('patients.view', id=id))
        
    patient = Patient.query.get_or_404(id)
    form = PrescriptionForm()
    if form.validate_on_submit():
        prescription = Prescription(
            diagnosis=form.diagnosis.data,
            medications=form.medications.data,
            instructions=form.instructions.data,
            date=date.today(),
            doctor=current_user,
            patient=patient
        )
        db.session.add(prescription)
        db.session.commit()
        flash('Prescription added successfully!', 'success')
        return redirect(url_for('patients.view', id=patient.id))
    return render_template('patients/prescribe.html', title='Add Prescription', 
                          form=form, patient=patient)