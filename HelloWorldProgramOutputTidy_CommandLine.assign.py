from X3Dpackage import *
X3D0 = X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.3"
# x3dVersionComparisonTest for this model: supportsX3dVersion(X3DObject.VERSION_3_0)=true 

head1 = head()
# comment #1 
# comment #2 
# comment #3 
# comment #4 

component2 = component()
component2.level = 3
component2.name = "Navigation"
head1.addComponent([component2])

component3 = component()
component3.level = 1
component3.name = "Layering"
head1.addComponent([component3])

component4 = component()
component4.level = 1
component4.name = "Shaders"
head1.addComponent([component4])

component5 = component()
component5.level = 2
component5.name = "CADGeometry"
head1.addComponent([component5])

component6 = component()
component6.level = 2
component6.name = "DIS"
head1.addComponent([component6])

component7 = component()
component7.level = 1
component7.name = "H-Anim"
head1.addComponent([component7])

unit8 = unit(category = "angle")
unit8.conversionFactor = 1.0
unit8.name = "AngleUnitConversion"
head1.addUnit([unit8])

unit9 = unit(category = "length")
unit9.conversionFactor = 1.0
unit9.name = "LengthUnitConversion"
head1.addUnit([unit9])

unit10 = unit(category = "force")
unit10.conversionFactor = 4.4482
unit10.name = "ForceFromPoundsToNewtons"
head1.addUnit([unit10])

meta11 = meta()
meta11.content = "HelloWorldProgramOutput.x3d"
meta11.name = "title"
head1.addMeta([meta11])

meta12 = meta()
meta12.content = "continued development and testing in progress"
meta12.name = "info"
head1.addMeta([meta12])

meta13 = meta()
meta13.content = "Example HelloWorldProgram creates an X3D model using the X3D Java Scene Access Interface Library (X3DJSAIL)"
meta13.name = "description"
head1.addMeta([meta13])

meta14 = meta()
meta14.content = "http://www.web3d.org/specifications/java/X3DJSAIL.html"
meta14.name = "reference"
head1.addMeta([meta14])

meta15 = meta()
meta15.content = "HelloWorldProgramOutput.java"
meta15.name = "generator"
head1.addMeta([meta15])

meta16 = meta()
meta16.content = "6 September 2016"
meta16.name = "created"
head1.addMeta([meta16])

meta17 = meta()
meta17.content = "19 June 2019"
meta17.name = "modified"
head1.addMeta([meta17])

meta18 = meta()
meta18.content = "X3D Java Scene Access Interface Library (X3DJSAIL)"
meta18.name = "generator"
head1.addMeta([meta18])

meta19 = meta()
meta19.content = "http://www.web3d.org/specifications/java/examples/HelloWorldProgram.java"
meta19.name = "generator"
head1.addMeta([meta19])

meta20 = meta()
meta20.content = "Netbeans http://www.netbeans.org"
meta20.name = "generator"
head1.addMeta([meta20])

meta21 = meta()
meta21.content = "Don Brutzman"
meta21.name = "creator"
head1.addMeta([meta21])

meta22 = meta()
meta22.content = "https://sourceforge.net/p/x3d/code/HEAD/tree/www.web3d.org/x3d/stylesheets/java/examples/HelloWorldProgramOutput.x3d"
meta22.name = "reference"
head1.addMeta([meta22])

meta23 = meta()
meta23.content = "Console output, ClassicVRML encoding, VRML97 encoding and pretty-print documentation:"
meta23.name = "reference"
head1.addMeta([meta23])

meta24 = meta()
meta24.content = "HelloWorldProgramOutput.txt"
meta24.name = "reference"
head1.addMeta([meta24])

meta25 = meta()
meta25.content = "HelloWorldProgramOutput.x3dv"
meta25.name = "reference"
head1.addMeta([meta25])

meta26 = meta()
meta26.content = "HelloWorldProgramOutput.wrl"
meta26.name = "reference"
head1.addMeta([meta26])

meta27 = meta()
meta27.content = "HelloWorldProgramOutput.html"
meta27.name = "reference"
head1.addMeta([meta27])

meta28 = meta()
meta28.content = "https://savage.nps.edu/X3dValidator?url=http://www.web3d.org/specifications/java/examples/HelloWorldProgramOutput.x3d"
meta28.name = "reference"
head1.addMeta([meta28])

meta29 = meta()
meta29.content = "http://www.web3d.org/specifications/java/examples/HelloWorldProgramOutput.x3d"
meta29.name = "identifier"
head1.addMeta([meta29])

meta30 = meta()
meta30.content = "../license.html"
meta30.name = "license"
head1.addMeta([meta30])
X3D0.head = head1

Scene31 = Scene()

ViewpointGroup32 = ViewpointGroup()
ViewpointGroup32.description = "Available viewpoints"

