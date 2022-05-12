import pandas
import streamlit

from urllib.error import URLError
import requests

from snowflake import connector
connector.paramstyle='qmark'


# New section
streamlit.header('Fruityvice Fruit Advice!')

def get_fruityvice(this_fruit_choice):
    fruityvice_responce = requests.get("https://www.fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_responce.json())
    return fruityvice_normalized
  
try:
  fruit_choice = streamlit.text_input('What fruit would you like informatin about?','Kiwi')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    back_from_function = get_fruityvice(fruit_choice)
    streamlit.dataframe(back_from_function)
except URLError as e:
    streamlit.error()
streamlit.text("Hello from Snowflake:")
streamlit.header('The fruit load list contains:..')
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("select * from fruit_load_list")
        return my_cur.fetchall()
if streamlit.button('Get Fruit Load List'):        
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    streamlit.dataframe(my_data_rows)

def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
        query = 'insert into fruit_load_list FRUIT_NAME values (?)'
        my_cur.execute(query,new_fruit)
        return "Thanks for adding " + new_fruit
add_my_fruit = streamlit.text_input('What fruit would you like to add?','Kiwi')

if streamlit.button('Add a Fruit to the List: '):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_function = insert_row_snowflake(add_my_fruit)
    streamlit.text(back_from_function)
    
