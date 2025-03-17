# map_visualization.py
# 지도 및 위치 데이터 시각화
import numpy as np
import pandas as pd
import streamlit as st

def show():
    st.header("예시. 서울 강남구 지도 시각화")
    
    # 서울 강남구 중심 좌표 (https://blog.naver.com/kiakass/222449339999)
    center_lat = 37.514575
    center_lon = 127.0495556

    # 무작위 데이터 생성 (±0.01 정도의 범위)
    df = pd.DataFrame(
        np.random.randn(100, 2) / [100, 100] + [center_lat, center_lon], 
        columns=["lat", "lon"]
    )

    # 지도 출력
    st.map(df)

if __name__ == "__main__":
    show()

