# Movie Recommendation System using Streamlit
# Import necessary libraries
import streamlit as st
import pickle
import pandas as pd
import requests

st.markdown("""
    <style>
    .stForm {
        background-color: #5ab413;
    }
    </style>
""", unsafe_allow_html=True)


# Load movie data , similarity matrix and votes
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
vote = pickle.load(open('movie_vote.pkl', 'rb'))

# Function to fetch movie poster from TMDB
def fetch_poster(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=67f55045faf26a3520b80700703afe44'
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = f'https://image.tmdb.org/t/p/w500{poster_path}'
    return full_path

# Movie recommendation function
def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]  # Get index of selected movie
    distance = similarity[movie_index]  # Get similarity scores for the selected movie
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]  # Get top 5 recommendations
    
    recommended_movies = []  # List to store movie titles
    recommended_movies_poster = []  # List to store movie posters
    recommended_votes = []  # List to store movie votes

    # Loop through recommended movies and fetch their details
    for idx, _ in movies_list:
        idx = int(idx)  # Ensure idx is an integer
        if idx < len(movies):  # Ensure the index is within valid bounds
            movie_id = movies.iloc[idx]["id"]
            recommended_movies.append(movies.iloc[idx]["title"])
            recommended_movies_poster.append(fetch_poster(movie_id))
            recommended_votes.append(vote.iloc[idx]["vote_count"])
        else:
            print(f"Invalid index: {idx}")
    
    return recommended_movies, recommended_movies_poster,recommended_votes


# Streamlit UI setup
st.title("Movie Recommendation System")
st.header("Machine Learning Based Recommendations")

# Movie selection dropdown
selected_movie = st.selectbox("Select a Movie", movies['title'].values)

# Button to trigger movie recommendations
if st.button("Recommend"):
    # Get recommendations and posters
    recommend_movie, recommend_poster ,recommended_votes= recommend(selected_movie)

    # Display the recommendations in a grid layout
    col1, col2, col3, col4, col5= st.columns(5)
    
    with col1:
        st.text(recommend_movie[0])
        st.markdown(f"<p style='color:yellow;'>Votes: {recommended_votes[0]}</p>", unsafe_allow_html=True)
        st.image(recommend_poster[0])
        
    with col2:
        st.text(recommend_movie[1])
        # st.text(f"Votes: {recommended_votes[1]}")
        st.markdown(f"<p style='color:yellow;'>Votes: {recommended_votes[1]}</p>", unsafe_allow_html=True)
        st.image(recommend_poster[1])
        
    with col3:
        st.text(recommend_movie[2])
        # st.text(f"Votes: {recommended_votes[2]}")
        st.markdown(f"<p style='color:yellow;'>Votes: {recommended_votes[2]}</p>", unsafe_allow_html=True)

        st.image(recommend_poster[2])
        
    with col4:
        st.text(recommend_movie[3])
        # st.text(f"Votes: {recommended_votes[3]}")
        st.markdown(f"<p style='color:yellow;'>Votes: {recommended_votes[3]}</p>", unsafe_allow_html=True)
        st.image(recommend_poster[3])
        
    with col5:
        st.text(recommend_movie[4])
        st.markdown(f"<p style='color:Yellow;'>Votes: {recommended_votes[4]}</p>", unsafe_allow_html=True)
        st.image(recommend_poster[4])
        