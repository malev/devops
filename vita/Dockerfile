FROM ubuntu:14.04
RUN apt-get update -qq
RUN apt-get install build-essential wget unzip curl git-core vim -yq
RUN apt-get install apt-src scons mingw32-runtime p7zip-full gawk gzip \
                    perl autoconf m4 automake libtool libncurses5-dev \
                    gettext gperf dejagnu expect tcl autogen guile-1.8 \
                    flex flip bison tofrodos texinfo g++ gcc-multilib \
                    libgmp3-dev libmpfr-dev debhelper texlive \
                    texlive-extra-utils zlib1g-dev pkg-config -yq
WORKDIR /root
RUN wget https://bintray.com/vitasdk/vitasdk/download_file?file_path=vitasdk-linux-nightly-c86e2b4b45bd9cad07abbbcb208519b0357a639a.tar.bz2 -O toolchain.tar.bz2
RUN tar xvjf toolchain.tar.bz2
RUN mv gcc-arm-vita-eabi-4_9-2016q3 /usr/local/vitasdk


ENV PATH /usr/local/vitasdk/bin/:$PATH
ENV VITASDK /usr/local/vitasdk

# Installing vita portlibs
RUN git clone https://github.com/xerpi/vita_portlibs
WORKDIR /root/vita_portlibs
RUN make

# Installing vita2dlib
WORKDIR /root
RUN git clone https://github.com/xerpi/vita2dlib.git
WORKDIR /root/vita2dlib/libvita2d
RUN sed -i 's_^CFLAGS .*_& -I$(VITASDK)/arm-vita-eabi/include/libpng16/_' Makefile
RUN make install

WORKDIR /root

# Installing libzip
RUN wget https://nih.at/libzip/libzip-1.1.3.tar.xz -q
RUN tar xf libzip-1.1.3.tar.xz
WORKDIR /root/libzip-1.1.3
RUN ./configure
RUN make
RUN make install
RUN apt-get install libzip-dev -yq

WORKDIR /root
RUN wget http://sprunge.us/UiaL -O vita-pack-vpk.c -q
RUN cc -o vita-pack-vpk vita-pack-vpk.c $(pkg-config --libs --cflags libzip)
RUN mv vita-pack-vpk $VITASDK/bin

# Cleanup

RUN rm /root/toolchain.tar.bz2
RUN rm -rf /root/vita_portlibs
RUN rm -rf /root/vita2dlib
RUN rm -rf /root/libzip-1.1.3
RUN rm libzip-1.1.3.tar.xz vita-pack-vpk.c
