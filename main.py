from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

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
    combined_parameters = f"I enjoy {', '.join(user_responses['interests'])} and prefer spending time on {', '.join(user_responses['time_preferences'])}"
    
if __name__ == '__main__':
    app.run(port=54321, debug=True)
