import streamlit as st
import pickle

movies_list = pickle.load(open('movies.pkl','rb'))
movies_list = movies_list['title'].values
st.title('Movie Recommender System')

option=st.selectbox(
'How would you like to be contacted?',
('Email','Phone number','Mobile phone'))

option=st.selectbox(
'Select your Favourite movie',
movies_list)