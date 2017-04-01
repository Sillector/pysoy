#!/usr/bin/env python
import soy
import plane
from time import sleep

sce = soy.Scene()
cam = soy.bodies.Camera(sce)
cam.shape=soy.shapes.Sphere(2)
cam.position = (0.0, 0.0, 10.0)
lig = soy.bodies.lights.Light(sce)
lig.position = (-10.0,10.0,2.0)
m = soy.bodies.fields.Monopole(sce)
m.shape=soy.shapes.Sphere(15)
m.multiplier=.01
pl = plane.plane(sce)
fps = soy.textures.Print()

scr = soy.Screen()
win = soy.Window(scr, 'Moving Plane', background=soy.colors.Teal())
pro = soy.widgets.Projector(win, camera=cam)
can = soy.widgets.Canvas(win, texture=fps)
key = soy.controllers.Keyboard(win)
key['a'] = soy.actions.Force(pl, -100,    0,    0)
key['d'] = soy.actions.Force(pl,  100,    0,    0)
key['w'] = soy.actions.Force(pl,  0,    0,    -100)
key['s'] = soy.actions.Force(pl,    0, 0,    100)
wcn = soy.controllers.Window(win)
wcn['close'] = soy.actions.Quit()

if __name__ == '__main__' :
  while True:
    sleep(.1)
    if cam.fps:
      fps.text = '%sfps' % str(int(cam.fps)).zfill(4)
