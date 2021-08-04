# from PIL import Image
# import streamlit as st

# st.image('https://images.unsplash.com/photo-1494548162494-384bba4ab999?ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8c3VucmlzZXxlbnwwfHwwfHw%3D&ixlib=rb-1.2.1&w=1000&q=80')
# # st.image(image='https://upload.wikimedia.org/wikipedia/en/thumb/b/b4/Tottenham_Hotspur.svg/1200px-Tottenham_Hotspur.svg.png')
# # st.image(image='test.svg')
# # st.image(image='https://i.pinimg.com/originals/79/bd/00/79bd00c9e1ab7e30242bc47c25689e91.jpg')
# @vdonato Okay, so I ran some few tests with `st.image()` with an image URL, and I think this issue might have more to do with the backend of `PIL` than streamlit itself. I would've troubleshooted it, but unfortunately I'm not too familiar with the more subtle workings of image processing. 

# Here's what I tried:
# ```python
from PIL import Image
import streamlit as st

# image = Image.open('https://images.unsplash.com/photo-1494548162494-384bba4ab999?ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8c3VucmlzZXxlbnwwfHwwfHw%3D&ixlib=rb-1.2.1&w=1000&q=80')

# st.image('test.svg')
st.image('test.svg', width=20)


