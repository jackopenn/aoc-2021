make:
	mkdir day$(day)
	cp template.py day$(day)/day$(day).py
	sed -i '' 's/input/day$(day)\/input/g' day$(day)/day$(day).py
	touch day$(day)/input
	touch day$(day)/input_test
	/usr/local/bin/python3 setup.py $(day)