# data_handling.py
# 데이터프레임 및 파일 업로드 실습
import pandas as pd
import streamlit as st


def show():
    st.header("데이터 처리 및 파일 업로드")
    uploaded_file = st.file_uploader("CSV 파일을 업로드하세요.", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write(df)
    
    st.subheader("샘플 데이터 출력")
    df_sample = pd.DataFrame({"이름": ["홍길동", "김철수", "이영희"], "나이": [25, 30, 22]})
    st.table(df_sample)

if __name__ == "__main__":
    show()