Viewpoint33 = Viewpoint()
Viewpoint33.DEF = "DefaultView"
Viewpoint33.description = "Hello X3DJSAIL"
ViewpointGroup32.addChildren([Viewpoint33])

Viewpoint34 = Viewpoint()
Viewpoint34.DEF = "TopDownView"
Viewpoint34.position = [0,100,0]
Viewpoint34.orientation = [1,0,0,-1.570796]
Viewpoint34.description = "top-down view from above"
ViewpointGroup32.addChildren([Viewpoint34])
Scene31.children = ViewpointGroup32

NavigationInfo35 = NavigationInfo()
NavigationInfo35.type = ["EXAMINE","FLY","ANY"]
Scene31.addChildren([NavigationInfo35])

WorldInfo36 = WorldInfo()
WorldInfo36.DEF = "WorldInfoDEF"
WorldInfo36.title = "HelloWorldProgram produced by X3D Java SAI Library (X3DJSAIL)"
Scene31.addChildren([WorldInfo36])

WorldInfo37 = WorldInfo()
WorldInfo37.USE = "WorldInfoDEF"
Scene31.addChildren([WorldInfo37])

WorldInfo38 = WorldInfo()
WorldInfo38.USE = "WorldInfoDEF"
Scene31.addChildren([WorldInfo38])

MetadataString39 = MetadataString()
MetadataString39.DEF = "scene.addChildMetadata"
MetadataString39.value = ["Top-level root Metadata node beneath Scene needs to be one of '-children' in JSON encoding"]
MetadataString39.name = "test"
Scene31.metadata = MetadataString39

LayerSet40 = LayerSet()
LayerSet40.DEF = "scene.addChildLayerSetTest"
Scene31.children = LayerSet40

Transform41 = Transform()
Transform41.DEF = "LogoGeometryTransform"
Transform41.translation = [0,1.5,0]

Anchor42 = Anchor()
Anchor42.description = "select for X3D Java SAI Library (X3DJSAIL) description"
Anchor42.url = ["../X3DJSAIL.html","http://www.web3d.org/specifications/java/X3DJSAIL.html"]

Shape43 = Shape()
Shape43.DEF = "BoxShape"

Appearance44 = Appearance()

Material45 = Material()
Material45.DEF = "GreenMaterial"
Material45.diffuseColor = [0,1,1]
Material45.transparency = 0.1
Material45.emissiveColor = [0.8,0,0]
Appearance44.material = Material45

ImageTexture46 = ImageTexture()
ImageTexture46.url = ["images/X3dJavaSceneAccessInterfaceSaiLibrary.png","http://www.web3d.org/specifications/java/examples/images/X3dJavaSceneAccessInterfaceSaiLibrary.png"]
Appearance44.texture = ImageTexture46
Shape43.appearance = Appearance44

Box47 = Box()
Box47.DEF = "test-NMTOKEN_regex.0123456789"
Box47.class_ = "untextured"
Shape43.geometry = Box47
Anchor42.addChildren([Shape43])
Transform41.addChildren([Anchor42])
Scene31.addChildren([Transform41])

Shape48 = Shape()
Shape48.DEF = "LineShape"

Appearance49 = Appearance()

Material50 = Material()
Material50.emissiveColor = [0.6,0.19607843,0.8]
Appearance49.material = Material50
Shape48.appearance = Appearance49

IndexedLineSet51 = IndexedLineSet(coordIndex = [0,1,2,3,4,0])
# Coordinate 3-tuple point count: 6 

Coordinate52 = Coordinate()
Coordinate52.point = [0,1.5,0,2,1.5,0,2,1.5,-2,-2,1.5,-2,-2,1.5,0,0,1.5,0]
IndexedLineSet51.coord = Coordinate52
Shape48.geometry = IndexedLineSet51
Scene31.addChildren([Shape48])

PositionInterpolator53 = PositionInterpolator()
PositionInterpolator53.DEF = "BoxPathAnimator"
PositionInterpolator53.key = [0,0.125,0.375,0.625,0.875,1]
PositionInterpolator53.keyValue = [0,1.5,0,2,1.5,0,2,1.5,-2,-2,1.5,-2,-2,1.5,0,0,1.5,0]
Scene31.addChildren([PositionInterpolator53])

TimeSensor54 = TimeSensor()
TimeSensor54.DEF = "OrbitClock"
TimeSensor54.cycleInterval = 8.0
TimeSensor54.loop = True
Scene31.addChildren([TimeSensor54])

ROUTE55 = ROUTE()
ROUTE55.fromField = "fraction_changed"
ROUTE55.fromNode = "OrbitClock"
ROUTE55.toField = "set_fraction"
ROUTE55.toNode = "BoxPathAnimator"
Scene31.addChildren([ROUTE55])

