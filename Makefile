make:
	mkdir day$(day)
	cp template.py day$(day)/day$(day).py
	touch day$(day)/input.txt
	touch day$(day)/input_test.txt
	/usr/local/bin/python3 setup.py $(day)
	cd day$(day)