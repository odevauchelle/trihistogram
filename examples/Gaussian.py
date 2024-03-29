
from pylab import *
import matplotlib.tri as tri
from numpy.random import normal

sys.path.append('../')
import trihistogram as th

theta = linspace(0,1,10)[:-1]*2*pi
r = logspace( -1, 0, 6 )

theta, r = meshgrid(theta, r)
theta = theta.flatten()
r = r.flatten()


T = tri.Triangulation( [0] + list( r*cos(theta) ), [0] + list( r*sin(theta) ) ) 

x, y = normal( scale = .4, size = (2,10000) )

H = th.trihistogram2d( T, x, y )
print(H)

H = th.trihistogram2d( T, x, y, dist = True )


figure()

tripcolor( T, H )


axis('equal')
axis('off')

savefig('Gaussian.svg', bbox_inches = 'tight')

figure()

triplot( T, lw = .75, color = 'grey' )
axis('equal')
axis('off')

savefig('Gaussian_mesh.svg', bbox_inches = 'tight')

step = 100
plot( x[::step], y[::step], '.' )
savefig('Gaussian_mesh_data.svg', bbox_inches = 'tight')


show()
