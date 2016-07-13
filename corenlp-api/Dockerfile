FROM java:8

MAINTAINER Marcos Vanetta

WORKDIR /root
RUN wget http://nlp.stanford.edu/software/stanford-corenlp-full-2015-12-09.zip -q
RUN wget http://nlp.stanford.edu/software/stanford-spanish-corenlp-2015-10-14-models.jar -q
RUN wget https://github.com/malev/devops/archive/master.zip -q

# Install CoreNLP
RUN unzip stanford-corenlp-full-2015-12-09.zip
RUN mv stanford-corenlp-full-2015-12-09 corenlp
RUN mv stanford-spanish-corenlp-2015-10-14-models.jar corenlp/
RUN rm stanford-corenlp-full-2015-12-09.zip

# Installing Node 4.x
RUN wget https://deb.nodesource.com/setup_4.x -O nodesource_setup.sh -q
RUN bash nodesource_setup.sh
RUN apt-get install nodejs -yq
RUN rm nodesource_setup.sh

# Install API app
RUN apt-get install default-jdk build-essential -yq
RUN unzip master.zip
RUN mv devops-master/corenlp-api/ api
RUN rm master.zip
RUN rm -rf devops-master
ENV CORENLP_LOC /root/corenlp

# Run API server
WORKDIR /root/api
RUN npm install .
RUN npm install forever -g

CMD bin/www

