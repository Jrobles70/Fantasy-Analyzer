
INVENV = . env/bin/activate ;
   
PYVENV = python3 -m venv
env:
	$(PYVENV)  env
	($(INVENV) pip install -r requirements.txt )

install:  env  credentials

credentials:  credentials.py

run:	env
	$(INVENV) cd memos; python3 flask_main.py

trial:	env
	$(INVENV) cd memos; python3 db_trial.py

test:	env
	$(INVENV) nosetests

dist:	env
	$(INVENV) pip freeze >requirements.txt

clean:
	cd memos; rm -f *.pyc
	cd memos; rm -rf __pycache__

veryclean:
	make clean
	rm -rf env

update:
	python3 setupMake.py

server:
	./cloud_sql_proxy -instances="fantasyfootballanalyzer-185320:us-central1:fantasyfootball"=tcp:3306