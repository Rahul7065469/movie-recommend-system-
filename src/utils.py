"""Utility functions for the Movie Recommendation System."""

import pandas as pd
from typing import List, Optional
import config


def get_movie_list(movies: pd.DataFrame) -> List[str]:
    """
    Get sorted list of movie titles.
    
    Args:
        movies (pd.DataFrame): DataFrame with movie data
    
    Returns:
        List[str]: Sorted list of movie titles
    """
    try:
        return sorted(movies['title'].values.tolist())
    except KeyError as e:
        raise KeyError(f"'title' column not found in movies DataFrame: {e}") from e


def validate_movie_input(movie_title: str, movies: pd.DataFrame) -> bool:
    """
    Validate if movie exists in database.
    
    Args:
        movie_title (str): Movie title to validate
        movies (pd.DataFrame): DataFrame with movie data
    
    Returns:
        bool: True if movie exists, False otherwise
    """
    if not isinstance(movie_title, str):
        return False
    
    if len(movie_title) < config.MIN_MOVIE_TITLE_LENGTH:
        return False
    
    if len(movie_title) > config.MAX_MOVIE_TITLE_LENGTH:
        return False
    
    return movie_title in movies['title'].values


def format_vote_count(vote_count: int) -> str:
    """
    Format vote count in human-readable format.
    
    Args:
        vote_count (int): Number of votes
    
    Returns:
        str: Formatted vote count (e.g., "1.2K", "1.5M")
    
    Example:
        >>> format_vote_count(1234)
        '1.2K'
        >>> format_vote_count(1234567)
        '1.2M'
    """
    try:
        vote_count = int(vote_count)
        
        if vote_count >= 1_000_000:
            return f"{vote_count / 1_000_000:.1f}M"
        elif vote_count >= 1_000:
            return f"{vote_count / 1_000:.1f}K"
        else:
            return str(vote_count)
    
    except (ValueError, TypeError):
        return "N/A"


def sanitize_movie_title(title: str) -> str:
    """
    Sanitize movie title by removing extra whitespace.
    
    Args:
        title (str): Movie title to sanitize
    
    Returns:
        str: Sanitized title
    """
    return title.strip() if isinstance(title, str) else ""


def get_similarity_percentage(similarity_score: float) -> float:
    """
    Convert similarity score to percentage.
    
    Args:
        similarity_score (float): Cosine similarity score (0-1)
    
    Returns:
        float: Percentage (0-100)
    """
    try:
        return float(similarity_score) * 100
    except (ValueError, TypeError):
        return 0.0
