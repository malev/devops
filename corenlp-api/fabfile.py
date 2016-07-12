from fabric.api import sudo, run, put, task


@task
def install_java():
    run('echo "java 8 installation"')
    sudo('apt-get install --yes python-software-properties')
    sudo('add-apt-repository ppa:webupd8team/java')
    sudo('apt-get update -qq')
    sudo('echo debconf shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections')
    sudo('echo debconf shared/accepted-oracle-license-v1-1 seen true | /usr/bin/debconf-set-selections')
    sudo('apt-get install --yes oracle-java8-installer')
    sudo('yes "" | apt-get -f install')


@task
def install_node():
    run('curl -sL https://deb.nodesource.com/setup_4.x -o nodesource_setup.sh')
    sudo('bash nodesource_setup.sh')
    sudo('apt-get install nodejs build-essential default-jdk -yq')


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
    sudo('sudo npm install -g forever')
    run('forever start bin/www')

@task
def install():
    install_java()
    install_node()
    install_corenlp()
    install_api()
