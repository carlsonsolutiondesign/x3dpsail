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
component3.name = "Shaders"
head1.addComponent([component3])

component4 = component()
component4.level = 1
component4.name = "Layering"
head1.addComponent([component4])

unit5 = unit(category = "angle")
unit5.conversionFactor = 1.0
unit5.name = "AngleUnitConversion"
head1.addUnit([unit5])

unit6 = unit(category = "length")
unit6.conversionFactor = 1.0
unit6.name = "LengthUnitConversion"
head1.addUnit([unit6])

meta7 = meta()
meta7.content = "HelloWorldProgramOutput.x3d"
meta7.name = "title"
head1.addMeta([meta7])

meta8 = meta()
meta8.content = "Example HelloWorldProgram creates an X3D model using the X3D Java Scene Access Interface Library (X3DJSAIL)"
meta8.name = "description"
head1.addMeta([meta8])

meta9 = meta()
meta9.content = "http://www.web3d.org/specifications/java/X3DJSAIL.html"
meta9.name = "reference"
head1.addMeta([meta9])

meta10 = meta()
meta10.content = "HelloWorldProgramOutput.java"
meta10.name = "generator"
head1.addMeta([meta10])

meta11 = meta()
meta11.content = "6 September 2016"
meta11.name = "created"
head1.addMeta([meta11])

meta12 = meta()
meta12.content = "27 December 2018"
meta12.name = "modified"
head1.addMeta([meta12])

meta13 = meta()
meta13.content = "X3D Java Scene Access Interface Library (X3DJSAIL)"
meta13.name = "generator"
head1.addMeta([meta13])

meta14 = meta()
meta14.content = "http://www.web3d.org/specifications/java/examples/HelloWorldProgram.java"
meta14.name = "generator"
head1.addMeta([meta14])

meta15 = meta()
meta15.content = "Netbeans http://www.netbeans.org"
meta15.name = "generator"
head1.addMeta([meta15])

meta16 = meta()
meta16.content = "Don Brutzman"
meta16.name = "creator"
head1.addMeta([meta16])

meta17 = meta()
meta17.content = "https://sourceforge.net/p/x3d/code/HEAD/tree/www.web3d.org/x3d/stylesheets/java/examples/HelloWorldProgramOutput.x3d"
meta17.name = "reference"
head1.addMeta([meta17])

meta18 = meta()
meta18.content = "Console output, ClassicVRML encoding, VRML97 encoding and pretty-print documentation:"
meta18.name = "reference"
head1.addMeta([meta18])

meta19 = meta()
meta19.content = "HelloWorldProgramOutput.txt"
meta19.name = "reference"
head1.addMeta([meta19])

meta20 = meta()
meta20.content = "HelloWorldProgramOutput.x3dv"
meta20.name = "reference"
head1.addMeta([meta20])

meta21 = meta()
meta21.content = "HelloWorldProgramOutput.wrl"
meta21.name = "reference"
head1.addMeta([meta21])

meta22 = meta()
meta22.content = "HelloWorldProgramOutput.html"
meta22.name = "reference"
head1.addMeta([meta22])

meta23 = meta()
meta23.content = "https://savage.nps.edu/X3dValidator?url=http://www.web3d.org/specifications/java/examples/HelloWorldProgramOutput.x3d"
meta23.name = "reference"
head1.addMeta([meta23])

meta24 = meta()
meta24.content = "http://www.web3d.org/specifications/java/examples/HelloWorldProgramOutput.x3d"
meta24.name = "identifier"
head1.addMeta([meta24])

meta25 = meta()
meta25.content = "../license.html"
meta25.name = "license"
head1.addMeta([meta25])
X3D0.head = head1

Scene26 = Scene()

ViewpointGroup27 = ViewpointGroup()
ViewpointGroup27.description = "Available viewpoints"

Viewpoint28 = Viewpoint()
Viewpoint28.DEF = "DefaultView"
Viewpoint28.description = "Hello X3DJSAIL"
ViewpointGroup27.addChildren([Viewpoint28])

Viewpoint29 = Viewpoint()
Viewpoint29.DEF = "TopDownView"
Viewpoint29.description = "top-down view from above"
Viewpoint29.orientation = [1,0,0,-1.570796]
Viewpoint29.position = [0,100,0]
ViewpointGroup27.addChildren([Viewpoint29])
Scene26.addChildren([ViewpointGroup27])

