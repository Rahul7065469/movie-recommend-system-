"""Movie Recommendation System - Core modules."""

__version__ = "1.0.0"
__author__ = "Rahul7065469"

from src.recommender import load_models, recommend
from src.api import fetch_poster, fetch_movie_details
from src.utils import get_movie_list, validate_movie_input

__all__ = [
    'load_models',
    'recommend',
    'fetch_poster',
    'fetch_movie_details',
    'get_movie_list',
    'validate_movie_input',
]
