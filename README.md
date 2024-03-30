# First Flask API Project

The "First Flask API Project" is a beginner-level project aimed at introducing Flask API development. It provides a simple API endpoint where users can send two numbers in JSON format, and the API will return the sum of these numbers. This project serves as a practical learning exercise for understanding the basics of building APIs with Flask, handling JSON data, and sending requests using tools like Postman.

## Table of Contents
- [Use Case](#use-case)
- [Usage](#usage)
  - [Setup](#setup)
  - [Running the Program](#running-the-program)
  - [Testing the API](#testing-the-api)
- [Note](#note)
- [License](#license)
- [Author](#author)

## Use Case
This project's use case includes:
- Learning Flask API Development: This project serves as a hands-on introduction to Flask API development for beginners.
- Understanding JSON Data Handling: Users can learn how to handle JSON data in Flask applications, including parsing incoming requests and formatting outgoing responses.
- Practice with API Testing: Users can practice sending requests to the API using tools like Postman to test its functionality and verify responses.

## Usage
### Setup
1. Clone the repository to your local machine.
2. Install the necessary dependencies by running the following command in your terminal:
   ```bash
   pip install -r requirements.txt
   ```
### Running the Program
Run the program using Gunicorn:
```bash
  gunicorn app:app
```

### Testing the API
To test the API:
- Use Postman or any other API testing tool.
- Send JSON data containing two numbers to the API endpoint.
- Check the response to verify that it returns the sum of the two numbers.

## Note
- This is an API project with no graphical user interface (UI).
- Ensure data is sent in the correct JSON format to receive accurate responses.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
