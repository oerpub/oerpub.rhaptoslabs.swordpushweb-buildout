OERPUB-REMIX is for importing, editing, and depositing educational documents, especially textbooks. The deposit 
protocol is based on SWORD and works with Connexions (cnx.org) currently. The application imports documents in Word, Open 
Office, LaTeX, Google Docs, or HTML format. Then an HTML5 editor, based on Aloha, is used to edit the documents. Finally, 
metadata is added, and then the document can be downloaded and saved locally, or uploaded to cnx.org for publishing as part
of an open textbook and educational resource library.

For more about the project as a whole (non technical) see our website: http://oerpub.org

Setup your system for development
=================
Buildout for development of the oerpub.rhaptoslabs.swordpushweb web application.

Installation is based on Ubuntu 10.04 or newer.

The installation of packages and setup of Libre-/OpenOffice and Tralics only need to be done once!

Install::

    sudo apt-get install git-core libxslt1.1 libxslt1-dev libcurl3-gnutls libcurl4-gnutls-dev librtmp-dev python-dev python-virtualenv libtidy-0.99-0 blahtexml jing mysql-server libmysqlclient-dev

The Word/OpenOffice importer depends on your Ubuntu version. You will either need LibreOffice (newer) or OpenOffice (older).

This should install either LibreOffice or OpenOffice on all Ubuntu versions::

    sudo apt-get install openoffice.org

Optional packages which you may need if you develop stuff locally::

    sudo apt-get install python-lxml python-libxslt1 python-imaging

Install of experimental HTML5 tidy-html for Ubuntu 12.04 x64 (needed)
---------------------------------------------------------------------

If you use Ubuntu 12.04 x64 version you can install it quite easily::

Add the following line to /etc/apt/sources.list::

    deb http://public.upfronthosting.co.za/debian/precise-amd64 /
    
Execute::

    sudo apt-get update
    sudo apt-get install tidy libtidy-0.99-0

Install of experimental HTML5 tidy-html for other Ubuntu (needed)
-----------------------------------------------------------------

If you use another Ubuntu and/or 32bit Ubuntu follow these steps::

    sudo apt-get install build-essential fakeroot
    git clone git://github.com/oerpub/tidy-html5.git
    cd tidy-html5
    dpkg-checkbuildeps

Install anything it lists using apt-get (and sudo). You should be doing the git checkout and then building as a non-root user.

Once you have it all installed, run::

    dpkg-buildpackage -b -uc -rfakeroot

When this process is done, assuming there are no errors, you will have a number of .deb files in the parent directory. 
These can be installed either directly with dpkg::

    dpkg -i tidy_20121113git-1_amd64.deb libtidy-0.99-0_20121113git-1_amd64.deb

or you can use the graphical package manager, which is generally a bit safer because it also handles dependency management (though there
should be no such issues, since you just built it on the same machine).

Watch out for the tidy-doc package. I have reports that its post-install script errors, but you don't need it anyway, it is no
different than the one that comes with your distro.

Setup Libre-/OpenOffice (needed for doc conversion)
---------------------------------------------------

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
    


LaTeX Tralics importer (optional)
---------------------------------

The LaTeX importer is optional. If you want to import LaTeX you will need the following packages.

These Ubuntu packages are necessary for the LaTeX importer (about 2GB!)::

    sudo apt-get install g++ imagemagick xsltproc texlive-full zlib1g-dev

Then compile and follow instructions for Tralics here:

https://github.com/oerpub/oerpub.rhaptoslabs.tralics


Production buildout:
====================

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

Development buildout for people with write access to OERPUB:
============================================================

The instructions below will give you writable checkouts of the git repositories. 
The writeable repository links are in the dev.cfg file. 
If you have write access to all the repositories make the buildout this way. 
If you only have write access to some of them, just remove the lines mentioning the ones you have read-only access to 
from dev.cfg::

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

The in-development packages are in the src directory. Each one of those is a self-contained git/hg repository. 
To get the newest code for all of them::

    ./bin/develop up

If you use the dev.cfg build, you get Fabric to help with deployment and updating on the server. 
fabfile.py holds the main commands, but you can add a fab_config.py to add different server contexts and commands 
without modifying the main fabfile. fab_config.py will be ignored by git. You would typically use it to set up an 
alternative to the qa server for your own testing. Typical usage of fabric:
:

    ./bin/fab -l
    ./bin/fab qa status pull stop start

For more info, see:

https://github.com/jbeyers/projecttools/blob/master/presentation/presentation.rst

http://fabfile.org
