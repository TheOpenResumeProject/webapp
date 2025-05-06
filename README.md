# OpenResume Web
This is a web-based tool that will analyse your existing resume
so that it can turned into an OpenResume-compliant resume. The parser
is a work-in-progress, so expect it to not work. Meanwhile, you can
take a complainat resume to get different looks or formats using pre-defined
templates.


## Contributing
We are refining a contributor's guide; we'll update the repo once it's done.

### Developing Locally

1. **Set up Python virtual environment:**
   - Create a virtual environment for Python 3 using the following command:
     ```
     python3 -m venv .venv
     ```
   - Activate the virtual environment:
     ```
     source .venv/bin/activate
     ```

2. **Install dependencies:**
   - Run the following command to install necessary packages from `requirements.txt`:
     ```
     pip install -r requirements.txt
     ```
   - Once activated, the virtual environment name will appear in your terminal prompt.

3. **Run the Application**
   - Run the flask app with the following command:
     ```
     flask run
     ```