ROUTE56 = ROUTE()
ROUTE56.fromField = "value_changed"
ROUTE56.fromNode = "BoxPathAnimator"
ROUTE56.toField = "set_translation"
ROUTE56.toNode = "LogoGeometryTransform"
Scene31.addChildren([ROUTE56])

Transform57 = Transform()
Transform57.DEF = "TextTransform"
Transform57.translation = [0,-1.5,0]

Shape58 = Shape()

Appearance59 = Appearance()

Material60 = Material()
Material60.USE = "GreenMaterial"
Appearance59.material = Material60
Shape58.appearance = Appearance59

Text61 = Text()
Text61.string = ["X3D Java","SAI Library","X3DJSAIL"]
# Comment example A, plain quotation marks: He said, \"Immel did it!\" 
# Comment example B, XML character entities: He said, &quot;Immel did it!&quot; 

MetadataSet62 = MetadataSet()
MetadataSet62.name = "EscapedQuotationMarksMetadataSet"

MetadataString63 = MetadataString()
MetadataString63.value = ["MFString example C, backslash-escaped quotes: He said, \"Immel did it!\""]
MetadataString63.name = "quotesTestC"
MetadataSet62.value = MetadataString63

MetadataString64 = MetadataString()
MetadataString64.value = ["checks MetadataSetObject addValue() method"]
MetadataString64.name = "extraChildTest"
MetadataSet62.value = MetadataString64
Text61.metadata = MetadataSet62

FontStyle65 = FontStyle(justify = ["MIDDLE","MIDDLE"])
Text61.fontStyle = FontStyle65
Shape58.geometry = Text61
Transform57.addChildren([Shape58])

Collision66 = Collision()
# test containerField='proxy' 

Shape67 = Shape()
Shape67.DEF = "ProxyShape"
# alternative XML encoding: Text string='\"One, Two, Comment\" \"\" \"He said, \\&quot;Immel did it!\\&quot;\"' 
# alternative XML encoding: Text string='\"One, Two, Comment\" \"\" \"He said, \\&quot;Immel did it!\\&quot;\" \"\"' 
# alternative Java source: .setString(new String [] {\"One, Two, Comment\", \"\", \"He said, \\\"Immel did it!\\\"\"}) 
# reference: http://www.web3d.org/x3d/content/examples/Basic/X3dSpecifications/StringArrayEncodingExamplesIndex.html 

Text68 = Text()
Text68.string = ["One, Two, Text","","He said, \"Immel did it!\" \"\""]
Shape67.geometry = Text68
Collision66.proxy = Shape67
Transform57.addChildren([Collision66])
# It's a beautiful world 
# ... for you! 
# https://en.wikipedia.org/wiki/Beautiful_World_(Devo_song) 
Scene31.addChildren([Transform57])
# repeatedly spin 180 degrees as a readable special effect 

OrientationInterpolator69 = OrientationInterpolator()
OrientationInterpolator69.DEF = "SpinInterpolator"
OrientationInterpolator69.key = [0,0.5,1]
OrientationInterpolator69.keyValue = [0,1,0,4.712389,0,1,0,0,0,1,0,1.5707964]
Scene31.addChildren([OrientationInterpolator69])

TimeSensor70 = TimeSensor()
TimeSensor70.DEF = "SpinClock"
TimeSensor70.cycleInterval = 5.0
TimeSensor70.loop = True
Scene31.addChildren([TimeSensor70])

ROUTE71 = ROUTE()
ROUTE71.fromField = "fraction_changed"
ROUTE71.fromNode = "SpinClock"
ROUTE71.toField = "set_fraction"
ROUTE71.toNode = "SpinInterpolator"
Scene31.addChildren([ROUTE71])

ROUTE72 = ROUTE()
ROUTE72.fromField = "value_changed"
ROUTE72.fromNode = "SpinInterpolator"
ROUTE72.toField = "rotation"
ROUTE72.toNode = "TextTransform"
Scene31.addChildren([ROUTE72])

Group73 = Group()
Group73.DEF = "BackgroundGroup"

Background74 = Background()
Background74.DEF = "GradualBackground"
Group73.addChildren([Background74])

Script75 = Script()
Script75.DEF = "colorTypeConversionScript"

field76 = field()
field76.accessType = "inputOnly"
field76.name = "colorInput"
field76.type = "SFColor"
Script75.addField([field76])

field77 = field()
field77.accessType = "outputOnly"
field77.name = "colorsOutput"
field77.type = "MFColor"
Script75.addField([field77])

Script75.setSourceCode('''\n"+
"ecmascript:\n"+
"\n"+
"function colorInput (eventValue) // Example source code\n"+
"{\n"+
"   colorsOutput = new MFColor(eventValue); // assigning value sends output event\n"+
"// Browser.print('colorInput=' + eventValue + ', colorsOutput=' + colorsOutput + '\\n');\n"+
"}\n"+
"''')
Group73.addChildren([Script75])

