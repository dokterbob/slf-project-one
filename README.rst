slf-project-one
===============

Demonstration project for SLF Python workshop.

Installing
----------
Several options are available:

1. Install straight from GitHub::

       pip install git+https://github.com/dokterbob/slf-project-one.git#egg=slf-project-one

2. Clone from GitHub, then install in an editable way (so that code changes
   are active without reinstalling)::

       git clone git@github.com:dokterbob/slf-project-one.git
       pip install -e slf-project-one

Usage
-----
During installation, a `project_one` command is available on your system, see
`setup.py` for more information. This command requires a single `data_file`
parameter, pointing to the path of `data.txt` (usually it is wise to keep
data files out of version control).

Example (run from `slf-project-one` directory)::

    project_one project_one/data.txt
