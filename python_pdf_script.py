# Python program to convert
# text file to pdf file
import os

from fpdf import FPDF
from pathlib import Path
import tempfile
import zipfile
   
# save FPDF() class into 
# a variable pdf

def create_pdf_submission(zipped_submission):
    pdf = FPDF()   

    # unzip
    with tempfile.TemporaryDirectory() as tmp_submission_dir:
        tmp_submission_dir = Path(tmp_submission_dir)
        with zipfile.ZipFile(zipped_submission, mode='r') as zip_ref:
            zip_ref.extractall(tmp_submission_dir)
            
            dirs_in_tmp = [child for child in tmp_submission_dir.iterdir() if child.is_dir() and child.name != "__MACOSX"]
            # check if directory was zipped or if files were zipped
            if len(dirs_in_tmp) > 0:
                assignment_dir = dirs_in_tmp[0]
            else:
                assignment_dir = tmp_submission_dir

            # add coversheet to pdf
            coversheet = ""
            if not 'coversheet.txt' in [file.name for file in assignment_dir.iterdir()]:
                print("No coversheet found in: ", zipped_submission.name)
                return None
            coversheet = assignment_dir / 'coversheet.txt'
            pdf.add_page()
            pdf.set_font("Arial", style='', size=24)
            with coversheet.open(encoding='utf-8-sig') as f:
                for line in f:
                    line = line.encode('latin-1', 'replace').decode('latin-1')
                    pdf.multi_cell(0, 10, txt=line, align='L')

            # add other files to pdf
            for child in assignment_dir.iterdir():
                if child.suffix == ".html" or child.suffix == ".css":
                    # Add a page
                    pdf.add_page()
                    # Add file title
                    pdf.set_font("Arial", style='BU', size=24)
                    pdf.multi_cell(0, 10, txt=child.name, align="L")
                    # Add file contents  
                    pdf.set_font("Arial", style='', size=15)
                    with child.open(encoding='utf-8-sig') as f:
                        for line in f:
                            line = line.encode('latin-1', 'replace').decode('latin-1')
                            pdf.multi_cell(0, 10, txt=line, align='L')
    return pdf

submissions_dir = Path('student_submissions')
for child in submissions_dir.iterdir():
    if child.suffix == ".zip":
        try:
            submission_pdf = create_pdf_submission(child)
            if submission_pdf:
                submission_pdf.output("submissions_pdfs/" + child.stem + ".pdf")
        except Exception as e:
            print("Error: ", e)
            print("while converting: ", child)

