from flask import Flask, render_template, request, jsonify
from api import bedrock_api # Import the function from API.py

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

    prompt = "Recommend 3 majors based on personal context."
    parameters = f"I enjoy {interests}" # Add user interests to the parameters
    formatting = "\nFormat your response like this: -Make the first word of each major 'MAJOR' -before the description write 'DESCRIPTION' -Give a description that is around 100 words per major"
    
    # Call the Bedrock API and get the response
    api_response = get_bedrock_response(prompt, parameters, formatting)
    # Process data (e.g., store in a database, forward to another API, etc.)
    # For now, just log it
    print("API response:", api_response)
    return jsonify({"success": True, "message": "Interests received!", "api_response": api_response})

@app.route('/submit_preferences', methods=['POST'])
def submit_preferences():
    data = request.get_json()  # Get JSON data from the request
    
    preferences = data.get("preferences")
    timestamp = data.get("timestamp")

    # Log received data for debugging
    print("Received preferences:", preferences)
    print("Timestamp:", timestamp)

    # Prepare the prompt for the Bedrock API
    prompt = "Recommend 3 majors based on personal context."
    parameters = f"I prefer {', '.join(preferences)}"  # Add user preferences to the parameters
    formatting = "\nFormat your response like this: -Make the first word of each major 'MAJOR' -before the description write 'DESCRIPTION' -Give a description that is around 100 words per major"
    
    # Call the Bedrock API and get the response
    api_response = get_bedrock_response(interests, preferences)

    # Log the API response for debugging
    print("API response:", api_response)


    # render the results page (CS.html) with the API response
    return render_template('CS.html', majors_data=api_response)
    
if __name__ == '__main__':
    app.run(port=54321, debug=True)

