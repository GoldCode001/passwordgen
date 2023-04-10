import random
import string
import streamlit as st

# Set the page title and layout
st.set_page_config(page_title='Password Generator API')

def generate_password(length):
    """Generate a random password."""
    # Define the character sets to use for the password
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    #symbols = string.punctuation

    # Combine the character sets
    all_chars = lowercase + uppercase + digits #+ symbols

    # Generate a password using random.choice()
    password = ''.join(random.choice(all_chars) for i in range(length))

    return password

def main():
    """Main function of the Streamlit app."""
    

    # Add a header and description
    st.header('Password Generator API')
    st.write('Enter the desired length of the password to generate below:')

    # Add a slider to select the length of the password
    length = st.slider('Length', min_value=8, max_value=32, value=12, step=1)

    # Add a button to generate the password
    if st.button('Generate Password'):
        # Generate the password
        password = generate_password(length)

        # Display the password to the user
        st.write('Generated password:', password)

def local_css(file_name):
    with open(file_name)as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")
st.write('Gold Code')
if __name__ == '__main__':
    main()
