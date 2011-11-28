clean:
	find . -name "*.pyc" -exec rm -rf {} \;
	find . -name "*.pyo" -exec rm -rf {} \;
	find . -name "*~" -exec rm -rf {} \;
	find . -name "#*" -exec rm -rf {} \;
