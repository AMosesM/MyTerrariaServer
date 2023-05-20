export TERRARIA_VERSION = 1.4.4.9
export PYTHONDONTWRITEBYTECODE=1
export PORT=7778

# Docker
DOCKER_TAG:=${PROJECT}-${TERRARIA_VERSION}

.PHONY: localhost
localhost: export APP_HOME=${PWD}
localhost:
	python3 run_terraria_server.py

.PHONY: server
server:
	python3 download_terraria_server.py

.PHONY: build
build: server
	docker build  -t ${DOCKER_TAG} .

.PHONY: rm_container
rm_container:
	docker container stop ${DOCKER_TAG}
	docker rm ${DOCKER_TAG}
	
.PHONY: clean
clean: rm_container
	docker rmi ${DOCKER_TAG}

.PHONY: run
run:
	docker run --name ${DOCKER_TAG} -e PORT=${PORT} -e TERRARIA_VERSION=${TERRARIA_VERSION} -p ${PORT}:${PORT} ${DOCKER_TAG}
