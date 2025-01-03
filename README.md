# Playwright Python Login Demo
Login and validate portfolio using the Playwright Pytest framework.

## Setup

1. Using the example `env_example` file, create a `.env` file in the root of the project and customize the values.
    ```bash
    $ cp env_example .env
    ```


All commands from root of project:
1. Activate venv
    > Its a good idea to install a [virtual environment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) to isolate packages from your global pythong installation.

    ```bash
    $ python3 -m venv .qa
    
    $ source .qa/bin/activate
    ```

1. Install dependencies to the .qa venv
    ```bash
    $ pip install -r requirements.txt
    ```

1. Run tests

    ```bash
    pytest

    ```

1. If you get the follwing error, run `playwright install` as instructed.
    ```bash
    E           ║ Looks like Playwright was just installed or updated.       ║
    E           ║ Please run the following command to download new browsers: ║
    E           ║                                                            ║
    E           ║     playwright install    
    ```