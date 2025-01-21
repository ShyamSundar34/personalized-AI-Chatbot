from flask import Flask, render_template, request
import google.generativeai as genai

# Create a Flask application instance
app = Flask(__name__)

# Configure the Google Generative AI API
def configure_ai():
    try:
        genai.configure(api_key="AIzaSyChwnVlpMe4mBLKqVGnP3UiUcb9wEBRIIg")
        return genai.GenerativeModel("gemini-1.5-flash")
    except Exception as e:
        print(f"Error configuring AI: {e}")
        return None

# Route for the homepage with both GET and POST methods
@app.route('/', methods=['GET', 'POST'])
def hello_world():
    response_text = None
    if request.method == 'POST':
        user_query = request.form['query']
        print(user_query)
        # Interact with the AI to generate a response
        model = configure_ai()
        if model:
            try:
                final = ""
                response = model.generate_content(user_query)
                response_text = response.text
            except Exception as e:
                print(f"Error generating content: {e}")
                response_text = "An error occurred while fetching the AI response."
        else:
            response_text = "AI configuration failed."

    return render_template('index.html', response=response_text)

# Run the app
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)