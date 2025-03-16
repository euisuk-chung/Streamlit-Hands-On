# app.py
# 기본 Streamlit 애플리케이션
import streamlit as st


def main():
    st.title("Streamlit 연습용 앱")
    st.write("이 앱은 Streamlit을 활용한 예제 모음입니다.")
    
    st.sidebar.header("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "UI Elements", "Charts", "Data Handling", "Widgets", "Map"])
    
    if page == "Home":
        st.write("Streamlit을 활용한 다양한 기능을 배울 수 있습니다.")
    elif page == "UI Elements":
        import ui_elements
        ui_elements.show()
    elif page == "Charts":
        import charts
        charts.show()
    elif page == "Data Handling":
        import data_handling
        data_handling.show()
    elif page == "Widgets":
        import interactive_widgets
        interactive_widgets.show()
    elif page == "Map":
        import map_visualization
        map_visualization.show()

if __name__ == "__main__":
    main()
