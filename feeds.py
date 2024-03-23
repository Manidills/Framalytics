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

def api_hit(url):

    url = url

    headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mb3JtYXRpb24iOnsiaWQiOiJiZTJiNjM3ZC04NTRmLTQyYmEtYTFmMC0yNWM5YTAxMWI1ZmQiLCJlbWFpbCI6Im1hbmlkaWxsczQxQGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJwaW5fcG9saWN5Ijp7InJlZ2lvbnMiOlt7ImlkIjoiRlJBMSIsImRlc2lyZWRSZXBsaWNhdGlvbkNvdW50IjoxfSx7ImlkIjoiTllDMSIsImRlc2lyZWRSZXBsaWNhdGlvbkNvdW50IjoxfV0sInZlcnNpb24iOjF9LCJtZmFfZW5hYmxlZCI6ZmFsc2UsInN0YXR1cyI6IkFDVElWRSJ9LCJhdXRoZW50aWNhdGlvblR5cGUiOiJzY29wZWRLZXkiLCJzY29wZWRLZXlLZXkiOiIxYzUzM2U0OTBkMTlmZjVhZmQzYiIsInNjb3BlZEtleVNlY3JldCI6IjA5NjM0YWM0NjkyYTUwYzUzZGM2ZGVkZmU0ZGU0YzBmYzliODcwNzkxNjUxMWZlY2U0NmQxMDg3YmI3NWQyMDEiLCJpYXQiOjE3MTEwNTExODB9.hip0CcmHeyUSkX1hKd8MSaWSyyr3dCIK2vcS5BeRUn0"}

    response = requests.request("GET", url, headers=headers)

    return(response.json())




def feeds():
    st.markdown("##")
    genre = st.radio(
    "select the category",
    [":rainbow[Casts]", "***Channels***", "Users :movie_camera:"],
    index=0, horizontal=True
)
    if genre == ':rainbow[Casts]':
        with st.form("form1", clear_on_submit=False): 
            hash = st.text_input('Hash')
            submit = st.form_submit_button("Submit")
        if submit:
            st.markdown("##")
            st.markdown("##")
            url = f"https://api.pinata.cloud/v3/farcaster/casts/{hash}"
            casts_data = api_hit(url)

            col1, col2 = st.columns(2)

            with col1:
                st.image(casts_data['data']['author']['pfp_url'])
            with col2:
                st.write(casts_data['data'])

        else:
            st.markdown("##")
            st.markdown("##")
            url = "https://api.pinata.cloud/v3/farcaster/casts?pageSize=10"
            casts_data = api_hit(url)
            
            num_images = len(casts_data['data']['casts'])
            images_per_row = 3
            num_rows = (num_images + images_per_row - 1) // images_per_row

            # Display images and metadata in a grid with 4 images per row
            for row in range(num_rows):
                col1, col2, col3 = st.columns(3)
                for col, idx in zip([col1, col2, col3], range(row * images_per_row, min((row + 1) * images_per_row, num_images))):
                    st.markdown("##")
                    image_data = casts_data['data']['casts'][idx]
                    col.image(image_data['author']['pfp_url'], caption=f'Image {idx + 1}')
                    col.write(image_data)
                st.markdown('---')  # Add a horizontal line between each row

    elif genre == '***Channels***':
        with st.form("form1", clear_on_submit=False): 
            name = st.text_input('Name')
            submit = st.form_submit_button("Submit")
        if submit:
            st.markdown("##")
            st.markdown("##")
            url = f"https://api.pinata.cloud/v3/farcaster/channels/{name}"
            casts_data = api_hit(url)
            col1, col2 = st.columns(2)

            with col1:
                st.image(casts_data['data']['image_url'])
            with col2:
                st.write(casts_data['data'])

        else:
            st.markdown("##")
            st.markdown("##")
            url = "https://api.pinata.cloud/v3/farcaster/channels?pageSize=10"
            casts_data = api_hit(url)
            
            num_images = len(casts_data['data']['channels'])
            images_per_row = 3
            num_rows = (num_images + images_per_row - 1) // images_per_row

            # Display images and metadata in a grid with 4 images per row
            for row in range(num_rows):
                col1, col2, col3 = st.columns(3)
                for col, idx in zip([col1, col2, col3], range(row * images_per_row, min((row + 1) * images_per_row, num_images))):
                    st.markdown("##")
                    image_data = casts_data['data']['channels'][idx]
                    col.image(image_data['image_url'], caption=f'Image {idx + 1}')
                    col.write(image_data)
                st.markdown('---')  # Add a horizontal line between each row


    elif genre == 'Users :movie_camera:':
        with st.form("form1", clear_on_submit=False): 
            fid = st.text_input('Fid')
            submit = st.form_submit_button("Submit")
        if submit:
            st.markdown("##")
            st.markdown("##")
            url = f"https://api.pinata.cloud/v3/farcaster/users/{fid}"
            casts_data = api_hit(url)
            col1, col2 = st.columns(2)

            with col1:
                st.image(casts_data['data']['pfp_url'])
            with col2:
                st.write(casts_data['data'])

        else:
            st.markdown("##")
            st.markdown("##")
            url = "https://api.pinata.cloud/v3/farcaster/users?pageSize=10"
            casts_data = api_hit(url)
            
            num_images = len(casts_data['data']['users'])
            images_per_row = 3
            num_rows = (num_images + images_per_row - 1) // images_per_row

            # Display images and metadata in a grid with 4 images per row
            for row in range(num_rows):
                col1, col2, col3 = st.columns(3)
                for col, idx in zip([col1, col2, col3], range(row * images_per_row, min((row + 1) * images_per_row, num_images))):
                    st.markdown("##")
                    image_data = casts_data['data']['users'][idx]
                    col.image(image_data['pfp_url'], caption=f'Image {idx + 1}')
                    col.write(image_data)
                st.markdown('---')  # Add a horizontal line between each row