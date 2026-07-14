.PHONY: build deploy test clean

build:
	sam build

deploy:
	sam deploy --guided

test:
	python -m pytest tests/ -v

clean:
	rm -rf .aws-sam/
	python -m pipenv --rm 2>/dev/null || true
