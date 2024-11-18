import json
import streamlit as st
from main import create_medical_professional

# from main import create_medical_professional

# Create columns
col1, col2 = st.columns(2)
col1.header("Prompt")
col2.header("Saved Prompt")

# Initialize session state for response if not already done
if "response" not in st.session_state:
    st.session_state.response = None

with col1:
    prompt = st.text_input("Prompt: Create a profile for a mental health professional")
    submit_button = st.button("Submit")

    # Handle submit button click
    if submit_button:
        # Simulate the response creation
        st.session_state.response =  create_medical_professional(prompt)
        st.write(st.session_state.response)

    if st.session_state.response:
        save = st.button("Save")

        if save:
            try:
                with open('responses.json', 'r') as file:
                    data = json.load(file)
            except FileNotFoundError:
                data = []

            # Append the response and save to file
            data.append(st.session_state.response)
            with open('responses.json', 'w') as file:
                json.dump(data, file, indent=4)

            st.success("Response saved successfully!")
            # Clear the saved response from session state after saving
            st.session_state.response = None



with col2:
    # Display the saved prompts
    try:
        with open('responses.json', 'r') as file:
            data = json.load(file)
        for i, response in enumerate(data):
            st.write(response)
            if st.button(f"Delete {i}", key= f"delete_{i}"):
                data.pop(i)
                with open('responses.json', 'w') as file:
                    json.dump(data, file, indent=4)
                st.success("Response deleted successfully!")
                st.rerun()

    except FileNotFoundError:
        st.write("No saved responses yet.")