import streamlit as st
import pandas as pd 

  # Set page title
st.title("My First Streamlit App")

  # Add header
st.header("Welcome to the dashboard")
 
  # Add text
st.write("This is a simple demonstration of Streamlit capabilities")

  ## Creating a Simple Streamlit Chatbot
def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []

def main():
    st.title("Simple Chatbot")
    
    initialize_session_state()

    # Display chat messages from history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # Chat input
    if prompt := st.chat_input("What's on your mind?"):
        # Display user message
        with st.chat_message("user"):
            st.write(prompt)
        
        # Add user message to history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Add simple bot response
        response = f"You said: {prompt}"
        
        # Display bot message
        with st.chat_message("assistant"):
            st.write(response)
        
        # Add bot message to history
        st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()

# Sample DataFrame
df = pd.DataFrame({
    'Month': ['January', 'February', 'March', 'January'],
    'Price': [1000, 1500, 2000, 1200]
})

# Add sidebar
st.sidebar.header("Filters")

# Add dropdown
selected_month = st.sidebar.selectbox(
    "Select Month",
    options=df['Month'].unique()
)

# Add slider
price_range = st.sidebar.slider(
    "Select Price Range",
    min_value=0,
    max_value=3000,
    value=(0, 3000)
    )


import streamlit as st
import pandas as pd
import random

# Page configuration
st.set_page_config(
    page_title="Student Dashboard",
    page_icon="📊",
    layout="centered"
)

import streamlit as st
import pandas as pd
import os

# Page title
st.title("📚 Study Buddy Matcher")

st.write("""
Find study partners from the same subject,
discuss assignments, and prepare for exams together.
""")

# Create CSV file if it doesn't exist
if not os.path.exists("students.csv"):
    df = pd.DataFrame(columns=[
        "name",
        "subject",
        "goal"
    ])
    df.to_csv("students.csv", index=False)

# User input
name = st.text_input("Enter your name")

subject = st.selectbox(
    "Choose your subject",
    [
        "Math",
        "Physics",
        "Chemistry",
        "Biology",
        "Computer Science"
    ]
)

goal = st.text_area("What do you need help with?")

# Button
if st.button("Find Study Group"):

    # Save student data
    new_student = pd.DataFrame({
        "name": [name],
        "subject": [subject],
        "goal": [goal]
    })

    new_student.to_csv(
        "students.csv",
        mode="a",
        header=False,
        index=False
    )

    # Read all students
    df = pd.read_csv("students.csv")

    # Find matching students
    matches = df[df["subject"] == subject]

    st.success("🎉 Study group found!")

    st.subheader("Students studying the same subject")

    st.dataframe(matches)

    