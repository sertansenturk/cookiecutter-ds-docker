FROM sphinxdoc/sphinx

RUN useradd -ms /bin/bash sphinxuser && \
    chown -R sphinxuser /docs 
USER sphinxuser
