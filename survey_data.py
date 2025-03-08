# q1Dict = {"Solving Math Problems": False,'Science, healthcare, and understanding how the world works':False,'Coding, computer science, and new technology':False,'Designing visuals, animation, or creative projects':False,'Writing, journalism, or storytelling':False,'Psychology, counseling, or understanding human behavior':False,'Business, marketing, and financial strategies':False,' Law, public policy, and government affairs':False,'Nature, sustainability, and environmental sciences':False}
# q2Dict = {"Design and build machines, buildings, or systems": False,'Science, healthcare, and understanding how the world works':False,'Coding, computer science, and new technology':False,'Designing visuals, animation, or creative projects':False,'Writing, journalism, or storytelling':False,'Psychology, counseling, or understanding human behavior':False,'Write and test code for software, apps, or websites':False,'Conduct experiments and analyze scientific data':False,'Create and edit digital content (art, videos, music, design)':False,'Manage money, investments, or business operations':False,'Work with people directly (teaching, therapy, customer service)':False,'Speak publicly, argue cases, or write persuasive content':False,'Study the earth, environment, or space':False}


# def q1_answer_choice(answer):
#     if q1Dict[answer] == False:
#         return True
    
# def q2_answer_choice(answer):
#     if q2Dict[answer] == False:
#         return True
    
user_responses = {
    "interests": [],
    "time_preferences": []
}

def add_interest(interest):
    """Add a selected interest to the user's responses."""
    user_responses["interests"].append(interest)

def add_time_preference(preference):
    """Add a selected time preference to the user's responses."""
    user_responses["time_preferences"].append(preference)

def get_user_responses():
    """Return the user's responses."""
    return user_responses

def create_prompt():
    """Generate a prompt for the API based on user responses."""
    interests = user_responses.get("interests", [])
    time_preferences = user_responses.get("time_preferences", [])

    prompt = f"""
    A first-year student has provided the following information:
    - Interests: {', '.join(interests)}
    - Time Preferences: {', '.join(time_preferences)}

    Based on this information, suggest suitable majors and provide a brief explanation for each suggestion.
    """
    return prompt