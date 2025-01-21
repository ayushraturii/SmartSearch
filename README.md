<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SmartSearch Project README</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
        }
        .container {
            width: 80%;
            margin: 0 auto;
            padding: 20px;
            background-color: #fff;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1, h2 {
            color: #333;
        }
        pre {
            background-color: #f4f4f4;
            padding: 15px;
            border: 1px solid #ddd;
            overflow-x: auto;
        }
        ul {
            list-style-type: disc;
            margin-left: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>SmartSearch: Search Engine Enhancement</h1>

        <p><strong>SmartSearch</strong> is a machine learning-based project aimed at improving search results by incorporating user behavior, including previous search results and clicks. The project is built with Flask and TensorFlow, utilizing natural language processing (NLP) techniques and machine learning models to rank search results based on relevance.</p>

        <h2>Features</h2>
        <ul>
            <li>Improved search ranking based on past user activities</li>
            <li>Machine learning-based ranking algorithm</li>
            <li>'Did you mean?' feature for query correction</li>
            <li>Search history-based search results</li>
            <li>Support for multiple writing styles (casual, formal, technical, email, simple message)</li>
        </ul>

        <h2>Technologies Used</h2>
        <ul>
            <li>Flask (Web Framework)</li>
            <li>TensorFlow (Machine Learning)</li>
            <li>Google Custom Search API</li>
            <li>Python</li>
            <li>HTML, CSS, JavaScript</li>
            <li>SQL (Database Integration)</li>
        </ul>

        <h2>Project Functionality</h2>
        <p>The <strong>SmartSearch</strong> application improves search results by using machine learning and user history to rank results dynamically based on relevance. Here is how the project is structured:</p>

        <h3>1. <strong>app.py</strong></h3>
        <p>This is the main Flask application file. It handles the web server, user interaction, and routes requests. Key functionalities include:</p>
        <ul>
            <li>Accepting user search queries from the frontend</li>
            <li>Calling the backend services to fetch and rank search results</li>
            <li>Displaying search results and suggestions to the user</li>
        </ul>

        <h3>2. <strong>search.py</strong></h3>
        <p>This file is responsible for managing the search functionality. It communicates with the Google Custom Search API, retrieves search results, and processes them for display. Key tasks include:</p>
        <ul>
            <li>Fetching search results from the Google Custom Search API</li>
            <li>Processing the results and filtering them based on relevance</li>
            <li>Sending the processed results back to the frontend for display</li>
        </ul>

        <h3>3. <strong>ml_rankings.py</strong></h3>
        <p>This file contains the machine learning model that ranks search results based on user interactions and relevance. It utilizes NLP techniques and historical data to improve the ranking of search results over time. Key tasks include:</p>
        <ul>
            <li>Training machine learning models on past user behavior (e.g., clicks, search history)</li>
            <li>Ranking search results based on similarity to past searches</li>
            <li>Improving search ranking as the model learns from more data</li>
        </ul>

        <h3>4. <strong>filters.py</strong></h3>
        <p>This file is responsible for filtering out irrelevant or unwanted search results. It ensures that only relevant results are shown to the user based on predefined rules or user feedback. Key tasks include:</p>
        <ul>
            <li>Filtering out duplicate or low-quality results</li>
            <li>Improving search relevance by excluding irrelevant results based on predefined criteria</li>
        </ul>

        <h3>5. <strong>storage.py</strong></h3>
        <p>This file handles database interactions. It stores search queries, search results, and user feedback to improve future searches. It tracks user interactions and ensures that the search engine learns over time. Key tasks include:</p>
        <ul>
            <li>Storing search queries, results, and user feedback in a database</li>
            <li>Updating the database with user interactions (e.g., marking results as relevant)</li>
            <li>Retrieving historical data for training machine learning models</li>
        </ul>

        <h2>How the Search Ranking Works</h2>
        <p>The system works by analyzing user behavior, including the search queries, clicks, and interactions with search results. The machine learning model (in <strong>ml_rankings.py</strong>) ranks the search results based on relevance. Over time, as more data is collected, the model improves, providing more relevant search results.</p>

        <h2>Contributing</h2>
        <p>We welcome contributions to the project. To contribute:</p>
        <ol>
            <li>Fork the repository</li>
            <li>Create a new branch for your feature or bug fix</li>
            <li>Make your changes and commit them</li>
            <li>Push to your forked repository</li>
            <li>Open a pull request</li>
        </ol>

        <h2>License</h2>
        <p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>
    </div>
</body>
</html>
