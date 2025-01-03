# Playwright Python Login Demo
Login and validate portfolio using the Playwright Pytest framework.

## Setup

1. Using the example `env_example` file, create a `.env` file and customize the values.
    ```bash
    $ cp env_example .env
    ```


All commands from root of project:
1. Activate venv
    > Its a good idea to install a [virtual environment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) to isolate packages from your global python installation.

    ```bash
    $ python3 -m venv .qa
    
    $ source .qa/bin/activate
    ```

1. Install dependencies to the now active .qa venv
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

# Known Issues
 - Device Approval always requred due to playwright test isolation, the app thinks its a new device and sends an email for approval.
 - A workaround is to first run with: `PWDEBUG=1 pytest -s`, stepping through the playwright debugger and
   leaving the window open while you go check email, and approve device. This saves full state in storage_state.json
   and the debugger will login after approval and test will pass.
   Howver, subsequent runs that use the stored session are still returning as expired and I don't know why.        