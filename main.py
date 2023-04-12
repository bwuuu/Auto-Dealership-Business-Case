import streamlit as st
import numpy as np
import pandas as pd

st.title("Sales Volume Assumption")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    nc_sales_y1 = st.number_input("1st Year NC Sales Volume", format=("%i"))
    uc_sales_y1 = st.number_input("1st Year UC Sales Volume", format=("%i"))
with col2:
    nc_sales_y2 = st.number_input("2nd Year NC Sales Volume", format=("%i"))
    uc_sales_y2 = st.number_input("2nd Year UC Sales Volume", format=("%i"))
with col3:
    nc_sales_y3 = st.number_input("3rd Year NC Sales Volume", format=("%i"))
    uc_sales_y3 = st.number_input("3rd Year UC Sales Volume", format=("%i"))
with col4:
    nc_sales_y4 = st.number_input("4th Year NC Sales Volume", format=("%i"))
    uc_sales_y4 = st.number_input("4th Year UC Sales Volume", format=("%i"))
with col5:
    nc_sales_y5 = st.number_input("5th Year NC Sales Volume", format=("%i"))
    uc_sales_y5 = st.number_input("5th Year UC Sales Volume", format=("%i"))



