if [[ "${ENV}" == "ci" ]]; then
	pip install -r src/requirements-dev.txt
elif [[ "${ENV}" == "local" ]]; then
	poetry install
elif [[ "${ENV}" == "dev" ]]; then
	docker-compose up
fi