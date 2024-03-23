import re
import streamlit as st
import plotly.express as px
import pandas as pd
import datetime
import altair as alt
import math
import requests
from PIL import Image
from io import BytesIO
import urllib.request

def api_hit_get(url):

    url = url

    response = requests.request("GET", url)

    return(response.json())

def api_hit_post(url, values):

    headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
    }

    json_data = values

    response = requests.post(url, headers=headers, json=json_data)
    return(response.json())



def ranking():
    st.markdown("##")
    genre = st.radio(
    "select the category",
    ["Scorings", "***Frames***"],
    index=0, horizontal=True
)
    if genre == 'Scorings':
        st.markdown("##")
        st.markdown("##")
        with st.form("form1", clear_on_submit=False): 
            f_1 = st.radio(
            "select",
            ["Global", "***personalized***"],
            index=0, horizontal=True
        )
            f_2 = st.radio(
                "select",
            ["following", "***engagement***"],
            index=0, horizontal=True
        )
            f_3 = st.radio(
                "select",
            ["fid", "***handle***"],
            index=0, horizontal=True
        )
            values = st.text_input('values')
            submit = st.form_submit_button("Submit")

        if submit:
            st.markdown("##")
            st.markdown("##")
            if f_1 == 'Global' and f_2 == 'following' and f_3 == 'fid':
                collect_numbers = lambda x : [int(i) for i in re.split("[^0-9]", x) if i != ""]
                values = collect_numbers(values)
                data = api_hit_post('https://graph.cast.k3l.io/scores/global/following/fids',values)
                df = pd.DataFrame(data['result'])
                st.data_editor(df,  num_rows="dynamic",use_container_width=True)
                st.markdown("##")
                st.write(data)
            elif f_1 == 'Global' and f_2 == 'following' and f_3 == '***handle***':
                # collect_numbers = lambda x : [int(i) for i in re.split("[^0-9]", x) if i != ""]
                val = [values]
                data = api_hit_post('https://graph.cast.k3l.io/scores/global/following/handles',val)
                df = pd.DataFrame(data['result'])
                st.data_editor(df,  num_rows="dynamic",use_container_width=True)
                st.markdown("##")
                st.write(data)
            elif f_1 == 'Global' and f_2 == '***engagement***' and f_3 == 'fid':
                collect_numbers = lambda x : [int(i) for i in re.split("[^0-9]", x) if i != ""]
                values = collect_numbers(values)
                data = api_hit_post('https://graph.cast.k3l.io/scores/global/engagement/fids',values)
                df = pd.DataFrame(data['result'])
                st.data_editor(df,  num_rows="dynamic",use_container_width=True)
                st.markdown("##")
                st.write(data)
            elif f_1 == 'Global' and f_2 == '***engagement***' and f_3 == '***handle***':
                # collect_numbers = lambda x : [int(i) for i in re.split("[^0-9]", x) if i != ""]
                val = [values]
                data = api_hit_post('https://graph.cast.k3l.io/scores/global/engagement/handles',val)
                df = pd.DataFrame(data['result'])
                st.data_editor(df,  num_rows="dynamic",use_container_width=True)
                st.markdown("##")
                st.write(data)
            elif f_1 == '***personalized***' and f_2 == 'following' and f_3 == 'fid':
                collect_numbers = lambda x : [int(i) for i in re.split("[^0-9]", x) if i != ""]
                values = collect_numbers(values)
                data = api_hit_post('https://graph.cast.k3l.io/scores/personalized/following/fids',values)
                df = pd.DataFrame(data['result'])
                st.data_editor(df,  num_rows="dynamic",use_container_width=True)
                st.markdown("##")
                st.write(data)
            elif f_1 == '***personalized***' and f_2 == 'following' and f_3 == '***handle***':
                # collect_numbers = lambda x : [int(i) for i in re.split("[^0-9]", x) if i != ""]
                val = [values]
                data = api_hit_post('https://graph.cast.k3l.io/scores/personalized/following/handles',val)
                df = pd.DataFrame(data['result'])
                st.data_editor(df,  num_rows="dynamic",use_container_width=True)
                st.markdown("##")
                st.write(data)
            elif f_1 == '***personalized***' and f_2 == '***engagement***' and f_3 == 'fid':
                collect_numbers = lambda x : [int(i) for i in re.split("[^0-9]", x) if i != ""]
                values = collect_numbers(values)
                data = api_hit_post('https://graph.cast.k3l.io/scores/personalized/engagement/fids',values)
                df = pd.DataFrame(data['result'])
                st.data_editor(df,  num_rows="dynamic",use_container_width=True)
                st.markdown("##")
                st.write(data)
            elif f_1 == '***personalized***' and f_2 == '***engagement***' and f_3 == '***handle***':
                # collect_numbers = lambda x : [int(i) for i in re.split("[^0-9]", x) if i != ""]
                val = [values]
                data = api_hit_post('https://graph.cast.k3l.io/scores/personalized/engagement/handles',val)
                df = pd.DataFrame(data['result'])
                st.data_editor(df,  num_rows="dynamic",use_container_width=True)
                st.markdown("##")
                st.write(data)
        else:
            st.markdown("##")
            st.markdown("##")
            st.title(" Get Top Following Profiles")
            url = 'https://graph.cast.k3l.io/scores/global/following/rankings?offset=0&limit=100'
            data = api_hit_get(url)
            df = pd.DataFrame(data['result'])
            st.data_editor(df,  num_rows="dynamic",use_container_width=True)
            st.markdown("##")

              
            st.markdown("##")
            st.title(" Get Top Engagement Profiles")
            url = 'https://graph.cast.k3l.io/scores/global/engagement/rankings?offset=0&limit=100'
            data = api_hit_get(url)
            df = pd.DataFrame(data['result'])
            st.data_editor(df,  num_rows="dynamic",use_container_width=True)
            st.markdown("##")

    if genre == '***Frames***':
        st.markdown("##")
        st.markdown("##")
        with st.form("form1", clear_on_submit=False): 
            f_1 = st.radio(
            "select",
            ["Fid", "Handle"],
            index=0, horizontal=True
        )
            values = st.text_input('values')
            submit = st.form_submit_button("Submit")

        if submit:
            st.markdown("##")
            st.markdown("##")
            if f_1 == 'Fid':
                collect_numbers = lambda x : [int(i) for i in re.split("[^0-9]", x) if i != ""]
                values = collect_numbers(values)
                url = 'https://graph.cast.k3l.io/frames/personalized/rankings/fids?agg=sumsquare&weights=L1C10R5&voting=single&k=2&limit=100'
                data = api_hit_post(url, values)
                df = pd.DataFrame(data['result'])
                st.data_editor(df,  num_rows="dynamic",use_container_width=True)
                st.markdown("##")
            if f_1 == 'Handle':
                val = [values]
                url = 'https://graph.cast.k3l.io/frames/personalized/rankings/handles?agg=sumsquare&weights=L1C10R5&voting=single&k=2&limit=100'
                data = api_hit_post(url, val)
                df = pd.DataFrame(data['result'])
                st.data_editor(df,  num_rows="dynamic",use_container_width=True)
                st.markdown("##")
        else:
            st.markdown("##")
            st.title(" Get Top Framess")
            st.markdown("##")
            url = 'https://graph.cast.k3l.io/frames/global/rankings?agg=sumsquare&weights=L1C10R5&details=false&offset=0&limit=100'
            data = api_hit_get(url)
            df = pd.DataFrame(data['result'])
            st.data_editor(df,  num_rows="dynamic",use_container_width=True)
            st.markdown("##")





