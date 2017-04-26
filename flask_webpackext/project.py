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

"""Webpack project utilities for Flask-WebpackExt."""

from __future__ import absolute_import, print_function

from os.path import join

from flask import current_app
from flask.helpers import get_root_path
from pywebpack import WebpackBundleProject, WebpackTemplateProject

from .proxies import current_webpack


def flask_config():
    """Flask configuration injected in Webpack."""
    return {
        'build': {
            'debug': current_app.debug,
            'assetsPath': current_app.config['WEBPACKEXT_PROJECT_DISTDIR'],
            'assetsURL': current_app.config['WEBPACKEXT_PROJECT_DISTURL'],
            'staticPath': current_app.static_folder,
            'staticURL': current_app.static_url_path,
        }
    }


class WebpackProject(WebpackTemplateProject):
    """Flask webpack project."""

    def __init__(self, import_name, project_folder=None, config=None,
                 config_path=None,):
        super(WebpackProject, self).__init__(
            None,
            project_template=join(get_root_path(import_name), project_folder),
            config=config or flask_config,
            config_path=config_path,
        )

    @property
    def path(self):
        """Get path to project."""
        return current_app.config['WEBPACKEXT_PROJECT_BUILDDIR']

    @property
    def storage_cls(self):
        """Get storage class."""
        return current_webpack.storage_cls
