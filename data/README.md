# Data Directory

This directory contains the pre-trained models and data files for the Movie Recommendation System.

## Files

### 1. `movie_list.pkl`
- **Description:** Pickled pandas DataFrame containing movie information
- **Contents:** Movie titles, IDs, genres, keywords, cast, crew, etc.
- **Size:** ~5-10 MB
- **Used by:** `src/recommender.py`

### 2. `similarity.pkl`
- **Description:** Pre-computed cosine similarity matrix
- **Dimensions:** (num_movies, num_movies)
- **Computation:** Based on TF-IDF vectorization of movie features
- **Used by:** Recommendation algorithm

### 3. `movie_vote.pkl`
- **Description:** Vote counts for each movie from TMDB
- **Contents:** Vote count for display purposes
- **Used by:** Display recommendations with popularity metrics

## 📊 Data Source

- **Source:** TMDB (The Movie Database)
- **API:** https://www.themoviedb.org/settings/api
- **Total Movies:** 1,000+

## 🔄 How to Regenerate Models

To rebuild these pickle files:

1. Open `notebooks/movie.ipynb`
2. Run all cells
3. Models will be saved to this directory

```python
# Example from notebook
pickle.dump(movies, open('data/movie_list.pkl', 'wb'))
pickle.dump(similarity, open('data/similarity.pkl', 'wb'))
pickle.dump(votes, open('data/movie_vote.pkl', 'wb'))
```

## ⚠️ Important Notes

- **DO NOT commit these files to Git** (too large)
- They are listed in `.gitignore`
- Download or generate them locally
- Use Git LFS (Large File Storage) if you need version control

## 📥 Getting the Data

1. **Option 1:** Run the notebook
   ```bash
   jupyter notebook notebooks/movie.ipynb
   ```

2. **Option 2:** Download from releases
   - Check GitHub Releases for pre-generated pickle files

3. **Option 3:** Use your own TMDB data
   - Modify the notebook with your TMDB API key
   - Generate fresh models
