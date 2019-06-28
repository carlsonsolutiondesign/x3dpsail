import x3dpsail
X3D0 = x3dpsail.X3D()
X3D0.setProfile("Immersive")
X3D0.setVersion("3.1")
head1 = x3dpsail.head()
meta2 = x3dpsail.meta()
meta2.setContent("CleatClamp.MeshLab.x3d")
meta2.setName("title")

head1.addMeta(meta2)
meta3 = x3dpsail.meta()
meta3.setContent("Generated from Meshlab X3D Exported")
meta3.setName("description")

head1.addMeta(meta3)
meta4 = x3dpsail.meta()
meta4.setContent("19 June 2019")
meta4.setName("created")

head1.addMeta(meta4)
meta5 = x3dpsail.meta()
meta5.setContent("Meshlab X3D Exported, http://meshlab.sourceforge.net")
meta5.setName("generator")

head1.addMeta(meta5)

X3D0.setHead(head1)
Scene6 = x3dpsail.Scene()
Shape7 = x3dpsail.Shape()
IndexedFaceSet8 = x3dpsail.IndexedFaceSet()
IndexedFaceSet8.setSolid(False)
Coordinate9 = x3dpsail.Coordinate()

IndexedFaceSet8.setCoord(Coordinate9)

Shape7.setGeometry(IndexedFaceSet8)

Scene6.addChildren(Shape7)

X3D0.setScene(Scene6)
X3D0.toFileX3D("HelloWorldProgramOutput_MeshLabImport_RoundTrip.x3d")
