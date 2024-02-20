# -*- coding: utf-8 -*-
"""Data Cleaning_Books.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EYHeoQr-3P_T4iCB7aVp0hHQq2vN3DjJ
"""

import pandas as pd
import numpy as np
from functools import reduce

books=pd.read_csv("/content/drive/MyDrive/DataSet/BL-Flickr-Images-Book.csv")
print(books.head())

books.shape

for col in books:
  print(col)

to_drop=['Edition Statement',
         'Corporate Author',
         'Corporate Contributors',
         'Former owner',
         'Engraver',
         'Contributors',
         'Issuance type',
         'Shelfmarks']

books.drop(to_drop, inplace=True, axis=1)
books.head()

for col in books.columns:
  print(col)

books.set_index('Identifier', inplace=True)
books.head()

books['Date of Publication'].head(25)

unwanted_characters=['[',',','-']

def clean_dates(item):
  dop=str(item.loc['Date of Publication'])

  if dop=='nan' or dop[0]=='[':
    return np.NaN

  for character in unwanted_characters:
    if character in dop:
      character_index=dop.find(character)
      dop=dop[:character_index]
      return dop

books['Date of Publication']=books.apply(clean_dates,axis=1)

books['Date of Publication'].head(25)

def clean_Title(Title):

  if Title=='nan':
    return 'NaN'

  if Title[0]=='[':
    Title=Title[1:Title.find(']')]

  if 'by' in Title:
    Title=Title[:Title.find('by')]
  elif 'By' in Title:
    Title=Title[:Title.find('By')]

  if '[' in Title:
    Title=Title[:Title.find('[')]

  Title=Title[:-2]

  Title=list(map(str.capitalize,Title.split()))
  return ''.join(Title)

books['clean_Title']=books['Title'].apply(clean_Title)
books.head()

