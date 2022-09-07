import streamlit
streamlit.title   ('Мое первое приложение на Phyton :)')
streamlit.header  ('Достался адский сценарий про здоровую еду...')

streamlit.header  ('🥑    Меню на завтрак')
streamlit.text    ('🥣    Omega 3 & Скучная жратва')
streamlit.text    ('🥗    Шпинат & прочий ацтой')
streamlit.text    ('🍞  Яйца - единственное, что можно есть')

streamlit.header('🍌🥭 Собери рецепт своего Смусси... 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Выбери фрукты для Смусси:", list(my_fruit_list.index),['Avocado','Cantaloupe'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
##streamlit.dataframe(my_fruit_list)
# dsplay the table on the page
streamlit.dataframe(fruits_to_show)

#New section to display fruityvice api response
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
