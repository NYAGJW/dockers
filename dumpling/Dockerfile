FROM debian:stretch

# Step 1 - Prepare the dough for the dumpling.
# Install Python development tools, compilers, and build dependencies.
# unixodbc-dev is needed to build pyodbc.
# GDAL depends on specific versions of its C/C++ libraries, so just
# install the Debian package instead of building from source.
RUN apt-get update && apt-get install -y --no-install-recommends \
       g++ \
       gcc \
       python3-dev \
       python3-gdal \
       python3-pip \
       python3-setuptools \
       python3-wheel \
       unixodbc-dev \
       virtualenv \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create a symlink from python/pip to Python 3,
# since we are not using Python 2.
RUN ln -s ../../bin/python3 /usr/local/bin/python \
    && ln -s ../../bin/pip3 /usr/local/bin/pip

# Step 2 - Pack the dumpling with lots of veggies and steam it.
# Install lots of Python packages for data science.
RUN pip3 install --no-cache-dir \
        beautifulsoup4 \
        bokeh \
        civis \
        dash \
        emoji \
        Fiona \
        folium \
        fuzzywuzzy[speedup] \
        geopandas \
        jupyter_contrib_nbextensions \
        line_profiler \
        lxml \
        notebook \
        matplotlib \
        memory_profiler \
        nbdiff \
        neo4j-driver \
        nltk \
        numpy \
        pandas \
        pandas-datareader \
        pdfminer.six \
        Pillow \
        plotly \
        pre-commit \
        probablepeople \
        pyodbc \
        PyPDF2 \
        pyproj \
        requests \
        scikit-image \
        scikit-learn \
        scipy \
        scrapy \
        seaborn \
        shapely \
        six \
        sqlalchemy \
        sqlalchemy-redshift \
        statsmodels \
        tenacity \
        tensorflow \
        tox \
        unidecode \
        xmltodict \
    && true

# Step 3 - Add some dipping sauce to the dumpling.
# Install Debian packages for convenient CLI work.
RUN apt-get update && apt-get install -y --no-install-recommends \
       awscli \
       bash-completion \
       bc \
       cowsay \
       curl \
       dnsutils \
       git \
       ghostscript \
       gosu \
       host \
       htop \
       imagemagick \
       jq \
       less \
       lsof \
       man-db \
       nano \
       net-tools \
       openssh-client \
       p7zip-full \
       postgresql-client \
       procps \
       sudo \
       tree \
       vim \
       watch \
       wget \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Step 4 - Indulge in the dumpling.
# Enable sudo without a password.
# Modify bashrc to enable bash-completion and other savories.
# Enable git pull rebase autostash.
# TODO: colorify prompt and add git branch name to prompt.
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' > /etc/sudoers.d/nopasswd \
    && echo '. /usr/share/bash-completion/bash_completion' >> /etc/bash.bashrc \
    && echo '/usr/games/cowsay -f tux "Happy Coding!"' >> /etc/bash.bashrc
COPY gitconfig /etc/

# Step 5 - Serve the chopsticks.
# Use an entrypoint script to add users from host to the container.
COPY docker-entrypoint /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint
ENTRYPOINT ["docker-entrypoint"]
CMD ["bash"]
