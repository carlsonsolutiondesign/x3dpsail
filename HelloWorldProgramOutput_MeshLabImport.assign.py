from X3Dpackage import *
X3D0 = X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.1"

head1 = head()

meta2 = meta()
meta2.content = "CleatClamp.MeshLab.x3d"
meta2.name = "title"
head1.addMeta([meta2])

meta3 = meta()
meta3.content = "Generated from Meshlab X3D Exported"
meta3.name = "description"
head1.addMeta([meta3])

meta4 = meta()
meta4.content = "19 June 2019"
meta4.name = "created"
head1.addMeta([meta4])

meta5 = meta()
meta5.content = "Meshlab X3D Exported, http://meshlab.sourceforge.net"
meta5.name = "generator"
head1.addMeta([meta5])
X3D0.head = head1

Scene6 = Scene()

Shape7 = Shape()

IndexedFaceSet8 = IndexedFaceSet(solid = False)

Coordinate9 = Coordinate()
IndexedFaceSet8.coord = Coordinate9
Shape7.geometry = IndexedFaceSet8
Scene6.addChildren([Shape7])
X3D0.scene = Scene6
