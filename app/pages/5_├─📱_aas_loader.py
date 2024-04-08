import os
from pathlib import Path
import streamlit as st
import pandas as pd
from utils.resource_loader import DocLoader
from utils.app_config import AppConfig

config = AppConfig()
doc = DocLoader('enne')

st.title('Acting All Scared')
st.write(doc.get_doc('hello.md'))
st.write(config.open_ai_key)