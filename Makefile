export TERRARIA_VERSION = 1.4.4.9
export PYTHONDONTWRITEBYTECODE=1
export PORT=7777

# Google Cloud
LOCATION:=us-central1
PROJECT:=myterrariaserver
REPOSITORY:=cloud-run-source-deploy
IMAGE:=my-terraria-server

# Docker
DOCKER_TAG:=${PROJECT}-${TERRARIA_VERSION}

.PHONY: gcloud
gcloud:
	gcloud run deploy ${IMAGE} --allow-unauthenticated --source .

.PHONY: gclean
gclean:
	gcloud run services delete ${IMAGE} --quiet
	gcloud artifacts docker images delete ${LOCATION}-docker.pkg.dev/${PROJECT}/${REPOSITORY}/${IMAGE} --delete-tags --quiet

.PHONY: reload
reload: gclean gcloud
	echo done.

.PHONY: reqs
reqs:
	python3 -m pip install -r requirements.txt

.PHONY: localhost
localhost: export APP_HOME=${PWD}
localhost:
	python3 run_terraria_server.py

.PHONY: server
server:
	python3 download_terraria_server.py

.PHONY: build
build: server
	docker build -t ${DOCKER_TAG} .

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