# VID - Virtual Instructional Droid

## Overview

VID, short for Virtual Instructional Droid, is a full-stack web application designed to serve as a powerful assistant for solving educational programming tasks. It incorporates the JetBrains AI Grazie API to enhance the user experience. The frontend is developed using Angular, and the backend is implemented in Python with Flask. MongoDB is utilized as the database to store essential information.

## Setup and Installation

### Prerequisites

- Node.js and npm
- Python (3.6 or higher)
- MongoDB
- JetBrains AI Grazie API key (obtain it [here](https://www.jetbrains.com/grazie/download/))

### Backend Setup

1. Navigate to the `backend` directory:

    ```bash
    cd backend
    ```

2. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

4. Install dependencies using `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

5. Set up the environment variables:

    ```bash
    export FLASK_APP=app
    export FLASK_ENV=development
    export GRAZIE_API_KEY=your_jetbrains_api_key
    ```

6. Run the Flask application:

    ```bash
    flask run
    ```

### Frontend Setup

1. Navigate to the `frontend` directory:

    ```bash
    cd frontend
    ```

2. Install Angular CLI (if not already installed):

    ```bash
    npm install -g @angular/cli
    ```

3. Install project dependencies:

    ```bash
    npm install
    ```

4. Run the Angular development server:

    ```bash
    ng serve
    ```

## Accessing the Application

Once both the backend and frontend servers are running, access the application by navigating to [http://localhost:4200](http://localhost:4200) in your web browser.

## License

This project is licensed under the [MIT License](LICENSE).
