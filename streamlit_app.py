import streamlit as st
import pandas as pd
import numpy as np

st.title('Seoul House Price')
st.header('Seoul House Price Prediction Project')


# 지역 변수를 제외한 나머지 변수 설정하는 sidebar
width = st.slider("면적을 선택하세요 단위(m^2)", 11, 291)
# 6. 날짜 입력
contractdate = st.date_input('계약년월')  # 디폴트로 오늘 날짜가 찍혀 있다.
contractString = contractdate.strftime("%Y%m")
contract = float(contractString)
st.write(contractdate.strftime("%Y%m"))

floor = st.slider("층을 선택하세요", 1, 60)
builtYear = st.slider("건축년도를 선택하세요(년도)", 1971, 2022)
