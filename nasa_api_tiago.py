# -*- coding: utf-8 -*-
"""NASA_API_Tiago.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lwh04hHsAwZmuxkzm3YhrIx1oQaqfm_j
"""





"""Nome: Tiago Castro Orbite
RA: 23011105
MAHLI
"""

import requests



r = requests.get('https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=2000&camera=MAHLI&api_key=n7eHVk1JAmkVdbJxgA8py91hFxNWCA6vstKSFE9B')



lst = []
for i in range(len(dict(r.json())['photos'])):
  lst.append(dict(r.json())['photos'][i]['img_src'])
print(f'Os links são: {lst}')
print(f'Link da primeira imagem: {dict(r.json())["photos"][0]["img_src"]}')
