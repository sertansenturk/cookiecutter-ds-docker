ARG SPHINX_VERSION
FROM sphinxdoc/sphinx:${SPHINX_VERSION}

ENV SPHINX_OPTS=

RUN useradd -ms /bin/bash sphinxuser && \
    chown -R sphinxuser /docs && \
    pip install sphinx_rtd_theme
USER sphinxuser

CMD make clean; make html SPHINXOPTS:=$SPHINX_OPTS