NavigationInfo30 = NavigationInfo()
NavigationInfo30.avatarSize = [0.25,1.6,0.75]
NavigationInfo30.transitionType = ["LINEAR"]
NavigationInfo30.type = ["EXAMINE","FLY","ANY"]
Scene26.addChildren([NavigationInfo30])

WorldInfo31 = WorldInfo()
WorldInfo31.DEF = "WorldInfoDEF"
WorldInfo31.title = "HelloWorldProgram produced by X3D Java SAI Library (X3DJSAIL)"
Scene26.addChildren([WorldInfo31])

WorldInfo32 = WorldInfo()
WorldInfo32.USE = "WorldInfoDEF"
Scene26.addChildren([WorldInfo32])

WorldInfo33 = WorldInfo()
WorldInfo33.USE = "WorldInfoDEF"
Scene26.addChildren([WorldInfo33])

MetadataString34 = MetadataString()
MetadataString34.DEF = "scene.addChildMetadata"
MetadataString34.name = "test"
MetadataString34.value = ["Top-level root Metadata node beneath Scene needs to be one of '-children' in JSON encoding"]
Scene26.addChildren([MetadataString34])

LayerSet35 = LayerSet(order = [0])
LayerSet35.DEF = "scene.addChildLayerSetTest"
Scene26.addLayerSet([LayerSet35])

Transform36 = Transform()
Transform36.DEF = "LogoGeometryTransform"
Transform36.translation = [0,1.5,0]

Anchor37 = Anchor()
Anchor37.description = "select for X3D Java SAI Library (X3DJSAIL) description"
Anchor37.url = ["../X3DJSAIL.html","http://www.web3d.org/specifications/java/X3DJSAIL.html"]

Shape38 = Shape()
Shape38.DEF = "BoxShape"

Appearance39 = Appearance()

Material40 = Material()
Material40.DEF = "GreenMaterial"
Material40.diffuseColor = [0,1,1]
Material40.emissiveColor = [0.8,0,0]
Material40.transparency = 0.1
Appearance39.material = Material40

ImageTexture41 = ImageTexture()
ImageTexture41.url = ["images/X3dJavaSceneAccessInterfaceSaiLibrary.png","http://www.web3d.org/specifications/java/examples/images/X3dJavaSceneAccessInterfaceSaiLibrary.png"]
Appearance39.texture = ImageTexture41
Shape38.appearance = Appearance39

Box42 = Box()
Box42.DEF = "test-NMTOKEN_regex.0123456789"
Box42.class_ = "untextured"
Shape38.geometry = Box42
Anchor37.addChildren([Shape38])
Transform36.addChildren([Anchor37])
Scene26.addChildren([Transform36])

Shape43 = Shape()
Shape43.DEF = "LineShape"

Appearance44 = Appearance()

Material45 = Material()
Material45.emissiveColor = [0.6,0.19607843,0.8]
Appearance44.material = Material45
Shape43.appearance = Appearance44

IndexedLineSet46 = IndexedLineSet(coordIndex = [0,1,2,3,4,0])
# Coordinate 3-tuple point count: 6 

Coordinate47 = Coordinate()
Coordinate47.point = [0,1.5,0,2,1.5,0,2,1.5,-2,-2,1.5,-2,-2,1.5,0,0,1.5,0]
IndexedLineSet46.coord = Coordinate47
Shape43.geometry = IndexedLineSet46
Scene26.addChildren([Shape43])

PositionInterpolator48 = PositionInterpolator()
PositionInterpolator48.DEF = "BoxPathAnimator"
PositionInterpolator48.key = [0,0.125,0.375,0.625,0.875,1]
PositionInterpolator48.keyValue = [0,1.5,0,2,1.5,0,2,1.5,-2,-2,1.5,-2,-2,1.5,0,0,1.5,0]
Scene26.addChildren([PositionInterpolator48])

TimeSensor49 = TimeSensor()
TimeSensor49.DEF = "OrbitClock"
TimeSensor49.cycleInterval = 8.0
TimeSensor49.loop = True
Scene26.addChildren([TimeSensor49])

ROUTE50 = ROUTE()
ROUTE50.fromField = "fraction_changed"
ROUTE50.fromNode = "OrbitClock"
ROUTE50.toField = "set_fraction"
ROUTE50.toNode = "BoxPathAnimator"
Scene26.addChildren([ROUTE50])

