install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

run:
	python main.py

# test:
# 	python -m pytest -vv --cov=mylib test_mathcode.py

# lint:
# 	pylint --disable=R,C mylib cli

# all: install lint test