deletetable:
	sh mylib/delete_table.sh
createtable:
	sh mylib/create_table.sh
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python test_main.py

format:	
	black *.py 

lint:
	ruff check mylib/*.py

		
all: install lint test format

