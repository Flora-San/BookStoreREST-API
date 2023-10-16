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



## Unit Testing  - Exercise : Book Store REST API
### for my  solution approach I use python, pytest, and the configuration described is for linux 

**Install poetry _linux instructions_**

update first if is necessary
```
sudo snap install curl  # version 8.1.2
```
and then run the following command line to install poetry
```
curl -sSL https://install.python-poetry.org | python3 -
```
check poetry version 
```
poetry --version
```
**Install pytest**

pytest
```
pip install pytest
```

**Run Tests**

You can run these test cases using pytest by executing the following command in your project directory:
Replace _name_test_file.py_ with the name of the Python test cases file you want to run.
```
pytest your_test_file.py

example:

create_new_book_test.py
```
Inside some test created, I added some comments just to clarify the actions and decisions taken, like the example below:

```
# Positive Test Cases
def test_create_book_positive():
    # Define valid book data
    book_data = {
        "title": "Positive Test Book",
        "author": "Author Name",
        "published_date": "2023-09-06",
        "isbn": "1234567890",
        "price": 19.99
    }

    # Send a POST request to create a new book
    response = requests.post(BASE_URL, json=book_data)

    # Assert that the response status code is 201 (Created)
    assert response.status_code == 201

    # Validate response payload
    created_book = response.json()
    assert created_book['title'] == book_data['title']
    assert created_book['author'] == book_data['author']
    
```    
