mkfile_path := $(abspath $(lastword $(MAKEFILE_LIST)))
CURRENT_DIR := $(shell pwd)

ifndef NAME
  NAME = HttpServiceApp
endif

VIRTUALENV_DIR = $HttpServiceApp/.env
INTERPRETER = $(CURRENT_DIR)/$(VIRTUALENV_DIR)/bin/
PATH := ${PATH}:$(INTERPRETER)

help:
	@echo "Usage: $ make <target> [NAME=Flaskproject]"
	@echo " > create    : create flask project $HttpServiceApp"
	@echo " > deps      : install dependencies via pip"
	@echo " > serve     : Run app in dev environment"

create:
	@echo "[RUN]: create flask project"
	@mkdir -p $(CURRENT_DIR)/${NAME}/app/{templates,static/{images,css,js,public},controllers}
	echo "Flask==0.11.1\nFlask-SQLAlchemy==2.1\nFlask-Script==2.0.5\nFlask-Assets==0.12\nFlask-Cache==0.13.1\nFlask-DebugToolbar==0.10.0\ncssmin==0.2.0\njsmin==2.2.1" \
	> $(CURRENT_DIR)/$HttpServiceApp/requirements.txt
	make env

env:
	@echo "[RUN]: create/activate virtualenv"
	@virtualenv $(VIRTUALENV_DIR) && \
	. $(VIRTUALENV_DIR)/bin/activate && \
	make deps

deps:
	@echo "[RUN]: install dependentcies"
	$(VIRTUALENV_DIR)/bin/pip install -r $(CURRENT_DIR)/$HttpServiceApp/requirements.txt

serve:
	FLASK_APP=main.py pipenv run flask run