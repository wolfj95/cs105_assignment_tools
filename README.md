# CS105 HTML/CSS Assignment PDF Generator
This tool helps turn HTML/CSS files into a single PDF to use when grading
student assignments.

## Using the script
1. **Install the requirements for the tool using `pip install -r requirements.txt`.**
1. **Downoad your zipped student submissions.** Submissions should be
a single zipped folder containing all of the students files for the assignemnt.
1. **Place the zip files in the `student_submissions` directory in the repo.**
Make sure the files are extracted from the folder you downloaded them in.
1. **Run the script using `python3 python_pdf_script.py`.** The script will
print out if there are any errors while trying to convert the files. You'll
have to follow up with these manually.
1. **The `submissions_pdfs` directory contains the converted PDFs.** You must
make sure this directory exists *before* running the script.

p.s. Make sure you're using Python3 to run the script.
