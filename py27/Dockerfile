FROM ubuntu:14.04

RUN apt-get update
RUN apt-get install vim git-core wget gcc -y

WORKDIR /root
RUN wget https://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86_64.sh -q -O miniconda.sh
RUN chmod +x miniconda.sh
RUN ./miniconda.sh -b -p /root/miniconda2
ENV PATH=/root/miniconda2/bin:$PATH

RUN /root/miniconda2/bin/conda install anaconda-client conda-build anaconda-build -y
RUN /root/miniconda2/bin/conda install pill -c malev -y

RUN git config --global user.email "marcosvanetta@gmail.com"
RUN git config --global user.name "malev"
