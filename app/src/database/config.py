import streamlit as st
import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment variables from .env file
load_dotenv()

def get_secret(key):
    # Try streamlit secrets first
    try:
        return st.secrets[key]
    except (KeyError, FileNotFoundError):
        # Fallback to environment variables
        return os.getenv(key)

supabase: Client = create_client(
    get_secret("SUPABASE_URL"),
    get_secret("SUPABASE_KEY")
)