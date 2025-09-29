# Book store site

## Description
Book Site is online book buying platform that allows user to buy, rate, search etc. The application feature user authentication, book catalog with advanced filtering, author and publisher pages, shopping cart functionality, and order management. Users can explore books by various criteria while administrators can manage the book inventory, authors, and publishers.

## Endpoints
| **Endpoint** | **Request** | **Usage** | **Response Body** |
| --- | --- | --- | --- |
| /books | GET | Show all books | [{"id": "decimal", "name": "string", "price": "decimal"}, ..]
| /books/id | GET | Show specific book | {"id": "decimal", "name": "string", "price": "decimal"}
| /books/id | PUT | Update book | {"id": "decimal", "name": "string", "price": "decimal"}
| /books | POST | Create a new book | [{"id": "decimal", "name": "string", "price": "decimal"}, ..]
| /books/id | DELETE | Delete specific book | {"id": "decimal", "name": "string", "price": "decimal"}

## Data Base representation

<img src="/images/logo.png" alt="Logo" width="817" height="615">