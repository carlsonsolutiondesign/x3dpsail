import x3dpsail


X3D0 = (x3dpsail.X3D().setProfile(x3dpsail.SFString("Immersive")).setVersion(x3dpsail.SFString("3.1"))
      .setHead(x3dpsail.head()
        .addMeta(x3dpsail.meta().setContent(x3dpsail.SFString("CleatClamp.MeshLab.x3d")).setName(x3dpsail.SFString("title")))
        .addMeta(x3dpsail.meta().setContent(x3dpsail.SFString("Generated from Meshlab X3D Exported")).setName(x3dpsail.SFString("description")))
        .addMeta(x3dpsail.meta().setContent(x3dpsail.SFString("19 June 2019")).setName(x3dpsail.SFString("created")))
        .addMeta(x3dpsail.meta().setContent(x3dpsail.SFString("Meshlab X3D Exported, http://meshlab.sourceforge.net")).setName(x3dpsail.SFString("generator"))))
      .setScene(x3dpsail.Scene()
        .addChild(x3dpsail.Shape()
          .setGeometry(x3dpsail.IndexedFaceSet().setSolid(x3dpsail.SFBool(False))
            .setCoord(x3dpsail.Coordinate())))))

X3D0.toFileX3D("HelloWorldProgramOutput_MeshLabImport_RoundTrip.x3d")
