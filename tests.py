from PIL import Image
import streamlit as st

# st.image('https://images.unsplash.com/photo-1494548162494-384bba4ab999?ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8c3VucmlzZXxlbnwwfHwwfHw%3D&ixlib=rb-1.2.1&w=1000&q=80')

# st.image('''<svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
# 	 width="472px" height="392px" viewBox="0 0 472 392" enable-background="new 0 0 472 392" xml:space="preserve">
# <g id="Layer_3">
# 	<path fill="#FFB564" d="M288.7,187.7c-53.7-32.6-119.8,1-119.8,1s11.6,92.6,11.4,121.4c-0.8,2-1,4.1-0.4,6.3
# 		c-0.2,1.2-0.6,1.7-1,1.7h1.7c1.1,3,2.9,4.3,5.8,5.3c10.9,4,21.5,6.8,33.1,7.7c3.6,0.3,7.1,0.2,10.5-0.2c1.6,1.5,4,2.4,7.1,2.1
# 		c13.2-1.2,28-1.9,38.6-10.3c1.7-1.4,2.7-2.7,3.1-4.7h0.8L288.7,187.7z"/>
# 	<polygon fill="#52E2D7" points="173.2,146.4 180.5,184 206.6,177.2 200.1,144 	"/>
# 	<path fill="#FFFBE8" d="M222.6,133.8c0,0-17.9-15.6-5.3,39.9c0.6,2.5,19.4,3.4,19.4,3.4L222.6,133.8z"/>
# 	<path fill="#F9A035" d="M188.6,181.4c0,0-20.6,0-20.6,12.4c0.1,17.2,13.4,105.6,13.1,119.9c-0.2,9.3,19.1,13.6,19.1,13.6"/>
# 	<path fill="#FFB564" d="M200.2,93.3c0,0,9.7,50.2,11.6,48.4c2-1.8,10.8-7.9,10.8-7.9l-13.5-40.5H200.2z"/>
# 	<path fill="#FFFBE8" d="M184.1,123.6c0,0-12.9,24.6-10.9,22.8c2-1.8,27-2.4,27-2.4L184.1,123.6z"/>
# 	<path fill="#F25F68" d="M257.9,92.8c-1.5,2-3,4.1-4.4,6.3c-1.2,1.9-2.9,2.3-4.6,1.9c-1.7,3.4-3.5,6.7-5.7,9.8
# 		c-6.2,22.4-0.7,41.7-8.7,63.8c-1.3,3.5,0.3,0.3,2.2,2.5c5.6-3,31.1,3.5,38.7,4.2c1.7-2.3-9.1-3.3-10.3-6.6c1.4,3.9,0.2-5.2,0.2-6.1
# 		c0.3-2.6,0-5.5,0.3-8.1c0.7-4.6-1.4-6.4-0.8-11c1.9-14.5,3.4-29.4,3-44.1c-2.2-3.9-4.1-7.9-5.6-12.1
# 		C261,92.9,259.4,92.7,257.9,92.8z"/>
# </g>
# <g id="Layer_2">
	
# 		<polyline fill="none" stroke="#AF3A46" stroke-width="4.9763" stroke-linecap="square" stroke-linejoin="round" stroke-miterlimit="10" points="
# 		238,171.1 245.2,109 260.4,86.9 267.7,110.8 265.1,174.8 	"/>
	
# 		<polyline fill="none" stroke="#AF3A46" stroke-width="4.9763" stroke-linecap="square" stroke-linejoin="round" stroke-miterlimit="10" points="
# 		180.2,182.4 173.8,144 184.1,123.6 200.1,139.2 206.6,176.2 	"/>
	
# 		<path fill="none" stroke="#AF3A46" stroke-width="4.9763" stroke-linecap="square" stroke-linejoin="round" stroke-miterlimit="10" d="
# 		M218.2,174.8c0,0-4.5-16.5-9-36.4c-4.8-21.3-9.7-43.8-9-45.1c1.3-2.6,5.4-4.8,8.9,0c2,2.7,7.9,21.6,13.5,40.5
# 		c6.3,21.1,12.2,42.3,11.9,40.8"/>
# 	<path fill="#AF3A46" stroke="#AF3A46" stroke-width="2.4882" stroke-miterlimit="10" d="M200.2,93.3c-11.6-12.2-10.4-19.2-6.6-23
# 		c6.6-6.6-2.8-16.6-0.9-16.8c6.6-0.6,28.6,9.6,17.3,36.9"/>
	
# 		<path fill="none" stroke="#AF3A46" stroke-width="4.9763" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" d="
# 		M245.2,109c0,0,11.3-4.8,22.5,1.9"/>
	
# 		<path fill="#FFFBE8" stroke="#AF3A46" stroke-width="4.9763" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" d="
# 		M200.1,139.2c0,4.7-12.2,4.7-12.2,4.7c-3.2,5.3-14.1,0-14.1,0"/>
# 	<path fill="#AF3A46" d="M190.9,130.3c3.4,3.3-12,3.5-12,3.5l5.1-10.2L190.9,130.3z"/>
	
# 		<path fill="none" stroke="#AF3A46" stroke-width="4.9763" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" d="
# 		M211.8,141.6c7.7,0,11.4-6,11.4-6"/>
	
# 		<path fill="none" stroke="#AF3A46" stroke-width="4.9763" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" d="
# 		M169,188.8L169,188.8c43.9-21.5,94.3-16.6,119.8-1.1L277,321.9c0,0-39.9,23.2-95.2-1.1L169,188.8z"/>
	
# 		<path fill="none" stroke="#AF3A46" stroke-width="4.8228" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" d="
# 		M255.7,270.4l-2.2-32.6l-24.4-18.9L205,236.6c0.3,11.8,1.4,22.8,1.7,34.6C206.6,271.2,236,275.9,255.7,270.4z"/>
	
# 		<line fill="none" stroke="#AF3A46" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" x1="229.5" y1="219" x2="229.5" y2="246"/>
	
# 		<path fill="none" stroke="#AF3A46" stroke-width="3.8582" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" d="
# 		M233.2,240.8c-1.5,0-2.9,0.3-6.8,0.4c0,0-1-0.9-0.1,5.9c2.9,0.1,4,0.2,6.9,0.2C233.2,247.4,233.2,242.5,233.2,240.8z"/>
# </g>
# </svg>
# ''')

st.image('test.svg')