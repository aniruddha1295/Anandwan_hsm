from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.inventory import bp
from app.models import Inventory
from app.inventory.forms import InventoryForm
from app import db
from datetime import datetime

@bp.route('/')
@bp.route('/index')
@login_required
def index():
    inventory = Inventory.query.all()
    return render_template('inventory/index.html', title='Inventory', inventory=inventory)

@bp.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = InventoryForm()
    if form.validate_on_submit():
        item = Inventory(
            name=form.name.data,
            category=form.category.data,
            quantity=form.quantity.data,
            unit=form.unit.data,
            expiry_date=form.expiry_date.data,
            last_updated=datetime.utcnow()
        )
        db.session.add(item)
        db.session.commit()
        flash('Inventory item added successfully!', 'success')
        return redirect(url_for('inventory.index'))
    return render_template('inventory/add.html', title='Add Inventory Item', form=form)

@bp.route('/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit(id):
    item = Inventory.query.get_or_404(id)
    form = InventoryForm(obj=item)
    if form.validate_on_submit():
        item.name = form.name.data
        item.category = form.category.data
        item.quantity = form.quantity.data
        item.unit = form.unit.data
        item.expiry_date = form.expiry_date.data
        item.last_updated = datetime.utcnow()
        db.session.commit()
        flash('Inventory item updated successfully!', 'success')
        return redirect(url_for('inventory.index'))
    return render_template('inventory/edit.html', title='Edit Inventory Item', form=form, item=item)
@bp.route('/<int:id>/delete')
@login_required
def delete(id):
    item = Inventory.query.get_or_404(id)
    
    # Optional: Add permission check
    # if current_user.role != 'admin' and current_user.role != 'nurse':
    #     flash('You do not have permission to delete inventory items.', 'danger')
    #     return redirect(url_for('inventory.index'))
    
    name = item.name  # Store name before deletion
    db.session.delete(item)
    db.session.commit()
    flash(f'Inventory item "{name}" has been deleted!', 'success')
    return redirect(url_for('inventory.index'))

@bp.route('/<int:id>/update-quantity', methods=['POST'])
@login_required
def update_quantity(id):
    item = Inventory.query.get_or_404(id)
    new_quantity = request.form.get('quantity', type=int)
    
    if new_quantity is not None and new_quantity >= 0:
        item.quantity = new_quantity
        item.last_updated = datetime.utcnow()
        db.session.commit()
        flash(f'Quantity updated for {item.name}!', 'success')
    else:
        flash('Invalid quantity value!', 'danger')
    
    return redirect(url_for('inventory.index'))