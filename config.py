"""Configuration settings for Movie Recommendation System."""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# TMDB API Configuration
TMDB_API_KEY = os.getenv('TMDB_API_KEY', 'your_api_key_here')
TMDB_API_URL = 'https://api.themoviedb.org/3/movie'
POSTER_BASE_URL = 'https://image.tmdb.org/t/p/w500'

# Recommendation Settings
NUM_RECOMMENDATIONS = 5          # Number of movies to recommend
SIMILARITY_METRIC = 'cosine'    # Similarity calculation method

# UI Settings
PAGE_TITLE = "🎬 Movie Recommendation System"
PAGE_ICON = "🎬"
LAYOUT = "wide"                 # Streamlit layout mode
INITIAL_SIDEBAR_STATE = "expanded"

# File Paths
DATA_DIR = 'data'
MODELS_DIR = 'models'
NOTEBOOKS_DIR = 'notebooks'

MOVIE_LIST_PATH = os.path.join(DATA_DIR, 'movie_list.pkl')
SIMILARITY_PATH = os.path.join(DATA_DIR, 'similarity.pkl')
VOTE_COUNT_PATH = os.path.join(DATA_DIR, 'movie_vote.pkl')

# Features for recommendations
FEATURES = ['genres', 'keywords', 'cast', 'crew', 'overview']

# Display settings
COLUMN_COUNT = 5  # Number of recommendation columns
POSTER_SIZE = 'w500'  # TMDB poster resolution

# Validation
MIN_MOVIE_TITLE_LENGTH = 1
MAX_MOVIE_TITLE_LENGTH = 200

# App version
VERSION = "1.0.0"
AUTHOR = "Rahul7065469"
