from fabric.api import task, sudo, run


@task
def _install_dependencies():
    sudo('apt-get update -qq')
    sudo('apt-get install unzip vim authbind -yq')


@task
def _install_java():
    sudo('apt-get install --yes python-software-properties')
    sudo('add-apt-repository ppa:webupd8team/java')
    sudo('apt-get update -qq')
    sudo('echo debconf shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections')
    sudo('echo debconf shared/accepted-oracle-license-v1-1 seen true | /usr/bin/debconf-set-selections')
    sudo('apt-get install --yes oracle-java8-installer')
    sudo('yes "" | apt-get -f install')


@task
def _install_corenlp():
    run('wget http://nlp.stanford.edu/software/stanford-corenlp-full-2015-12-09.zip -O stanford-corenlp-full.zip')
    run('wget http://nlp.stanford.edu/software/stanford-spanish-corenlp-2015-10-14-models.jar')
    run('unzip stanford-corenlp-full.zip')
    sudo('mv stanford-corenlp-full-2015-12-09 /opt/corenlp')
    sudo('mv stanford-spanish-corenlp-2015-10-14-models.jar /opt/corenlp/')
    sudo('adduser --disabled-password --gecos "" nlp')
    sudo('mkdir -p /etc/authbind/byport/')
    sudo('touch /etc/authbind/byport/80')
    sudo('chown nlp:nlp /etc/authbind/byport/80')
    sudo('chmod 600 /etc/authbind/byport/80')
    sudo('wget https://gist.githubusercontent.com/malev/02ea99a38c7a2d0551744f72f78b45ae/raw/f7c124ac359312f9ad1a4fe5777785d7e9625845/corenlp -O /etc/init.d/corenlp')
    sudo('chmod a+x /etc/init.d/corenlp')
    sudo('ln -s /etc/init.d/corenlp /etc/rc2.d/S75corenlp')
    sudo('service corenlp start')


@task
def install_corenlp():
    _install_dependencies()
    _install_java()
    _install_corenlp()


if __name__ == '__main__':
    print "Installing CoreNLP in Ubuntu"
    print "Run:"
    print "    fab -h root@DO-IP-ADDRESS install_corenlp"
    print "Enjoy!"
