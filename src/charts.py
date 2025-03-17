# charts.py
# 차트 및 데이터 시각화 실습
import numpy as np
import pandas as pd
import streamlit as st


def show():
    st.header("차트 및 데이터 시각화 실습")
    
    df = pd.DataFrame(
        np.random.randn(20, 3),
        columns=["A", "B", "C"]
    )
    
    st.subheader("라인 차트")
    st.line_chart(df)
    
    st.subheader("바 차트")
    st.bar_chart(df)
    
    st.subheader("영역 차트")
    st.area_chart(df)

if __name__ == "__main__":
    show()
