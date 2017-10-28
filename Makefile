test:
	python3 -m unittest
	coverage run test_rpn.py
	coverage report -m
	coverage-badge -o README.md

.PHONY: test
