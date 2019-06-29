import X3Dpackage


X3D0 = (X3Dpackage.X3D().setProfile("Immersive").setVersion("3.1")
      .setHead(X3Dpackage.head()
        .addMeta(X3Dpackage.meta().setContent("CleatClamp.MeshLab.x3d").setName("title"))
        .addMeta(X3Dpackage.meta().setContent("Generated from Meshlab X3D Exported").setName("description"))
        .addMeta(X3Dpackage.meta().setContent("19 June 2019").setName("created"))
        .addMeta(X3Dpackage.meta().setContent("Meshlab X3D Exported, http://meshlab.sourceforge.net").setName("generator")))
      .setScene(X3Dpackage.Scene()
        .addChildren(X3Dpackage.Shape()
          .setGeometry(X3Dpackage.IndexedFaceSet(setSolid = False)
            .setCoord(X3Dpackage.Coordinate())))))

