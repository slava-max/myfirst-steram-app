import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title   ('Мое первое приложение на Phyton :)')
streamlit.header  ('Достался адский сценарий про здоровую еду...')

streamlit.header  ('Меню на завтрак')
streamlit.text    ('🥣    Omega 3 & Скучная жратва')
streamlit.text    ('🥗    Шпинат & прочий ацтой')
streamlit.text    ('🍞    Яйца - можно есть')

streamlit.header('🥭 Собери рецепт своего Смусси... 🥝')

# import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Выбери фрукты для Смусси:", list(my_fruit_list.index),['Avocado','Cantaloupe'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
##streamlit.dataframe(my_fruit_list)
# dsplay the table on the page
streamlit.dataframe(fruits_to_show)

# New section to display fruityvice api response
streamlit.header  ('Типа совет дня...')
try:
fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choise:
    streamlit.error("Выбери фрукт! Че не понятно то?")
  else
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    streamlit.dataframe(fruityvice_normalized)
except URLError as e:
  streamlit.error()
    
# do not run anything after that = troubleshooting
streamlit.stop()

# import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)

add_my_fruit = streamlit.text_input('What fruit would you like to add?','Jackfruit')
streamlit.write('Thanks for adding ', add_my_fruit)
