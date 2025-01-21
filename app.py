from flask import Flask, render_template, request, redirect, url_for
from google_search import fetch_search_results, store_query_result, rank_results_with_bert, get_search_history
from fuzzywuzzy import process
from textblob import TextBlob  # Importing TextBlob for spelling correction
import sqlite3
app = Flask(__name__)

# Route to display search page
@app.route('/')
def index():
    return render_template('index.html')


# Route to handle search logic
@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']

    # Correct the query using TextBlob to fix spelling mistakes
    blob = TextBlob(query)
    corrected_query = str(blob.correct())  # Get the corrected query using TextBlob

    # Fetch search results from Google Custom Search API using the corrected query
    search_results = fetch_search_results(corrected_query)

    # Store the results in the database
    store_query_result(corrected_query, search_results)

    # Rank the results using BERT-based similarity
    ranked_results = rank_results_with_bert(corrected_query, search_results)

    # Get possible corrections for the query (fetch search history)
    all_queries = get_search_history()

    # Suggest the closest matching query using fuzzywuzzy
    suggestion = process.extractOne(corrected_query, all_queries)

    # If the similarity score is above a threshold, suggest the corrected query
    if suggestion and suggestion[1] > 80:  # You can adjust this threshold as needed
        corrected_query = suggestion[0]  # If we have a match, use the suggestion
    else:
        corrected_query = corrected_query  # If no match, use the TextBlob corrected query

    # Return the template with the corrected query and search results
    return render_template('index.html', query=corrected_query, results=ranked_results, corrected_query=corrected_query)


@app.route('/increase_relevance', methods=['POST'])
def increase_relevance():
    link = request.form['link']

    # Increase relevance of the search result in the database
    conn = sqlite3.connect('search_engine.db')
    c = conn.cursor()

    # Update the relevance of the link
    c.execute("UPDATE search_results SET relevance = relevance + 1 WHERE link = ?", (link,))
    conn.commit()
    conn.close()

    return redirect(link)  # Redirect to the clicked link


if __name__ == '__main__':
    app.run(debug=True)

