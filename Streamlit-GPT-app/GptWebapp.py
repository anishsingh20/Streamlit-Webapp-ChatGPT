import streamlit as st
import openai
import os

# Set your OpenAI API key here
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to interact with the GPT-3.5-turbo model with tunable parameters
def generate_response(prompt, temperature=0.7, max_tokens=256, top_p=0.9, n=2, stop=None, frequency_penalty=0.9, presence_penalty=0.9):
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt},
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        n=n,
        stop=stop,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty
    )

    return response['choices'][0]['message']['content']

# tattooes geek logo
logo1 = 'https://miro.medium.com/v2/resize:fit:180/1*ypRBA86IBBbZbti76vm4Hg.png'
# Streamlit app header and title
st.set_page_config(page_title="Personal ChatGPT bot | By Anish Singh Walia", page_icon=logo1 , layout="wide")


st.write("# Personal Chatbot with GPT-3.5-turbo :sunglasses: ")
st.write("Made with love by - [Anish Singh Walia](https://anishsinghwalia.medium.com/)")
st.write("Welcome to your personal chatbot! Type your message below:")


st.sidebar.markdown("# Model Parameters")
temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.7, 0.1)
max_tokens = st.sidebar.number_input("Max Tokens", 50, 500, 256, step=50)
top_p = st.sidebar.slider("Top P", 0.1, 1.0, 0.9, 0.1)
n = st.sidebar.number_input("N", 1, 5, 2, step=1)
stop = st.sidebar.text_input("Stop", "")
frequency_penalty = st.sidebar.slider("Frequency Penalty", 0.0, 1.0, 0.9, 0.1)
presence_penalty = st.sidebar.slider("Presence Penalty", 0.0, 1.0, 0.9, 0.1)

# Main app loop
user_input = st.text_area("You:", "", key="user_input")
generate_button = st.button("Generate Response")

# Sidebar with social profiles and model parameters

st.sidebar.markdown("# Follow me on my Social Profiles")
st.sidebar.markdown(
    """<a href="https://github.com/anishsingh20" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="GitHub" width="60px"></a>
    <a href="https://www.linkedin.com/in/anish-singh-walia-924529103/" target="_blank"><img src="https://cdn1.iconfinder.com/data/icons/logotypes/32/circle-linkedin-512.png" alt="LinkedIn" width="60px"></a>
    <a href="https://medium.com/@anishsinghwalia" target="_blank"><img src="https://cdn1.iconfinder.com/data/icons/social-media-circle-7/512/Circled_Medium_svg5-512.png" alt="Medium" width="60px"></a>
    <a href="https://instagram.com/cali_br20" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Instagram_logo_2016.svg/2048px-Instagram_logo_2016.svg.png" alt="Instagram" width="60px"></a>
    """,
    unsafe_allow_html=True,
)


if generate_button and user_input.strip() != "":
    # Generate response using GPT-3.5-turbo with selected parameters
    response = generate_response(user_input, temperature, max_tokens, top_p, n, stop, frequency_penalty, presence_penalty)

    # Display the model's response
    st.text_area("Chatbot:", response, key="model_response", height=200)

# Additional styling to make the app visually appealing
st.markdown(
    """
    <style>
        body {
            font-family: Montserrat, sans-serif;
        }
        .stTextInput>div>div>textarea {
            background-color: #f0f0f0;
            color: #000;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
        }
    </style>
    """,
    unsafe_allow_html=True,
)