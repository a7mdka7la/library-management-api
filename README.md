# Library Management API

A RESTful API for managing a collection of books in a library. This API supports operations like adding books, listing all books, searching books, updating book details, and deleting books.

---

## Features
- Add a new book
- List all books
- Search for books by author, published year, or genre
- Update book details by ISBN
- Delete a book by ISBN
- Swagger UI for interactive API documentation

---

## Prerequisites
- Install [Docker](https://docs.docker.com/get-docker/)
- Install [Docker Compose](https://docs.docker.com/compose/install/)

---

## a. Building and Running the Docker Container

Follow these steps to build and run the Dockerized API:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Build the Docker Image**:
   ```bash
   docker-compose build
   ```

3. **Run the Docker Container**:
   ```bash
   docker-compose up
   ```

4. **Verify the API is Running**:
   - The API will be available at `http://localhost:5000`

---

## b. Accessing the Swagger API Documentation

Swagger UI provides an interactive interface to test and document API endpoints.

1. **Start the API**:
   - Ensure the API is running (see the steps above).

2. **Access Swagger Documentation**:
   - Open your browser and navigate to: `http://localhost:5000/api-docs`

3. **Explore API Endpoints**:
   - Use the Swagger UI to test API endpoints interactively.
   - Each endpoint provides details about request parameters and response formats.

---

## API Endpoints

| Method | Endpoint               | Description                              |
|--------|------------------------|------------------------------------------|
| POST   | `/books`               | Add a new book                          |
| GET    | `/books`               | List all books                          |
| GET    | `/books/search`        | Search books by author, year, or genre  |
| PUT    | `/books/{isbn}`        | Update book details by ISBN             |
| DELETE | `/books/{isbn}`        | Delete a book by ISBN                   |

---

## Example Usage with cURL

### Add a New Book
```bash
curl -X POST http://localhost:5000/books \
-H "Content-Type: application/json" \
-d '{
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "published_year": 1925,
  "isbn": "1234567890",
  "genre": "Fiction"
}'
```

### List All Books
```bash
curl -X GET http://localhost:5000/books
```

### Search for Books
```bash
curl -X GET "http://localhost:5000/books/search?author=F.+Scott+Fitzgerald"
```

### Update a Book
```bash
curl -X PUT http://localhost:5000/books/1234567890 \
-H "Content-Type: application/json" \
-d '{
  "genre": "Classic Fiction"
}'
```

### Delete a Book
```bash
curl -X DELETE http://localhost:5000/books/1234567890
```

---

## Postman Collection

1. **Import the Postman Collection**:
   - Use the exported `Postman Collection` JSON file provided in this repository.

2. **Test API Endpoints**:
   - Open Postman and import the collection.
   - Test all endpoints interactively.

---

## Troubleshooting

1. **Port Conflicts**:
   - Ensure port `5000` is free or modify the `docker-compose.yml` file to use a different port.

2. **Container Not Starting**:
   - Check Docker logs using:
     ```bash
     docker-compose logs
     ```

---

## License
This project is licensed under the MIT License.
