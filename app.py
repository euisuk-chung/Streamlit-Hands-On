# app.py
# 기본 Streamlit 애플리케이션
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

import streamlit as st

def main():
    st.title("Streamlit 연습용 앱")
    st.write("이 앱은 Streamlit을 활용한 예제 모음입니다.")
    
    st.sidebar.header("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "UI Elements", "Charts", "Data Handling", "Widgets", "Map", "YouTube", "Record"])
    
    if page == "Home":
        st.write("Streamlit을 활용한 다양한 기능을 배울 수 있습니다.")
    elif page == "UI Elements":
        import src.ui_elements as ui_elements
        ui_elements.show()
    elif page == "Charts":
        import src.charts as charts
        charts.show()
    elif page == "Data Handling":
        import src.data_handling as data_handling
        data_handling.show()
    elif page == "Widgets":
        import src.interactive_widgets as interactive_widgets
        interactive_widgets.show()
    elif page == "Map":
        import src.map_visualization as map_visualization
        map_visualization.show()
    elif page == "YouTube":
        import src.yt_img_app as yt_img_app
        yt_img_app.show()
    elif page == "Record":
        import src.record_save as record_save
        record_save.show()

if __name__ == "__main__":
    main()