ROUTE51 = ROUTE()
ROUTE51.fromField = "value_changed"
ROUTE51.fromNode = "BoxPathAnimator"
ROUTE51.toField = "set_translation"
ROUTE51.toNode = "LogoGeometryTransform"
Scene26.addChildren([ROUTE51])

Transform52 = Transform()
Transform52.DEF = "TextTransform"
Transform52.translation = [0,-1.5,0]

Shape53 = Shape()

Appearance54 = Appearance()

Material55 = Material()
Material55.USE = "GreenMaterial"
Appearance54.material = Material55
Shape53.appearance = Appearance54

Text56 = Text()
Text56.string = ["X3D Java","SAI Library","X3DJSAIL"]
# Comment example A, plain quotation marks: He said, \"Immel did it!\" 
# Comment example B, XML character entities: He said, &quot;Immel did it!&quot; 

MetadataSet57 = MetadataSet()
MetadataSet57.name = "EscapedQuotationMarksMetadataSet"

MetadataString58 = MetadataString()
MetadataString58.name = "quotesTestC"
MetadataString58.value = ["MFString example C, backslash-escaped quotes: He said, \"Immel did it!\""]
MetadataSet57.value = MetadataString58

MetadataString59 = MetadataString()
MetadataString59.name = "extraChildTest"
MetadataString59.value = ["checks MetadataSetObject addValue() method"]
MetadataSet57.value = MetadataString59
Text56.metadata = MetadataSet57

FontStyle60 = FontStyle(family = ["SERIF"], justify = ["MIDDLE","MIDDLE"])
Text56.fontStyle = FontStyle60
Shape53.geometry = Text56
Transform52.addChildren([Shape53])

Collision61 = Collision()
# test containerField='proxy' 

Shape62 = Shape()
Shape62.DEF = "ProxyShape"
# alternative XML encoding: Text string='\"One, Two, Comment\" \"\" \"He said, \\&quot;Immel did it!\\&quot;\"' 
# alternative XML encoding: Text string='\"One, Two, Comment\" \"\" \"He said, \\&quot;Immel did it!\\&quot;\" \"\"' 
# alternative Java source: .setString(new String [] {\"One, Two, Comment\", \"\", \"He said, \\\"Immel did it!\\\"\"}) 
# reference: http://www.web3d.org/x3d/content/examples/Basic/X3dSpecifications/StringArrayEncodingExamplesIndex.html 

Text63 = Text()
Text63.string = ["One, Two, Text","","He said, \"Immel did it!\" \"\""]
Shape62.geometry = Text63
Collision61.proxy = Shape62
Transform52.addChildren([Collision61])
# It's a beautiful world 
# ... for you! 
# https://en.wikipedia.org/wiki/Beautiful_World_(Devo_song) 
Scene26.addChildren([Transform52])
# repeatedly spin 180 degrees as a readable special effect 

OrientationInterpolator64 = OrientationInterpolator()
OrientationInterpolator64.DEF = "SpinInterpolator"
OrientationInterpolator64.key = [0,0.5,1]
OrientationInterpolator64.keyValue = [0,1,0,4.712389,0,1,0,0,0,1,0,1.5707964]
Scene26.addChildren([OrientationInterpolator64])

TimeSensor65 = TimeSensor()
TimeSensor65.DEF = "SpinClock"
TimeSensor65.cycleInterval = 5.0
TimeSensor65.loop = True
Scene26.addChildren([TimeSensor65])

ROUTE66 = ROUTE()
ROUTE66.fromField = "fraction_changed"
ROUTE66.fromNode = "SpinClock"
ROUTE66.toField = "set_fraction"
ROUTE66.toNode = "SpinInterpolator"
Scene26.addChildren([ROUTE66])

ROUTE67 = ROUTE()
ROUTE67.fromField = "value_changed"
ROUTE67.fromNode = "SpinInterpolator"
ROUTE67.toField = "rotation"
ROUTE67.toNode = "TextTransform"
Scene26.addChildren([ROUTE67])

Group68 = Group()
Group68.DEF = "BackgroundGroup"

Background69 = Background()
Background69.DEF = "GradualBackground"
Group68.addChildren([Background69])

Script70 = Script()
Script70.DEF = "colorTypeConversionScript"

field71 = field()
field71.accessType = "inputOnly"
field71.name = "colorInput"
field71.type = "SFColor"
Script70.addField([field71])

field72 = field()
field72.accessType = "outputOnly"
field72.name = "colorsOutput"
field72.type = "MFColor"
Script70.addField([field72])

