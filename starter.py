from flask import Flask, request, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
import json

app = Flask(__name__)

books = [] 

SWAGGER_URL = '/api-docs'  
API_DOCS_JSON = '/swagger.json'  
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_DOCS_JSON,
    config={
        'app_name': "Library Management API" 
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to the Library Management"
    }), 200

# Add a new book
@app.route('/books', methods=['POST'])
def add_book():
    data = request.json
    required_fields = ['title', 'author', 'published_year', 'isbn']
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required book details. Required fields: title, author, published_year, isbn."}), 400
    books.append(data)
    return jsonify({
        "message": "Book added successfully.",
        "book": data
    }), 201

# Get all books
@app.route('/books', methods=['GET'])
def list_books():
    return jsonify({"books": books}), 200  

# Search for books based on filters
@app.route('/books/search', methods=['GET'])
def search_books():
    author = request.args.get('author')
    published_year = request.args.get('published_year')
    genre = request.args.get('genre')

    # Filter logic - looping through the books
    results = [
        book for book in books if (
            (not author or book['author'].lower() == author.lower()) and
            (not published_year or str(book['published_year']) == published_year) and
            (not genre or book.get('genre', '').lower() == genre.lower())
        )
    ]
    return jsonify({"results": results}), 200

# Delete a book by its ISBN
@app.route('/books/<isbn>', methods=['DELETE'])
def delete_book(isbn):
    global books  
    books = [book for book in books if book['isbn'] != isbn]
    return jsonify({"message": "Book deleted successfully."}), 200

# Update book details by ISBN
@app.route('/books/<isbn>', methods=['PUT'])
def update_book(isbn):
    data = request.json 
    for book in books:
        if book['isbn'] == isbn:
            book.update(data)  # Just updating the matching book
            return jsonify({
                "message": "Book updated successfully.",
                "book": book
            }), 200
    return jsonify({"error": "Book not found."}), 404

if __name__ == '__main__':
    app.run(debug=True)

