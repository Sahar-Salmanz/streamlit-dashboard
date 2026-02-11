import streamlit as st
from io import StringIO
import json

login_option = st.sidebar.radio('Login/SignUp', ('Login', 'SignUp'))
if login_option == 'Login':
    with st.sidebar.form("Login"):
        st.write("Login Here.")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        
        # every form must have a submit button
        submitted = st.form_submit_button("Login")
        if submitted:
            pass

else:
    with st.sidebar.form("SignUp"):
        st.write("Sign Up Here.")
        email = st.text_input("Email")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        
        # every form must have a submit button
        submitted = st.form_submit_button("SignUp")
        if submitted:
            pass

#st.logo('./streamlit_banner.webp', size='large')
st.image('./streamlit_logo.png')
st.title(':chart_with_upwards_trend: Streamlit Dashboard Project')

# with st.expander('Statistics'):
#     uploaded_file = st.file_uploader("Choose a file")
#     if uploaded_file is not None:

#         # To convert to a string based IO:
#         stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
#         #st.write(stringio)

#         # To read file as string:
#         string_data = stringio.read()
#         st.write(string_data)

#         data = json.loads(string_data)
#         st.json(data)

with st.expander('User Info.'):
    col1, col2 = st.columns(2)
    col1.text_input('Name:')
    col2.text_input('Location:')
    st.camera_input('Camera Input', key='camera_input')