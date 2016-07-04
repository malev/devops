FROM ubuntu:14.04
MAINTAINER marcosvanetta@gmail.com

RUN locale-gen en_US.UTF-8
RUN apt-get update -q
RUN apt-get install build-essential automake autoconf libtool wget -y -q
RUN apt-get install libboost-regex-dev libicu-dev zlib1g-dev \
                    libboost-system-dev libboost-program-options-dev \
                    libboost-thread-dev -y -q

WORKDIR /tmp
RUN wget https://github.com/TALP-UPC/FreeLing/releases/download/4.0/FreeLing-4.0.tar.gz -q

RUN tar xzvf FreeLing-4.0.tar.gz
WORKDIR /tmp/FreeLing-4.0
RUN autoreconf --install
RUN ./configure
RUN make
RUN make install
RUN rm -rf /tmp/freeling-4.0

EXPOSE 50005
ENV FREELINGSHARE /usr/local/share/freeling
CMD echo 'Hello world' | analyze -f $FREELINGSHARE/config/en.cfg | grep -c 'world world NN 1'
