test:
	python3 -m unittest
	coverage run test_rpn.py
	coverage report -m

.PHONY: test
