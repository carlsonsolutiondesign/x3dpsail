import x3dpsail

(x3dpsail.ProtoBody()
    .addChild(x3dpsail.TouchSensor()
      .setIS(x3dpsail.IS()
        .addConnect(x3dpsail.connect()))))
