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

def submit_interests():
    data = request.get_json()
    
    interests = data.get("interests")
    timestamp = data.get("timestamp")
    
    # Log received data for debugging
    print("Received interests:", interests)
    print("Timestamp:", timestamp)
    
    #Process data
    #For now, just log it

    
    
    return jsonify({"success": True, "message": "Interests received!"})
    
if __name__ == '__main__':
    app.run(port=54321, debug=True)
