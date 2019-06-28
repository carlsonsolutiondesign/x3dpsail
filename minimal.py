import jnius_config
jnius_config.set_classpath('.', 'c:/Users/coderextreme/x3dpsail/X3DJSAIL.3.3.full.jar', '../../../../stylesheets/java/jars/X3DJSAIL.3.3.full.jar', './X3DJSAIL.3.3.full.jar')
from jnius import autoclass
TouchSensorObject = autoclass('org.web3d.x3d.jsail.PointingDeviceSensor.TouchSensorObject')
connectObject = autoclass('org.web3d.x3d.jsail.Core.connectObject')
ISObject = autoclass('org.web3d.x3d.jsail.Core.ISObject')
ProtoBodyObject = autoclass('org.web3d.x3d.jsail.Core.ProtoBodyObject')
