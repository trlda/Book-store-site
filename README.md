# Book store site

## Description
Book Site is online book buying platform that allows user to buy, rate, search etc. The application feature user authentication, book catalog with advanced filtering, author and publisher pages, shopping cart functionality, and order management. Users can explore books by various criteria while administrators can manage the book inventory, authors, and publishers.

## Book Endpoints
| **Endpoint** | **Request** | **Usage** | **Response Body** |
| --- | --- | --- | --- |
| /books | GET | Show all books | [{"id": "decimal", "name": "string", "price": "decimal"}, ..]
| /books/id | GET | Show specific book | {"id": "decimal", "name": "string", "price": "decimal"}
| /books/id | PUT | Update book | {"id": "decimal", "name": "string", "price": "decimal"}
| /books | POST | Create a new book | [{"id": "decimal", "name": "string", "price": "decimal"}, ..]
| /books/id | DELETE | Delete specific book | {"id": "decimal", "name": "string", "price": "decimal"}

## Authors Endpoints
| **Endpoint** | **Request** | **Usage** | **Response Body** |
| /authors | GET | Show all authors | [{"id":"decimal", "name": "string"}, ...] |
| /authors/id | GET | Show speicific author | {"id": "decimal", "name":"string"} |

## Publisher Endpoints
| **Endpoint** | **Request** | **Usage** | **Response Body** |
| /publisher | GET | Show all publishers | [{"id":"decimal", "name": "string"}, ...] |
| /publisher/id | GET | Show specific publisher | {"id": "decimal", "name": "string"} |

## Genre Endpoints
| **Endpoint** | **Request** | **Usage** | **Response Body** |
| /genre | GET | Show all genres | [{"id": "decimal", "name": "string"}, ...] |
| /genre/id | GET | Show all book with this genre | {"id": "decimal", "name": "string"} |

## Data Base representation

<img width="409" height="308" alt="database" src="https://github.com/user-attachments/assets/67627618-3900-4aad-987d-279965c9a1d6" />



Will change as the project progresses