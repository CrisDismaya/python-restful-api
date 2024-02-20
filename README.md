# Flask PostgreSQL API

This repository contains a simple Python Flask API with PostgreSQL database integration. It provides a basic structure for building RESTful APIs using Flask and interacting with a PostgreSQL database.

## Getting Started

These instructions will help you set up and run the project locally on your machine.

### Build with
[![Python][Python]][Python-url] 
[![PostgreSQL][PostgreSQL]][PostgreSQL-url] 

### Required to install
- Python
- PostgreSQL
- Pip
- Psycopg2 Library
- Flask Library
- Matplotlib Library
- Mplcursors Library

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/CrisDismaya/python-restful-api.git && cd python-restful-api
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
    "new_topic": "Edited Topic"
}
```


<!-- MARKDOWN LINKS & IMAGES -->
[Php]: https://img.shields.io/badge/PHP-777BB4?style=for-the-badge&logo=php&logoColor=white
[Php-url]: https://www.php.net/

[JavaScript]: https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black
[JavaScript-url]: https://www.javascript.com/

[JQuery]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com/

[Laravel]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com/

[Vue]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vue.js&logoColor=4FC08D
[Vue-url]: https://vuejs.org/

[TypeScript]: https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white
[TypeScript-url]: https://www.typescriptlang.org/

[Bootstrap]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com/

[Python]: https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/

[PostgreSQL]: https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white
[PostgreSQL-url]: https://www.postgresql.org/
