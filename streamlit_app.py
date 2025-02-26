import streamlit as st
import re

if "entries" not in st.session_state:
    st.session_state.entries = []

def validate_name(name):
    return bool(re.match(r"^[A-Za-z\s]+$", name))

def validate_inputs(name, age, gender):
    errors = []
    if not name.strip():
        errors.append("❌ Please enter your name!")
    elif not validate_name(name):
        errors.append("❌ Name should contain only letters!")

    if gender == "Select...":
        errors.append("❌ Please select a valid gender!")

    if not (10 <= age <= 75):
        errors.append("❌ Age must be between 10 and 75!")

    return errors

st.title("Employee & Intern Tracker")
st.write("Track employees and interns based on age and gender.")

name = st.text_input("Enter your name:", placeholder="Enter only alphabets (e.g., John Doe)")
if name:
    st.write("✅ Valid Name" if validate_name(name) else "❌ Invalid Name (Only letters allowed)")

age = st.number_input("Enter your age:", min_value=10, max_value=75, step=1, format="%d")
if age:
    if 10 <= age <= 75:
        st.write("✅ Valid Age")
    else:
        st.write("❌ Invalid Age (Must be between 10 and 75)")

gender = st.selectbox("Select your gender:", [None, "Male", "Female"], format_func=lambda x: x if x else "Select...")
if gender:
    st.write("✅ Gender Selected")
else:
    st.write("❌ Please select a gender")

if st.button("Check Category"):
    errors = validate_inputs(name, age, gender)
    if errors:
        for error in errors:
            st.error(error)
    else:
        category = "Employee" if age > 22 else "Intern"
        if not any(e["Name"] == name and e["Age"] == age and e["Gender"] == gender for e in st.session_state.entries):
            st.session_state.entries.append({"Name": name, "Age": age, "Gender": gender, "Category": category})
            st.success(f"✅ {name} is categorized as a {category}.")
        else:
            st.warning("⚠️ This entry already exists!")

if st.session_state.entries:
    st.subheader("Recorded Data")
    st.table([{"Name": e["Name"], "Age": e["Age"], "Gender": e["Gender"], "Category": e["Category"]} for e in st.session_state.entries])

    total_employees = sum(1 for e in st.session_state.entries if e["Category"] == "Employee")
    total_interns = sum(1 for e in st.session_state.entries if e["Category"] == "Intern")

    st.subheader("Summary")
    st.write(f"Total Employees: {total_employees}")
    st.write(f"Total Interns: {total_interns}")

if st.button("Reset Data"):
    if st.confirm("Are you sure you want to reset all records?"):
        st.session_state.entries = []
        st.success("All records have been cleared!")

st.write("Made By Ashwin B VI-'B'")
