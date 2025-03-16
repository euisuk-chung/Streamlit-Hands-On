# interactive_widgets.py
# 인터랙티브 위젯 실습
import streamlit as st


def show():
    st.header("인터랙티브 위젯 실습")
    name = st.text_input("이름을 입력하세요.")
    if st.button("입력 완료"):
        st.write(f"입력한 이름: {name}")
    
    agree = st.checkbox("동의합니다.")
    if agree:
        st.write("동의하셨습니다!")
    
    number = st.slider("숫자를 선택하세요.", 1, 100, 50)
    st.write(f"선택한 숫자: {number}")

if __name__ == "__main__":
    show()
