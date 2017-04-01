import soy
from random import random

class PlaneMesh(soy.meshes.Mesh) :
  def __init__(self, diffuse, specular) :
    mycol = soy.materials.Material()
    mycol.ambient = diffuse
    mycol.diffuse = diffuse
    mycol.specular = specular
    mycol.shininess = 5.0
    black = soy.materials.Material()
    black.ambient.hex = '#000'
    black.diffuse.hex = '#444'
    black.specular.hex = '#888'
    black.shininess = 5.0
    Vert = VertexGroup(self)

    # Create Faces
    # 2 Halves
    points = (Vert(0, (1, 1, 0), (1, 0, 0)),    # 0
              Vert(0, (1, 0, 0), (1, 0, 0)),    # 1
              Vert(0, (0, 1, 0), (1, 0, 0)),    # 2
              Vert(0, (0, 0, 0), (1, 0, 0)))
    faces = ([points[0], points[1], points[3]])
    faces.reverse()
    f = soy.atoms.Face(self, verts=faces, material=mycol)
    faces = ([points[0], points[3], points[2]])
    faces.reverse()
    f = soy.atoms.Face(self, verts=faces, material=mycol)


class VertexGroup :
  def __init__(self, mesh) :
    self.verts = {}
    self.mesh  = mesh

  def __call__(self, shift, coord, normal) :
    if   shift == 1 :
      coord = (coord[1], coord[2], coord[0])
      normal = (normal[1], normal[2], normal[0])
    elif shift == 2 :
      coord = (coord[2], coord[0], coord[1])
      normal = (normal[2], normal[0], normal[1])
    if not self.verts.has_key(coord) :
      self.verts[coord] = soy.atoms.Vertex(self.mesh, position=coord,
                                           normal=normal)
    return self.verts[coord]

def srand() :
  return random()-.5

def plane(sce):
  color = ((1.0, 1.0, 1.0), (0.0, 0.0, 0.0), ( 0,0,0))
  diffuse = soy.colors.Color(floats=color[0])
  specular = soy.colors.Color(floats=color[1])
  bmesh = PlaneMesh(diffuse, specular)
  plane = soy.bodies.Body(sce, mesh=bmesh, 
                                  position=color[2])
  plane.shape = soy.shapes.Box(1,1,1)
  t = -0.5
  return plane
