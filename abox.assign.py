from X3Dpackage import *
X3D0 = X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.3"

head1 = head()

meta2 = meta()
meta2.name = "title"
meta2.content = "abox.x3d"
head1.addMeta([meta2])

meta3 = meta()
meta3.name = "creator"
meta3.content = "John Carlson"
head1.addMeta([meta3])

meta4 = meta()
meta4.name = "generator"
meta4.content = "manual"
head1.addMeta([meta4])

meta5 = meta()
meta5.name = "identifier"
meta5.content = "https://coderextreme.net/X3DJSONLD/abox.x3d"
head1.addMeta([meta5])

meta6 = meta()
meta6.name = "description"
meta6.content = "a box"
head1.addMeta([meta6])
X3D0.head = head1

Scene7 = Scene()

ProtoDeclare8 = ProtoDeclare()
ProtoDeclare8.name = "anyShape"

ProtoInterface9 = ProtoInterface()

field10 = field()
field10.name = "myShape"
field10.accessType = "inputOutput"
field10.type = "MFNode"

Shape11 = Shape()

Sphere12 = Sphere()
Shape11.geometry = Sphere12
field10.addChildren([Shape11])
ProtoInterface9.addField([field10])
ProtoDeclare8.protoInterface = ProtoInterface9

ProtoBody13 = ProtoBody()

Transform14 = Transform()

IS15 = IS()

connect16 = connect()
connect16.nodeField = "children"
connect16.protoField = "myShape"
IS15.addConnect([connect16])
Transform14.IS = IS15
ProtoBody13.addChildren([Transform14])
ProtoDeclare8.protoBody = ProtoBody13
Scene7.addChildren([ProtoDeclare8])

ProtoDeclare17 = ProtoDeclare()
ProtoDeclare17.name = "one"

ProtoInterface18 = ProtoInterface()

field19 = field()
field19.name = "myShape"
field19.accessType = "inputOutput"
field19.type = "MFNode"

Shape20 = Shape()

Cylinder21 = Cylinder()
Shape20.geometry = Cylinder21
field19.addChildren([Shape20])
ProtoInterface18.addField([field19])
ProtoDeclare17.protoInterface = ProtoInterface18

ProtoBody22 = ProtoBody()

Transform23 = Transform()

ProtoInstance24 = ProtoInstance()
ProtoInstance24.name = "anyShape"

IS25 = IS()

connect26 = connect()
connect26.nodeField = "myShape"
connect26.protoField = "myShape"
IS25.addConnect([connect26])
ProtoInstance24.IS = IS25
Transform23.addChildren([ProtoInstance24])
ProtoBody22.addChildren([Transform23])
ProtoDeclare17.protoBody = ProtoBody22
Scene7.addChildren([ProtoDeclare17])

ProtoInstance27 = ProtoInstance()
ProtoInstance27.name = "one"

fieldValue28 = fieldValue()
fieldValue28.name = "myShape"

Shape29 = Shape()

Box30 = Box(size = [140,140,140])
Shape29.geometry = Box30
fieldValue28.addChildren([Shape29])
ProtoInstance27.addFieldValue([fieldValue28])
Scene7.addChildren([ProtoInstance27])
X3D0.scene = Scene7