Script70.setSourceCode('''\n"+
"ecmascript:\n"+
"\n"+
"function colorInput (eventValue) // Example source code\n"+
"{\n"+
"   colorsOutput = new MFColor(eventValue); // assigning value sends output event\n"+
"// Browser.print('colorInput=' + eventValue + ', colorsOutput=' + colorsOutput + '\\n');\n"+
"}\n"+
"''')
Group68.addChildren([Script70])

ColorInterpolator73 = ColorInterpolator()
ColorInterpolator73.DEF = "ColorAnimator"
ColorInterpolator73.key = [0,0.5,1]
ColorInterpolator73.keyValue = [0.9411765,1,1,0.29411766,0,0.50980395,0.9411765,1,1]
# AZURE to INDIGO and back again 
Group68.addChildren([ColorInterpolator73])

TimeSensor74 = TimeSensor()
TimeSensor74.DEF = "ColorClock"
TimeSensor74.cycleInterval = 60.0
TimeSensor74.loop = True
Group68.addChildren([TimeSensor74])

ROUTE75 = ROUTE()
ROUTE75.fromField = "colorsOutput"
ROUTE75.fromNode = "colorTypeConversionScript"
ROUTE75.toField = "skyColor"
ROUTE75.toNode = "GradualBackground"
Group68.addChildren([ROUTE75])

ROUTE76 = ROUTE()
ROUTE76.fromField = "value_changed"
ROUTE76.fromNode = "ColorAnimator"
ROUTE76.toField = "colorInput"
ROUTE76.toNode = "colorTypeConversionScript"
Group68.addChildren([ROUTE76])

ROUTE77 = ROUTE()
ROUTE77.fromField = "fraction_changed"
ROUTE77.fromNode = "ColorClock"
ROUTE77.toField = "set_fraction"
ROUTE77.toNode = "ColorAnimator"
Group68.addChildren([ROUTE77])
Scene26.addChildren([Group68])

ProtoDeclare78 = ProtoDeclare()
ProtoDeclare78.appinfo = "tooltip: ArtDeco01Material prototype is a Material node"
ProtoDeclare78.name = "ArtDeco01Material"

ProtoInterface79 = ProtoInterface()

field80 = field()
field80.accessType = "inputOutput"
field80.appinfo = "tooltip for descriptionField"
field80.name = "description"
field80.type = "SFString"
field80.value = "ArtDeco01Material prototype is a Material node"
ProtoInterface79.addField([field80])

field81 = field()
field81.accessType = "inputOutput"
field81.name = "enabled"
field81.type = "SFBool"
field81.value = "true"
ProtoInterface79.addField([field81])
ProtoDeclare78.protoInterface = ProtoInterface79

ProtoBody82 = ProtoBody()
# Initial node of ProtoBody determines prototype node type 

Material83 = Material()
Material83.ambientIntensity = 0.25
Material83.diffuseColor = [0.282435,0.085159,0.134462]
Material83.shininess = 0.127273
Material83.specularColor = [0.276305,0.11431,0.139857]
ProtoBody82.addChildren([Material83])
# [HelloWorldProgram diagnostic] should be connected to scene graph: artDeco01ProtoDeclare.getNodeType()=\"Material\" 
# presence of follow-on TouchSensor shows that additional nodes are allowed in ProtoBody after initial node, regardless of node types 

TouchSensor84 = TouchSensor()
TouchSensor84.description = "within ProtoBody"

IS85 = IS()

connect86 = connect()
connect86.nodeField = "description"
connect86.protoField = "description"
IS85.addConnect([connect86])

connect87 = connect()
connect87.nodeField = "enabled"
connect87.protoField = "enabled"
IS85.addConnect([connect87])
TouchSensor84.IS = IS85
ProtoBody82.addChildren([TouchSensor84])
ProtoDeclare78.protoBody = ProtoBody82
Scene26.addChildren([ProtoDeclare78])

ExternProtoDeclare88 = ExternProtoDeclare()
ExternProtoDeclare88.appinfo = "this is a different Material node"
ExternProtoDeclare88.name = "ArtDeco02Material"
ExternProtoDeclare88.url = ["http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/ArtDecoPrototypesExcerpt.x3d#ArtDeco02Material","http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/ArtDecoPrototypesExcerpt.x3dv#ArtDeco02Material"]
# [HelloWorldProgram diagnostic] artDeco02ExternProtoDeclare.getNodeType()=\"ERROR_UNKNOWN_EXTERNPROTODECLARE_NODE_TYPE: ExternProtoDeclare name='ArtDeco02Material' type cannot be remotely accessed at run time. TODO X3DJSAIL needs to add further capability that retrieves the ExternProtoDeclare file.\" 

