# map_visualization.py
# 지도 및 위치 데이터 시각화
import numpy as np
import pandas as pd
import streamlit as st


def show():
    st.header("지도 시각화 실습")
    df = pd.DataFrame(
        np.random.randn(100, 2) / [50, 50] + [37.76, -122.4],
        columns=["lat", "lon"]
    )
    st.map(df)

if __name__ == "__main__":
    show()
