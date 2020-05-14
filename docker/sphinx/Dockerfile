ARG SPHINX_VERSION
FROM sphinxdoc/sphinx:${SPHINX_VERSION}

ENV SPHINX_OPTS=

RUN useradd -ms /bin/bash sphinxuser && \
    mkdir /repo && \
    chown -R sphinxuser /repo && \
    pip install sphinx_rtd_theme
USER sphinxuser

WORKDIR /repo/docs

CMD make clean; make html SPHINXOPTS:=$SPHINX_OPTS
