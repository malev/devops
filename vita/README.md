# Vita toolchain Dockerfile

Your vita runs an ARM processor therefore you'll need to compile on an ARM
processor. That can be hard to find and can be very slow. You can also
compile in your laptop, but you'll need a toolchain. So far you have two
options:

  - prebuilt toolchain[1]
  - Compile the toolchain yourself[2]

Both process are quit complicated. That's why here I'm presenting a 3rd option:
Using a docker image with the toolchain and `vita-pack-vpk` already working on
it. You will need:

  - Docker installed on your laptop
  - ... that's it

There are hundreds of videos explaining how to install docker. Just google it
and you'll have it working. After you can run:

```
docker run -it malev/vita-toolchain bash
```

And you'll have an Ubuntu 14.04 with the toolchain installed in
`/usr/local/vitasdk` among other useful tools.

## VitaHelloWorld

```
git clone https://github.com/xerpi/vitahelloworld
docker run -it -v $PWD/vitahelloworld:/root/vitahelloworld malev/vita-toolchain bash
cd vitahelloworld
make all
```

And we will be able to see the package `vitahelloworld.vpk`.

## FTPVitaLib

```
git clone https://github.com/xerpi/ftpvitalib.git
docker run -it -v $PWD/ftpvitalib:/root/ftpvitalib malev/vita-toolchain bash
cd ftpvitalib/libftpvita
make install

cd ../sample/
make all
```

And again we will have `FTPVita.vpk` ready to go!

## References

[1] https://bintray.com/package/files/vitasdk/vitasdk/toolchain?order=desc&sort=fileLastModified&basePath=&tab=files
[2] https://github.com/vitasdk/buildscripts