ColorInterpolator78 = ColorInterpolator()
ColorInterpolator78.DEF = "ColorAnimator"
ColorInterpolator78.key = [0,0.5,1]
ColorInterpolator78.keyValue = [0.9411765,1,1,0.29411766,0,0.50980395,0.9411765,1,1]
# AZURE to INDIGO and back again 
Group73.addChildren([ColorInterpolator78])

TimeSensor79 = TimeSensor()
TimeSensor79.DEF = "ColorClock"
TimeSensor79.cycleInterval = 60.0
TimeSensor79.loop = True
Group73.addChildren([TimeSensor79])

ROUTE80 = ROUTE()
ROUTE80.fromField = "colorsOutput"
ROUTE80.fromNode = "colorTypeConversionScript"
ROUTE80.toField = "skyColor"
ROUTE80.toNode = "GradualBackground"
Group73.addChildren([ROUTE80])

ROUTE81 = ROUTE()
ROUTE81.fromField = "value_changed"
ROUTE81.fromNode = "ColorAnimator"
ROUTE81.toField = "colorInput"
ROUTE81.toNode = "colorTypeConversionScript"
Group73.addChildren([ROUTE81])

ROUTE82 = ROUTE()
ROUTE82.fromField = "fraction_changed"
ROUTE82.fromNode = "ColorClock"
ROUTE82.toField = "set_fraction"
ROUTE82.toNode = "ColorAnimator"
Group73.addChildren([ROUTE82])
Scene31.addChildren([Group73])

ProtoDeclare83 = ProtoDeclare()
ProtoDeclare83.appinfo = "tooltip: ArtDeco01Material prototype is a Material node"
ProtoDeclare83.name = "ArtDeco01Material"

ProtoInterface84 = ProtoInterface()

field85 = field()
field85.accessType = "inputOutput"
field85.appinfo = "tooltip for descriptionField"
field85.name = "description"
field85.type = "SFString"
field85.value = "ArtDeco01Material prototype is a Material node"
ProtoInterface84.addField([field85])

field86 = field()
field86.accessType = "inputOutput"
field86.name = "enabled"
field86.type = "SFBool"
field86.value = "true"
ProtoInterface84.addField([field86])
ProtoDeclare83.protoInterface = ProtoInterface84

ProtoBody87 = ProtoBody()
# Initial node of ProtoBody determines prototype node type 

Material88 = Material()
Material88.shininess = 0.127273
Material88.ambientIntensity = 0.25
Material88.specularColor = [0.276305,0.11431,0.139857]
Material88.diffuseColor = [0.282435,0.085159,0.134462]
ProtoBody87.addChildren([Material88])
# [HelloWorldProgram diagnostic] should be connected to scene graph: artDeco01ProtoDeclare.getNodeType()=\"Material\" 
# presence of follow-on TouchSensor shows that additional nodes are allowed in ProtoBody after initial node, regardless of node types 

TouchSensor89 = TouchSensor()
TouchSensor89.description = "within ProtoBody"

IS90 = IS()

connect91 = connect()
connect91.nodeField = "description"
connect91.protoField = "description"
IS90.addConnect([connect91])

connect92 = connect()
connect92.nodeField = "enabled"
connect92.protoField = "enabled"
IS90.addConnect([connect92])
TouchSensor89.IS = IS90
ProtoBody87.addChildren([TouchSensor89])
ProtoDeclare83.protoBody = ProtoBody87
Scene31.addChildren([ProtoDeclare83])

ExternProtoDeclare93 = ExternProtoDeclare()
ExternProtoDeclare93.appinfo = "this is a different Material node"
ExternProtoDeclare93.name = "ArtDeco02Material"
ExternProtoDeclare93.url = ["http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/ArtDecoPrototypesExcerpt.x3d#ArtDeco02Material","http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/ArtDecoPrototypesExcerpt.x3dv#ArtDeco02Material"]
# [HelloWorldProgram diagnostic] artDeco02ExternProtoDeclare.getNodeType()=\"ERROR_UNKNOWN_EXTERNPROTODECLARE_NODE_TYPE: ExternProtoDeclare name='ArtDeco02Material' type cannot be remotely accessed at run time. TODO X3DJSAIL needs to add further capability that retrieves the ExternProtoDeclare file.\" 

field94 = field()
field94.accessType = "inputOutput"
field94.appinfo = "tooltip for descriptionField"
field94.name = "description"
field94.type = "SFString"
ExternProtoDeclare93.addField([field94])
Scene31.addChildren([ExternProtoDeclare93])
# Tested ArtDeco01ProtoInstance, ArtDeco02ProtoInstance for improper node type when ProtoInstance is added in wrong place 

Shape95 = Shape()
Shape95.DEF = "TestShape1"

Appearance96 = Appearance()
Appearance96.DEF = "TestAppearance1"
# ArtDeco01Material prototype goes here... TODO ensure setContainerField is handled in exported Java 

