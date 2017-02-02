from flask import Flask, request, flash, redirect, url_for, send_from_directory
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello!'

@app.route('/add', methods=['GET','POST'])
def add():
    if request.method == 'POST':
	if 'file' not in request.files:
	    flash('No file')
	    return redirect(request.url)
	f = request.files['file']
	if f.filename == '':
	    flash('No file')
	    return redirect(request.url)
	if f:
	    f.save('/tmp/'+f.filename)
	    return redirect(url_for('added_file', filename=f.filename))

    return '''
	<form method=post enctype=multipart/form-data>
	      <input type=file name=file>
	      <input type=submit name=Upload>
	</form>
	'''
@app.route('/uploads/<filename>')
def added_file(filename):
    return send_from_directory('/tmp/', filename)

if __name__ == "__main__":
    app.run('0.0.0.0')
