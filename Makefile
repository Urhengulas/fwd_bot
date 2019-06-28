run:
	env/bin/python bot.py

dep:
	if [ ! -d "env" ];then virtualenv env;fi
	env/bin/pip install -r my-requirements.txt