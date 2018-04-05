# boilerplate flask_restful app
# Copyright (c) 2018 Jozef Van den broeck, All Rights Reserved
# -*- coding: utf-8 -+-
# vim: set ts=4 sw=4 noexpandtab :
from flask import Flask
from flask_restful import Api, Resource
from celery import Celery

app = Flask(__name__)
api = Api(app)

celery_app = Celery(broker='redis://queue')
frobble = celery_app.signature('worker.frobble')

class HelloResource(Resource):
	def get(self):
		frobble.delay('nonsense')
		return { 'hello' : 'there' }

api.add_resource(HelloResource, '/')

if __name__ == '__main__':
	app.run('0.0.0.0', port=8080, debug=True)
