from flask import Flask, request, render_template
import unidecode 

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('my-form.html')
              
@app.route('/convert', method=['POST'])
def convert():  
   Tr_string = request.args.get("text")
   Eng_string = unidecode.unidecode('Trstring')
   return render('Eng_string')

app.run(host="127.0.0.1", port=8080, debug=True)








