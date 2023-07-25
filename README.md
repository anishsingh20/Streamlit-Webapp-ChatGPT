# Streamlit-Webapp-ChatGPT
Your own customizable ChatGPT Webapp made in Python using Streamlit.

## Running the app

1) Simply clone this repository using:
   ```shell
   $ git clone https://github.com/anishsingh20/Streamlit-Webapp-ChatGPT/
   ```

2) Install required libraries:
   ```shell
   pip install streamlit openai
   ``` 
3) Get inside the directory ```Streamlit-GPT-app```.
   
4) Run the following python ```GptWebappv2.py``` file which has the source code using command:
   
   ```shell
    $ streamlit run chatbot_app.py
   ```
   <img width="1673" alt="Screenshot 2023-07-25 at 8 21 36 AM" src="https://github.com/anishsingh20/Streamlit-Webapp-ChatGPT/assets/15655876/ca0b7138-47e9-4406-8069-358c4fa6456e">


## INTRODUCTION

[Streamlit](https://www.streamlit.io/) is an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science. You can build and deploy powerful data apps in just a few minutes. So let's get started!

Imagine having your AI-powered chatbot web app ready to answer questions, generate creative content, and assist you in your daily tasks. Thanks to OpenAI's powerful language models and easy-to-use APIs, building a personal AI assistant is now within reach of any Python developer. This tutorial will show you how to create your ChatGPT bot using the Streamlit framework and OpenAI's GPT-3.5-turbo model.

### 1. Setting Up OpenAI API Key and Streamlit

Before building the ChatGPT bot, ensure access to OpenAI's API. You can sign up for an [API key](https://platform.openai.com/account/api-keys) on the [OpenAI website](https://platform.openai.com/account/api-keys) if you haven't already. Once you have your API key, set it up as an environment variable in your development environment on the terminal/shell:

```shell 
$ export OPENAI_API_KEY=<YOUR_API_KEY>
```

Next, install the required libraries and set up your Python environment:

```shell
$ pip install streamlit openai
```


### 2. Building the ChatGPT Bot with Streamlit

Let's dive into the code to build our chatbot using Streamlit. Create a Python file (e.g., chatbot_app.py) and follow along:

```python

import streamlit as st
import openai
import os

# Set your OpenAI API key here
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to interact with the GPT-3.5-turbo model with tunable parameters
def generate_response(prompt, temperature=0.7, max_tokens=256, top_p=0.9, n=2, stop=None, frequency_penalty=0.9, presence_penalty=0.9, chat_history=None):
    if chat_history is None:
        chat_history = []

    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt},
    ]
    messages.extend(chat_history)

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

# Streamlit app header and title
 # tattooed geek logo
logo1 = 'https://miro.medium.com/v2/resize:fit:180/1*ypRBA86IBBbZbti76vm4Hg.png'
# Streamlit app header and title
st.set_page_config(page_title="Personal ChatGPT bot | By Anish Singh Walia", page_icon=logo1 , layout="wide")

st.write("# Personal Chatbot with GPT-3.5-turbo :sunglasses: ")
st.write("Made with love by - [Anish Singh Walia](https://anishsinghwalia.medium.com/)")
st.write("Welcome to your personal chatbot app! Type your message below:")

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

# HTML sidebar to fine-tune model's parameters to customize the bot's responses.
st.sidebar.markdown("# Model Parameters")
temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.7, 0.1)
max_tokens = st.sidebar.number_input("Max Tokens", 50, 500, 256, step=50)
top_p = st.sidebar.slider("Top P", 0.1, 1.0, 0.9, 0.1)
n = st.sidebar.number_input("N", 1, 5, 2, step=1)
stop = st.sidebar.text_input("Stop", "")
frequency_penalty = st.sidebar.slider("Frequency Penalty", 0.0, 1.0, 0.9, 0.1)
presence_penalty = st.sidebar.slider("Presence Penalty", 0.0, 1.0, 0.9, 0.1)

# Main app where user enters prompt and gets the response
user_input = st.text_area("You:", "", key="user_input")
generate_button = st.button("Generate Response")

# Chat history
messages = []
if user_input.strip() != "":
    messages.append({"role": "user", "content": user_input})
    response = generate_response(user_input, temperature, max_tokens, top_p, n, stop, frequency_penalty, presence_penalty)
    messages.append({"role": "assistant", "content": response})

st.subheader("Chat History")
for message in messages:
    if message["role"] == "user":
        st.text_area("You:", value=message["content"], height=50, max_chars=200, key="user_history", disabled=True)
    else:
        st.text_area("Jarvis:", value=message["content"], height=500, key="chatbot_history")

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
        .stTextArea>div>textarea {
            resize: none;
        }
        .st-subheader {
            margin-top: 20px;
            font-size: 16px;
        }
        .stTextArea>div>div>textarea {
            height: 100px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

```

The above code can also be found inside the directory ```Streamlit-GPT-app\GptWebappv2.py``` 

### 3. Running the ChatGPT Bot using Streamlit

To run the ChatGPT bot, execute the following command in your terminal or command prompt:

```shell

$ streamlit run chatbot_app.py

```
<img width="1676" alt="Screenshot 2023-07-25 at 8 38 35 AM" src="https://github.com/anishsingh20/Streamlit-Webapp-ChatGPT/assets/15655876/b0107b9b-f634-491a-8b02-ee2736420615">

