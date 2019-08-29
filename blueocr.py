from flask import Flask, render_template, request
from werkzeug import secure_filename
import pytesseract
from pytesseract import image_to_string as its
from PIL import Image
import os
app = Flask(__name__)

@app.route('/' ,methods=['GET','POST'])
def upload_file():
   return render_template('uploadd.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def uploader_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      #return 'file uploaded successfully'
      pytesseract.pytesseract.tesseract_cmd = r'tesseract-OCR\tesseract'
      text=its(Image.open(f.filename))
      
      #return text
      img_src='ads'
      os.remove(f.filename)
      return render_template('uploadd.html',
                                   msg='Successfully processed',
                                   extracted_text=text,
                                   img_src=img_src)
      

      
if __name__ == '__main__':
   app.run(debug = True)






#stringout=ocr('ex.jpg')
#print(stringout)
