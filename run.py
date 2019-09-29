from flask import Flask, request, render_template, redirect,json

app = Flask(__name__)

@app.route('/')
def index():
	return 'Hello, world!'

@app.route('/cheers')
def cheers():
	name = request.args.get('name', 'Mr. Anonymous')
	return 'Hello, {}'.format(name)

@app.route( "/upload-image", methods = ["GET","POST"] )
def upload_image():
	if request.method == 'POST':
		if request.data:
			#image = request.files['image']
			#print( image )
			#return json.dumps({'success': True}, 200, {'ContentType' : 'application/json'})
            res = app.response._class(
                response = json.dumps({'status': True}),
                status=200,
                mimetype='application/json'
            )
            return res
        


if __name__ == '__main__':
	app.run(debug = True, port = 5000)
