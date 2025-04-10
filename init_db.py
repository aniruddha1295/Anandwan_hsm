from app import create_app, db
from app.models import User, Patient, Inventory, Prescription
from datetime import date, datetime, timedelta
from werkzeug.security import generate_password_hash
import random

def init_database():
    app = create_app()
    with app.app_context():
        # Create tables
        db.create_all()
        
        # Check if inventory exists
        if Inventory.query.count() == 0:
            print("Creating sample inventory...")
            
            # Sample inventory items
            medications = [
                ('Dapsone 100mg', 'medication', 1000, 'tablets', date.today() + timedelta(days=365)),
                ('Rifampicin 600mg', 'medication', 500, 'tablets', date.today() + timedelta(days=365)),
                ('Clofazimine 50mg', 'medication', 750, 'tablets', date.today() + timedelta(days=365)),
                ('Prednisolone 5mg', 'medication', 200, 'tablets', date.today() + timedelta(days=180)),
                ('Bandages', 'supplies', 100, 'rolls', None),
                ('Surgical Gloves', 'supplies', 500, 'pairs', None),
                ('Wheelchair', 'equipment', 5, 'units', None),
                ('Crutches', 'equipment', 10, 'pairs', None),
                ('Protective Footwear', 'supplies', 30, 'pairs', None)
            ]
            
            inventory_items = []
            for name, category, quantity, unit, expiry in medications:
                item = Inventory(
                    name=name,
                    category=category,
                    quantity=quantity,
                    unit=unit,
                    expiry_date=expiry,
                    last_updated=datetime.utcnow()
                )
                inventory_items.append(item)
            
            db.session.add_all(inventory_items)
            db.session.commit()
            print("Sample inventory created!")
            
        print("Inventory initialization complete!")

if __name__ == "__main__":
    init_database()