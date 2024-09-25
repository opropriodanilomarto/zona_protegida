CMD=python manage.py

r:
	${CMD} runserver

t:
	${CMD} test

m:
	${CMD} migrate

mm:
	${CMD} makemigrations

s:
	${CMD} shell