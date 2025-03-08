from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def menu():
    return render_template('menu.html')

@app.route('/Q1')
def q1():
    return render_template('Q1.html')

@app.route('/Q2')
def q2():
    return render_template('Q2.html')

@app.route('/submit_interests', methods=['POST'])  # Add this route
def submit_interests():
    data = request.get_json()  # Get JSON data from the request
    
    interests = data.get("interests")
    timestamp = data.get("timestamp")
    
    # Log received data for debugging
    print("Received interests:", interests)
    print("Timestamp:", timestamp)
    
    # Process data (e.g., store in a database, forward to another API, etc.)
    # For now, just log it
    
    return jsonify({"success": True, "message": "Interests received!"})
    
if __name__ == '__main__':
    app.run(port=54321, debug=True)
