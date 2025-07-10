import streamlit as st
import random
import requests

st.set_page_config(
    page_title='finanzas',
    page_icon='🏆',
    layout='wide'
)

# funcion para obtener los datos
def get_data(name):
    try:
        response = requests.get(f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=N5S662LNIFVDSBZ4/{name.lower()}')
        if response.status_code==200:
            return response.json()
        else:
            return None
    except:
        return None
    
print(get_data('2025-07-09'))

