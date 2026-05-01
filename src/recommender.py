"""Core recommendation logic for movie suggestions."""

import pickle
import pandas as pd
import numpy as np
from typing import Tuple, List, Optional
import config
from src.api import fetch_poster


def load_models() -> Tuple[pd.DataFrame, np.ndarray, pd.DataFrame]:
    """
    Load pre-trained models and data from pickle files.
    
    Returns:
        Tuple[pd.DataFrame, np.ndarray, pd.DataFrame]:
            - movies: DataFrame with movie information
            - similarity: Similarity matrix (cosine similarity)
            - votes: DataFrame with vote counts
    
    Raises:
        FileNotFoundError: If pickle files are not found
        pickle.UnpicklingError: If pickle files are corrupted
    """
    try:
        movies = pickle.load(open(config.MOVIE_LIST_PATH, 'rb'))
        similarity = pickle.load(open(config.SIMILARITY_PATH, 'rb'))
        votes = pickle.load(open(config.VOTE_COUNT_PATH, 'rb'))
        return movies, similarity, votes
    
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Model file not found: {e}") from e
    except pickle.UnpicklingError as e:
        raise pickle.UnpicklingError(f"Error loading pickle file: {e}") from e


def recommend(movie_title: str, 
              movies: pd.DataFrame, 
              similarity: np.ndarray, 
              votes: pd.DataFrame,
              num_recommendations: int = config.NUM_RECOMMENDATIONS) -> Tuple[List[str], List[str], List[int]]:
    """
    Get movie recommendations based on cosine similarity.
    
    Args:
        movie_title (str): Title of the selected movie
        movies (pd.DataFrame): DataFrame with movie data
        similarity (np.ndarray): Similarity matrix
        votes (pd.DataFrame): DataFrame with vote counts
        num_recommendations (int): Number of recommendations to return
    
    Returns:
        Tuple[List[str], List[str], List[int]]:
            - recommended_movies: List of movie titles
            - recommended_posters: List of poster URLs
            - recommended_votes: List of vote counts
    
    Raises:
        ValueError: If movie not found in database
    """
    try:
        # Find movie index
        movie_index = movies[movies["title"] == movie_title].index
        
        if len(movie_index) == 0:
            raise ValueError(f"Movie '{movie_title}' not found in database")
        
        movie_index = movie_index[0]
        
        # Get similarity scores
        distance = similarity[movie_index]
        
        # Sort and get top N similar movies (excluding the selected movie)
        similar_movies_indices = sorted(
            list(enumerate(distance)), 
            reverse=True, 
            key=lambda x: x[1]
        )[1:num_recommendations + 1]
        
        recommended_movies = []
        recommended_posters = []
        recommended_votes = []
        
        # Fetch details for each recommended movie
        for idx, similarity_score in similar_movies_indices:
            idx = int(idx)
            
            if idx >= len(movies):
                continue
            
            try:
                movie_id = movies.iloc[idx]["id"]
                title = movies.iloc[idx]["title"]
                
                # Fetch poster
                poster = fetch_poster(movie_id)
                if poster is None:
                    poster = "https://via.placeholder.com/500x750?text=No+Poster"
                
                vote_count = int(votes.iloc[idx]["vote_count"]) if not votes.empty else 0
                
                recommended_movies.append(title)
                recommended_posters.append(poster)
                recommended_votes.append(vote_count)
            
            except (IndexError, KeyError) as e:
                print(f"Error processing movie at index {idx}: {e}")
                continue
        
        return recommended_movies, recommended_posters, recommended_votes
    
    except ValueError as e:
        raise ValueError(f"Recommendation error: {e}") from e
