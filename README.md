# Book Store REST API

##  Description

You will be provided with a REST API that performs CRUD (Create, Read, Update, Delete) operations for a bookstore. The API has the following endpoints:

1. `POST /books` - Create a new book
2. `GET /books` - Retrieve a list of all books
3. `GET /books/{book_id}` - Retrieve details of a single book
4. `PUT /books/{book_id}` - Update a book's details
5. `DELETE /books/{book_id}` - Delete a book

### API Schema for Book

```json
{
  "book_id": "string",
  "title": "string",
  "author": "string",
  "published_date": "YYYY-MM-DD",
  "isbn": "string",
  "price": "float"
}

```

###  Requirements

1. **Testing Framework**
The testing framework used is pytest
you can install with the following command

2. **Test Scenarios**
    - Write test cases for CRUD operations.
        1. Validate correct HTTP status codes.
        2. Validate response payload.
        3. Validate response headers.
        4. Validate fault conditions.


## How to run the API

```bash
python bookstore_api.py

```

Your API will start running at **`http://127.0.0.1:5000/`**.

### **API Endpoints:**

- **Create a New Book**: POST request to **`http://127.0.0.1:5000/books`**
- **Retrieve All Books**: GET request to **`http://127.0.0.1:5000/books`**
- **Retrieve a Single Book**: GET request to **`http://127.0.0.1:5000/books/{book_id}`**
- **Update a Book**: PUT request to **`http://127.0.0.1:5000/books/{book_id}`**
- **Delete a Book**: DELETE request to **`http://127.0.0.1:5000/books/{book_id}`**