ProtoInstance97 = ProtoInstance()
ProtoInstance97.name = "ArtDeco01Material"
# [HelloWorldProgram diagnostic] ArtDeco01ProtoInstance.getNodeType()=\"Material\" 

fieldValue98 = fieldValue()
fieldValue98.name = "description"
fieldValue98.value = "ArtDeco01Material can substitute for a Material node"
ProtoInstance97.addFieldValue([fieldValue98])
Appearance96.material = ProtoInstance97
Shape95.appearance = Appearance96

Sphere99 = Sphere(radius = 0.001)
Shape95.geometry = Sphere99
Scene31.addChildren([Shape95])

Shape100 = Shape()
Shape100.DEF = "TestShape2"

Appearance101 = Appearance()
Appearance101.DEF = "TestAppearance2"
# ArtDeco02Material prototype goes here... TODO ensure setContainerField is handled in exported Java 

ProtoInstance102 = ProtoInstance()
ProtoInstance102.DEF = "ArtDeco02MaterialDEF"
ProtoInstance102.name = "ArtDeco02Material"
# [HelloWorldProgram diagnostic] ArtDeco02ProtoInstance.getNodeType()=\"ERROR_UNKNOWN_EXTERNPROTODECLARE_NODE_TYPE: ExternProtoDeclare name='ArtDeco02Material' type cannot be remotely accessed at run time. TODO X3DJSAIL needs to add further capability that retrieves the ExternProtoDeclare file.\" 

fieldValue103 = fieldValue()
fieldValue103.name = "description"
fieldValue103.value = "ArtDeco02Material can substitute for another Material node"
ProtoInstance102.addFieldValue([fieldValue103])
Appearance101.material = ProtoInstance102
Shape100.appearance = Appearance101

Cone104 = Cone(bottomRadius = 0.001, height = 0.001)
Shape100.geometry = Cone104
Scene31.addChildren([Shape100])

Shape105 = Shape()
Shape105.DEF = "TestShape3"

Appearance106 = Appearance()
Appearance106.DEF = "TestAppearance3"
# ArtDeco02Material ProtoInstance USE goes here. Note that name field is NOT defined as part of ProtoInstance USE. 

ProtoInstance107 = ProtoInstance()
ProtoInstance107.USE = "ArtDeco02MaterialDEF"
Appearance106.material = ProtoInstance107
Shape105.appearance = Appearance106

Cylinder108 = Cylinder(height = 0.001, radius = 0.001)
Shape105.geometry = Cylinder108
Scene31.addChildren([Shape105])

Inline109 = Inline()
Inline109.DEF = "inlineSceneDef"
Inline109.url = ["someOtherScene.x3d","http://www.web3d.org/specifications/java/examples/someOtherScene.x3d"]
Scene31.addChildren([Inline109])

IMPORT110 = IMPORT()
IMPORT110.importedDEF = "WorldInfoDEF"
IMPORT110.inlineDEF = "inlineSceneDef"
IMPORT110.AS = "WorldInfoDEF2"
Scene31.addChildren([IMPORT110])

EXPORT111 = EXPORT()
EXPORT111.localDEF = "WorldInfoDEF"
EXPORT111.AS = "WorldInfoDEF3"
Scene31.addChildren([EXPORT111])

ProtoDeclare112 = ProtoDeclare()
ProtoDeclare112.appinfo = "mimic a Material node and modulate fields as an animation effect"
ProtoDeclare112.name = "MaterialModulator"
ProtoDeclare112.documentation = "http://x3dgraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/MaterialModulatorIndex.html"

ProtoInterface113 = ProtoInterface()

field114 = field()
field114.accessType = "inputOutput"
field114.name = "enabled"
field114.type = "SFBool"
field114.value = "true"
ProtoInterface113.addField([field114])

field115 = field()
field115.accessType = "inputOutput"
field115.name = "diffuseColor"
field115.type = "SFColor"
field115.value = "0 0 0"
ProtoInterface113.addField([field115])

field116 = field()
field116.accessType = "inputOutput"
field116.name = "emissiveColor"
field116.type = "SFColor"
field116.value = "0.05 0.05 0.5"
ProtoInterface113.addField([field116])

field117 = field()
field117.accessType = "inputOutput"
field117.name = "specularColor"
field117.type = "SFColor"
field117.value = "0 0 0"
ProtoInterface113.addField([field117])

field118 = field()
field118.accessType = "inputOutput"
field118.name = "transparency"
field118.type = "SFFloat"
field118.value = "0.0"
ProtoInterface113.addField([field118])

field119 = field()
field119.accessType = "inputOutput"
field119.name = "shininess"
field119.type = "SFFloat"
field119.value = "0.0"
ProtoInterface113.addField([field119])

