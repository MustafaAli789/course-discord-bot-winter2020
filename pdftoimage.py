from pdf2image import convert_from_path, convert_from_bytes

PDF_PATH = "mat2377.pdf"
OUTPUT_FOLDER = "./mat2377"
FIRST_PAGE=17

pages = convert_from_path(PDF_PATH, poppler_path=r"C:\Users\alimu\Documents\poppler-20.12.1\Library\bin", output_folder=OUTPUT_FOLDER, fmt="jpeg", first_page=FIRST_PAGE, output_file="")
