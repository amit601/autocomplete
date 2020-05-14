#################################

Hi this is readme document for task 3

1 --> build docker image
	docker build -t task3 .

2 --> run docker 
	docker run -dit task3 /bin/bash

3 --> get docker name
	docker ps -a  
	(Note the Container ID and name of ccontainer running from image task3 )

4 --> get docker console
	docker attach --detach-keys="ctrl-a,x" Name  ( from sterp 3 )

5 --> run redis server in background
	redis server &

6 --> run python main.py with arguments
	python main.py /add_word/word=foo
	python main.py /autocomplete/query=fo



Note :- Redis not starting inside container, thats the reason i am doing all this inside container.
	I am new to containers, not much familier with containers. In order to complete this task i learned a lot.

Thank you
Amit Kumar Yadav