field120 = field()
field120.accessType = "inputOutput"
field120.name = "ambientIntensity"
field120.type = "SFFloat"
field120.value = "0.0"
ProtoInterface113.addField([field120])
ProtoDeclare112.protoInterface = ProtoInterface113

ProtoBody121 = ProtoBody()

Material122 = Material()
Material122.DEF = "MaterialNode"

IS123 = IS()

connect124 = connect()
connect124.nodeField = "diffuseColor"
connect124.protoField = "diffuseColor"
IS123.addConnect([connect124])

connect125 = connect()
connect125.nodeField = "emissiveColor"
connect125.protoField = "emissiveColor"
IS123.addConnect([connect125])

connect126 = connect()
connect126.nodeField = "specularColor"
connect126.protoField = "specularColor"
IS123.addConnect([connect126])

connect127 = connect()
connect127.nodeField = "transparency"
connect127.protoField = "transparency"
IS123.addConnect([connect127])

connect128 = connect()
connect128.nodeField = "shininess"
connect128.protoField = "shininess"
IS123.addConnect([connect128])

connect129 = connect()
connect129.nodeField = "ambientIntensity"
connect129.protoField = "ambientIntensity"
IS123.addConnect([connect129])
Material122.IS = IS123
ProtoBody121.addChildren([Material122])
# Only first node (the node type) is renderable, others are along for the ride 

Script130 = Script()
Script130.DEF = "MaterialModulatorScript"

field131 = field()
field131.accessType = "inputOutput"
field131.name = "enabled"
field131.type = "SFBool"
Script130.addField([field131])

field132 = field()
field132.accessType = "inputOutput"
field132.name = "diffuseColor"
field132.type = "SFColor"
Script130.addField([field132])

field133 = field()
field133.accessType = "outputOnly"
field133.name = "newColor"
field133.type = "SFColor"
Script130.addField([field133])

field134 = field()
field134.accessType = "inputOnly"
field134.name = "clockTrigger"
field134.type = "SFTime"
Script130.addField([field134])

IS135 = IS()

connect136 = connect()
connect136.nodeField = "enabled"
connect136.protoField = "enabled"
IS135.addConnect([connect136])

connect137 = connect()
connect137.nodeField = "diffuseColor"
connect137.protoField = "diffuseColor"
IS135.addConnect([connect137])
Script130.IS = IS135

Script130.setSourceCode('''\n"+
"ecmascript:\n"+
"function initialize ()\n"+
"{\n"+
"    newColor = diffuseColor; // start with correct color\n"+
"}\n"+
"function set_enabled (newValue)\n"+
"{\n"+
"	enabled = newValue;\n"+
"}\n"+
"function clockTrigger (timeValue)\n"+
"{\n"+
"    if (!enabled) return;\n"+
"    red   = newColor.r;\n"+
"    green = newColor.g;\n"+
"    blue  = newColor.b;\n"+
"    \n"+
"    // note different modulation rates for each color component, % is modulus operator\n"+
"    newColor = new SFColor ((red + 0.02) % 1, (green + 0.03) % 1, (blue + 0.04) % 1);\n"+
"	if (enabled)\n"+
"	{\n"+
"		Browser.print ('diffuseColor=(' + red + ',' + green + ',' + blue + ') newColor=' + newColor.toString() + '\\n');\n"+
"	}\n"+
"}\n"+
"''')
ProtoBody121.addChildren([Script130])
ProtoDeclare112.protoBody = ProtoBody121
Scene31.addChildren([ProtoDeclare112])
# Test success: declarative statement createDeclarativeShapeTests() 

Group138 = Group()
Group138.DEF = "DeclarativeGroupExample"

Shape139 = Shape()

MetadataString140 = MetadataString()
MetadataString140.DEF = "FindableMetadataStringTest"
MetadataString140.value = ["test case"]
MetadataString140.name = "findThisNameValue"
Shape139.metadata = MetadataString140

Appearance141 = Appearance()
Appearance141.DEF = "DeclarativeAppearanceExample"
# DeclarativeMaterialExample gets overridden by subsequently added MaterialModulator ProtoInstance 

ProtoInstance142 = ProtoInstance()
ProtoInstance142.DEF = "MyMaterialModulator"
ProtoInstance142.name = "MaterialModulator"
Appearance141.material = ProtoInstance142
Shape139.appearance = Appearance141

