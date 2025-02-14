# Silent Errors in Python: Handling Exceptions for Robustness

This repository demonstrates a common, yet subtle, type of bug in Python: silent failures.  These occur when exceptions are raised but not properly handled, resulting in unexpected behavior or incomplete program execution. The examples show how to improve the code's robustness by handling exceptions effectively.

The `bug.py` file contains the code with the silent failure. The `bugSolution.py` provides an improved version that gracefully handles potential exceptions.

## Key Concepts:

* **ZeroDivisionError:** A common exception raised when dividing by zero.
* **Exception Handling (try-except):**  The proper way to handle potential errors in your code.
* **Silent Failures:** Exceptions that occur without explicit error messages, making them harder to debug.

## How to Run:

1. Clone this repository.
2. Run `bug.py` to see the silent failure example.
3. Run `bugSolution.py` to observe how the improved code handles exceptions.