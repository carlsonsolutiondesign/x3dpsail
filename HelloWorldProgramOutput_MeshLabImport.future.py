import x3dpsail as x3d


X3D0 = (x3d.X3D().setProfile("Immersive").setVersion("3.1")
      .setHead(x3d.head()
        .addMeta(x3d.meta().setContent("CleatClamp.MeshLab.x3d").setName(x3d.SFString("title")))
        .addMeta(x3d.meta().setContent("Generated from Meshlab X3D Exported").setName(x3d.SFString("description")))
        .addMeta(x3d.meta().setContent("19 June 2019").setName(x3d.SFString("created")))
        .addMeta(x3d.meta().setContent("Meshlab X3D Exported, http://meshlab.sourceforge.net").setName(x3d.SFString("generator"))))
      .setScene(x3d.Scene()
        .addChild(x3d.Shape()
          .setGeometry(x3d.IndexedFaceSet().setSolid(False)
            .setCoord(x3d.Coordinate())))))

X3D0.toFileX3D("HelloWorldProgramOutput_MeshLabImport_RoundTrip.x3d")
