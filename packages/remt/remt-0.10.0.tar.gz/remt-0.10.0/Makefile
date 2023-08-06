.PHONY: doc doc-upload doc-clean test check
RSYNC=rsync -av \
	--exclude=\*~ --exclude=.\* \
	--delete-excluded --delete-after \
	--no-owner --no-group \
	--progress --stats

VERSION := $(shell grep '^version' setup.cfg | awk -F= '{gsub(/ /, "", $$2); print $$2}')

doc: .sphinx-stamp

doc-upload:
	$(RSYNC) build/doc/ wrobell@dcmod.org:~/public_html/remt

doc-clean:
	rm -rf build/doc build/latex

.sphinx-stamp:
	PYTHONPATH=. sphinx-build doc build/doc
	PYTHONPATH=. sphinx-build -b latex doc build/latex
	make -C build/latex
	cp build/latex/remt-$(VERSION).pdf build/doc

test:
	pytest

check:
	mypy --strict --implicit-reexport --scripts-are-modules bin/remt
	flake8 bin/remt remt
