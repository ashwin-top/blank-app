import streamlit as st

if "entries" not in st.session_state:
    st.session_state.entries = []

def validate_inputs(name, age, gender):
    if not name.strip():
        st.error("Please enter your name!")
        return False
    if gender == "Select...":
        st.error("Please select a valid gender!")
        return False
    if not (10 <= age <= 75):
        st.error("Age must be between 10 and 75!")
        return False
    return True


st.title("Employee & Intern Tracker")
st.write("Track employees and interns based on age and gender.")


name = st.text_input("Enter your name:", placeholder="Type your full name...")
age = st.number_input("Enter your age:", min_value=10, max_value=75, step=1)
gender = st.selectbox("Select your gender:", ["Select...", "Male", "Female"])

if st.button("Check Category"):
    if validate_inputs(name, age, gender):
        category = "Employee" if age > 22 else "Intern"

  
        st.session_state.entries.append({"Name": name, "Age": age, "Category": category})

       
        st.success(f"{name} is categorized as a {category}.")

if st.session_state.entries:
    st.subheader("Recorded Data")
    st.table([{"Name": e["Name"], "Age": e["Age"], "Category": e["Category"]} for e in st.session_state.entries])
    
    total_employees = sum(1 for e in st.session_state.entries if e["Category"] == "Employee")
    total_interns = sum(1 for e in st.session_state.entries if e["Category"] == "Intern")
    
    st.subheader("Summary")
    st.write(f"Total Employees: {total_employees}")
    st.write(f"Total Interns: {total_interns}")

if st.button("Reset Data"):
    st.session_state.entries = []
    st.success("All records have been cleared!")
