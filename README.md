# 🎬 Movie Recommendation System

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue?style=flat-square&logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-red?style=flat-square&logo=streamlit)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/psf/black)

---

## 📖 Overview

A **content-based movie recommendation system** that suggests similar movies based on user selection. Using machine learning (cosine similarity), the app recommends **5 similar movies** with vote counts from a database of **1,000+ titles**.

### ✨ Key Features

- 🎯 **Content-based filtering** using cosine similarity
- 🎬 **1,000+ movies** to choose from
- ⭐ **Vote counts** for each recommendation
- 🖼️ **Movie posters** fetched from TMDB API
- 🚀 **Fast & interactive** web interface with Streamlit
- ☁️ **Deployed on Hugging Face Spaces**
- 🔐 **Secure API key** management with .env

---

## 🎓 How It Works

### Algorithm: Cosine Similarity

1. **Feature Extraction** → Convert movie data (genres, cast, crew, keywords) into vectors
2. **Calculate Similarity** → Compute cosine similarity between movies
3. **Rank Similar Movies** → Find top 5 most similar movies
4. **Fetch Details** → Get posters and vote counts from TMDB API
5. **Display Results** → Show recommendations in interactive UI

### Example
```
User selects: "The Dark Knight"
         ↓
System finds: Inception, Interstellar, The Matrix, Memento, Prestige
         ↓
Fetches: Movie posters + vote counts
         ↓
Displays: Beautiful grid layout with recommendations
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|-----------|----------|
| **Python 3.8+** | Core programming language |
| **Streamlit** | Interactive web interface |
| **Pandas** | Data manipulation |
| **Scikit-learn** | Machine learning (cosine similarity) |
| **Requests** | TMDB API integration |
| **Pickle** | Model serialization |
| **TMDB API** | Movie posters & metadata |
| **Hugging Face Spaces** | Cloud deployment |

---

## 📁 Project Structure

```
movie-recommend-system-/
├── README.md                  # Project documentation
├── LICENSE                    # MIT License
├── requirements.txt           # Python dependencies
├── .gitignore                 # Git ignore rules
├── .env.example              # Environment variables template
├── config.py                 # Configuration settings
├── app.py                    # Main Streamlit application
│
├── src/                      # Core modules
│   ├── api.py               # TMDB API functions
│   ├── recommender.py       # Recommendation logic
│   ├── utils.py             # Utility functions
│   └── __init__.py
│
├── notebooks/               # Jupyter notebooks
│   ├── movie.ipynb         # Exploration & model building
│   └── README.md           # Notebook guide
│
├── data/                    # Data directory
│   ├── movie_list.pkl      # Movie list (pickled)
│   ├── similarity.pkl      # Similarity matrix (pickled)
│   ├── movie_vote.pkl      # Vote counts (pickled)
│   └── README.md           # Data guide
│
and models/
│   └── (pre-trained models)
└── tests/                   # Unit tests (optional)
    └── test_recommender.py
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip or conda
- TMDB API key (free signup at [themoviedb.org](https://www.themoviedb.org/))

### Installation

#### 1. Clone the Repository
```bash
git clone https://github.com/Rahul7065469/movie-recommend-system-.git
cd movie-recommend-system-
```

#### 2. Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4. Setup API Key
```bash
# Copy template
cp .env.example .env

# Edit .env and add your TMDB API key
# TMDB_API_KEY=your_api_key_here
```

**How to get TMDB API key:**
1. Visit https://www.themoviedb.org/settings/api
2. Sign up (free account)
3. Request API key
4. Copy and paste into `.env` file

#### 5. Run the Application
```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

---

## 💻 Usage

1. **Select a Movie** → Choose from dropdown list of 1,000+ movies
2. **Click "Recommend"** → System finds 5 similar movies
3. **View Results** → See movie posters and vote counts
4. **Explore** → Select different movies to get new recommendations

### Example Output
```
You selected: Inception

Recommended Movies:
┌─────────────────┬──────────────┬──────────────┬──────────────┬──────────────┐
│  The Dark       │ Interstellar │  The Matrix  │   Memento    │  Prestige    │
│  Knight         │              │              │              │              │
├─────────────────┼──────────────┼──────────────┼──────────────┼──────────────┤
│ Votes: 28,451   │ Votes: 35,718│ Votes: 42,556│ Votes: 31,206│ Votes: 25,143│
│ [Poster Image]  │ [Poster]     │ [Poster]     │ [Poster]     │ [Poster]     │
└─────────────────┴──────────────┴──────────────┴──────────────┴──────────────┘
```

---

## 🌐 Live Demo

👉 **[Try the App on Hugging Face Spaces](https://huggingface.co/spaces/Rahul9971/Streamlit-app)**

---

## 📊 Dataset Information

- **Total Movies:** 1,000+
- **Features Used:** Genres, cast, crew, keywords
- **Vectorization:** TF-IDF (Term Frequency-Inverse Document Frequency)
- **Similarity Metric:** Cosine Similarity
- **Data Source:** TMDB (The Movie Database)

---

## 🔒 Security

- ✅ API key stored in `.env` (never committed)
- ✅ `.gitignore` prevents uploading sensitive data
- ✅ Error handling for API failures
- ✅ Input validation for movie selection

---

## 🛠️ Configuration

Edit `config.py` to customize:

```python
# API Settings
TMDB_API_KEY = os.getenv('TMDB_API_KEY')
TMDB_API_URL = 'https://api.themoviedb.org/3/movie'

# Recommendation Settings
NUM_RECOMMENDATIONS = 5          # Number of movies to recommend
POSTER_SIZE = 'w500'            # TMDB poster resolution

# UI Settings
PAGE_TITLE = "Movie Recommendation System"
LAYOUT = "wide"                 # Streamlit layout
```

---

## 🐛 Troubleshooting

### Problem: "API Key Error"
**Solution:** 
1. Check `.env` file exists
2. Verify API key is correct
3. Ensure `.env` is in project root

### Problem: "Movie not found"
**Solution:** 
1. Ensure `movie_list.pkl` is in `data/` folder
2. Verify pickle files are not corrupted

### Problem: "Poster not loading"
**Solution:** 
1. Check internet connection
2. Verify TMDB API is accessible
3. Check if movie has poster on TMDB

### Problem: "Streamlit not found"
**Solution:** 
```bash
pip install -r requirements.txt
```

---

## 📈 Future Improvements

- [ ] Collaborative filtering (user ratings)
- [ ] Hybrid recommendation system
- [ ] User rating system
- [ ] Watch history tracking
- [ ] Advanced filtering (year, genre, rating)
- [ ] Movie details popup
- [ ] Recommendation explanations
- [ ] Multi-language support
- [ ] Performance optimization
- [ ] Database integration

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/your-feature`
3. **Make changes** and test them
4. **Commit** with clear message: `git commit -m "Add feature description"`
5. **Push** to your fork: `git push origin feature/your-feature`
6. **Create Pull Request** and describe your changes

### Guidelines
- Keep code clean and documented
- Add docstrings to functions
- Use type hints
- Test your changes
- Update README if needed

---

## 📄 License

MIT License - See [LICENSE](LICENSE) file for details

You can:
- ✅ Use this project commercially
- ✅ Modify the code
- ✅ Distribute copies
- ⚠️ Include license notice

---

## 👤 Author

**Rahul** - [GitHub Profile](https://github.com/Rahul7065469)

---

## 🙏 Acknowledgments

- TMDB (The Movie Database) for API and movie data
- Streamlit for interactive web framework
- Hugging Face for free hosting
- YouTube tutorials and ChatGPT for learning

---

