# Playwright Python Login Demo
Login and validate portfolio using the Playwright Pytest framework.

## Setup
All commands from root of project:
1. Activate venv
    > Its a good idea to install a [virtual environment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) to isolate packages from your global pythong installation.

    ```bash
    # Create virtual environment named .qa
    $ python3 -m venv .qa
    
    # Activate
    $ source .qa/bin/activate
    ```

1. Install dependencies to venv
    ```bash
    $ pip install -r requirements.txt
    ```
1. Run tests

    ```bash
    pytest

    ```