import pandas as pd
import streamlit as st
import streamlit_shadcn_ui as ui

df1 = pd.read('1_MilkTeaTransactions.csv')
df2 = pd.read('2_MilkTeaOperations.csv')
df3 = pd.read('3_MilkTeaCustomers.csv')

st.title('奶茶店交易记录')
ui.table(df1.head(10))
st.markdown('---')

st.title('奶茶店运营状况')
ui.table(df2.head(10))
st.markdown('---')

st.title('奶茶店客户信息')
ui.table(df3.head(10))
st.markdown('---')
