from supabase import Client, create_client
import streamlit as st
import hashlib
import os

# """ 
# TODO: pip install streamlit supabase
# TODO: Run the program: streamlit run your_script.py
# TODO: Change the values of the environment variables to your own Supabase URL and Key.
# """

supabase: Client = create_client("https://ofmwqlmgvqmboaydgvdg.supabase.co", 
"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9mbXdxbG1ndnFtYm9heWRndmRnIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTg4MjgxMTcsImV4cCI6MjAxNDQwNDExN30.a5nNJDcU5HmwRRFW3mX9fmEEesIQ7yWiNZX_aReNSTE")
st.set_page_config(page_title="SignUp", page_icon="🔒", layout="centered")
st.title("SignUp")

name = st.text_input("Name")
userName = st.text_input("Username")
email = st.text_input("Email")
password = st.text_input("Password", type="password")


# Function to generate a random salt
def generate_salt():
    return os.urandom(16)  # 16 bytes (128 bits) of random data

# Function to hash the password with the salt
def hash_password(password):
    
    salt = generate_salt()
    password_salt = salt + password.encode()
    hashed_password = hashlib.sha256(password_salt).hexdigest()

    return salt.hex(), hashed_password



response = None  

if st.button("Signup"):
    salt, hashed_password = hash_password(password)

    # Define the user data as a dictionary
    user_data = {
        "name": name,
        "username": userName,
        "email": email,
        "password": hashed_password,
        "salting": salt
    }

    # Insert the user data into the "users" table
    response = supabase.table("users").upsert([user_data]).execute()

    st.success("Signed up as {}".format(email))
    st.balloons()


    st.markdown("Login http://192.168.10.9:8501")

    


    

    

    





