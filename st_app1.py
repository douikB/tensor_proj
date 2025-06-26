import streamlit as st

st.set_page_config(
    page_title='hello',
    page_icon='🤗'
)

st.write("# Welcome to Streaemlit!")

st.sidebar.success('데모 선택')

st.markdown(
    """
    Streamlit은 머신 러닝 및 데이터 과학 프로젝트를 위해 특별히 제작된 오픈 소스 앱 프레임워크입니다..
    ### 자세히 알아보고 싶으신가요?
    - [streamlit.io](https://streamlit.io) 
    - [설명서](https://docs.streamlit.io)
    - [커뮤니티 포럼](https://discuss.streamlit.io)에서 질문하기
    """
)

st.code("1234")

name = st.text_input("이름")

print(name)

st.write(name)
