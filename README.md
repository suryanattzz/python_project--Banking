# Python Bank Application with MongoDB

This Python code simulates a basic banking system using MongoDB as the database.

## Features

- Create a new account
- Login to an existing account
- Forget PIN and recover account
- Deposit and withdraw money
- Check balance and view transaction history

## Prerequisites

- Python 3.x installed on your machine
- MongoDB installed and running on `localhost:27017`

## Getting Started

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/bank-app-mongodb.git
    cd bank-app-mongodb
    ```

2. Install the required Python packages:

    ```bash
    pip install pymongo
    ```

3. Run the application:

    ```bash
    python bank_app.py
    ```

## Application Structure

- **bank_app.py**: Contains the main application logic.
- **Bank_database_pymongo.py**: Defines the `bank_database` class for interacting with MongoDB.

## Usage

1. Follow the prompts to create a new account, login, or perform other banking operations.

2. Forgetting PIN and recovering account involves providing valid details.

3. Transactions are recorded in MongoDB, and the balance is updated accordingly.




