from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, DateField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class InventoryForm(FlaskForm):
    name = StringField('Item Name', validators=[DataRequired()])
    category = SelectField('Category', choices=[
        ('medication', 'Medication'),
        ('equipment', 'Equipment'),
        ('supplies', 'Supplies')
    ])
    quantity = IntegerField('Quantity', validators=[DataRequired(), NumberRange(min=0)])
    unit = StringField('Unit', validators=[DataRequired()])
    expiry_date = DateField('Expiry Date (if applicable)', format='%Y-%m-%d', validators=[])
    submit = SubmitField('Save Item')