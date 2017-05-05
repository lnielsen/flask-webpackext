# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2017 CERN.
#
# Invenio is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

"""Minimal Flask application example.

First install Flask-WebpackExt, create the instance folder and export
environment variables:

.. code-block:: console

   $ pip install -e .[all]
   $ cd examples
   $ mkdir instance
   $ export FLASK_APP=app.py FLASK_DEBUG=1

Next, install and build the assets with webpack:

.. code-block:: console

   $ flask webpack buildall

Start the development server:

.. code-block:: console

   $ flask run

and open the example application in your browser:

.. code-block:: console

    $ open http://127.0.0.1:5000/

To reset the example application run:

.. code-block:: console

    $ ./app-teardown.sh
"""

from __future__ import absolute_import, print_function

from flask import Flask, render_template

from flask_webpackext import FlaskWebpackExt, WebpackProject

# Create a Webpack project.
project = WebpackProject(
    __name__,
    project_folder='assets',
    config_path='build/config.json',
)

# Create Flask application
app = Flask(__name__, template_folder='templates')
app.config.update(dict(
    WEBPACKEXT_PROJECT=project,
    # WEBPACKEXT_STORAGE_CLS='pywebpack:LinkStorage',
))

# Initialize extension
FlaskWebpackExt(app)


# Basic view
@app.route('/')
def index():
    """Frontpage."""
    return render_template('index.html')
