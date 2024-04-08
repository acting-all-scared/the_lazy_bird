import streamlit as st
from utils.resource_loader import DocLoader

docs = DocLoader('enne')

st.title('Acting All Scared😎')
st.write(docs.get_doc('my_first_doc.md'))
st.image('doc/enne/20190610144311678496.png')

option = st.selectbox(
     '지금 보고 있는 사진은 **`누구`** 입니까?',
     ('벌꿀오소리', '크앙무섭지', '오소리벌꿀' , '꿀벌오소리')
     ,index=None)


if option=='벌꿀오소리' and option is not None:
    # st.write('이 사진은', option , '입니다.')
    st.write('정답입니다.')

elif option is not None: 
    # st.write('이 사진은', option , '입니다.')
    st.write('틀렸습니다.')