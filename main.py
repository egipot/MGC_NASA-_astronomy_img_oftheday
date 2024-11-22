import requests
import streamlit as st 

# Define API key and URL
# 
api_key = 'DEMO_KEY'
url = 'https://api.nasa.gov/planetary/apod?api_key=' + f'{api_key}'
print(f'{url}')

#get the data
response1 = requests.get(url)
data = response1.json()

#extract image, title, url, explanation
title1 = data['title']
image_url = data['url']
explanation = data['explanation']

#downlaod the image
image_filepath = 'img.png'
response2 = requests.get(image_url)

with open(image_filepath, 'wb') as file:
    file.write(response2.content)

st.title(title1)
st.image(image_filepath)
st.write(explanation)