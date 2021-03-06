"""The :mod:`streamlit_app` serves as a demo application to show the scoring API system at work.
This runs on sreamlit
"""
# Author: Christopher Dare
import json

import pandas as pd
import requests
import streamlit as st

base_url = "http://127.0.0.1:8080"

st.title("Welcome to burn area predictor (Codename: Ozai)")
st.write(
    """Predict how much land area will be burned based on land profile"""
)  # description

burn_area = ""
st.title(burn_area)

climate_vs = st.text_input("Climate VS", 0)
climate_def = st.text_input("Climate DEF", 0)
climate_vap = st.text_input("Climate VAP", 0)
climate_aet = st.text_input("Climate AET", 0)
precipation = st.text_input("Precipation", 0)
land_cover = st.text_input("Land Cover", 0)

if st.button("Predict burn area"):
    profile = dict()
    profile["climate_vs"] = float(climate_vs)
    profile["climate_def"] = float(climate_def)
    profile["climate_vap"] = float(climate_vap)
    profile["climate_aet"] = float(climate_aet)
    profile["precipitation"] = float(land_cover)
    profile["landcover_5"] = float(land_cover)

    payload = json.dumps(profile)
    st.write("Posting")
    st.write(payload)
    response = requests.post(f"{base_url}/score", data=payload)
    data = response.json()
    output = "An error occured"
    if data["success"]:
        burn_area = data["payload"]
        burn_area = round(burn_area, 2)
        if burn_area > 0:
            output = f"Burn area is {burn_area}"
        else:
            output = f"No fire, congratulations"

    st.title(output)
