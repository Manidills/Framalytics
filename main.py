from os import pread
from analytics import analytics_chart
from feeds import feeds
from recommend import ranking
import streamlit as st
import plotly.express as px
import pandas as pd
import datetime
import altair as alt
from streamlit_option_menu import option_menu


# Layout
st.set_page_config(page_title="DUBAI",
    page_icon="chart_with_upwards_trend",layout="wide")

padding_top = 0

st.markdown(f"""
    <style>
        .reportview-container .main .block-container{{
            padding-top: {padding_top}rem;
        }}
    </style>""",
    unsafe_allow_html=True,
)

IMAGE = "https://assets-global.website-files.com/6364e65656ab107e465325d2/637aede94d31498505bc9412_DpYIEpePqjDcHIbux04cOKhrRwBhi7F0-dBF_JCdCYY.png"

a, b= st.columns([1,2])
a.image(IMAGE, width=200)
with b:
    title = "Framalytics"
    t =  f"<p style='font-size:90px;'>{title}</p>"
    st.markdown(t,unsafe_allow_html=True)
st.markdown("##")
st.markdown("##")




option =  option_menu("Home", ["About", "Analytics", "Feeds", "Scoring"],
                         icons=['house', 'camera fill', 'kanban', 'book'],
                         menu_icon="app-indicator", default_index=0,orientation="horizontal",
                         styles={
        "container": {"padding": "5!important", "background-color": "black"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "black"},
    }
    )

if option == 'About':
    st.markdown("##")
    st.write("Framalytics is a versatile platform that offers in-depth analytics, interactive data tools thats regards Frames.")
    st.markdown("##")
    st.write("""   
    #### :red[Analytics] : The analytics section provides profound insights into  frames analytics and growth patterns.  ####  """)
    st.markdown("##")
    st.write("""   
    #### :red[Feeds] : This section facilitates the filtering and interaction with data related to casts, channels, and users. It also periodically retrieves the top data from each section, enabling users to engage with and manage relevant information efficiently. ####  """)
    st.markdown("##")
    st.write("""   
    #### :red[Scoring] : This section is designed to combat spam effectively while also enhancing the user experience through personalized ranking and recommendations. By utilizing the EigenTrust (Pagerank) algorithm, users can create a powerful ranking and recommendation engine tailored specifically for profiles, frames, and casts, allowing for greater customization and optimization of content delivery. ####  """)
    st.markdown("##")
  
    st.success(f"Source data from {'https://docs.pinata.cloud/farcaster/farcaster-api/getting-started'}")
    st.success(f"Source data from {'https://docs.karma3labs.com/farcaster'}")
    st.success(f"Source data from {'https://docs.base.org/tools/data-indexers'}")
elif option == 'Analytics':
    analytics_chart()
elif option == 'Feeds':
    feeds()
elif option == 'Scoring':
    ranking()
