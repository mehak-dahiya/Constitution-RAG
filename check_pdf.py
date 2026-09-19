from pypdf import PdfReader

try:
    reader = PdfReader("Data/Data.pdf")
    print("PDF loaded successfully!")
    print("Pages:", len(reader.pages))
except Exception as e:
    print("ERROR:")
    print(e)