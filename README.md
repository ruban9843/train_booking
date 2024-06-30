# train_booking
its an train booking system demonstration project with my mongo db atlas

# Train Booking System

This is a web application built with Flask that allows users to book train tickets. It provides functionalities for both administrators and users, ensuring a smooth booking experience.

## Features

- **Admin Dashboard**: Manage train schedules, add, edit, and delete tickets.
- **User Booking**: Book tickets with ease and view available train schedules.
- **Secure Admin Login**: Access protected by a password.
- **Responsive Design**: Built using Bootstrap for a seamless user experience.

## Technologies Used

- **Flask**: Web framework for Python.
- **MongoDB Atlas**: Database for storing tickets and bookings.
- **HTML/CSS**: Frontend design.
- **Bootstrap**: For responsive UI design.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name

Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Set Up Environment Variables:
Create a .env file and add your MongoDB connection string:

plaintext
Copy code
MONGO_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/ticket_booking?retryWrites=true&w=majority
Run the Application:

bash
Copy code
flask run
Access the Application:
Visit http://localhost:5000 in your browser.

Usage
Admin Login: Access the admin dashboard by entering the admin password.
Manage Tickets: Add, edit, and delete train tickets.
Book Tickets: Users can book tickets and view available options.
Important Note
Please update the default admin password and database credentials in the .env file for security purposes.

Future Improvements
Implement user registration and authentication.
Add payment gateway integration.
Enhance UI with additional features.
