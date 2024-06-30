from flask import Flask, render_template, url_for, redirect, request, flash, session
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime

app = Flask(__name__)

# MongoDB Configuration
client = MongoClient("mongodb+srv://ruban984301:rubanruban9843@cluster0.w6pm70b.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.ticket_booking
tickets_collection = db.tickets
passengers_collection = db.passengers
bookings_collection = db.bookings

# Secret key for session management
app.secret_key = "ruban9843"
ADMIN_PASSWORD = "password"

# Load Home Page
@app.route("/")
def home():
    tickets = list(tickets_collection.find())
    return render_template("home.html", tickets=tickets)

# Admin Login
@app.route("/admin", methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        password = request.form['password']
        if password == ADMIN_PASSWORD:
            session['admin_logged_in'] = True
            return redirect(url_for("admin"))
        else:
            flash('Incorrect password, please try again.')
            return redirect(url_for("admin_login"))
    return render_template("admin_login.html")

# Admin Page
@app.route("/admin/dashboard")
def admin():
    if 'admin_logged_in' not in session:
        return redirect(url_for('admin_login'))
    tickets = list(tickets_collection.find())
    return render_template("admin.html", tickets=tickets)

# Add New Ticket
@app.route("/admin/addTicket", methods=['GET', 'POST'])
def addTicket():
    if request.method == 'POST':
        event = request.form['event']
        date = request.form['date']
        price = request.form['price']
        tickets_collection.insert_one({"event": event, "date": date, "price": price})
        flash('Ticket Added Successfully')
        return redirect(url_for("admin"))
    return render_template("add_ticket.html")

# Edit Ticket
@app.route("/admin/editTicket/<string:id>", methods=['GET', 'POST'])
def editTicket(id):
    if request.method == 'POST':
        event = request.form['event']
        date = request.form['date']
        price = request.form['price']
        tickets_collection.update_one({"_id": ObjectId(id)}, {"$set": {"event": event, "date": date, "price": price}})
        flash('Ticket Updated Successfully')
        return redirect(url_for("admin"))

    ticket = tickets_collection.find_one({"_id": ObjectId(id)})
    return render_template("edit_ticket.html", ticket=ticket)

# Delete Ticket
@app.route("/admin/deleteTicket/<string:id>", methods=['GET', 'POST'])
def deleteTicket(id):
    tickets_collection.delete_one({"_id": ObjectId(id)})
    flash('Ticket Deleted Successfully')
    return redirect(url_for("admin"))

# Book Ticket
@app.route("/bookTicket/<string:id>", methods=['GET', 'POST'])
def bookTicket(id):
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        passenger_id = passengers_collection.insert_one({"name": name, "email": email}).inserted_id
        bookings_collection.insert_one({"passenger_id": passenger_id, "ticket_id": ObjectId(id), "booking_date": datetime.now()})
        flash('Ticket Booked Successfully')
        return redirect(url_for("home"))

    return render_template("book_ticket.html", ticket_id=id)

# View Booked Passengers
@app.route("/admin/viewBookings/<string:id>")
def viewBookings(id):
    bookings = list(bookings_collection.aggregate([
        {"$match": {"ticket_id": ObjectId(id)}},
        {"$lookup": {
            "from": "passengers",
            "localField": "passenger_id",
            "foreignField": "_id",
            "as": "passenger_info"
        }},
        {"$unwind": "$passenger_info"},
        {"$project": {
            "name": "$passenger_info.name",
            "email": "$passenger_info.email",
            "booking_date": 1
        }}
    ]))
    return render_template("booked_passengers.html", bookings=bookings, ticket_id=id)

if __name__ == '__main__':
    app.secret_key = "abc123"
    app.run(debug=True)
