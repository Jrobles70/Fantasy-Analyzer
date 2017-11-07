
INVENV = . env/bin/activate ;
   
PYVENV = python3 -m venv
env:
	$(PYVENV)  env
	($(INVENV) pip install -r requirements.txt )

install:  env  credentials

credentials:  memos/credentials.ini
memos/credentials.ini:
	echo "You just install the database and credentials.ini for it"

run:	env credentials
	$(INVENV) cd memos; python3 flask_main.py

trial:	env credentials
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




