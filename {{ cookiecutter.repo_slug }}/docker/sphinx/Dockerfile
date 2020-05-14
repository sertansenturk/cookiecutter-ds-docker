ARG SPHINX_VERSION
FROM sphinxdoc/sphinx:${SPHINX_VERSION}

ENV SPHINX_OPTS=

RUN useradd -ms /bin/bash sphinxuser && \
    mkdir /{{ cookiecutter.repo_slug }} && \
    chown -R sphinxuser /{{ cookiecutter.repo_slug }} && \
    pip install sphinx_rtd_theme
USER sphinxuser

WORKDIR /{{ cookiecutter.repo_slug }}/docs

CMD make clean; make html SPHINXOPTS:=$SPHINX_OPTS