import streamlit as st
from backend.hub import Hub
from backend.database import Database
from frontend.pages import pages
import atexit


@st.cache_resource
def get_database():
    connection_string = st.secrets["config"]["connection_string"]
    database = Database(connection_string)
    atexit.register(lambda db: db.close_all(), database)
    return database

# @st.cache_resource
# def get_hub():
#     return Hub(get_database())

#st.write(st.session_state)

if "hub" not in st.session_state:
    config = st.secrets["config"]
    st.session_state.hub = Hub(get_database())
    #hub = get_hub()


if "logged_in" in st.session_state and st.session_state.logged_in:
    page = st.navigation([pages["home"], pages["logout"]])
else:
    page = st.navigation([pages["login"], pages["signup"]])
    
page.run()