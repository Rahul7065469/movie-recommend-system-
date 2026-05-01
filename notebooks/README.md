# Jupyter Notebooks

This directory contains Jupyter notebooks for data exploration, model building, and experimentation.

## Notebooks

### `movie.ipynb`
**Purpose:** Main notebook for building the recommendation system

**Contents:**
1. **Data Loading** - Load movie data from TMDB or CSV
2. **Exploratory Data Analysis (EDA)**
   - Dataset overview
   - Missing values analysis
   - Feature distributions
3. **Feature Engineering**
   - Combine text features (genres, keywords, cast, crew)
   - Clean and preprocess text
4. **Feature Vectorization**
   - TF-IDF Vectorization
   - Convert text to numerical features
5. **Similarity Computation**
   - Calculate cosine similarity matrix
   - Store in pickle format
6. **Model Evaluation**
   - Test recommendations
   - Validate output

## 🚀 How to Run

### Prerequisites
```bash
pip install -r requirements.txt
jupyter notebook
```

### Running the Notebook
```bash
# Start Jupyter
jupyter notebook

# Or use JupyterLab
jupyter lab
```

### Cell Execution
1. Run cells sequentially from top to bottom
2. Each cell builds on previous results
3. Final cells save pickle files to `data/`

## 📊 Expected Output

After running all cells:
```
✅ data/movie_list.pkl     (movie information)
✅ data/similarity.pkl     (similarity matrix)
✅ data/movie_vote.pkl     (vote counts)
```

## 🔧 Customization

### Change Number of Movies
```python
df = df.head(5000)  # Limit to 5000 movies
```

### Change Features
```python
features = ['genres', 'keywords', 'cast', 'crew', 'production_companies']
```

### Change Similarity Metric
```python
# Instead of cosine
from sklearn.metrics.pairwise import manhattan_distances
similarity = manhattan_distances(tfidf_matrix)
```

## 📝 Tips

- Run cells one at a time to debug
- Use `Shift+Enter` to run current cell
- Use `Ctrl+Enter` to run and stay in cell
- Monitor memory usage for large datasets
- Save checkpoints with pickle if notebook is long

## 🐛 Troubleshooting

### "Memory Error"
- Reduce number of movies: `df.head(1000)`
- Clear cell outputs: `Kernel → Restart Kernel`

### "Import Error"
- Install dependencies: `pip install -r requirements.txt`

### "TMDB API Error"
- Check API key in notebook
- Verify internet connection
- Check API rate limits

## 📚 Resources

- [Scikit-learn TF-IDF](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html)
- [Cosine Similarity](https://scikit-learn.org/stable/modules/metrics.pairwise.html#cosine-similarity)
- [Pandas Documentation](https://pandas.pydata.org/)
- [TMDB API Documentation](https://www.themoviedb.org/settings/api)