field89 = field()
field89.accessType = "inputOutput"
field89.appinfo = "tooltip for descriptionField"
field89.name = "description"
field89.type = "SFString"
ExternProtoDeclare88.addField([field89])
Scene26.addChildren([ExternProtoDeclare88])
# Tested ArtDeco01ProtoInstance, ArtDeco02ProtoInstance for improper node type when ProtoInstance is added in wrong place 

Shape90 = Shape()
Shape90.DEF = "TestShape1"

Appearance91 = Appearance()
Appearance91.DEF = "TestAppearance1"
# ArtDeco01Material prototype goes here... TODO ensure setContainerField is handled in exported Java 

ProtoInstance92 = ProtoInstance()
ProtoInstance92.name = "ArtDeco01Material"
# [HelloWorldProgram diagnostic] ArtDeco01ProtoInstance.getNodeType()=\"Material\" 

fieldValue93 = fieldValue()
fieldValue93.name = "description"
fieldValue93.value = "ArtDeco01Material can substitute for a Material node"
ProtoInstance92.addFieldValue([fieldValue93])
Appearance91.material = ProtoInstance92
Shape90.appearance = Appearance91

Sphere94 = Sphere(radius = 0.001)
Shape90.geometry = Sphere94
Scene26.addChildren([Shape90])

Shape95 = Shape()
Shape95.DEF = "TestShape2"

Appearance96 = Appearance()
Appearance96.DEF = "TestAppearance2"
# ArtDeco02Material prototype goes here... TODO ensure setContainerField is handled in exported Java 

ProtoInstance97 = ProtoInstance()
ProtoInstance97.DEF = "ArtDeco02MaterialDEF"
ProtoInstance97.name = "ArtDeco02Material"
# [HelloWorldProgram diagnostic] ArtDeco02ProtoInstance.getNodeType()=\"ERROR_UNKNOWN_EXTERNPROTODECLARE_NODE_TYPE: ExternProtoDeclare name='ArtDeco02Material' type cannot be remotely accessed at run time. TODO X3DJSAIL needs to add further capability that retrieves the ExternProtoDeclare file.\" 

fieldValue98 = fieldValue()
fieldValue98.name = "description"
fieldValue98.value = "ArtDeco02Material can substitute for another Material node"
ProtoInstance97.addFieldValue([fieldValue98])
Appearance96.material = ProtoInstance97
Shape95.appearance = Appearance96

Cone99 = Cone(bottomRadius = 0.001, height = 0.001)
Shape95.geometry = Cone99
Scene26.addChildren([Shape95])

Shape100 = Shape()
Shape100.DEF = "TestShape3"

Appearance101 = Appearance()
Appearance101.DEF = "TestAppearance3"
# ArtDeco02Material ProtoInstance USE goes here. Note that name field is NOT defined as part of ProtoInstance USE. 

ProtoInstance102 = ProtoInstance()
ProtoInstance102.USE = "ArtDeco02MaterialDEF"
Appearance101.material = ProtoInstance102
Shape100.appearance = Appearance101

Cylinder103 = Cylinder(height = 0.001, radius = 0.001)
Shape100.geometry = Cylinder103
Scene26.addChildren([Shape100])

Inline104 = Inline()
Inline104.DEF = "inlineSceneDef"
Inline104.url = ["someOtherScene.x3d","http://www.web3d.org/specifications/java/examples/someOtherScene.x3d"]
Scene26.addChildren([Inline104])

IMPORT105 = IMPORT()
IMPORT105.AS = "WorldInfoDEF2"
IMPORT105.importedDEF = "WorldInfoDEF"
IMPORT105.inlineDEF = "inlineSceneDef"
Scene26.addChildren([IMPORT105])

EXPORT106 = EXPORT()
EXPORT106.AS = "WorldInfoDEF3"
EXPORT106.localDEF = "WorldInfoDEF"
Scene26.addChildren([EXPORT106])

ProtoDeclare107 = ProtoDeclare()
ProtoDeclare107.appinfo = "mimic a Material node and modulate fields as an animation effect"
ProtoDeclare107.documentation = "http://x3dgraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/MaterialModulatorIndex.html"
ProtoDeclare107.name = "MaterialModulator"

