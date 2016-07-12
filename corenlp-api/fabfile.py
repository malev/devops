from fabric.api import sudo, run, put, task


@task
def install_java():
    sudo('echo "java 8 installation"')
    run('wget https://s3-us-west-2.amazonaws.com/data.codingnews.info/jre-8u91-linux-x64.tar.gz')
    sudo('tar xvzf jre-8u91-linux-x64.tar.gz')
    sudo('mv jre1.8.0_91 /usr/java')
    sudo('ln -s /usr/java/bin/java /usr/bin/java')


@task
def install_node():
    run('curl -sL https://deb.nodesource.com/setup_4.x -o nodesource_setup.sh')
    sudo('bash nodesource_setup.sh')
    sudo('apt-get install build-essential default-jdk -yq')


@task
def install_corenlp():
    sudo('apt-get install unzip -yq')
    run('wget http://nlp.stanford.edu/software/stanford-corenlp-full-2015-12-09.zip -O corenlp.zip')
    run('wget http://nlp.stanford.edu/software/stanford-spanish-corenlp-2015-10-14-models.jar')
    run('unzip corenlp')
    run('mv stanford-corenlp-full-2015-12-09 corenlp')
    run('mv stanford-spanish-corenlp-2015-10-14-models.jar corenlp/')


@task
def install_api():
    put('api', '~')
    put('bin', '~')
    put('app.js', '~')
    put('package.json', '~')
    put('StanfordCoreNLP-spanish.properties', '~')
    run('npm install .')
    sudo('npm install -g forever')
    run('forever start bin/www')

@task
def install():
    install_java()
    install_node()
    install_corenlp()
    install_api()
