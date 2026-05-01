"""TMDB API integration for fetching movie details and posters."""

import requests
from typing import Optional, Dict, Any
import config


def fetch_poster(movie_id: int) -> Optional[str]:
    """
    Fetch movie poster URL from TMDB API.
    
    Args:
        movie_id (int): TMDB movie ID
    
    Returns:
        Optional[str]: Full poster URL or None if failed
    
    Raises:
        requests.exceptions.RequestException: If API request fails
    """
    try:
        if not config.TMDB_API_KEY or config.TMDB_API_KEY == 'your_api_key_here':
            raise ValueError("TMDB API key not configured. Set TMDB_API_KEY in .env")
        
        url = f"{config.TMDB_API_URL}/{movie_id}?api_key={config.TMDB_API_KEY}"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        
        data = response.json()
        poster_path = data.get('poster_path')
        
        if poster_path:
            return f"{config.POSTER_BASE_URL}{poster_path}"
        return None
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching poster for movie {movie_id}: {e}")
        return None
    except (KeyError, ValueError) as e:
        print(f"Error parsing TMDB response: {e}")
        return None


def fetch_movie_details(movie_id: int) -> Optional[Dict[str, Any]]:
    """
    Fetch comprehensive movie details from TMDB API.
    
    Args:
        movie_id (int): TMDB movie ID
    
    Returns:
        Optional[Dict]: Movie details or None if failed
    """
    try:
        if not config.TMDB_API_KEY or config.TMDB_API_KEY == 'your_api_key_here':
            raise ValueError("TMDB API key not configured")
        
        url = f"{config.TMDB_API_URL}/{movie_id}?api_key={config.TMDB_API_KEY}"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        
        return response.json()
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching details for movie {movie_id}: {e}")
        return None


def is_api_key_valid() -> bool:
    """
    Validate if TMDB API key is configured and working.
    
    Returns:
        bool: True if API key is valid, False otherwise
    """
    if not config.TMDB_API_KEY or config.TMDB_API_KEY == 'your_api_key_here':
        return False
    
    try:
        # Try a simple API call
        url = f"{config.TMDB_API_URL}/1?api_key={config.TMDB_API_KEY}"
        response = requests.get(url, timeout=5)
        return response.status_code == 200
    except:
        return False
