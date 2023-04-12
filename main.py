import streamlit as st
import numpy as np
import pandas as pd

st.title("Sales Volume Assumption")
nc_sales_y1 = st.number_input("1st Year NC Sales Volume")
nc_sales_y2 = st.number_input("2nd Year NC Sales Volume")
nc_sales_y3 = st.number_input("3rd Year NC Sales Volume")
nc_sales_y4 = st.number_input("4th Year NC Sales Volume")
nc_sales_y5 = st.number_input("5th Year NC Sales Volume")

uc_sales_y1 = st.number_input("1st Year UC Sales Volume")
uc_sales_y2 = st.number_input("2nd Year UC Sales Volume")
uc_sales_y3 = st.number_input("3rd Year UC Sales Volume")
uc_sales_y4 = st.number_input("4th Year UC Sales Volume")
uc_sales_y5 = st.number_input("5th Year UC Sales Volume")
