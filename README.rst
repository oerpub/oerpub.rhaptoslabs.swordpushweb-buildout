Buildout for development of the oerpub.rhaptoslabs.swordpushweb web app

Setup your system
=================

Installation is based on Ubuntu 10.04 or newer.

The installation of packages and setup of Libre-/OpenOffice and Tralics only need to be done once!

Install::

    sudo apt-get install git-core mercurial libxslt1.1 libxslt1-dev python-dev python-virtualenv python-lxml python-libxslt1 libtidy-0.99-0 blahtexml

For the LaTeX importer we need (this takes longer because it is about 2GB!)::

    sudo apt-get install g++ imagemagick python-imaging xsltproc texlive-full

For the Word/OpenOffice importer we need dependent on your Ubuntu version either LibreOffice (newer) or OpenOffice (older).

This should install either LibreOffice or OpenOffice on all Ubuntu versions::

    sudo apt-get install openoffice.org

Setup Libre-/OpenOffice
-----------------------

You need to copy the macro file Module1.xba to your Libre-/OpenOffice config folder from

https://github.com/jbeyers/oerpub.rhaptoslabs.swordpushweb/tree/develop/docs/office_macro

for OpenOffice, to::

    cp Module1.xba ~/.openoffice.org/3/user/basic/Standard/.

for LibreOffice, to::

    cp Module1.xba ~/.config/.libreoffice/3/user/basic/Standard/.


Setup Tralics (for LaTeX import)
--------------------------------

Please look at

https://github.com/therealmarv/oerpub.rhaptoslabs.tralics


For the LaTeX importer we need (this takes longer because it is about 2GB!)::

    sudo apt-get install g++ imagemagick python-imaging xsltproc texlive-full

For the Word/OpenOffice importer we need dependent on your Ubuntu version either LibreOffice (newer) or OpenOffice (older).

This should install either LibreOffice or OpenOffice on all Ubuntu versions::

    sudo apt-get install openoffice.org

Setup Libre-/OpenOffice
-----------------------

(TODO: needs instruction for placing the OOo-macros to the right place)

Setup Tralics (for LaTeX import)
--------------------------------

Please look at

https://github.com/therealmarv/oerpub.rhaptoslabs.tralics


Quick start:
============

To get the app going::

    git clone git://github.com/jbeyers/oerpub.rhaptoslabs.swordpushweb-buildout.git swordpushweb-buildout
    cd swordpushweb-buildout
    virtualenv --no-site-packages .
    ./bin/python bootstrap.py
    ./bin/buildout -Nvv
    ./dev.sh
    firefox http://localhost:6544/

Notes:
======

The instructions will give you read-only checkouts of the git repositories. The writeable repository links are in the dev.cfg file. If you have write access to al the repositories, just replace::

    ./bin/buildout -Nvv

with::
  
    ./bin/buildout -Nvvc dev.cfg

The port number is also different::

    firefox http://localhost:6543/

If you only have write access to some of them, just remove the lines mentioning the ones you have read-only access to from dev.config, and run::
  
    ./bin/buildout -Nvvc dev.cfg

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
