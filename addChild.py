import x3dpsail

X3D0 = (x3dpsail.X3D()
      .setScene(x3dpsail.Scene()
        .setChildren(x3dpsail.ViewpointGroup())
        .addChild(x3dpsail.NavigationInfo())))
