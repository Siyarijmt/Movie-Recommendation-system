import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommend_movies =[]

    for i in movies_list:
        movie_id=i[0]
        #fetch poster from API
        recommend_movies.append(movies.iloc[i[0]].title)
    return recommend_movies

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)


similarity = pickle.load(open('similarity.pkl','rb'))

movies_list = pickle.load(open('movies.pkl','rb'))
movies_list = movies_list['title'].values
st.title('Movie Recommender System')

option = st.selectbox(
'How would you like to be contacted?',
('Email','Phone number','Mobile phone'))

movie_name=st.selectbox(
'Select your Favourite movie',
movies['title'].values)


if st.button('Recommend'):
    recommendation = recommend(movie_name)
    for i in recommendation:
        st.write(i)