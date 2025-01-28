from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

#Database configuration (replace with your details)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'jdbc:mysql://localhost:3306/?user=root'
db = SQLAlchemy(app)

#user model (actual model structure)
class User(db.Model):
  id = db.Column(db.Integer , primary_key=True)
  name = db.Column(db.String(80), nullable=False)
  registration_number = db.Column(db.String(20), unique=True, nullable=False)
  def __repr__(self):
    return f'<User {self.name}>'
#Helper functions to hash passwords securely
def hash_password(password):
  #replace with a secure hashing library like bcrypy
  return password #placholder for demonstration



# Route for user registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')  # Display registration form
    else:
        name = request.form['name']
        registration_number = request.form['registration_number']
        password = request.form['password']
        hashed_password = hash_password(password)  # Replace with actual hashing

        # Validate user data (e.g., check for empty fields, unique registration number)
        # ...

        # Create user object and add to database
        new_user = User(name=name, registration_number=registration_number, hashed_password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))  # Redirect to login page after successful registration




# Route for login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')  # Display login form
    else:
        registration_number = request.form['registration_number']
        password = request.form['password']

        # Fetch user from database based on registration number
        user = User.query.filter_by(registration_number=registration_number).first()

        if user and password == user.hashed_password:  # Replace with secure password comparison
            # Login successful (replace with session management or other actions)
            return f"Login successful! Welcome, {user.name}"
        else:
            return "Invalid credentials. Please try again."
        
#Route for the main page (replace with actual content)
@app.route('/')
def index():
   return render_template('index.html')

if __name__== '__main__':
   with app.app_context():
      db.create_all()
   app.run(debug=True)
              