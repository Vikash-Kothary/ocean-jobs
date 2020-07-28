if [[ "${ENV}" == "local" ]]; then
	poetry install
elif [[ "${ENV}" == "dev" ]]; then
	docker-compose up
fi