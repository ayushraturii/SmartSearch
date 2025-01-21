from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class SearchQuery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(100), nullable=False)
    query = db.Column(db.String(500), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)


class SearchResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    query_id = db.Column(db.Integer, db.ForeignKey('search_query.id'), nullable=False)
    title = db.Column(db.String(500))
    url = db.Column(db.String(1000))
    snippet = db.Column(db.Text)
    rank = db.Column(db.Integer)


class ClickData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(100), nullable=False)
    query_id = db.Column(db.Integer, db.ForeignKey('search_query.id'), nullable=False)
    result_id = db.Column(db.Integer, db.ForeignKey('search_result.id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)