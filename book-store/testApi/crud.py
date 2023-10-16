import pytest
import requests
import utilities


def test_create_book():
    book_data = utilities.create_book("New Book", "Author Name", "2023-09-06", "1234567890", 19.99)

    utilities.delete_book_by_id(book_data['book_id'])


def test_retrieve_all_books():
    response = requests.get(utilities.BASE_URL)
    assert response.status_code == 200


def test_retrieve_single_book():
    book_data = utilities.create_book("Test Book", "Test Author", "2023-09-07", "9876543210", 29.99)
    book_id = book_data['book_id']

    response = utilities.get_book_by_id(book_id)
    assert response.status_code == 200

    utilities.delete_book_by_id(book_id)


def test_update_book():
    book_data = utilities.create_book("Original Title", "Original Author", "2023-09-08", "1111111111", 39.99)
    book_id = book_data['book_id']

    updated_data = {
        "title": "Updated Title",
        "price": 49.99
    }
    response = requests.put(f"{utilities.BASE_URL}/{book_id}", json=updated_data)
    assert response.status_code == 200

    utilities.delete_book_by_id(book_id)


def test_delete_book():
    book_data = utilities.create_book("Book to Delete", "Delete Author", "2023-09-09", "9999999999", 9.99)
    book_id = book_data['book_id']

    response = requests.delete(f"{utilities.BASE_URL}/{book_id}")
    assert response.status_code == 204
