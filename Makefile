ROOT_DIR:=./
SRC_DIR:=./src
VENV_BIN_DIR:="venv/bin"

PIP:="$(VENV_BIN_DIR)/pip"
CMD_FROM_VENV:=". $(VENV_BIN_DIR)/activate, which"
PYTHON=$(shell "$(CMD_FROM_VENV)" "python")

define create-venv
virtualenv venv -p python3
endef

hello:
	@echo "Hello World!"

venv:
	@$(create-venv)
	$(PIP) install -r "$(ROOT_DIR/requirements.txt)"

run: venv
	@$(PYTHON) $(SRC_DIR)/main.py runserver