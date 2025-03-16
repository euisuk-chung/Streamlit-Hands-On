# ui_elements.py
# 다양한 UI 요소 실습
import streamlit as st


def show():
    st.header("텍스트 및 UI 요소 실습")
    st.subheader("기본 텍스트 출력")
    st.text("이것은 일반 텍스트입니다.")
    st.markdown("**이것은 마크다운 형식입니다.**")
    st.caption("이것은 캡션입니다.")
    
    st.subheader("코드 블록")
    st.code("""
def hello():
    print("Hello, Streamlit!")
""", language="python")
    
    st.subheader("경고 및 상태 메시지")
    st.success("성공 메시지")
    st.warning("경고 메시지")
    st.error("오류 메시지")

if __name__ == "__main__":
    show()
