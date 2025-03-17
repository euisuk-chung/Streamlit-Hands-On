import streamlit as st
import os
import datetime

# 📂 저장 디렉토리 설정
BASE_DIR = "recordings"
os.makedirs(BASE_DIR, exist_ok=True)  # recordings 폴더 생성

def show():

    # 🎯 오늘 날짜 폴더 생성
    today_str = datetime.datetime.now().strftime("%Y-%m-%d")
    SAVE_DIR = os.path.join(BASE_DIR, today_str)
    os.makedirs(SAVE_DIR, exist_ok=True)  # 날짜 폴더 없으면 생성

    st.title("🎙️ 오디오 녹음 및 저장 앱")
    st.write(f"📅 녹음 파일은 `{SAVE_DIR}` 폴더에 저장됩니다.")

    # 🎤 오디오 녹음 위젯
    audio_file = st.audio_input("음성을 녹음하세요:")

    # ✍ 파일 이름 입력
    file_name = st.text_input("저장할 파일 이름을 입력하세요 (확장자 제외):")

    # ✅ 파일 저장 기능
    if audio_file and file_name:
        file_path = os.path.join(SAVE_DIR, f"{file_name}.wav")

        # 동일한 파일명이 있을 경우 경고
        if os.path.exists(file_path):
            st.error("⚠️ 이미 존재하는 파일명입니다. 다른 이름을 입력하세요.")
        else:
            if st.button("📥 녹음 파일 저장"):
                with open(file_path, "wb") as f:
                    f.write(audio_file.read())
                st.success(f"✅ 파일이 저장되었습니다: `{file_path}`")

    # 📂 저장된 파일 리스트
    st.subheader("📁 저장된 오디오 파일 목록")

    # 날짜별 저장된 파일들 가져오기
    audio_files = [f for f in os.listdir(SAVE_DIR) if f.endswith(".wav")]

    if audio_files:
        selected_file = st.selectbox("재생할 파일을 선택하세요:", audio_files)

        if selected_file:
            file_path = os.path.join(SAVE_DIR, selected_file)
            st.audio(file_path, format="audio/wav")
    else:
        st.write("❌ 저장된 오디오 파일이 없습니다.")


if __name__ == "__main__":
    show()