ProtoInterface108 = ProtoInterface()

field109 = field()
field109.accessType = "inputOutput"
field109.name = "enabled"
field109.type = "SFBool"
field109.value = "true"
ProtoInterface108.addField([field109])

field110 = field()
field110.accessType = "inputOutput"
field110.name = "diffuseColor"
field110.type = "SFColor"
field110.value = "0 0 0"
ProtoInterface108.addField([field110])

field111 = field()
field111.accessType = "inputOutput"
field111.name = "emissiveColor"
field111.type = "SFColor"
field111.value = "0.05 0.05 0.5"
ProtoInterface108.addField([field111])

field112 = field()
field112.accessType = "inputOutput"
field112.name = "specularColor"
field112.type = "SFColor"
field112.value = "0 0 0"
ProtoInterface108.addField([field112])

field113 = field()
field113.accessType = "inputOutput"
field113.name = "transparency"
field113.type = "SFFloat"
field113.value = "0.0"
ProtoInterface108.addField([field113])

field114 = field()
field114.accessType = "inputOutput"
field114.name = "shininess"
field114.type = "SFFloat"
field114.value = "0.0"
ProtoInterface108.addField([field114])

field115 = field()
field115.accessType = "inputOutput"
field115.name = "ambientIntensity"
field115.type = "SFFloat"
field115.value = "0.0"
ProtoInterface108.addField([field115])
ProtoDeclare107.protoInterface = ProtoInterface108

ProtoBody116 = ProtoBody()

Material117 = Material()
Material117.DEF = "MaterialNode"

IS118 = IS()

connect119 = connect()
connect119.nodeField = "diffuseColor"
connect119.protoField = "diffuseColor"
IS118.addConnect([connect119])

connect120 = connect()
connect120.nodeField = "emissiveColor"
connect120.protoField = "emissiveColor"
IS118.addConnect([connect120])

connect121 = connect()
connect121.nodeField = "specularColor"
connect121.protoField = "specularColor"
IS118.addConnect([connect121])

connect122 = connect()
connect122.nodeField = "transparency"
connect122.protoField = "transparency"
IS118.addConnect([connect122])

connect123 = connect()
connect123.nodeField = "shininess"
connect123.protoField = "shininess"
IS118.addConnect([connect123])

connect124 = connect()
connect124.nodeField = "ambientIntensity"
connect124.protoField = "ambientIntensity"
IS118.addConnect([connect124])
Material117.IS = IS118
ProtoBody116.addChildren([Material117])
# Only first node (the node type) is renderable, others are along for the ride 

Script125 = Script()
Script125.DEF = "MaterialModulatorScript"

field126 = field()
field126.accessType = "inputOutput"
field126.name = "enabled"
field126.type = "SFBool"
Script125.addField([field126])

field127 = field()
field127.accessType = "inputOutput"
field127.name = "diffuseColor"
field127.type = "SFColor"
Script125.addField([field127])

field128 = field()
field128.accessType = "outputOnly"
field128.name = "newColor"
field128.type = "SFColor"
Script125.addField([field128])

field129 = field()
field129.accessType = "inputOnly"
field129.name = "clockTrigger"
field129.type = "SFTime"
Script125.addField([field129])

IS130 = IS()

connect131 = connect()
connect131.nodeField = "enabled"
connect131.protoField = "enabled"
IS130.addConnect([connect131])

connect132 = connect()
connect132.nodeField = "diffuseColor"
connect132.protoField = "diffuseColor"
IS130.addConnect([connect132])
Script125.IS = IS130

