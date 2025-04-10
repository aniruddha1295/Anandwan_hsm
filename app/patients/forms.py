from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Optional, NumberRange

class PatientForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    gender = SelectField('Gender', choices=[
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    ])
    age = IntegerField('Age', validators=[NumberRange(min=0, max=120)])
    contact = StringField('Contact Number')
    address = TextAreaField('Address')
    
    # Leprosy specific fields
    leprosy_type = SelectField('Leprosy Type', choices=[
        ('MB', 'Multibacillary (MB)'),
        ('PB', 'Paucibacillary (PB)'),
        ('Unknown', 'Unknown/Not Determined')
    ])
    disability_grade = SelectField('Disability Grade', choices=[
        ('0', '0 - No disability'),
        ('1', '1 - Visible deformity or damage'),
        ('2', '2 - Severe visual impairment; hand/foot deformity')
    ], coerce=int)
    treatment_status = SelectField('Treatment Status', choices=[
        ('active', 'Active - Under Treatment'),
        ('completed', 'Completed Treatment'),
        ('defaulted', 'Defaulted'),
        ('new', 'New Case')
    ])
    notes = TextAreaField('Notes')
    
    submit = SubmitField('Save Patient')

class PrescriptionForm(FlaskForm):
    diagnosis = StringField('Diagnosis', validators=[DataRequired()])
    medications = TextAreaField('Medications', validators=[DataRequired()])
    instructions = TextAreaField('Instructions')
    submit = SubmitField('Save Prescription')
    