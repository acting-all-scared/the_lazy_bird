import streamlit as st
from utils.resource_loader import DocLoader

doc = DocLoader('enne')

st.title('Acting All Scared😎')
with st.expander('acting all scared는 누구인가?'):
     st.write('뒤늦게 개발이라는 영역에 발을 들여 놓은 노베이스 늦깎이 비전공자 하고 싶은건 많은데 끈기와 실행능력은 아직 살짝 부족할지도..')
st.write(doc.get_doc('hello.md'))


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



# 다중 옵션
st.header('st.multiselect')

options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])

st.write('You selected:', options)

# 체크박스 만들기
st.header('st.checkbox')

st.write ('What would you like to order?')

icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')

if icecream:
     st.write("Great! Here's some more 🍦")

if coffee: 
     st.write("Okay, here's some coffee ☕")

if cola:
     st.write("Here you go 🥤")


if st.button('발사'):
     st.balloons()
else:
     st.write('Goodbye')

