**A tool to convert resumes to the OpenResume standard**

1. **Set up the landing page (index.html):**
   - Create an `index.html` file, which will serve as the landing page.
   - Add a form to allow users to upload resumes in PDF format.

2. **Link the script (script.js):**
   - Create a `script.js` file and link it to `index.html`.
   - In the script, use a tool like `FileReader` to extract the content of the uploaded PDF file.
   - Store the extracted content in `sessionStorage`, optionally as a JSON string.

3. **Add a 'Next' button:**
   - After the resume is uploaded, include a 'Next' button.
   - Clicking this button should navigate users to the `editor.html` page.

4. **Display the resume content (editor.html):**
   - On the `editor.html` page, display the content of the uploaded resume as a test.

5. **Transmit content to the backend:**
   - Add a button on the `editor.html` page to send the PDF content to the backend for processing.

6. **Set up Python virtual environment:**
   - Create a virtual environment for Python 3 using the following command:
     ```
     python3 -m venv .venv
     ```
   - Activate the virtual environment:
     ```
     source .venv/bin/activate
     ```

7. **Install dependencies:**
   - Run the following command to install necessary packages from `requirements.txt`:
     ```
     pip install -r requirements.txt
     ```
   - Once activated, the virtual environment name will appear in your terminal prompt.

8. **Set up backend (app.py):**
   - Create an `app.py` file in the project folder (outside of the `.venv` directory).
   - In `app.py`, define routes for handling web page navigation and for receiving the content sent from `editor.html`.

9. **Extract and display data:**
   - Use regular expressions (regex) in `app.py` to extract email addresses and phone numbers from the uploaded resume.
   - Send the extracted data to the front-end for display on the `editor.html` page.


