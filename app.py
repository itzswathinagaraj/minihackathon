import time
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
@app.context_processor
def inject_time():
    # This sends the current time to all templates
    return {'time': int(time.time())}

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Logic for login will go here
        return redirect(url_for('index'))
    return render_template('login.html')

# Register User page
@app.route('/register', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        # Logic for registering user will go here
        return redirect(url_for('success'))
    return render_template('register_user.html')

# Create Event page
@app.route('/create_event', methods=['GET', 'POST'])
def create_event():
    if request.method == 'POST':
        # Logic for creating event will go here
        return redirect(url_for('admin_dashboard'))
    return render_template('create_event.html')

# Event Detail page
@app.route('/event/<int:event_id>')
def event_detail(event_id):
    # In a real app, you would fetch event data from DB
    return render_template('event_detail.html', event_id=event_id)

# Admin Dashboard
@app.route('/admin')
def admin_dashboard():
    return render_template('admin_dashboard.html')

# My Registrations
@app.route('/my_registrations')
def my_registrations():
    return render_template('my_registrations.html')

# Success page
@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
