import requests

BASE_URL = "http://127.0.0.1:5000/books"


# Utility function to create a new book
def create_book(title, author, published_date, isbn, price):
    book_data = {
        "title": title,
        "author": author,
        "published_date": published_date,
        "isbn": isbn,
        "price": price
    }
    response = requests.post(BASE_URL, json=book_data)
    assert response.status_code == 201
    return response.json()


# Utility function to retrieve a book by ID
def get_book_by_id(book_id):
    response = requests.get(f"{BASE_URL}/{book_id}")
    return response


# Utility function to delete a book by ID
def delete_book_by_id(book_id):
    response = requests.delete(f"{BASE_URL}/{book_id}")
    assert response.status_code == 204
