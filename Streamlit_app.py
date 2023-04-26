
import streamlit
import pandas
streamlit.title('My parents new healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🍞 Orange Juice')
streamlit.text('🐔 Boiled Eggs')
streamlit.text('🥣 Oat Cereal')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index("Fruit")
streamlit.dataframe(my_fruit_list)

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits :",list(my_fruit_list.index),['Avocado','Apple'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

#new section to display API fruityvice response
streamlit.header('Fruityvice Fruit Advice!')

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)

# take the json version and normalize it
fruityvice_normalize = pandas.json_normalize(fruityvice_response.json())

# output it on screen as a table
streamlit.dataframe(fruityvice_normalize)

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)

add_my_fruit = streamlit.text_input('What fruit would you like to add?','Kiwi')
streamlit.write('The user entered ', add_my_fruit)
