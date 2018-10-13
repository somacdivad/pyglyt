lint:
		flake8
		cd tests && flake8
		black --check .

test:
		pytest --cov pyglyt/
