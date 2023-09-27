ifneq (,$(wildcard ./.env))
    include .env
    export
endif

THIS_DIR := $(dir $(abspath $(firstword $(MAKEFILE_LIST))))
STREAMLIT_MAIN := Home.py
PATH_TO_BIN := venv/bin



run:  ## Runs the Streamlit application
	podman start steampipe-jira ||  podman run \
		-p 9193:9193 \
		-d \
		-e STEAMPIPE_DATABASE_PASSWORD="${STEAMPIPE_DATABASE_PASSWORD}" \
		-e JIRA_URL="${JIRA_URL}" \
		-e JIRA_PERSONAL_ACCESS_TOKEN="${JIRA_PERSONAL_ACCESS_TOKEN}" \
		-e JIRA_USER="${JIRA_USER}" \
		--name steampipe-jira \
		--rm \
		steampipe-jira service start --foreground

	${PATH_TO_BIN}/streamlit run \
		--server.headless 1 \
		--server.runOnSave 1 \
		$(STREAMLIT_MAIN)

help: ## Show this help screen
	@echo 'Usage: make <OPTIONS> ... <TARGETS>'
	@echo ''
	@echo 'Available targets are:'
	@echo ''
	@grep -E '^[ a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
	@echo ''
