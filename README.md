
# Data Processing and Storage

## Overview
This project uses a key-value database that supports transactions. The database allows users to perform operations like `put`, `get`, `commit`, and `rollback` within a single transaction. It ensures that uncommitted changes are not visible and maintains data consistency.

## Features
- **Key-Value Store**: Uses string keys and integer values.
- **Transactions**:
  - `begin_transaction()`: Begin a new transaction.
  - `put(key, value)`: Insert or update a key-value pair within a transaction.
  - `get(key)`: Retrieve values from the database (committed only).
  - `commit()`: Apply all changes in the current transaction.
  - `rollback()`: Discard all changes in the current transaction.
- Single transaction allowed at a time.

## Requirements
- Python 3.7 or above.

## Usage
1. Clone the repository
2. Open a terminal and navigate to the directory containing the file.
3. Run the script using the command:
   ```bash
   python main.py
   ```
4. Observe the output of the test cases provided in the script.


## Modifications for Improvement
1. **Clarifications**:
   - Explicitly mention whether nested transactions should be supported.
2. **Grading Enhancements**:
   - There should be some automated test cases to validate the implementation.
   - Include edge cases like rollback without changes or commit without a transaction.

