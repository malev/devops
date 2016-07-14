from fabric.api import sudo, run, put, task


@task
def install_java():
    run('echo "java 8 installation"')
    sudo('apt-get install --yes python-software-properties')
    sudo('add-apt-repository ppa:webupd8team/java')
    sudo('apt-get update -qq')
    sudo('echo debconf shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections')
    sudo('echo debconf shared/accepted-oracle-license-v1-1 seen true | /usr/bin/debconf-set-selections')
    sudo('echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | sudo /usr/bin/debconf-set-selections')
    sudo('apt-get install --yes oracle-java8-installer')
    sudo('update-java-alternatives -s java-8-oracle')
    sudo('apt-get install oracle-java8-set-default')
    sudo('yes "" | apt-get -f install')


@task
def install_node():
    run('curl -sL https://deb.nodesource.com/setup_4.x -o nodesource_setup.sh')
    sudo('bash nodesource_setup.sh')
    sudo('apt-get install nodejs build-essential -yq')


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


@task
def dockerize():
    # Docker
    sudo('apt-get install nginx -yq')
    sudo('rm /etc/nginx/sites-enabled/default')
    sudo('apt-get install apt-transport-https ca-certificates -yq')
    sudo('sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D')
    sudo('echo "deb https://apt.dockerproject.org/repo ubuntu-trusty main" > /etc/apt/sources.list.d/docker.list')
    sudo('apt-get update -yq')
    sudo('apt-get install docker-engine -yq')
    # Docker-compose
    sudo('apt-get install python-pip')
    sudo('pip install docker-compose')
    put('docker-compose.yml')
    
