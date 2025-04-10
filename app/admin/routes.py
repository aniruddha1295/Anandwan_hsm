from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.admin import bp
from app.models import User
from app import db
from .forms import UserForm, SystemSettingsForm
from app.admin.utils import admin_required

# Admin Dashboard
@bp.route('/')
@login_required
@admin_required
def index():
    user_count = User.query.count()
    return render_template('admin/index.html', title='Admin Dashboard', user_count=user_count)

# User Management
@bp.route('/users')
@login_required
@admin_required
def users():
    users = User.query.all()
    return render_template('admin/users.html', title='User Management', users=users)

@bp.route('/users/add', methods=['GET', 'POST'])
@login_required
@admin_required
def add_user():
    form = UserForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,
                   email=form.email.data,
                   role=form.role.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'User {form.username.data} has been added!', 'success')
        return redirect(url_for('admin.users'))
    return render_template('admin/add_user.html', title='Add User', form=form)

@bp.route('/users/<int:id>/edit', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_user(id):
    user = User.query.get_or_404(id)
    form = UserForm(obj=user)
    
    # Don't require password for edit
    form.password.validators = []
    form.password.flags.required = False
    
    if form.validate_on_submit():
        user.username = form.username.data
        user.email = form.email.data
        user.role = form.role.data
        
        # Only update password if provided
        if form.password.data:
            user.set_password(form.password.data)
            
        db.session.commit()
        flash(f'User {user.username} has been updated!', 'success')
        return redirect(url_for('admin.users'))
    
    return render_template('admin/edit_user.html', title='Edit User', form=form, user=user)

@bp.route('/users/<int:id>/delete')
@login_required
@admin_required
def delete_user(id):
    user = User.query.get_or_404(id)
    
    # Prevent self-deletion
    if user.id == current_user.id:
        flash('You cannot delete your own account!', 'danger')
        return redirect(url_for('admin.users'))
    
    username = user.username
    db.session.delete(user)
    db.session.commit()
    flash(f'User {username} has been deleted!', 'success')
    return redirect(url_for('admin.users'))

# System Settings
@bp.route('/settings', methods=['GET', 'POST'])
@login_required
@admin_required
def settings():
    form = SystemSettingsForm()
    
    if form.validate_on_submit():
        # In a real app, save settings to database
        # For now, just show success message
        flash('System settings have been updated!', 'success')
        return redirect(url_for('admin.settings'))
    
    # In a real app, load settings from database
    # For demo purposes, we're using defaults
    
    return render_template('admin/settings.html', title='System Settings', form=form)