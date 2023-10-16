# Book Store REST API

### **API Endpoints:**

- **Create a New Book**: POST request to **`http://127.0.0.1:5000/books`**
- **Retrieve All Books**: GET request to **`http://127.0.0.1:5000/books`**
- **Retrieve a Single Book**: GET request to **`http://127.0.0.1:5000/books/{book_id}`**
- **Update a Book**: PUT request to **`http://127.0.0.1:5000/books/{book_id}`**
- **Delete a Book**: DELETE request to **`http://127.0.0.1:5000/books/{book_id}`**

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

## How to run the API

```bash
python bookstore_api.py

```

Your API will start running at **`http://127.0.0.1:5000/`**.
   

## CRUD - Book Store REST API
For this simple crud I use python, pytest, and the configuration described is for linux 

**Install poetry _linux instructions_**

Update first if is necessary
```
sudo snap install curl  # version 8.1.2
```
and then run the following command line to install poetry
```
curl -sSL https://install.python-poetry.org | python3 -
```
Check poetry version 
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
