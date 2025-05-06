# Google Sheet-Calendar API for chipmeow
Using Python and GCP to construct a technical solution for linking Uyen's google sheet to her google calendar


## Contributors
* **Uyen T. Tran**: Designs architecture, collects data in a systematic format, and provides technical requests.

* **Anh V. Duong**: Researches, designs implementation, and provides technical solutions.

## Set up
* **Requirements**: [Python 3.13](https://www.python.org/downloads/release/python-3133/) (or above 3.10), Git(optional), and pip (usually comes with Python after installation).

* To check for your pip, open Command Prompt (cmd):
    ```bash
    pip --version
    ```

* To replicate our results, a set up guidance is provided below, notice that the guidance is for Windows 11's user (Uyen) only.

* (Optional) A virtual machine is highly recommend:
    ```bash
    py -m venv venv
    ```
    ```bash
    source venv/bin/activate
    ```

* After a virtual machine is set up, the required Python packages are specified in the file ```requirements.txt```, to install:
    ```bash
    pip3 install -r requirements.txt
    ```

## Call the API
* To call the API directly on the Calendar's UI, execute the following command:
    ```bash
    py api_intergration.py
    ```