Cone143 = Cone(bottomRadius = 0.05, height = 0.1, bottom = False)
Shape139.geometry = Cone143
Group138.addChildren([Shape139])
# Test success: declarativeGroup.addChild() singleton pipeline method 
Scene31.addChildren([Group138])
# Test success: declarative statement addChild() 
# Test success: x3dModel.findNodeByDEF(DeclarativeAppearanceExample) = <Appearance DEF='DeclarativeAppearanceExample'/> i.e. <Appearance DEF='DeclarativeAppearanceExample'> <!- - DeclarativeMaterialExample gets overridden by subsequently added MaterialModulator ProtoInstance - -> <ProtoInstance DEF='MyMaterialModulator' name='MaterialModulator' containerField='material'/> </Appearance> 
# Test success: x3dModel.findElementByNameValue(findThisNameValue) = <MetadataString DEF='FindableMetadataStringTest' name='findThisNameValue' value='\"test case\"'/> 
# Test success: x3dModel.findElementByNameValue(\"ArtDeco01Material\", \"ProtoDeclare\") found 
# Test success: x3dModel.findElementByNameValue(\"MaterialModulator\", \"ProtoDeclare\") found 
# Test success: x3dModel.findElementByNameValue(\"MaterialModulator\", \"ProtoInstance\") found 

Group144 = Group()
Group144.DEF = "TestFieldObjectsGroup"
# testFieldObjects() results 
# SFBool default=true, true=true, false=false, negate()=true 
# MFBool default=, initial=true false true, negate()=false true false 
# SFFloat default=0.0, initial=1.0, setValue(2)=2.0, setValue(3.0f)=3.0, setValue(4.0)=4.0 
# MFFloat default=, initial=1 2 3, append(5)=1 2 3 5, inserts(3,4)(0,0)=0 1 2 3 4 5, append(6)=0 1 2 3 4 5 6, size()=7 
# ... get1Value[3]=3.0, remove[1]=0 2 3 4 5 6, set1Value(0,10)=10 2 3 4 5 6, multiply(2)=20 4 6 8 10 12, clear= 
# SFVec3f default=0 0 0, initial=1 2 3, setValue=4 5 6, multiply(2)=8 10 12, normalize()=0.45584232 0.5698029 0.68376344, regex matches()=true 
# regex test SFVec3f().matches(\"1 2 3\")=true, regex test SFVec3f().matches(\"1 2 3 4\")=false, regex test (SFRotationObject.matches(\"0 0 0 0\")=true, failure detecting illegal (zero axis) rotation value 
Scene31.addChildren([Group144])

Sound145 = Sound()
Sound145.location = [0,1.6,0]
# set sound-ellipsoid location height at 1.6m to match typical avatar height 

AudioClip146 = AudioClip()
AudioClip146.description = "chimes"
AudioClip146.url = ["chimes.wav","http://www.web3d.org/x3d/content/examples/ConformanceNist/Sounds/AudioClip/chimes.wav"]
# Scene example fragment from http://www.web3d.org/x3d/content/examples/ConformanceNist/Sounds/AudioClip/default.x3d 
Sound145.source = AudioClip146
Scene31.addChildren([Sound145])

Sound147 = Sound()
Sound147.location = [0,1.6,0]
# set sound-ellipsoid location height at 1.6m to match typical avatar height 

MovieTexture148 = MovieTexture()
MovieTexture148.description = "mpgsys.mpg from ConformanceNist suite"
MovieTexture148.url = ["mpgsys.mpg","http://www.web3d.org/x3d/content/examples/ConformanceNist/Appearance/MovieTexture/mpgsys.mpg"]
# Scene example fragment from http://www.web3d.org/x3d/content/examples/ConformanceNist/Appearance/MovieTexture/mpeg1-systems.x3d 
# Expected containerField='source', allowed containerField values=\"texture\" \"source\" \"back\" \"bottom\" \"front\" \"left\" \"right\" \"top\" \"backTexture\" \"bottomTexture\" \"frontTexture\" \"leftTexture\" \"rightTexture\" \"topTexture\" \"watchList\" 
Sound147.source = MovieTexture148
Scene31.addChildren([Sound147])
# Test success: AnchorObject.isNode()=true, siteAnchor.isNode()=true 
# Test success: AnchorObject.isStatement()=false, siteAnchor.isStatement()=false 
# Test success: ROUTEObject.isNode()=false, orbitPositionROUTE.isNode()=false 
# Test success: ROUTEObject.isStatement()=true, orbitPositionROUTE.isStatement()=true 
# Test success: CommentsBlock.isNode()=false, testComments.isNode()=false 
# Test failure: CommentsBlock.isStatement()=true, testComments.isStatement()=true 

Shape149 = Shape()
Shape149.DEF = "ExtrusionShape"
# ExampleExtrusion isCrossSectionClosed()=true, crossSection='[1.0, 1.0, 1.0, -1.0, -1.0, -1.0, -1.0, 1.0, 1.0, 1.0]' 
# ExampleExtrusion isSpineClosed()=false, spine='[0.0, 0.0, 0.0, 0.0, 1.0, 0.0]' 

Appearance150 = Appearance()
Appearance150.DEF = "TransparentAppearance"

Material151 = Material()
Material151.transparency = 1.0
Appearance150.material = Material151
Shape149.appearance = Appearance150

