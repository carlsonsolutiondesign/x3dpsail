from X3Dpackage import *
X3D0 = X3D(profile="Immersive", version="3.3",    head1 = head(    meta2 = meta(name="title", content="abox.x3d"), 
    meta3 = meta(name="creator", content="John Carlson"), 
    meta4 = meta(name="generator", content="manual"), 
    meta5 = meta(name="identifier", content="https://coderextreme.net/X3DJSONLD/abox.x3d"), 
    meta6 = meta(name="description", content="a box")), 
   Scene7 = Scene(    ProtoDeclare8 = ProtoDeclare(name="anyShape",      ProtoInterface9 = ProtoInterface(      field10 = field(name="myShape", accessType="inputOutput", type="MFNode",        Shape11 = Shape(        Sphere12 = Sphere()))), 
     ProtoBody13 = ProtoBody(      Transform14 = Transform(       IS15 = IS(        connect16 = connect(nodeField="children", protoField="myShape"))))), 
    ProtoDeclare17 = ProtoDeclare(name="one",      ProtoInterface18 = ProtoInterface(      field19 = field(name="myShape", accessType="inputOutput", type="MFNode",        Shape20 = Shape(        Cylinder21 = Cylinder()))), 
     ProtoBody22 = ProtoBody(      Transform23 = Transform(       ProtoInstance24 = ProtoInstance(name="anyShape",         IS25 = IS(         connect26 = connect(nodeField="myShape", protoField="myShape")))))), 
    ProtoInstance27 = ProtoInstance(name="one",      fieldValue28 = fieldValue(name="myShape",       Shape29 = Shape(       Box30 = Box(size=[140,140,140]))))))
