# Book store site

## Description
Book Site is online book buying platform that allows user to buy, rate, search etc. The application feature user authentication, book catalog with advanced filtering, author and publisher pages, shopping cart functionality, and order management. Users can explore books by various criteria while administrators can manage the book inventory, authors, and publishers.

## Book Endpoints
| **Endpoint** | **Request** | **Usage** |
| --- | --- | --- |
| /books | GET | Show all books |
| /books/id | GET | Show specific book |
| /books/id | PUT | Update book |
| /books | POST | Create a new book |
| /books/id | DELETE | Delete specific book |

## Book request/response body
| **Endpoint** | **Request** | **Request Body** | **Response Body** |
| --- | --- | --- | --- |
| /books | GET | [{"id": "decimal", "name": "string", "price": "decimal"}, ...] | [{"id": "decimal", "name": "string", "price": "decimal"}, ...] |
| /books/id | GET | {"id": "decimal", "name": "string", "price": "decimal"} | {"id": "decimal", "name": "string", "price": "decimal"} |
| /books/id | PUT | {"id": "decimal", "name": "string", "price": "decimal"} | {"id": "decimal", "name": "string", "price": "decimal"} |
| /books | POST | [{"id": "decimal", "name": "string", "price": "decimal"}, ...] | [{"id": "decimal", "name": "string", "price": "decimal"}, ...] |
| /books/id | DELETE | {"id": "decimal", "name": "string", "price": "decimal"} |


## Authors Endpoints
| **Endpoint** | **Request** | **Usage** |
| --- | --- | --- |
| /authors | GET | Show all authors |
| /authors/id | GET | Show speicific author |
| /authors/id | PUT | Update author |
| /authors | POST | Add new author |
| /authors/id | DELETE | Delete specific author |

## Authors request/response body
| **Endpoint** | **Request** | **Request Body** | **Response Body** |
| --- | --- | --- | --- |
| /authors | GET | [{"id":"decimal", "name": "string"}, ...] | [{"id":"decimal", "name": "string"}, ...] |
| /authors/id | GET | {"id": "decimal", "name":"string"} | {"id": "decimal", "name":"string"} |
| /authors/id | PUT | {"id": "decimal", "name":"string"} | {"id": "decimal", "name":"string"} |
| /authors | POST | [{"id":"decimal", "name": "string"}, ...] | [{"id":"decimal", "name": "string"}, ...] |
| /authors/id | DELETE | {"id": "decimal", "name":"string"} | {"id": "decimal", "name":"string"} |


## Publisher Endpoints
| **Endpoint** | **Request** | **Usage** |
| --- | --- | --- |
| /publishers | GET | Show all publishers |
| /publishers/id | GET | Show specific publisher |
| /publishers/id | PUT | Update publisher | 
| /publishers | POST | Add new publisher |
| /publishers/id | DELETE | Delete specific publisher |

## Publisher request/response body
| **Endpoint** | **Request** | **Request Body** | **Response Body** |
| --- | --- | --- | --- |
| /publishers | GET | [{"id":"decimal", "name": "string"}, ...] | [{"id":"decimal", "name": "string"}, ...] |
| /publishers/id | GET | {"id": "decimal", "name":"string"} | {"id": "decimal", "name":"string"} |
| /publishers/id | PUT | {"id": "decimal", "name":"string"} | {"id": "decimal", "name":"string"} |
| /publishers | POST | [{"id":"decimal", "name": "string"}, ...] | [{"id":"decimal", "name": "string"}, ...] |
| /publishers/id | DELETE | {"id": "decimal", "name":"string"} | {"id": "decimal", "name":"string"} |


## Genre Endpoints
| **Endpoint** | **Request** | **Usage** |
| --- | --- | --- |
| /genres | GET | Show all genres |
| /genres/id | GET | Show all book with this genre |
| /genres/id | PUT | Update genre |
| /genres | POST | Add new genre |
| /genres/id | DELETE | Delete specific genre |

## Genre request/response body
| **Endpoint** | **Request** | **Request Body** | **Response Body** |
| --- | --- | --- | --- |
| /genres | GET | [{"id":"decimal", "name": "string"}, ...] | [{"id":"decimal", "name": "string"}, ...] |
| /genres/id | GET | {"id": "decimal", "name":"string"} | {"id": "decimal", "name":"string"} |
| /genres/id | PUT | {"id": "decimal", "name":"string"} | {"id": "decimal", "name":"string"} |
| /genres | POST | [{"id":"decimal", "name": "string"}, ...] | [{"id":"decimal", "name": "string"}, ...] |
| /genres/id | DELETE | {"id": "decimal", "name":"string"} | {"id": "decimal", "name":"string"} |


## Data Base representation

<img width="409" height="308" alt="database" src="https://github.com/user-attachments/assets/67627618-3900-4aad-987d-279965c9a1d6" />



## How to run project

1. Create virtual env
2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Apply migrations
```bash
python manage.py migrate
```
4. Run the server
```bash
python manage.py runserver
```
5. Run live server for frontend
> For Vscode u need to install extension "Live Server by Ritwick Dey"
> PyCharm has his own built-in live server

Will change as the project progresses
