PACKAGE_NAME = markdocs
BINARY_NAME = $(PACKAGE_NAME)
INSTALL_DIR = $(HOME)/.local/bin
VENV_DIR = venv

all: build

build:
	$(VENV_DIR)/bin/pyinstaller --onefile --name=$(BINARY_NAME) main.py
	mv dist/$(BINARY_NAME) .

venv:
	python3 -m venv $(VENV_DIR)
	$(VENV_DIR)/bin/python -m pip install pyinstaller
	$(VENV_DIR)/bin/python -m pip install -r requirements.txt

install: build
	install -m 755 $(BINARY_NAME) $(INSTALL_DIR)/$(BINARY_NAME)

uninstall:
	rm -f $(INSTALL_DIR)/$(BINARY_NAME)

clean:
	rm -rf build/ dist/ __pycache__ *.spec $(BINARY_NAME)

lean:
	@echo -e "\e[1;35m💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜\e[0m"
	@echo -e "\e[1;35m💜💜💜💜💜💜💜💜I LOVE LEAN!!!💜💜💜💜💜💜💜💜💜\e[0m"
	@echo -e "\e[1;35m💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜\e[0m"
	@echo -e "\e[1;35m💜I'M ON 'EM BEANS FOR REAL (YEH, YEAH, YEAH)💜\e[0m"
	@echo -e "\e[1;35m💜I'M ON THE LEAN FOR REAL (WHAT? YEAH, YEAH)💜\e[0m"
	@echo -e "\e[1;35m💜I'M ON 'EM BEANS FOR REAL (YEA, YEAH, YEAH)💜\e[0m"
	@echo -e "\e[1;35m💜💜💜I'M ON THE LEAN FOR REAL (YEAH-YEAH)💜💜💜\e[0m"
	@echo -e "\e[1;35m💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜\e[0m"
	@exit 1

.PHONY: all build install uninstall clean lean
