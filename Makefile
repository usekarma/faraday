.PHONY: check test
check:
	python3 scripts/validate.py
	python3 scripts/validate_context.py
	python3 -m unittest discover -s tests -v

test:
	python3 -m unittest discover -s tests -v
