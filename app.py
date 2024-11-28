import pandas as pd
import streamlit as st
import streamlit_shadcn_ui as ui

df1 = pd.read_csv('1_MilkTeaTransactions.csv')
df2 = pd.read_csv('2_MilkTeaOperations.csv')
df3 = pd.read_csv('3_MilkTeaCustomers.csv')

analysis_type = ui.tabs(
    options = ['奶茶店交易记录', '奶茶店运营状况', '奶茶店客户信息'],
    default_value = '奶茶店交易记录'
)

if analysis_type == '奶茶店交易记录':  
    st.title('奶茶店交易记录')
    st.dataframe(df1.head(10))
    st.markdown('---')
elif analysis_type == '奶茶店运营状况': 
    st.title('奶茶店运营状况')
    st.dataframe(df2.head(10))
    st.markdown('---')
elif analysis_type == '奶茶店客户信息':  
    st.title('奶茶店客户信息')
    ui.table(df3.head(10))
    st.markdown('---')