Script125.setSourceCode('''\n"+
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
ProtoBody116.addChildren([Script125])
ProtoDeclare107.protoBody = ProtoBody116
Scene26.addChildren([ProtoDeclare107])
# Test success: declarative statement createDeclarativeShapeTests() 

Group133 = Group()
Group133.DEF = "DeclarativeGroupExample"

Shape134 = Shape()

MetadataString135 = MetadataString()
MetadataString135.DEF = "FindableMetadataStringTest"
MetadataString135.name = "findThisNameValue"
MetadataString135.value = ["test case"]
Shape134.metadata = MetadataString135

Appearance136 = Appearance()
Appearance136.DEF = "DeclarativeAppearanceExample"
# DeclarativeMaterialExample gets overridden by subsequently added MaterialModulator ProtoInstance 

ProtoInstance137 = ProtoInstance()
ProtoInstance137.DEF = "MyMaterialModulator"
ProtoInstance137.name = "MaterialModulator"
Appearance136.material = ProtoInstance137
Shape134.appearance = Appearance136

Cone138 = Cone(bottom = False, bottomRadius = 0.05, height = 0.1)
Shape134.geometry = Cone138
Group133.addChildren([Shape134])
# Test success: declarativeGroup.addChild() singleton pipeline method 
Scene26.addChildren([Group133])
# Test success: declarative statement addChild() 
# Test success: x3dModel.findNodeByDEF(DeclarativeAppearanceExample) = <Appearance DEF='DeclarativeAppearanceExample'/> i.e. <Appearance DEF='DeclarativeAppearanceExample'> <!- - DeclarativeMaterialExample gets overridden by subsequently added MaterialModulator ProtoInstance - -> <ProtoInstance DEF='MyMaterialModulator' name='MaterialModulator' containerField='material'/> </Appearance> 
# Test success: x3dModel.findElementByNameValue(findThisNameValue) = <MetadataString DEF='FindableMetadataStringTest' name='findThisNameValue' value='\"test case\"'/> 
# Test success: x3dModel.findElementByNameValue(\"ArtDeco01Material\", \"ProtoDeclare\") found 
# Test success: x3dModel.findElementByNameValue(\"MaterialModulator\", \"ProtoDeclare\") found 
# Test success: x3dModel.findElementByNameValue(\"MaterialModulator\", \"ProtoInstance\") found 

Group139 = Group()
Group139.DEF = "TestFieldObjectsGroup"
# testFieldObjects() results 
# SFBool default=true, true=true, false=false, negate()=true 
# MFBool default=, initial=true false true, negate()=false true false 
# SFFloat default=0.0, initial=1.0, setValue(2)=2.0, setValue(3.0f)=3.0, setValue(4.0)=4.0 
# MFFloat default=, initial=1 2 3, append(5)=1 2 3 5, inserts(3,4)(0,0)=0 1 2 3 4 5, append(6)=0 1 2 3 4 5 6, size()=7 
# ... get1Value[3]=3.0, remove[1]=0 2 3 4 5 6, set1Value(0,10)=10 2 3 4 5 6, multiply(2)=20 4 6 8 10 12, clear= 
# SFVec3f default=0 0 0, initial=1 2 3, setValue=4 5 6, multiply(2)=8 10 12, normalize()=0.45584232 0.5698029 0.68376344, regex matches()=true 
# regex test SFVec3f().matches(\"1 2 3\")=true, regex test SFVec3f().matches(\"1 2 3 4\")=false, regex test (SFRotationObject.matches(\"0 0 0 0\")=true, failure detecting illegal (zero axis) rotation value 
Scene26.addChildren([Group139])

Sound140 = Sound()
Sound140.location = [0,1.6,0]
# set sound-ellipsoid location height at 1.6m to match typical avatar height 

AudioClip141 = AudioClip()
AudioClip141.description = "chimes"
AudioClip141.url = ["chimes.wav","http://www.web3d.org/x3d/content/examples/ConformanceNist/Sounds/AudioClip/chimes.wav"]
# Scene example fragment from http://www.web3d.org/x3d/content/examples/ConformanceNist/Sounds/AudioClip/default.x3d 
Sound140.source = AudioClip141
Scene26.addChildren([Sound140])

Sound142 = Sound()
Sound142.location = [0,1.6,0]
# set sound-ellipsoid location height at 1.6m to match typical avatar height 

MovieTexture143 = MovieTexture()
MovieTexture143.description = "mpgsys.mpg from ConformanceNist suite"
MovieTexture143.url = ["mpgsys.mpg","http://www.web3d.org/x3d/content/examples/ConformanceNist/Appearance/MovieTexture/mpgsys.mpg"]
# Scene example fragment from http://www.web3d.org/x3d/content/examples/ConformanceNist/Appearance/MovieTexture/mpeg1-systems.x3d 
# Expected containerField='source', allowed containerField values=\"texture\" \"source\" \"back\" \"bottom\" \"front\" \"left\" \"right\" \"top\" \"backTexture\" \"bottomTexture\" \"frontTexture\" \"leftTexture\" \"rightTexture\" \"topTexture\" \"watchList\" 
Sound142.source = MovieTexture143
Scene26.addChildren([Sound142])
# Test success: AnchorObject.isNode()=true, siteAnchor.isNode()=true 
# Test success: AnchorObject.isStatement()=false, siteAnchor.isStatement()=false 
# Test success: ROUTEObject.isNode()=false, orbitPositionROUTE.isNode()=false 
# Test success: ROUTEObject.isStatement()=true, orbitPositionROUTE.isStatement()=true 
# Test success: CommentsBlock.isNode()=false, testComments.isNode()=false 
# Test failure: CommentsBlock.isStatement()=true, testComments.isStatement()=true 

Shape144 = Shape()
Shape144.DEF = "ExtrusionShape"
# ExampleExtrusion isCrossSectionClosed()=true, crossSection='[1.0, 1.0, 1.0, -1.0, -1.0, -1.0, -1.0, 1.0, 1.0, 1.0]' 
# ExampleExtrusion isSpineClosed()=false, spine='[0.0, 0.0, 0.0, 0.0, 1.0, 0.0]' 

Appearance145 = Appearance()
Appearance145.DEF = "TransparentAppearance"

Material146 = Material()
Material146.transparency = 1.0
Appearance145.material = Material146
Shape144.appearance = Appearance145

Extrusion147 = Extrusion()
Extrusion147.DEF = "ExampleExtrusion"
Shape144.geometry = Extrusion147
Scene26.addChildren([Shape144])

Group148 = Group()
# Test MFNode children array as an ordered list consisting of comments, statements, ProtoInstance and nodes 

ProtoDeclare149 = ProtoDeclare()
ProtoDeclare149.name = "NewWorldInfo"

ProtoInterface150 = ProtoInterface()

field151 = field()
field151.accessType = "initializeOnly"
field151.name = "description"
field151.type = "SFString"
ProtoInterface150.addField([field151])
ProtoDeclare149.protoInterface = ProtoInterface150

ProtoBody152 = ProtoBody()

WorldInfo153 = WorldInfo()
ProtoBody152.addChildren([WorldInfo153])
ProtoDeclare149.protoBody = ProtoBody152
Group148.addChildren([ProtoDeclare149])

ProtoInstance154 = ProtoInstance()
ProtoInstance154.DEF = "Proto1"
ProtoInstance154.name = "NewWorldInfo"

fieldValue155 = fieldValue()
fieldValue155.name = "description"
fieldValue155.value = "testing 1 2 3"
ProtoInstance154.addFieldValue([fieldValue155])
Group148.addChildren([ProtoInstance154])

Group156 = Group()
Group156.DEF = "Node2"
# intentionally empty 
Group148.addChildren([Group156])

ProtoInstance157 = ProtoInstance()
ProtoInstance157.DEF = "Proto3"
ProtoInstance157.name = "NewWorldInfo"
Group148.addChildren([ProtoInstance157])

Transform158 = Transform()
Transform158.DEF = "Node4"
# intentionally empty 
Group148.addChildren([Transform158])
# Test satisfactorily creates MFNode children array as an ordered list with mixed content 
Scene26.addChildren([Group148])

ProtoDeclare159 = ProtoDeclare()
ProtoDeclare159.name = "ShaderProto"

ProtoBody160 = ProtoBody()

ProgramShader161 = ProgramShader()
ProtoBody160.addShaders([ProgramShader161])
ProtoDeclare159.protoBody = ProtoBody160
Scene26.addChildren([ProtoDeclare159])

Shape162 = Shape()

Appearance163 = Appearance()
# Test MFNode shaders array as an ordered list consisting of comments, ProtoInstance and nodes 
# Test satisfactorily creates MFNode shaders array as an ordered list with mixed content 

ProgramShader164 = ProgramShader()
ProgramShader164.DEF = "TestShader1"

ShaderProgram165 = ShaderProgram()
ShaderProgram165.DEF = "TestShader2"
ProgramShader164.addPrograms([ShaderProgram165])
Appearance163.addShaders([ProgramShader164])

ProtoInstance166 = ProtoInstance()
ProtoInstance166.DEF = "TestShader3"
ProtoInstance166.name = "ShaderProto"
Appearance163.shaders = ProtoInstance166

ComposedShader167 = ComposedShader()
ComposedShader167.DEF = "TestShader4"

ShaderPart168 = ShaderPart()
ShaderPart168.DEF = "TestShader5"
ComposedShader167.addParts([ShaderPart168])
Appearance163.addShaders([ComposedShader167])
Shape162.appearance = Appearance163
Scene26.addChildren([Shape162])
X3D0.scene = Scene26
