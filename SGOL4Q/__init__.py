# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SGOL4Q
                                 A QGIS plugin
 Plugin for managing SGOL layers in QGIS
                             -------------------
        begin                : 2017-06-17
        copyright            : (C) 2017 by Spatial Current, Inc.
        email                : patrick@spatialcurrent.io
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load SGOL4Q class from file SGOL4Q.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .sgol_qgis import SGOL4Q
    return SGOL4Q(iface)
