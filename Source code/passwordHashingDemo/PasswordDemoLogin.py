from supabase import Client, create_client
import streamlit as st
import hashlib

# """ 
# TODO: pip install streamlit supabase
# TODO: Run the program: streamlit run your_script.py
# TODO: Change the values of the environment variables to your own Supabase URL and Key.
# TODO: choose your proper hash function
# """



# Function to hash the password with the salt
def hash_password(password, salt=None):

    salt = bytes.fromhex(salt)  # Convert the stored salt from hex to bytes

    # Combine the password and salt and then hash
    password_salt = salt + password.encode()
    hashed_password = hashlib.sha256(password_salt).hexdigest()

    return hashed_password



supabase: Client = create_client("https://ofmwqlmgvqmboaydgvdg.supabase.co",

"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9mbXdxbG1ndnFtYm9heWRndmRnIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTg4MjgxMTcsImV4cCI6MjAxNDQwNDExN30.a5nNJDcU5HmwRRFW3mX9fmEEesIQ7yWiNZX_aReNSTE")
st.set_page_config(page_title="Login", page_icon="🔒", layout="centered")
st.title("Login")

email = st.text_input("Email")
password = st.text_input("Password", type="password")


if st.button("Login"):
    
    result = supabase.table("users").select("*").eq("email", email).execute().data

    if result:
        hashed_pass = result[0]['password']
        hashed_salt = result[0]['salting']
        if hashed_pass == hash_password(password, hashed_salt):
            st.success("Logged in as {}".format(email))
            st.balloons()
        else:
            st.error("Incorrect email or password")
    else:
        st.error("User with email {} not found".format(email))
