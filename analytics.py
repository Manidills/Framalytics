import streamlit as st
import plotly.express as px
import pandas as pd
import datetime
import altair as alt
import math



def trans_date():
    trans = pd.read_csv("data/farcaster_trans.csv")
    return trans


def trans_chain():
    chain = pd.read_csv("data/farcaster_chain.csv")
    return chain


def trans_vol():
    vol = pd.read_csv("data/farcaster_volume.csv")
    return vol


def base_user_date():
    base_users = pd.read_csv('data/top_base_users.csv')
    return base_users


def framers_data():
    framers = pd.read_csv('data/top_frames-by_interval.csv')
    return framers


def top_base_mints():
    base_mints = pd.read_csv('data/top_mints.csv')
    return base_mints


def growth():
    reactions = pd.read_csv('data/reactions_per_day.csv')
    followers = pd.read_csv("data/folloers_count.csv")
    frames_count = pd.read_csv("data/frames_count_growth.csv")
    return reactions, followers, frames_count


def analytics_chart():
    trans = trans_date()
    base_users = base_user_date()
    reactions, followers, frames_count = growth()
    chain = trans_chain()
    st.markdown("##")

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Farcaster Frames Transactions", 45069)
    col2.metric("Total Frames Transaction Volume", "$372,594")
    col3.metric("Total Farcastrer Frames Contracts", 331)

    st.markdown("##")
    st.write("""
        ### Total Frames Transaction ###
        """)
    st.markdown("##")
    st.altair_chart(
        alt.Chart(trans).mark_bar().encode(
            y='total_txs:N',
            x="date_time:T",    
            color='total_txs:N',
        ).properties(
        width=800,
        height=300
    ),  use_container_width=True
    )
    a,b = st.columns([2,2])
    with a:
        
        st.markdown("##")
        st.write("""
            ### Active Addresses Interactions ###
            """)
        st.markdown("##")
        st.altair_chart(
            alt.Chart(trans).mark_line(color='red').encode(
                y='total_active_users:N',
                x="date_time:T",    
            ).properties(
            width=800,
            height=300
        ),  use_container_width=True
        )
    
    with b:
        st.markdown("##")
        st.write("""
            ### Total Frames Contracts ###
            """)
        st.markdown("##")
        st.altair_chart(
            alt.Chart(trans).mark_line(color='green').encode(
                y='total_contracts:N',
                x="date_time:T",    
            ).properties(
            width=800,
            height=300
        ),  use_container_width=True
       
        )

    st.markdown("##")
    st.write("""
        ### Top Frames by Interval ###
        """)
    t_framers = framers_data()
    base_mints = top_base_mints()
    edited = st.data_editor(t_framers,  num_rows="dynamic",use_container_width=True)

    st.markdown("##")
    a,b = st.columns([2,2])
    with a:
        
        st.markdown("##")
        st.write("""
            ### Followers Count ###
            """)
        st.markdown("##")
        st.altair_chart(
            alt.Chart(followers).mark_line(color='blue').encode(
                y='followers_count:N',
                x="day:T",    
            ).properties(
            width=800,
            height=300
        ),  use_container_width=True
        )
    
    with b:
        st.markdown("##")
        st.write("""
            ### Reactions per day ###
            """)
        st.markdown("##")
        st.altair_chart(
            alt.Chart(reactions).mark_line(color='yellow').encode(
                y='total_reactions:N',
                x="day:T",    
            ).properties(
            width=800,
            height=300
        ),  use_container_width=True
       
        )


    st.markdown("##")
    st.write("""
        ### Frames Counts ###
        """)
    st.markdown("##")
    st.altair_chart(
        alt.Chart(frames_count).mark_area(color='white', 
opacity=0.7).encode(
            y='frames_count',
            x="day:T",    
        ).properties(
        width=800,
        height=300
    ),  use_container_width=True
    )

    a,b = st.columns([2,2])
    with a:
        
        st.markdown("##")
        st.write("""
            ### Active Addresses Blockchain ###
            """)
        st.markdown("##")
        st.altair_chart(
            alt.Chart(chain).mark_line(color='red').encode(
                y='total_active_users:N',
                x="date_time:T", 
                color='blockchain:N', 
            ).properties(
            width=800,
            height=300
        ),  use_container_width=True
        )
    
    with b:
        st.markdown("##")
        st.write("""
            ### Frames Contracts Blockchain ###
            """)
        st.markdown("##")
        st.altair_chart(
            alt.Chart(chain).mark_line(color='green').encode(
                y='total_contracts:N',
                x="date_time:T",    
                color='blockchain:N', 
            ).properties(
            width=800,
            height=300
        ),  use_container_width=True
       
        )


   
    st.markdown("##")
    st.write("""
            ### Cumulative value transferred ###
            """)
    vol = trans_vol()
    st.altair_chart(
        alt.Chart(vol).mark_line(color='pink', 
opacity=0.7).encode(
            y='total_value_transferred:N',
            x="date_time:T",    
        ).properties(
        width=800,
        height=300
    ),  use_container_width=True
    )

    st.markdown("##")
    a, b = st.columns([2,2])
    with a:
        st.markdown("##")
        st.write("""
            ### Top base users by Interval ###
            """)
        st.altair_chart(
        alt.Chart(base_users).mark_bar(color='red').encode(
        x='fname',
        y="total_transactions",
        color='fname',
        ).properties(
            width=800,
            height=500
        ), use_container_width=True
        )
    with b:
        st.markdown("##")
        st.write("""
            ### Top base mints ###
            """)
        st.data_editor(base_mints,  num_rows="dynamic",use_container_width=True)

    st.markdown("##")


        
        