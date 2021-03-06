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

"""Webpack integration for Flask."""

from .manifest import JinjaManifestLoader

WEBPACKEXT_MANIFEST_LOADER = JinjaManifestLoader
"""Manifest loader use to load manfest."""

WEBPACKEXT_MANIFEST_PATH = 'dist/manifest.json'
"""Path to manifest file relative to static folder."""

WEBPACKEXT_PROJECT = None
"""Webpack project."""

WEBPACKEXT_PROJECT_BUILDDIR = None
"""Directory where Webpack project should be copied to prior to build."""

WEBPACKEXT_PROJECT_DISTDIR = None
"""Directory where Webpack output files should be written to."""

WEBPACKEXT_PROJECT_DISTURL = None
"""URL path to where Webpack output files are accessible."""

WEBPACKEXT_STORAGE_CLS = None
"""Default storage class."""
