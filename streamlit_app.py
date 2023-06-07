import streamlit as st
import pandas as pd
import numpy as np
import time
import xgboost as xgb

xgb_model = xgb.XGBRegressor()
xgb_model.load_model('xgb_load_final2.model')

st.title('Seoul House Price')
st.header('Seoul House Price Prediction Project')

# Add a placeholder 진행 상황 바
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    # Update the progress bar with each iteration.
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.01)
    
# 변수는 총 4개
# 순서대로 전용면적, 계약년월, 거래금액, 층, 건축년도
st.write("""
## 사용 변수들
1. 전용면적
2. 계약년월
3. 층
4. 건축년도
""")

width = st.slider("면적을 선택하세요 단위(m^2)", 11, 291)
# 6. 날짜 입력
contractdate = st.date_input('계약년월')  # 디폴트로 오늘 날짜가 찍혀 있다.
contractString = contractdate.strftime("%Y%m")
contract = float(contractString)
st.write(contractdate.strftime("%Y%m"))

floor = st.slider("층을 선택하세요", 1, 60)
builtYear = st.slider("건축년도를 선택하세요(년도)", 1971, 2022)

# scaling되기 전의 데이터
realData = [[width, contract, floor, builtYear]]
mins = [12.0156, 202305.0, 1.0, 1968.0]
maxs = [244.84, 202305.0, 39.0, 2023.0]
# minMaxScaler를 통해 scaling해줬었으므로 여기서도 해줘야함 scaling 된 데이터를 저장할 곳
scaleData = []

# scaling
for i in range(0, len(realData)):
    scaleData.append((realData[0][i] - mins[i]) / (maxs[i] - mins[i]))
scaleData = [scaleData]
res1 = xgb_model.predict(scaleData)
