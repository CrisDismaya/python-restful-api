# Flask PostgreSQL API

This repository contains a simple Python Flask API with PostgreSQL database integration. It provides a basic structure for building RESTful APIs using Flask and interacting with a PostgreSQL database.

## Getting Started

These instructions will help you set up and run the project locally on your machine.

### Prerequisites

Make sure you have the following software installed on your machine:

- Python (3.6 or higher)
- PostgreSQL

### Clone the Repository

```bash
git clone https://github.com/your-username/flask-postgresql-api.git
cd flask-postgresql-api
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

# List of Endpoints

- **GET /api/getTopic:**
```
{
    "user_id": 1
}
```

- **GET /api/getMessageFromTopic:**
```
{
    "topic_id": 1
}
```

- **POST /api/addMessages:**
```
{
    "topic_id": 1,
    "user_id": 1,
    "message": "Sample Message"
}
```

- **DELETE /api/deleteMessage:**
```
{
    "topic_id": 1,
    "user_id": 1
}
```

- **DELETE /api/updateTopic:**
```
{
    "topic_id": 1,
    "new_topic": "magic"
}
```