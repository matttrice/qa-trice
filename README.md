# Playwright Python Login Demo
Login and validate portfolio amount using the [Playwright Pytest framework](https://playwright.dev/python/docs/intro).

# Known Issues / Notes
 - "Device Approval" via email is requred during the first run:
    1. On first execution, the test will pause and wait for you to approve the device via email.
    2. After approval, the test will continue and pass.
    3. Subsequent runs will utilize the stored session and should not require device approval.

# Setup

> All commands from root of project:

1. Using the example `env_example` file, create a `.env` file
    ```bash
    cp env_example .env
    ```
2. Customize the `.env` file with your own credentials, base_url and portfolio value.


1. Activate [Virtual Environment (venv)](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

    ```bash
    # Its a good idea to install a venv to isolate packages from your global python installation but this is not necessary on most machines.

    python3 -m venv .qa
    
    source .qa/bin/activate
    ```

1. Install dependencies to the now active .qa venv
    ```bash
    pip install -r requirements.txt
    ```
    
# Run tests

```bash
pytest --vv test_portfolio.py --headed

# If you want to run with debugger/inspector    
PWDEBUG=1 pytest -s test_portfolio.py --headed
```


If you get the follwing error, run `playwright install` as instructed.

```bash
E           ║ Looks like Playwright was just installed or updated.       ║
E           ║ Please run the following command to download new browsers: ║
E           ║                                                            ║
E           ║     playwright install    
```