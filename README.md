# blue-ocr

to run the blue ocr in your browser follow these steps

-----for windows-----
install tesseract ocr engine usingone of these following links based on your os(64bit/32bit)
https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w32-setup-v5.0.0-alpha.20190708.exe (32bit)
https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.0.0-alpha.20190708.exe (64bit)

change the path in blue-ocr.py to your directorywhere you instaled tesseract
pytesseract.pytesseract.tesseract_cmd = r'--your path here--'
it would either be c:\program files\tesseract-OCR\tesseract
or
be c:\program files(x86)\tesseract-OCR\tesseract
run pip install pytesseract
    pip install flask
    pip install pillow
    pip install os
    
now run blueocr.py 
and type ip address shown in the console in your browser
