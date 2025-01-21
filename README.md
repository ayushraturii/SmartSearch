# SmartSearch: Search Engine Enhancement

**SmartSearch** is a machine learning-based project aimed at improving search results by incorporating user behavior, including previous search results and clicks. The project is built with Flask and TensorFlow, utilizing natural language processing (NLP) techniques and machine learning models to rank search results based on relevance.

## Features

- Improved search ranking based on past user activities
- Machine learning-based ranking algorithm
- 'Did you mean?' feature for query correction
- Search history-based search results
- Support for multiple writing styles (casual, formal, technical, email, simple message)

## Technologies Used

- Flask (Web Framework)
- TensorFlow (Machine Learning)
- Google Custom Search API
- Python
- HTML, CSS, JavaScript
- SQL (Database Integration)

## Project Functionality

The **SmartSearch** application improves search results by using machine learning and user history to rank results dynamically based on relevance. Here is how the project is structured:

### 1. `app.py`
This is the main Flask application file. It handles the web server, user interaction, and routes requests. Key functionalities include:
- Accepting user search queries from the frontend
- Calling the backend services to fetch and rank search results
- Displaying search results and suggestions to the user

### 2. `search.py`
This file is responsible for managing the search functionality. It communicates with the Google Custom Search API, retrieves search results, and processes them for display. Key tasks include:
- Fetching search results from the Google Custom Search API
- Processing the results and filtering them based on relevance
- Sending the processed results back to the frontend for display

### 3. `ml_rankings.py`
This file contains the machine learning model that ranks search results based on user interactions and relevance. It utilizes NLP techniques and historical data to improve the ranking of search results over time. Key tasks include:
- Training machine learning models on past user behavior (e.g., clicks, search history)
- Ranking search results based on similarity to past searches
- Improving search ranking as the model learns from more data

### 4. `filters.py`
This file is responsible for filtering out irrelevant or unwanted search results. It ensures that only relevant results are shown to the user based on predefined rules or user feedback. Key tasks include:
- Filtering out duplicate or low-quality results
- Improving search relevance by excluding irrelevant results based on predefined criteria

### 5. `storage.py`
This file handles database interactions. It stores search queries, search results, and user feedback to improve future searches. It tracks user interactions and ensures that the search engine learns over time. Key tasks include:
- Storing search queries, results, and user feedback in a database
- Updating the database with user interactions (e.g., marking results as relevant)
- Retrieving historical data for training machine learning models

## How the Search Ranking Works

The system works by analyzing user behavior, including the search queries, clicks, and interactions with search results. The machine learning model (in `ml_rankings.py`) ranks the search results based on relevance. Over time, as more data is collected, the model improves, providing more relevant search results.

## Contributing

We welcome contributions to the project. To contribute:
1. Fork the repository
2. Create a new branch for your feature or bug fix
3. Make your changes and commit them
4. Push to your forked repository
5. Open a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
