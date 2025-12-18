### Project Description

#### Overview
This project aims to provide a robust library for parsing and converting date strings into datetime objects with customizable formats. The purpose of this project was driven by frequent interactions with various APIs that return dates in different formats, making it challenging to handle these conversions manually.

**Purpose**
- Flexible Date Parsing: Develop functions that can parse diverse date string formats into datetime objects.
- API Integration: Facilitate seamless integration with external services that provide dates in varied formats.
-- Consistency and Reliability: Ensure reliable parsing of dates regardless of their format, reducing manual conversion errors.

**Features**
- Customizable Date Formats: Support a wide range of date formats (e.g., %Y-%m-%d, %Y/%m/%dT%H:%M:%S, %Y/%m/%d %I:%M %p).
- Error Handling and Validation: Include robust error handling to manage invalid date strings gracefully.
- Extensive Test Coverage: Provide a comprehensive test suite to validate the functionality of the parsing functions.

#### Components

1. **Parser Module (`src/parser.py`)**:
   - This module contains the core functionality for parsing date strings.
   - It includes a function named `parse_date`, which takes arguments: 
        - date string 
        - format specifier
        - timestamp specifier
        - timezone
   - The function returns a `datetime` object representing the parsed date.

2. **Test Suite (`src/test_parser.py`)**:
   - This file contains unit tests to verify the correctness of the `parse_date` function from the parser module.
   - It uses Python's built-in `unittest` framework to define test cases and validate the expected behavior of the `parse_date` function.

#### Usage

To use the functionality provided by this project, you need to:

1. **Install Dependencies**:
   - Project has been initialized with uv (astral) to syncronize the project, ensure that you have uv installed on your system. And execute the command:

     ```bash
     uv sync
     ```

   - The project does not require any additional dependencies beyond the standard library for parsing dates.

2. **Run Tests**:
   - To verify that the `parse_date` function works as expected, run the tests provided in `src/test_parser.py`.
   - This can be done by executing the following command from the terminal:

     ```bash
     python src/test_parser.py
     ```

#### Features

- **Flexible Date Parsing**:
  - The `parse_date` function supports various date formats specified through format specifiers.
  - Commonly used formats include `%Y-%m-%d`, `%Y/%m/%d`, `%Y/%m/%dT%H:%M:%S`, and `%Y/%m/%d %I:%M %p`.

- **Error Handling**:
  - The tests cover various scenarios, including valid date strings and edge cases such as invalid dates.

#### Contributing

Contributions to this project are welcome. If you wish to contribute:

1. Fork the repository.
2. Make your changes in a new branch.
3. Submit a pull request describing your changes.

#### License
This project is licensed under the MIT License. For more information, please refer to the `LICENSE` file provided with the repository.

#### Acknowledgments

We would like to thank all contributors who have helped improve this project over time. Your contributions are highly appreciated!

---