import pandas as pd
import streamlit as st
import streamlit_shadcn_ui as ui

df1 = pd.read_csv('1_MilkTeaTransactions.csv')
df2 = pd.read_csv('2_MilkTeaOperations.csv')
df3 = pd.read_csv('3_MilkTeaCustomers.csv')

st.title('奶茶店交易记录')
ui.table(df1.head(10))
st.markdown('---')

st.title('奶茶店运营状况')
ui.table(df2.head(10))
st.markdown('---')

st.title('奶茶店客户信息')
ui.table(df3.head(10))
st.markdown('---')
