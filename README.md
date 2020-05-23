# blue-ocr

To run the blue ocr in your browser follow these steps

<b>-----for windows-----</b><br>
install tesseract ocr engine usingone of these following links based on your os(64bit/32bit)<br>
https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w32-setup-v5.0.0-alpha.20190708.exe (32bit)<br><br>
https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.0.0-alpha.20190708.exe (64bit)<br>

change the path in blue-ocr.py to your directorywhere you instaled tesseract<br>
pytesseract.pytesseract.tesseract_cmd = r'--your path here--'<br>
it would either be c:\program files\tesseract-OCR\tesseract<br>
<b>OR</b><br>
be c:\program files(x86)\tesseract-OCR\tesseract<br>
run<br>
pip install pytesseract<br>
pip install flask<br>
pip install pillow<br>
pip install os<br>
    
now run blueocr.py<br> 
and type ip address shown in the console in your browser<br>
