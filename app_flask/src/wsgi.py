# boilerplate flask_restful app
# Copyright (c) 2018 Jozef Van den broeck, All Rights Reserved
# -*- coding: utf-8 -+-
# vim: set ts=4 sw=4 noexpandtab :
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class HelloResource(Resource):
	def get(self):
		return { 'hello' : 'there' }

api.add_resource(HelloResource, '/')

if __name__ == '__main__':
	app.run('0.0.0.0', port=8080, debug=True)
