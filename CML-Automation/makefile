runcmdC runcmdJ:
	@if [ -z "$(CMD)" ]; then echo "CMD variable must be set"; false; fi
	docker exec -t $(NSO) bash -lc 'echo -e "unhide debug\nunhide full\n$(CMD)" | ncs_cli --stop-on-error -$(subst runcmd,,$@)u admin'


loadconf:
	@if [ -z "$(FILE)" ]; then echo "FILE variable must be set"; false; fi
	@echo "Loading configuration $(FILE)"
	@docker exec -t $(NSO) bash -lc "mkdir -p /tmp/$(shell echo $(FILE) | xargs dirname)"
	@docker cp $(FILE) $(NSO):/tmp/$(FILE)
	@$(MAKE) runcmdJ CMD="configure\nload merge /tmp/$(FILE)\ncommit"