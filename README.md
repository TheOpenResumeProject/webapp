# webapp
A tool to get your resume converted to conform to the OpenResume standard.

Set up index.html file – This will be the landing page for the web app. Include a form where users can upload resumes in PDF format.
Create a script.js file and link it to index.html. In the script file, use a reader (like FileReader) to extract the content of the uploaded file and store it in sessionStorage (optionally as a JSON string).
After the resume is uploaded, users will click a 'Next' button that directs them to the editor.html page.
As a test, display the content of the resume on the editor.html page.
On the editor.html page, create a button to transmit the PDF content to the backend.
Set up a Python virtual environment: Create a virtual environment named .venv for Python 3.
Activate the virtual environment by running source .venv/bin/activate.
Run pip install -r requirements.txt to install the necessary packages.
Once the virtual environment is activated, the name of the project will appear in the terminal prompt.
Set up app.py (and other project files) in the same folder as the project environment but outside the virtual environment directory (which only holds dependencies and packages).
In the app.py file, create functions with endpoints to handle routing for the web pages and to receive the content sent from editor.html (mentioned in step 5).
Use regular expressions (regex) to extract emails and phone numbers from the uploaded resume, and send them to be displayed on the front end (on editor.html).
