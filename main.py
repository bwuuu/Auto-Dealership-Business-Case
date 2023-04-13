import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title=("Business Case"), layout="wide")

with st.container():
    st.title("Information")
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text_input("Investor")
        st.text_input("Dealership")
    with col5:
        st.date_input("Date of input")
with st.container():
    st.title("Sales Volume Assumption")
    col1, col2, col3, col4, col5 = st.columns(5)    
    with col1:
        nc_sales_y1 = st.number_input("1st Year NC Sales Volume", step = 1)
        uc_sales_y1 = st.number_input("1st Year UC Sales Volume", step = 1)
    with col2:
        nc_sales_y2 = st.number_input("2nd Year NC Sales Volume", step = 1)
        uc_sales_y2 = st.number_input("2nd Year UC Sales Volume", step = 1)
    with col3:
        nc_sales_y3 = st.number_input("3rd Year NC Sales Volume", step = 1)
        uc_sales_y3 = st.number_input("3rd Year UC Sales Volume", step = 1)
    with col4:
        nc_sales_y4 = st.number_input("4th Year NC Sales Volume", step = 1)
        uc_sales_y4 = st.number_input("4th Year UC Sales Volume", step = 1)
    with col5:
        nc_sales_y5 = st.number_input("5th Year NC Sales Volume", step = 1)
        uc_sales_y5 = st.number_input("5th Year UC Sales Volume", step = 1)

col6, col7 = st.columns(2)

with st.container():
    with col6:
        nc_sales_y6 = st.number_input("6st Year NC Sales Volume", step = 1)
        uc_sales_y6 = st.number_input("6st Year UC Sales Volume", step = 1)
    with col7:
        nc_sales_y7 = st.number_input("6nd Year NC Sales Volume", step = 1)
        uc_sales_y7 = st.number_input("6nd Year UC Sales Volume", step = 1)


st.write("Hello!")