Extrusion152 = Extrusion()
Extrusion152.DEF = "ExampleExtrusion"
Shape149.geometry = Extrusion152
Scene31.addChildren([Shape149])

Group153 = Group()
# Test MFNode children array as an ordered list consisting of comments, statements, ProtoInstance and nodes 

ProtoDeclare154 = ProtoDeclare()
ProtoDeclare154.name = "NewWorldInfo"

ProtoInterface155 = ProtoInterface()

field156 = field()
field156.accessType = "initializeOnly"
field156.name = "description"
field156.type = "SFString"
ProtoInterface155.addField([field156])
ProtoDeclare154.protoInterface = ProtoInterface155

ProtoBody157 = ProtoBody()

WorldInfo158 = WorldInfo()
ProtoBody157.addChildren([WorldInfo158])
ProtoDeclare154.protoBody = ProtoBody157
Group153.addChildren([ProtoDeclare154])

ProtoInstance159 = ProtoInstance()
ProtoInstance159.DEF = "Proto1"
ProtoInstance159.name = "NewWorldInfo"

fieldValue160 = fieldValue()
fieldValue160.name = "description"
fieldValue160.value = "testing 1 2 3"
ProtoInstance159.addFieldValue([fieldValue160])
Group153.addChildren([ProtoInstance159])

Group161 = Group()
Group161.DEF = "Node2"
# intentionally empty 
Group153.addChildren([Group161])

ProtoInstance162 = ProtoInstance()
ProtoInstance162.DEF = "Proto3"
ProtoInstance162.name = "NewWorldInfo"
Group153.addChildren([ProtoInstance162])

Transform163 = Transform()
Transform163.DEF = "Node4"
# intentionally empty 
Group153.addChildren([Transform163])
# Test satisfactorily creates MFNode children array as an ordered list with mixed content 
Scene31.addChildren([Group153])

ProtoDeclare164 = ProtoDeclare()
ProtoDeclare164.name = "ShaderProto"

ProtoBody165 = ProtoBody()

ProgramShader166 = ProgramShader()
ProtoBody165.shaders = ProgramShader166
ProtoDeclare164.protoBody = ProtoBody165
Scene31.addChildren([ProtoDeclare164])

Shape167 = Shape()

Appearance168 = Appearance()
# Test MFNode shaders array as an ordered list consisting of comments, ProtoInstance and nodes 
# Test satisfactorily creates MFNode shaders array as an ordered list with mixed content 

ProgramShader169 = ProgramShader()
ProgramShader169.DEF = "TestShader1"

ShaderProgram170 = ShaderProgram()
ShaderProgram170.DEF = "TestShader2"
ProgramShader169.programs = ShaderProgram170
Appearance168.shaders = ProgramShader169

ProtoInstance171 = ProtoInstance()
ProtoInstance171.DEF = "TestShader3"
ProtoInstance171.name = "ShaderProto"
Appearance168.shaders = ProtoInstance171

ComposedShader172 = ComposedShader()
ComposedShader172.DEF = "TestShader4"

ShaderPart173 = ShaderPart()
ShaderPart173.DEF = "TestShader5"
ComposedShader172.parts = ShaderPart173
Appearance168.shaders = ComposedShader172
Shape167.appearance = Appearance168
Scene31.addChildren([Shape167])

Transform174 = Transform()
Transform174.DEF = "SpecialtyNodes"

CADLayer175 = CADLayer()

CADAssembly176 = CADAssembly()

CADPart177 = CADPart()

CADFace178 = CADFace()
CADPart177.addChildren([CADFace178])
CADAssembly176.addChildren([CADPart177])
CADLayer175.addChildren([CADAssembly176])
Transform174.addChildren([CADLayer175])

EspduTransform179 = EspduTransform()
Transform174.children = EspduTransform179

ReceiverPdu180 = ReceiverPdu()
ReceiverPdu180.receivedPower = 0.0
Transform174.children = ReceiverPdu180

SignalPdu181 = SignalPdu()
Transform174.children = SignalPdu181

TransmitterPdu182 = TransmitterPdu()
TransmitterPdu182.relativeAntennaLocation = [0,0,0]
TransmitterPdu182.transmitFrequencyBandwidth = 0.0
Transform174.children = TransmitterPdu182

DISEntityManager183 = DISEntityManager()

DISEntityTypeMapping184 = DISEntityTypeMapping()
DISEntityManager183.addMapping([DISEntityTypeMapping184])
Transform174.children = DISEntityManager183

HAnimHumanoid185 = HAnimHumanoid()
HAnimHumanoid185.DEF = "TestHumanoidDEF"
HAnimHumanoid185.version = "2.0"
HAnimHumanoid185.name = "TestHumanoid"
Transform174.addChildren([HAnimHumanoid185])
Scene31.addChildren([Transform174])
X3D0.scene = Scene31
