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


st.title("📚 Study Buddy Matcher")

st.write("""
Find study partners from the same subject,
discuss assignments, and prepare for exams together.
""")

name = st.text_input("Enter your name")
subject = st.selectbox(
    "Choose your subject",
    ["Math", "Physics", "Chemistry", "Biology"]
)

goal = st.text_area("What do you need help with?")

study_time = st.selectbox(
    "Preferred Study Time",
    ["Morning", "Afternoon", "Night"])

if st.button("Find Study Group"):
    st.success(f"Welcome {name}!")
    st.write(f"You are looking for help in {subject}")
    st.write(f"Study Goal: {goal}")

    st.subheader("Suggested Study Group")
    st.write("Group A - Students studying the same subject")

st.subheader("Matched Students")
if st.button("Find Group"):
    matches = df[df["subject"] == subject]

    st.dataframe(matches)
