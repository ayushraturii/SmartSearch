import sqlite3
import requests
from transformers import BertTokenizer, BertModel
import torch
from fuzzywuzzy import process

# API Key and CX for Google Custom Search
API_KEY="AIzaSyCgS5tF5ai_bhZMOVWSneNSsJ-j3YcyKQM"
CX="e47eec9e1bc6c47b5"


# Fetch search results from Google Custom Search API
def fetch_search_results(query):
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={API_KEY}&cx={CX}"
    response = requests.get(url)
    data = response.json()

    results = []
    for item in data.get('items', []):
        result = {
            'rank': item.get('position'),
            'link': item.get('link'),
            'title': item.get('title'),
            'snippet': item.get('snippet')
        }
        results.append(result)

    return results


# Store search results in the database
def store_query_result(query, results):
    conn = sqlite3.connect('search_engine.db')
    cursor = conn.cursor()

    for rank, result in enumerate(results, start=1):
        cursor.execute("""
            INSERT INTO search_results (query, rank, link, title, snippet, relevance)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (query, rank, result['link'], result['title'], result['snippet'], 0))  # Initial relevance is 0

    conn.commit()
    conn.close()


# Rank search results using BERT-based similarity
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')


def calculate_similarity(query, text):
    inputs = tokenizer([query, text], padding=True, truncation=True, return_tensors='pt')
    with torch.no_grad():
        outputs = model(**inputs)

    query_embedding = outputs[0][0][0]
    text_embedding = outputs[0][1][0]

    similarity = torch.cosine_similarity(query_embedding, text_embedding, dim=0)
    return similarity.item()


def rank_results_with_bert(query, results):
    ranked_results = []

    # Rank the results based on BERT similarity
    for result in results:
        title = result['title']
        similarity = calculate_similarity(query, title)
        result['similarity'] = similarity
        ranked_results.append(result)

    # Sort results by similarity (highest to lowest)
    ranked_results = sorted(ranked_results, key=lambda x: x['similarity'], reverse=True)

    # Now, update the rank for each result in the database based on the sorted results
    conn = sqlite3.connect('search_engine.db')
    cursor = conn.cursor()

    for rank, result in enumerate(ranked_results, start=1):
        cursor.execute("""
            UPDATE search_results
            SET rank = ?, relevance = ?
            WHERE link = ?
        """, (rank, result['similarity'], result['link']))  # Update rank and similarity for each result

    conn.commit()
    conn.close()

    return ranked_results


# Get search history (for spelling suggestion)
def get_search_history():
    conn = sqlite3.connect('search_engine.db')
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT query FROM search_results")
    queries = [row[0] for row in cursor.fetchall()]
    conn.close()
    return queries


# Correct query using fuzzy matching
from textblob import TextBlob

# Function to correct the query using TextBlob
def correct_query(query):
    corrected_query = str(TextBlob(query).correct())
    return corrected_query



# Get all search results from the database based on the query
def get_search_results(query):
    conn = sqlite3.connect('search_engine.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM search_results WHERE query = ?", (query,))
    results = cursor.fetchall()
    conn.close()

    return results

