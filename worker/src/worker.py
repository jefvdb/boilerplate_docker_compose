# boilerplate worker
# Copyright (c) 2018 Jozef Van den broeck, All Rights Reserved
# -*- coding: utf-8 -+-
# vim: set ts=4 sw=4 noexpandtab :
from celery import Celery
from celery.utils.log import get_task_logger
from random import choice

app = Celery(broker='redis://queue')
l = get_task_logger(__name__)

@app.task(name='worker.frobble', bind=True)
def frobble(self, something):
	l.info("commencing frobble({0!r})".format(something))

	try:
		if choice([ True, False ]):
			l.error("frobble({0!r}) failed.".format(something))
			raise Exception
		else:
			l.info("frobble({0!r}) succeeded.".format(something))
	except Exception as e:
		self.retry(exc=e, countdown=5)
