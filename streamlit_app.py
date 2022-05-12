import streamlit
import pandas
import requests
import snowflake.connector

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect("Pick some fruits: ", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

streamlit.header('Fruityvice Fruit Advice!')

fruit_choice = streamlit.text_input('What fruit would you like informatin about?','Kiwi')
streamlit.write('The user entered',fruit_choice)

fruityvice_responce = requests.get("https://www.fruityvice.com/api/fruit/" + fruit_choice)
fruityvice_normalized = pandas.json_normalize(fruityvice_responce.json())
streamlit.dataframe(fruityvice_normalized)

streamlit.text("Hello from Snowflake:")
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text(my_data_row)


