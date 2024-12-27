import streamlit as st

st.title("Streamlit Form Example")

# Create a form
with st.form("my_form"):
    st.header("Form Input Section")

    # Add input widgets to the form
    name = st.text_input("Enter your name")
    age = st.number_input("Enter your age", min_value=0, max_value=120, step=1)
    accept = st.checkbox("I accept the terms and conditions")

    # Add a submit button
    submitted = st.form_submit_button("Submit")

# Process the form submission
if submitted:
    if accept:
        st.success(f"Hello {name}, age {age}. Your form has been submitted successfully!")
    else:
        st.error("Please accept the terms and conditions to submit the form.")
