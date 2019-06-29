import x3dpsail


X3D0 = (x3dpsail.X3D().setProfile("Immersive").setVersion("3.1")
      .setHead(x3dpsail.head()
        .addMeta(x3dpsail.meta().setContent("CleatClamp.MeshLab.x3d").setName(x3dpsail.SFString("title")))
        .addMeta(x3dpsail.meta().setContent("Generated from Meshlab X3D Exported").setName(x3dpsail.SFString("description")))
        .addMeta(x3dpsail.meta().setContent("19 June 2019").setName(x3dpsail.SFString("created")))
        .addMeta(x3dpsail.meta().setContent("Meshlab X3D Exported, http://meshlab.sourceforge.net").setName(x3dpsail.SFString("generator"))))
      .setScene(x3dpsail.Scene()
        .addChild(x3dpsail.Shape()
          .setGeometry(x3dpsail.IndexedFaceSet().setSolid(False)
            .setCoord(x3dpsail.Coordinate())))))

X3D0.toFileX3D("HelloWorldProgramOutput_MeshLabImport_RoundTrip.x3d")
