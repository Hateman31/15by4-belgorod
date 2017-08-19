from flask import Flask, request, render_template, url_for, redirect, send_file, make_response
#import utils

from flask_restful import Resource, Api

app = Flask(__name__)
app.debug = True

api = Api(app)


@app.route('/')
def index():
        return render_template('index.html')

class demo(Resource):
	def get(self):
		return render_template('test.html')

api.add_resource(demo, '/demo')

if __name__ == '__main__':
    app.run()
