import x3dpsail
(x3dpsail.ProtoBody()
# Initial node of ProtoBody determines prototype node type 
  .addChild(x3dpsail.TouchSensor().setDescription(x3dpsail.SFString("within ProtoBody"))
    .setIS(x3dpsail.IS()
      .addConnect(x3dpsail.connect()))))
