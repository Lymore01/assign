# Exam Information Retrieval API

This Flask API serves exam information based on unit names provided by the user. It reads data from an Excel file and returns relevant exam details such as location, date, and time for the specified units.

## Overview

This project provides a RESTful API endpoint `/api/get_exam_info` to retrieve exam information. It utilizes Flask to handle HTTP requests and Pandas for data manipulation. The API reads data from an Excel file containing exam schedules and responds with details for the requested units.

## Features

- **Exam Information Retrieval**: Users can fetch exam details by providing unit names as input.
- **Excel Data Parsing**: The API parses exam data from an Excel file to extract relevant information.
- **Dynamic Response**: The API dynamically responds with exam details including location, date, and time for each unit.
- **Error Handling**: Error messages are provided for incorrect inputs or unexpected errors.

## Prerequisites

Before running the API, ensure you have the following installed:

- Python (>=3.6)
- Flask
- Pandas
- Flask-CORS (for enabling Cross-Origin Resource Sharing)

## Getting Started

1. **Clone the Repository**:

   ```bash
   git clone [https://github.com/your-username/exam-info-api.git](https://github.com/Lymore01/assign.git)
   cd assign
2. **start the server**:
 ```bash
 flask run 
```
3. **start the client**:
   ```bash
   cd client
   npm run dev```
![localhost_5173_ (4)](https://github.com/Lymore01/assign/assets/130097627/f73b9be7-573d-4f36-8d02-b3de0fc112fe)



4. **Example Usage**
```bash
curl -X POST -H "Content-Type: application/json" -d "{\"unit_names\": \"MAT120A\"}" http://localhost:5000/api/get_exam_info     //note: the units should be in UPPERCASE
