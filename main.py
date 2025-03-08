from flask import Flask, render_template, request, jsonify, session
from api import call_bedrock
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # You need a secret key to use sessions

user_responses = {
    "interests": [],
    "time_preferences": []
}

@app.route('/', methods=['GET','POST'])
def menu():
    return render_template('menu.html')

@app.route('/Q1')
def q1():
    return render_template('Q1.html')

@app.route('/Q2')
def q2():
    return render_template('Q2.html')

@app.route('/submit_interests', methods=['POST'])
def submit_interests():
    # Get JSON data from the request
    data = request.get_json()
    
    # Extract interests
    interests = data.get("interests")
    
    # Store interests in user_responses
    user_responses["interests"] = interests
    
    # Log received data for debugging
    print("Received interests:", interests)
    
    return jsonify({"success": True, "message": "Interests received!"})

@app.route('/submit_preferences', methods=['POST'])
def submit_preferences():
    # Get JSON data from the request
    data = request.get_json()
    
    # Extract time preferences
    time_preferences = data.get("preferences")
    
    # Store time preferences in user_responses
    user_responses["time_preferences"] = time_preferences
    
    # Log received data for debugging
    print("Received time preferences:", time_preferences)
    
    # Combine interests and time preferences into a single string
    combined_parameters = f"\nI enjoy {', '.join(user_responses['interests'])} and prefer spending time on {', '.join(user_responses['time_preferences'])}"
    
    # Call the Bedrock API and get majors data
    majors_data = call_bedrock(combined_parameters)
    
    # Store majors data in session
    session['majors_data'] = majors_data
    
    # Log for debugging
    print("Majors data stored in session:", majors_data)
    
    return jsonify({"success": True, "message": "Preferences received!"})

@app.route('/CS')
def cs():
    # Retrieve majors data from session
    majors_data = session.get('majors_data', {})
    
    if not majors_data:
        return "No majors data available", 500
    
    return render_template('CS.html', majors_data=majors_data)

if __name__ == '__main__':
    app.run(port=54321, debug=True)