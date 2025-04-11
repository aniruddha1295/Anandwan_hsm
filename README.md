# Anandwan Hospital Management System

A comprehensive web application designed to streamline hospital operations at Anandwan facility. This system manages patient records, doctor schedules, appointments, and administrative tasks through a secure, intuitive interface.

## Tech Stack

### Backend
- **Python 3.9+**: Core programming language
- **Flask**: Lightweight WSGI web application framework
- **SQLAlchemy**: SQL toolkit and Object-Relational Mapping (ORM) library
- **Flask-Login**: User session management for Flask
- **Flask-WTF**: Simple integration of Flask and WTForms, including CSRF protection
- **Flask-Migrate**: SQLAlchemy database migrations using Alembic
- **PyMySQL/mysqlclient**: MySQL database connector for Python

### Frontend
- **HTML5/CSS3**: Markup and styling
- **JavaScript**: Client-side scripting
- **Bootstrap 5**: Responsive UI framework
- **Jinja2**: Templating engine for Flask
- **Chart.js**: JavaScript charting for analytics visualizations
- **DataTables**: Advanced table controls for data display

### Database
- **MySQL**: Relational database for data storage
- **PlanetScale**: Serverless MySQL database platform (deployment)

### Deployment & Infrastructure
- **Vercel**: Serverless deployment platform
- **Git/GitHub**: Version control and code repository
- **Environment Variables**: Configuration management using python-dotenv

### Security
- **Bcrypt**: Password hashing
- **CSRF Protection**: Cross-Site Request Forgery prevention
- **Role-Based Access Control**: Permission management by user role

## Project Structure

## Features

### User Authentication & Authorization
- Multi-role user system (Admin, Doctor, Staff)
- Secure password management
- Role-based access control

### Patient Management
- Patient registration and profile management
- Medical history tracking
- Document upload and management

### Appointment System
- Schedule appointments with doctors
- Manage doctor availability
- Appointment reminders and notifications

### Medical Records
- Electronic health records
- Treatment history
- Prescription management

### Administrative Tools
- Staff management
- Department configuration
- System settings

### Analytics & Reporting
- Patient statistics
- Department utilization
- Appointment analytics

## Installation and Setup

### Prerequisites
- Python 3.9 or higher
- MySQL database
- Git

### Local Development Setup
1. Clone the repository

### Deployment to Vercel

1. Ensure you have `vercel.json` configured correctly
2. Set up environment variables in Vercel dashboard
3. Deploy using Vercel CLI or GitHub integration

## Future Enhancements

- Laboratory test integration
- Mobile application for patients
- Telemedicine capabilities
- Billing and insurance processing
- Pharmacy inventory management
- Advanced analytics dashboard

## Contributors

- Aniruddha - Project Lead & Developer

## License

This project is proprietary software developed for Anandwan Hospital.

---
Last updated: 2025-04-11
