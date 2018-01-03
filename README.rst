simple demo of a minimial (non-)python package to install an R-based command line utility (in ``bin/``). in this case the util sets up an r package (using ``devtools``) but it could be anything...

make-rstudio-project
====================

Make an Rstudio project with R (requires ``R`` with ``devtools``).

::

    $ git clone <this repository>
    $ cd <this repository>
    $ pip install -e make_rstudio_project

then

::

    $ mkrproj --args mynewproj
