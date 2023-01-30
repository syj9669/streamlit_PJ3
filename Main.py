import streamlit as st

st.set_page_config(
	page_title='Streamlit 프로토타입 만들기',
	page_icon='🎈',
	layout='wide'
)

st.text('🎈서영준 : Streamlit 프로토타입 만들기')

st.title('📌Title을 입력하세요.')

st.header('Header(머리글)을 입력하세요.')
st.subheader('Subheader(세부 머리글)을 입력하세요.')

st.markdown('# H1 #')
st.markdown('## H2 ##')
st.markdown('### H3 ###')
st.markdown('#### H4 ####')
st.markdown('##### H5 #####')
st.markdown('###### H6 ######')

# 순서가 있는 목록(숫자+점'.' 사용)
st.markdown('1. 하나')
st.markdown('2. 둘')
st.markdown('3. 셋')
# 순서가 없는 목록(글 머리 기호 '*, +, -' 사용
st.markdown('* 하나')
st.markdown('* 둘')
st.markdown('* 셋')

st.caption('이것은 Caption 입니다.')

st.text('기본 텍스트를 입력합니다.')
st.code('코드 블록 표시가 가능합니다.')

import pandas as pd

stocks_file = 'https://raw.githubusercontent.com/seokjam/stremlitProject/master/data/sp500_stocks_2022.csv'
index_file = 'https://raw.githubusercontent.com/seokjam/stremlitProject/master/data/sp500_index_2022.csv'
df_stocks = pd.read_csv(stocks_file)
df_index = pd.read_csv(index_file)

st.dataframe(df_stocks)

st.dataframe(df_index.style.highlight_max(axis=0))

symbol = st.selectbox('검색하고자 하는 기업을 선택하세요.', (df_stocks['Symbol'].unique()))
st.dataframe(df_stocks[df_stocks['Symbol'] == symbol])

import pandas as pd

stocks_file = 'https://raw.githubusercontent.com/seokjam/stremlitProject/master/data/sp500_stocks_2022.csv'
index_file = 'https://raw.githubusercontent.com/seokjam/stremlitProject/master/data/sp500_index_2022.csv'
df_stocks = pd.read_csv(stocks_file)
df_index = pd.read_csv(index_file)

df_chart = pd.DataFrame(columns=['Date'])
df_chart['Date'] = df_stocks['Date'].unique()

for symbol in df_stocks['Symbol'].unique():
	df_chart[symbol] = df_stocks[df_stocks['Symbol'] == symbol]['Close'].reset_index(drop=True)

st.line_chart(df_chart, x='Date')

