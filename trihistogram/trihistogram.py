#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# Olivier Devauchelle, 2024

from numpy import array, diff, cross
from collections import Counter

def triangle_area( T ) :
    '''
    A = triangle_area( T )

    Argument:
        T : matplotlib.tri.Triangulation object
    
    Output:
        A : the areas of the triangles of T
    '''

    A = []

    for triangle in T.triangles :

        u = diff( T.x[triangle] )
        v = diff( T.y[triangle] )

        A += [ abs( cross( u, v ) )/2 ]
    
    return A


def trihistogram2d( T, x, y, dist = False ) :
    '''
    H = trihistogram2d( T, x, y )

    Arguments:
        T : matplotlib.tri.Triangulation object
        x, y : lists of coordinates
        dist = False : whether to normalize with the triangle area

    Output:
        H: histogram
    '''

    indices = array( T.get_trifinder()( x, y ) )
    indices = indices[ indices >= 0 ] # -1 means in no triangle

    triangle_index, n = array( list( Counter( indices ).items() ) ).T
    
    H = array( [0]*len( T.triangles ) )
    H[triangle_index] = n

    if dist :
        H = H/array( triangle_area( T ) )
        H = H/len(x)

    return H



if __name__ == '__main__' :

    from pylab import *
    import matplotlib.tri as tri
    from numpy.random import normal

    theta = linspace(0,1,10)[:-1]*2*pi
    r = logspace( -1, 0, 6 )

    theta, r = meshgrid(theta, r)
    theta = theta.flatten()
    r = r.flatten()


    T = tri.Triangulation( [0] + list( r*cos(theta) ), [0] + list( r*sin(theta) ) ) 

    x, y = normal( scale = .4, size = (2,10000) )

    H = trihistogram2d( T, x, y, dist = True )
    tripcolor( T, H )
    # triplot( T, lw = .75, color = 'w', alpha = .3 )


    axis('equal')
    axis('off')
    show()