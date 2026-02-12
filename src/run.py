import os
import sys
import numpy as np
import streamlit as st
import json
import matplotlib.pyplot as plt
import seaborn as sns

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
from db.models import Message

# Login
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

# Banner
st.image('Data/streamlit_logo.png')
st.title(':chart_with_upwards_trend: Streamlit Dashboard Project')

# Questions
with st.expander('Q / A'):
    query = st.text_input('Search:')

    # select top 10 from messages
    for msg in Message.objects.all().order_by('-date'):
        if not msg.text or msg.text[-1] not in '؟?':
            continue

        if query and query not in msg.text:
            continue

        col1, col2 = st.columns([1, 4])
        col1.write(f'**{msg.user.username}**')
        col2.write(msg.text.replace(query, f'**{query}**'))

    col1, col2 = st.columns(2)
    col1.button('< Previous')
    col2.button('Next >')

# with st.expander('User Info.'):
#     col1, col2 = st.columns(2)
#     col1.text_input('Name:')
#     col2.text_input('Location:')
#     st.camera_input('Camera Input', key='camera_input')