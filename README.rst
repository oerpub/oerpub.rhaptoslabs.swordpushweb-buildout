OERPub is a SWORD based a document importer for Rhaptos and Connexions based installations.

more (non technical) info: http://oerpub.org


Buildout for development of the oerpub.rhaptoslabs.swordpushweb web app

Setup your system
=================

Installation is based on Ubuntu 10.04 or newer.

The installation of packages and setup of Libre-/OpenOffice and Tralics only need to be done once!

Install::

    sudo apt-get install git-core libxslt1.1 libxslt1-dev libcurl3-gnutls libcurl4-gnutls-dev librtmp-dev python-dev python-virtualenv libtidy-0.99-0 blahtexml jing mysql-server libmysqlclient-dev

For the Word/OpenOffice importer we need dependent on your Ubuntu version either LibreOffice (newer) or OpenOffice (older).

This should install either LibreOffice or OpenOffice on all Ubuntu versions::

    sudo apt-get install openoffice.org

Optional packages which you may need if you develop stuff locally::

    sudo apt-get install python-lxml python-libxslt1 python-imaging


Setup Libre-/OpenOffice
-----------------------

You need to copy the macro file Module1.xba to your Libre-/OpenOffice config folder from

https://github.com/oerpub/oerpub.rhaptoslabs.swordpushweb/tree/develop/docs/office_macro

to this OpenOffice subfolder (xxxx = libre/open)::

   .XXXXXXoffice/3/user/basic/Standard/.

To download that file from the web, be sure and use the "raw" link at the top right corner. 
Otherwise you might save something that has github web stuff mixed in.

You can find the openoffice config folder in your home directoy with::

   find ~ -name ".*office"

The openoffice config folder is in different places, depending on OpenOffice/LibreOffice's and Ubuntu's version.

Examples:

for OpenOffice to::

    cp Module1.xba ~/.openoffice.org/3/user/basic/Standard/.

for LibreOffice to::

    cp Module1.xba ~/.config/.libreoffice/3/user/basic/Standard/. 
OR::
    cp Module1.xba ~/.libreoffice/3/user/basic/Standard/.
    


LaTeX importer (Tralics)
------------------------

The LaTeX importer is optional. When you do now want to import LaTeX you do not need the following packages.

This Ubuntu packages are necessary for LaTeX importer (about 2GB!)::

    sudo apt-get install g++ imagemagick xsltproc texlive-full zlib1g-dev

Then compile and follow instructions for Tralics here:

https://github.com/oerpub/oerpub.rhaptoslabs.tralics


Quick start:
============

To get a readonly production buildout::

    git clone git://github.com/oerpub/oerpub.rhaptoslabs.swordpushweb-buildout.git oerpub-buildout
    cd oerpub-buildout
    virtualenv .
    ./bin/python bootstrap.py
    ./bin/buildout -Nv
    ./bin/easy_install -U distribute
    ./bin/buildout -Nv
    ./dev.sh
    firefox http://localhost:6543/

Dev Buildout:
=============

The instructions will give you read-only checkouts of the git repositories. The writeable repository links are in the dev.cfg file. If you have write access to all the repositories make the buildout this way. If you only have write access to some of them, just remove the lines mentioning the ones you have read-only access to from dev.cfg::

    git clone git://github.com/oerpub/oerpub.rhaptoslabs.swordpushweb-buildout.git oerpub-buildout
    cd oerpub-buildout
    virtualenv .
    ./bin/python bootstrap.py -v 1.5.2 -c dev.cfg
    ./bin/buildout -Nvc dev.cfg
    ./bin/easy_install -U distribute
    ./bin/buildout -Nvc dev.cfg
    ./dev.sh
    firefox http://localhost:6543/

Nice-to-haves:
==============

The in-development packages are in the src directory. Each one of those is a self-contained git/hg repository. To get the newest code for all of them::

    ./bin/develop up

If you use the dev.cfg build, you get Fabric to help with deployment and updating on the server. fabfile.py holds the main commands, but you can add a fab_config.py to add different server contexts and commands without modifying the main fabfile. fab_config.py will be ignored by git. You would typically use it to set up an alternative to the qa server for your own testing. Typical usage of fabric:
:

    ./bin/fab -l
    ./bin/fab qa status pull stop start

For more info, see:

https://github.com/jbeyers/projecttools/blob/master/presentation/presentation.rst

http://fabfile.org
