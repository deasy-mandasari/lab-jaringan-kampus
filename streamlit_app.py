from pathlib import Path

import streamlit as st


st.set_page_config(page_title="EL523 Jaringan Telekomunikasi", layout="wide")
st.iframe(
    Path(__file__).resolve().with_name("simulator.html"),
    height="content",
    alt="Simulator jaringan kampus dengan topologi dan daftar kejadian paket",
)
