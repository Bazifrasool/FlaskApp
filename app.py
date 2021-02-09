from flask import Flask,render_template,request,url_for,send_from_directory
from flask_bootstrap import Bootstrap
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '.\\uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
MEDIA_FOLDER =".\\database"
app = Flask(__name__)
app.config["UPLOAD_FOLDER"]=UPLOAD_FOLDER
app.config["MEDIA"]= MEDIA_FOLDER
Bootstrap(app)
@app.route("/")
def index():
    return render_template("base.html")

@app.route("/<path:filename>")
def img_send(filename):
    return send_from_directory(MEDIA_FOLDER,filename)


@app.route("/processing",methods=["GET","POST"])
def processing():
    if request.method == 'POST':
        if 'img' not in request.files:
            # flash('No file part')
            return "Missing"
        file = request.files['img']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            # flash('No selected file')
            return "Not Selected"
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # print(request.form["num"],type(request.form["num"]))
        
        lst=os.listdir("./database")
        return render_template("results.html",results=lst)

if __name__=="__main__":
    app.run(debug=True,host="192.168.29.250")