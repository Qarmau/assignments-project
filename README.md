Welcome to the Django Assignment Management System! This application allows teachers to upload assignments online, which students can then access remotely. This README file will guide you through setting up and using the system.

Features

- Teacher Dashboard: Upload and manage assignments.
- Student Portal: Access and download assignments.
- User Authentication: Separate logins for teachers and students.



 Requirements

- Python 3.8 or later
- Django 4.0 or later
- PostgreSQL or SQLite
- pip (Python package installer)

 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Qarmau/assignments-project
   cd assignments-project
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

4. Create a superuser for the admin interface:

   ```bash
   python manage.py createsuperuser
   ```

5. Run the development server:

   ```bash
   python manage.py runserver
   ```

   You can now access the application at `http://127.0.0.1:8000/`.


 Usage

1. Accessing the System:
   - Visit the admin interface at `http://127.0.0.1:8000/admin` to manage assignments and users.

2. Teacher Functions:
   - Log in to the teacher dashboard to upload and manage assignments.

3. Student Functions:
   - Students can log in to view and download assignments.

 Contributing

We welcome contributions to improve the Django Assignment Management System. If you have suggestions or improvements, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a pull request.

Please ensure that your code follows the existing style and includes relevant tests.

License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or support, please contact kamauj613@gmail.com

Thank you for using the Django Assignment Management System! We hope it enhances your educational experience.
