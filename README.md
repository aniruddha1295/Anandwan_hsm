# Anandwan Hospital Management System

A comprehensive web application designed to streamline hospital operations at Anandwan facility. This system manages patient records, prescriptions, medical inventory, and administrative tasks through a secure, intuitive interface.

**Live Demo:** [https://anandwan-hsm.vercel.app](https://anandwan-hsm.vercel.app)

## Tech Stack

### Backend
- **Python 3.12**: Core programming language
- **Flask**: Lightweight WSGI web application framework
- **SQLAlchemy**: SQL toolkit and Object-Relational Mapping (ORM) library
- **Flask-Login**: User session management for Flask
- **Flask-WTF**: Simple integration of Flask and WTForms, including CSRF protection
- **Flask-Migrate**: Database migration handling via Alembic
- **psycopg2**: PostgreSQL database adapter for Python

### Frontend
- **HTML5/CSS3**: Markup and styling
- **Bootstrap 5**: Responsive UI framework (via bootstrap-flask)
- **Jinja2**: Templating engine for Flask
- **Bootstrap Icons**: Icon library

### Database
- **SQLite**: Local development database
- **PostgreSQL (Neon)**: Serverless PostgreSQL for production deployment

### Deployment & Infrastructure
- **Vercel**: Serverless deployment platform
- **Neon**: Serverless PostgreSQL database
- **Git/GitHub**: Version control and code repository
- **python-dotenv**: Environment variable management

### Security
- **Werkzeug (scrypt)**: Password hashing
- **CSRF Protection**: Cross-Site Request Forgery prevention via Flask-WTF
- **Role-Based Access Control**: Permission management by user role

## Project Structure

```
Anandwan_hsm/
├── app/
│   ├── __init__.py          # App factory, extensions init
│   ├── models.py            # User, Patient, Prescription, Inventory models
│   ├── auth/                # Authentication (login, register, profile)
│   ├── patients/            # Patient management (CRUD, prescriptions)
│   ├── inventory/           # Medical inventory management
│   ├── admin/               # Admin dashboard, user management
│   ├── main/                # Home page, about page
│   ├── static/              # CSS, images, favicon
│   └── templates/           # Jinja2 HTML templates
├── config.py                # App configuration (env vars)
├── run.py                   # Development server entry point
├── wsgi.py                  # Production WSGI entry point (Vercel)
├── init_db.py               # Database initialization script
├── seed_demo.py             # Demo data seeding script
├── requirements.txt         # Python dependencies
├── vercel.json              # Vercel deployment config
└── Procfile                 # Gunicorn config for Heroku/Render
```

## Features

### User Authentication & Authorization
- Multi-role user system (Admin, Doctor, Nurse)
- Secure login and registration
- Role-based access control for different user types
- User profile management

### Patient Management
- Patient registration with personal details
- Leprosy-specific fields (MB/PB type, disability grade, treatment status)
- Patient profile viewing and editing
- Medical notes tracking

### Prescription System
- Create prescriptions linked to doctors and patients
- Diagnosis, medications, and instructions tracking
- Prescription history per patient

### Inventory Management
- Track medications, equipment, and supplies
- Quantity and unit management
- Expiry date tracking for medications

### Administrative Tools
- User management (edit roles, manage accounts)
- System settings
- Admin dashboard

## Installation and Setup

### Prerequisites
- Python 3.9 or higher
- Git

### Local Development Setup

1. Clone the repository
   ```bash
   git clone https://github.com/aniruddha1295/Anandwan_hsm.git
   cd Anandwan_hsm
   ```

2. Create and activate a virtual environment
   ```bash
   python -m venv venv
   source venv/Scripts/activate    # Windows (Git Bash)
   source venv/bin/activate        # macOS/Linux
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root
   ```
   SECRET_KEY=your-secret-key-here
   DATABASE_URL=sqlite:///app.db
   ```

5. Initialize the database
   ```bash
   python init_db.py
   ```

6. (Optional) Seed demo data
   ```bash
   python seed_demo.py
   ```

7. Run the application
   ```bash
   python run.py
   ```

8. Open http://127.0.0.1:5000 in your browser

### Demo Credentials

| Username | Password | Role |
|----------|----------|------|
| `dr_patil` | `doctor123` | Doctor |
| `dr_sharma` | `doctor123` | Doctor |
| `dr_deshmukh` | `doctor123` | Doctor |
| `nurse_kamble` | `nurse123` | Nurse |
| `nurse_jadhav` | `nurse123` | Nurse |
| `admin` | `admin123` | Admin |

### Deployment to Vercel

1. Push your code to GitHub
2. Create a free PostgreSQL database on [Neon](https://neon.tech)
3. Set environment variables in the Vercel dashboard:
   - `SECRET_KEY` — a strong random string
   - `DATABASE_URL` — your Neon PostgreSQL connection string
4. Deploy using Vercel CLI or connect your GitHub repo:
   ```bash
   vercel --prod
   ```

## Contributors

- Aniruddha - Project Lead & Developer

---
Last updated: 2026-03-09
