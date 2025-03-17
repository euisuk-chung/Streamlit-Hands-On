import streamlit as st
import re

def show():
    st.title('🖼️ YouTube 썸네일 추출기')
    st.header('YouTube 영상의 썸네일을 다운로드하세요.')

    with st.expander('이 앱에 대하여'):
        st.write('이 앱은 YouTube 동영상의 썸네일 이미지를 추출하여 표시합니다.')

    # 🎨 이미지 품질 선택
    st.sidebar.header('설정')
    img_dict = {
        'Max (최대 해상도)': 'maxresdefault',
        'High (고화질)': 'hqdefault',
        'Medium (중간 화질)': 'mqdefault',
        'Standard (표준 화질)': 'sddefault'
    }

    selected_img_quality = st.sidebar.selectbox(
        '이미지 품질 선택', 
        list(img_dict.keys()),
        format_func=lambda x: x.split(' ')[0]  # UI에서는 'Max', 'High' 등만 보이게 설정
    )
    img_quality = img_dict[selected_img_quality]

    # 🔗 YouTube URL 입력
    yt_url = st.text_input('YouTube URL 붙여넣기', '')

    # 🎯 YouTube ID 추출 함수
    def get_ytid(input_url):
        """YouTube URL에서 동영상 ID를 추출하는 함수"""
        regex = r"(?:youtu\.be/|youtube\.com/(?:.*v=|.*\/|embed\/|v/|shorts/))([^#&?]+)"
        match = re.search(regex, input_url)
        return match.group(1) if match else None

    # 🎬 썸네일 추출 및 표시
    if yt_url:
        ytid = get_ytid(yt_url)
        
        if ytid:
            yt_img = f'http://img.youtube.com/vi/{ytid}/{img_quality}.jpg'
            st.image(yt_img, caption="썸네일 이미지", use_container_width=True)  # ✅ Updated
            st.write('YouTube 동영상 썸네일 이미지 URL: ', yt_img)
        else:
            st.error('⚠️ 유효한 YouTube URL을 입력하세요.')
    else:
        st.info('🔗 YouTube 동영상의 URL을 입력하세요.')



if __name__ == "__main__":
    show()
