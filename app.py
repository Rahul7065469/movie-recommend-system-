"""Movie Recommendation System - Streamlit Web Application."""

import streamlit as st
import pandas as pd
from typing import Tuple, List
import config
from src.recommender import load_models, recommend
from src.utils import get_movie_list, validate_movie_input, format_vote_count

# Configure Streamlit
st.set_page_config(
    page_title=config.PAGE_TITLE,
    page_icon=config.PAGE_ICON,
    layout=config.LAYOUT,
    initial_sidebar_state=config.INITIAL_SIDEBAR_STATE
)

# Custom CSS
st.markdown("""
    <style>
    .recommendation-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .vote-count {
        color: #ffd700;
        font-weight: bold;
        font-size: 14px;
    }
    .movie-title {
        font-weight: bold;
        font-size: 16px;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Load models
@st.cache_resource
def load_data():
    """Load and cache models."""
    try:
        movies, similarity, votes = load_models()
        return movies, similarity, votes
    except Exception as e:
        st.error(f"Error loading models: {e}")
        st.stop()

# Main app
def main():
    """Main application function."""
    
    # Title and description
    st.title(config.PAGE_TITLE)
    st.markdown("""
        ### 🎯 Discover Similar Movies
        Select your favorite movie and get AI-powered recommendations based on genres, cast, and more!
    """)
    
    # Load data
    movies, similarity, votes = load_data()
    movie_list = get_movie_list(movies)
    
    # Sidebar
    with st.sidebar:
        st.header("About")
        st.info("""
            This app uses **Content-Based Filtering** with:
            - **Algorithm:** Cosine Similarity
            - **Features:** Genres, Cast, Crew, Keywords
            - **Database:** 1,000+ Movies
        """)
        
        st.header("How It Works")
        st.markdown("""
            1. Select a movie from the dropdown
            2. Click the "Recommend" button
            3. View 5 similar movies with posters
        """)
        
        st.header("Info")
        st.text(f"Version: {config.VERSION}")
        st.text(f"Total Movies: {len(movies)}")
    
    # Movie selection
    col1, col2 = st.columns([3, 1])
    
    with col1:
        selected_movie = st.selectbox(
            "Select a Movie",
            movie_list,
            help="Choose from 1,000+ movies"
        )
    
    with col2:
        recommend_button = st.button(
            "🎬 Recommend",
            use_container_width=True,
            type="primary"
        )
    
    # Get recommendations
    if recommend_button:
        # Validate input
        if not validate_movie_input(selected_movie, movies):
            st.error("⚠️ Invalid movie selection. Please try another movie.")
            return
        
        try:
            # Get recommendations
            with st.spinner("Finding similar movies..."):
                recommended_movies, recommended_posters, recommended_votes = recommend(
                    selected_movie, movies, similarity, votes
                )
            
            # Display results
            st.success(f"✅ Found {len(recommended_movies)} similar movies!")
            
            # Display recommendations in columns
            cols = st.columns(config.COLUMN_COUNT)
            
            for idx, col in enumerate(cols):
                if idx >= len(recommended_movies):
                    break
                
                with col:
                    st.markdown(f"<div class='recommendation-card'>", unsafe_allow_html=True)
                    
                    # Movie title
                    st.markdown(
                        f"<div class='movie-title'>{recommended_movies[idx]}</div>",
                        unsafe_allow_html=True
                    )
                    
                    # Vote count
                    vote_formatted = format_vote_count(recommended_votes[idx])
                    st.markdown(
                        f"<div class='vote-count'>⭐ {vote_formatted} votes</div>",
                        unsafe_allow_html=True
                    )
                    
                    # Movie poster
                    if recommended_posters[idx]:
                        st.image(
                            recommended_posters[idx],
                            use_column_width=True,
                            caption=""
                        )
                    else:
                        st.warning("Poster not available")
                    
                    st.markdown("</div>", unsafe_allow_html=True)
        
        except Exception as e:
            st.error(f"❌ Error getting recommendations: {e}")
    
    # Footer
    st.markdown("---")
    st.markdown("""
        <center>
        <p>Built with ❤️ using Streamlit | Powered by TMDB API</p>
        <p><a href="https://github.com/Rahul7065469/movie-recommend-system-">GitHub Repository</a></p>
        </center>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
