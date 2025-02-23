import streamlit as st
st.title("Employee and Intern Categorizer")
# Function to categorize employee or intern
def categorize_person(age, gender):
    if age > 22:
        return "Male Employee!" if gender.lower() == "male" else "Female Employee!"
    else:
        return "Male Intern!" if gender.lower() == "male" else "Female Intern!"

# Taking user input
age = st.text_input("Enter age:")

# Validate age input
if age:
    if age.isdigit(): # Check if input is a number
        age = int(age)
        gender = st.selectbox("Select Gender", ["Male", "Female"])
        
        # Display result
        st.success(categorize_person(age, gender))
    else:
        st.error("❌ Invalid input! Please enter a valid number for age.")
