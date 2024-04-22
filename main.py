import streamlit as st
import time

st.title('Streamlit 超入門')

st.write('Interactive Widgets')


text = st.text_input(
  '貴方の趣味を教えてください')

'貴方の好きな数字は、', text, 'です。'

# if st.checkbox('Show Image'):
#   img = Image.open('short_新潟スノボ.png')
#   st.image(img, caption='Kohei Imanishi', use_column_width=True)
