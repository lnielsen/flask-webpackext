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

"""CLI for Flask-WebpackExt."""

from __future__ import absolute_import, print_function

import click
from flask import current_app
from flask.cli import with_appcontext

from flask_webpackext import current_webpack


@click.group()
@with_appcontext
def webpack():
    """Webpack commands."""


@webpack.command()
@with_appcontext
def check():
    """Check if NPM and Webpack are installed."""


@webpack.command()
@with_appcontext
def create():
    """Create webpack project."""
    current_webpack.project.create()


@webpack.command()
@with_appcontext
def install():
    """Install webpack project assets."""


@webpack.command()
@with_appcontext
def build():
    """Build webpack project."""


@webpack.command()
@with_appcontext
def buildall():
    """Create, install and build webpack project."""


@webpack.command()
@with_appcontext
def run():
    """Run an NPM script."""
