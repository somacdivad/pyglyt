test:
		flake8
		cd tests && flake8
		black --check .
