from X3Dpackage import *
X3D0 = X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.3"

head1 = head()
# comment #1 
# comment #2 
# comment #3 
# comment #4 

component2 = component()
component2.name = "Navigation"
component2.level = 3
head1.addComponent([component2])

component3 = component()
component3.name = "Layering"
component3.level = 1
head1.addComponent([component3])

unit4 = unit(category = "angle")
unit4.name = "AngleUnitConversion"
unit4.conversionFactor = 1.0
head1.addUnit([unit4])

unit5 = unit(category = "length")
unit5.name = "LengthUnitConversion"
unit5.conversionFactor = 1.0
head1.addUnit([unit5])

meta6 = meta()
meta6.name = "title"
meta6.content = "HelloWorldProgramOutput.x3d"
head1.addMeta([meta6])

meta7 = meta()
meta7.name = "description"
meta7.content = "Example HelloWorldProgram creates an X3D model using the X3D Java Scene Access Interface (SAI) Library"
head1.addMeta([meta7])

meta8 = meta()
meta8.name = "reference"
meta8.content = "http://www.web3d.org/specifications/java/X3DJSAIL.html"
head1.addMeta([meta8])

meta9 = meta()
meta9.name = "generator"
meta9.content = "HelloWorldProgramOutput.java"
head1.addMeta([meta9])

meta10 = meta()
meta10.name = "created"
meta10.content = "6 September 2016"
head1.addMeta([meta10])

meta11 = meta()
meta11.name = "modified"
meta11.content = "10 September 2018"
head1.addMeta([meta11])

meta12 = meta()
meta12.name = "generator"
meta12.content = "X3D Java Scene Access Interface Library (X3DJSAIL)"
head1.addMeta([meta12])

meta13 = meta()
meta13.name = "generator"
meta13.content = "http://www.web3d.org/specifications/java/examples/HelloWorldProgram.java"
head1.addMeta([meta13])

meta14 = meta()
meta14.name = "generator"
meta14.content = "Netbeans http://www.netbeans.org"
head1.addMeta([meta14])

meta15 = meta()
meta15.name = "creator"
meta15.content = "Don Brutzman"
head1.addMeta([meta15])

meta16 = meta()
meta16.name = "reference"
meta16.content = "https://sourceforge.net/p/x3d/code/HEAD/tree/www.web3d.org/x3d/stylesheets/java/examples/HelloWorldProgramOutput.x3d"
head1.addMeta([meta16])

meta17 = meta()
meta17.name = "reference"
meta17.content = "Console output, ClassicVRML encoding, VRML97 encoding and pretty-print documentation:"
head1.addMeta([meta17])

meta18 = meta()
meta18.name = "reference"
meta18.content = "HelloWorldProgramOutput.txt"
head1.addMeta([meta18])

meta19 = meta()
meta19.name = "reference"
meta19.content = "HelloWorldProgramOutput.x3dv"
head1.addMeta([meta19])

meta20 = meta()
meta20.name = "reference"
meta20.content = "HelloWorldProgramOutput.wrl"
head1.addMeta([meta20])

meta21 = meta()
meta21.name = "reference"
meta21.content = "HelloWorldProgramOutput.html"
head1.addMeta([meta21])

meta22 = meta()
meta22.name = "X3dValidator"
meta22.content = "https://savage.nps.edu/X3dValidator?url=http://www.web3d.org/specifications/java/examples/HelloWorldProgramOutput.x3d"
head1.addMeta([meta22])

meta23 = meta()
meta23.name = "identifier"
meta23.content = "http://www.web3d.org/specifications/java/examples/HelloWorldProgramOutput.x3d"
head1.addMeta([meta23])

meta24 = meta()
meta24.name = "license"
meta24.content = "../license.html"
head1.addMeta([meta24])

meta25 = meta()
meta25.name = "SpecialTest"
meta25.content = "tested sat: name value cannot contain embedded space character"
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

WorldInfo30 = WorldInfo()
WorldInfo30.DEF = "WorldInfoDEF"
WorldInfo30.title = "HelloWorldProgram produced by X3D Java SAI Library (X3DJSAIL)"
Scene26.addChildren([WorldInfo30])

WorldInfo31 = WorldInfo()
WorldInfo31.USE = "WorldInfoDEF"
Scene26.addChildren([WorldInfo31])

WorldInfo32 = WorldInfo()
WorldInfo32.USE = "WorldInfoDEF"
Scene26.addChildren([WorldInfo32])

MetadataString33 = MetadataString()
MetadataString33.DEF = "scene.addChildMetadata"
MetadataString33.name = "test"
MetadataString33.value = ["Top-level root Metadata node beneath Scene needs to be one of '-children' in JSON encoding"]
Scene26.addChildren([MetadataString33])

LayerSet34 = LayerSet(order = [0])
LayerSet34.DEF = "scene.addChildLayerSetTest"
Scene26.addLayerSet([LayerSet34])

Transform35 = Transform()
Transform35.DEF = "LogoGeometryTransform"
Transform35.translation = [0,1.5,0]

Anchor36 = Anchor()
Anchor36.description = "select for X3D Java SAI Library (X3DJSAIL) description"
Anchor36.url = ["../X3DJSAIL.html","http://www.web3d.org/specifications/java/X3DJSAIL.html"]

Shape37 = Shape()
Shape37.DEF = "BoxShape"

Appearance38 = Appearance()

Material39 = Material()
Material39.DEF = "GreenMaterial"
Material39.diffuseColor = [0,1,1]
Material39.emissiveColor = [0.8,0,0]
Material39.transparency = 0.1
Appearance38.material = Material39

ImageTexture40 = ImageTexture()
ImageTexture40.url = ["images/X3dJavaSceneAccessInterfaceSaiLibrary.png","http://www.web3d.org/specifications/java/examples/images/X3dJavaSceneAccessInterfaceSaiLibrary.png"]
Appearance38.texture = ImageTexture40
Shape37.appearance = Appearance38

Box41 = Box()
Box41.DEF = "test-NMTOKEN_regex.0123456789"
Box41.class_ = "untextured"
Shape37.geometry = Box41
Anchor36.addChildren([Shape37])
Transform35.addChildren([Anchor36])
Scene26.addChildren([Transform35])

Shape42 = Shape()
Shape42.DEF = "LineShape"

Appearance43 = Appearance()

Material44 = Material()
Material44.emissiveColor = [0.6,0.19607843,0.8]
Appearance43.material = Material44
Shape42.appearance = Appearance43

IndexedLineSet45 = IndexedLineSet(coordIndex = [0,1,2,3,4,0])
# Coordinate 3-tuple point count: 6 

Coordinate46 = Coordinate()
Coordinate46.point = [0,1.5,0,2,1.5,0,2,1.5,-2,-2,1.5,-2,-2,1.5,0,0,1.5,0]
IndexedLineSet45.coord = Coordinate46
Shape42.geometry = IndexedLineSet45
Scene26.addChildren([Shape42])

PositionInterpolator47 = PositionInterpolator()
PositionInterpolator47.DEF = "BoxPathAnimator"
PositionInterpolator47.key = [0,0.125,0.375,0.625,0.875,1]
PositionInterpolator47.keyValue = [0,1.5,0,2,1.5,0,2,1.5,-2,-2,1.5,-2,-2,1.5,0,0,1.5,0]
Scene26.addChildren([PositionInterpolator47])

TimeSensor48 = TimeSensor()
TimeSensor48.DEF = "OrbitClock"
TimeSensor48.cycleInterval = 8.0
TimeSensor48.loop = True
Scene26.addChildren([TimeSensor48])

ROUTE49 = ROUTE()
ROUTE49.fromField = "fraction_changed"
ROUTE49.fromNode = "OrbitClock"
ROUTE49.toField = "set_fraction"
ROUTE49.toNode = "BoxPathAnimator"
Scene26.addChildren([ROUTE49])

ROUTE50 = ROUTE()
ROUTE50.fromField = "value_changed"
ROUTE50.fromNode = "BoxPathAnimator"
ROUTE50.toField = "set_translation"
ROUTE50.toNode = "LogoGeometryTransform"
Scene26.addChildren([ROUTE50])

Transform51 = Transform()
Transform51.DEF = "TextTransform"
Transform51.translation = [0,-1.5,0]

Shape52 = Shape()

Appearance53 = Appearance()

Material54 = Material()
Material54.USE = "GreenMaterial"
Appearance53.material = Material54
Shape52.appearance = Appearance53

Text55 = Text()
Text55.string = ["X3D Java","SAI Library","X3DJSAIL"]
# Comment example A, plain quotation marks: He said, \"Immel did it!\" 
# Comment example B, XML character entities: He said, &quot;Immel did it!&quot; 

MetadataSet56 = MetadataSet()
MetadataSet56.name = "EscapedQuotationMarksMetadataSet"

MetadataString57 = MetadataString()
MetadataString57.name = "quotesTestC"
MetadataString57.value = ["MFString example C, backslash-escaped quotes: He said, \"Immel did it!\""]
MetadataSet56.value = MetadataString57

MetadataString58 = MetadataString()
MetadataString58.name = "extraChildTest"
MetadataString58.value = ["checks MetadataSetObject addValue() method"]
MetadataSet56.value = MetadataString58
Text55.metadata = MetadataSet56

FontStyle59 = FontStyle(family = ["SERIF"], justify = ["MIDDLE","MIDDLE"])
Text55.fontStyle = FontStyle59
Shape52.geometry = Text55
Transform51.addChildren([Shape52])

Collision60 = Collision()
# test containerField='proxy' 

Shape61 = Shape()
Shape61.DEF = "ProxyShape"
# alternative XML encoding: Text string='\"One, Two, Comment\" \"\" \"He said, \\&quot;Immel did it!\\&quot;\"' 
# alternative XML encoding: Text string='\"One, Two, Comment\" \"\" \"He said, \\&quot;Immel did it!\\&quot;\" \"\"' 
# alternative Java source: .setString(new String [] {\"One, Two, Comment\", \"\", \"He said, \\\"Immel did it!\\\"\"}) 
# reference: http://www.web3d.org/x3d/content/examples/Basic/X3dSpecifications/StringArrayEncodingExamplesIndex.html 

Text62 = Text()
Text62.string = ["One, Two, Text","","He said, \"Immel did it!\" \"\""]
Shape61.geometry = Text62
Collision60.proxy = Shape61
Transform51.addChildren([Collision60])
# It's a beautiful world 
# ... for you! 
# https://en.wikipedia.org/wiki/Beautiful_World_(Devo_song) 
Scene26.addChildren([Transform51])
# repeatedly spin 180 degrees as a readable special effect 

OrientationInterpolator63 = OrientationInterpolator()
OrientationInterpolator63.DEF = "SpinInterpolator"
OrientationInterpolator63.key = [0,0.5,1]
OrientationInterpolator63.keyValue = [0,1,0,4.712389,0,1,0,0,0,1,0,1.5707964]
Scene26.addChildren([OrientationInterpolator63])

TimeSensor64 = TimeSensor()
TimeSensor64.DEF = "SpinClock"
TimeSensor64.cycleInterval = 5.0
TimeSensor64.loop = True
Scene26.addChildren([TimeSensor64])

ROUTE65 = ROUTE()
ROUTE65.fromField = "fraction_changed"
ROUTE65.fromNode = "SpinClock"
ROUTE65.toField = "set_fraction"
ROUTE65.toNode = "SpinInterpolator"
Scene26.addChildren([ROUTE65])

ROUTE66 = ROUTE()
ROUTE66.fromField = "value_changed"
ROUTE66.fromNode = "SpinInterpolator"
ROUTE66.toField = "rotation"
ROUTE66.toNode = "TextTransform"
Scene26.addChildren([ROUTE66])

Group67 = Group()
Group67.DEF = "BackgroundGroup"

Background68 = Background()
Background68.DEF = "GradualBackground"
Group67.addChildren([Background68])

Script69 = Script()
Script69.DEF = "colorTypeConversionScript"

field70 = field()
field70.name = "colorInput"
field70.accessType = "inputOnly"
field70.type = "SFColor"
Script69.addField([field70])

field71 = field()
field71.name = "colorsOutput"
field71.accessType = "outputOnly"
field71.type = "MFColor"
Script69.addField([field71])

Script69.setSourceCode('''\n"+
"ecmascript:\n"+
"\n"+
"function colorInput (eventValue) // Example source code\n"+
"{\n"+
"   colorsOutput = new MFColor(eventValue); // assigning value sends output event\n"+
"// Browser.print('colorInput=' + eventValue + ', colorsOutput=' + colorsOutput + '\\n');\n"+
"}\n"+
"''')
Group67.addChildren([Script69])

ColorInterpolator72 = ColorInterpolator()
ColorInterpolator72.DEF = "ColorAnimator"
ColorInterpolator72.key = [0,0.5,1]
ColorInterpolator72.keyValue = [0.9411765,1,1,0.29411766,0,0.50980395,0.9411765,1,1]
# AZURE to INDIGO and back again 
Group67.addChildren([ColorInterpolator72])

TimeSensor73 = TimeSensor()
TimeSensor73.DEF = "ColorClock"
TimeSensor73.cycleInterval = 60.0
TimeSensor73.loop = True
Group67.addChildren([TimeSensor73])

ROUTE74 = ROUTE()
ROUTE74.fromField = "colorsOutput"
ROUTE74.fromNode = "colorTypeConversionScript"
ROUTE74.toField = "skyColor"
ROUTE74.toNode = "GradualBackground"
Group67.addChildren([ROUTE74])

ROUTE75 = ROUTE()
ROUTE75.fromField = "value_changed"
ROUTE75.fromNode = "ColorAnimator"
ROUTE75.toField = "colorInput"
ROUTE75.toNode = "colorTypeConversionScript"
Group67.addChildren([ROUTE75])

ROUTE76 = ROUTE()
ROUTE76.fromField = "fraction_changed"
ROUTE76.fromNode = "ColorClock"
ROUTE76.toField = "set_fraction"
ROUTE76.toNode = "ColorAnimator"
Group67.addChildren([ROUTE76])
Scene26.addChildren([Group67])

ProtoDeclare77 = ProtoDeclare()
ProtoDeclare77.name = "ArtDeco01Material"
ProtoDeclare77.appinfo = "tooltip: ArtDeco01Material prototype is a Material node"

ProtoInterface78 = ProtoInterface()

field79 = field()
field79.name = "description"
field79.accessType = "inputOutput"
field79.appinfo = "tooltip for descriptionField"
field79.type = "SFString"
field79.value = "ArtDeco01Material prototype is a Material node"
ProtoInterface78.addField([field79])

field80 = field()
field80.name = "enabled"
field80.accessType = "inputOutput"
field80.type = "SFBool"
field80.value = "true"
ProtoInterface78.addField([field80])
ProtoDeclare77.protoInterface = ProtoInterface78

ProtoBody81 = ProtoBody()
# Initial node of ProtoBody determines prototype node type 

Material82 = Material()
Material82.ambientIntensity = 0.25
Material82.diffuseColor = [0.282435,0.085159,0.134462]
Material82.shininess = 0.127273
Material82.specularColor = [0.276305,0.11431,0.139857]
ProtoBody81.addChildren([Material82])
# [HelloWorldProgram diagnostic] should be connected to scene graph: ArtDeco01ProtoDeclare.getNodeType()=\"Material\" 
# presence of follow-on TouchSensor shows that additional nodes are allowed in ProtoBody after initial node, regardless of node types 

TouchSensor83 = TouchSensor()
TouchSensor83.description = "within ProtoBody"

IS84 = IS()

connect85 = connect()
connect85.nodeField = "description"
connect85.protoField = "description"
IS84.addConnect([connect85])

connect86 = connect()
connect86.nodeField = "enabled"
connect86.protoField = "enabled"
IS84.addConnect([connect86])
TouchSensor83.IS = IS84
ProtoBody81.addChildren([TouchSensor83])
ProtoDeclare77.protoBody = ProtoBody81
Scene26.addChildren([ProtoDeclare77])

ExternProtoDeclare87 = ExternProtoDeclare()
ExternProtoDeclare87.name = "ArtDeco02Material"
ExternProtoDeclare87.appinfo = "this is a different Material node"
ExternProtoDeclare87.url = ["http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/ArtDecoPrototypesExcerpt.x3d#ArtDeco02Material","http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/ArtDecoPrototypesExcerpt.x3dv#ArtDeco02Material"]
# [HelloWorldProgram diagnostic] ArtDeco02ExternProtoDeclare.getNodeType()=\"ERROR_UNKNOWN_EXTERNPROTODECLARE_NODE_TYPE: ExternProtoDeclare name='ArtDeco02Material' type cannot be remotely accessed at run time, TODO X3DJSAIL needs to add further capability.\" 

field88 = field()
field88.name = "description"
field88.accessType = "inputOutput"
field88.appinfo = "tooltip for descriptionField"
field88.type = "SFString"
ExternProtoDeclare87.addField([field88])
Scene26.addChildren([ExternProtoDeclare87])
# Tested ArtDeco01ProtoInstance, ArtDeco02ProtoInstance for improper node type when ProtoInstance is added in wrong place 

Shape89 = Shape()
Shape89.DEF = "TestShape1"

Appearance90 = Appearance()
Appearance90.DEF = "TestAppearance1"
# ArtDeco01Material prototype goes here... TODO ensure setContainerField is handled in exported Java 

ProtoInstance91 = ProtoInstance()
ProtoInstance91.name = "ArtDeco01Material"
# [HelloWorldProgram diagnostic] ArtDeco01ProtoInstance.getNodeType()=\"Material\" 

fieldValue92 = fieldValue()
fieldValue92.name = "description"
fieldValue92.value = "ArtDeco01Material can substitute for a Material node"
ProtoInstance91.addFieldValue([fieldValue92])
Appearance90.material = ProtoInstance91
Shape89.appearance = Appearance90

Sphere93 = Sphere(radius = 0.001)
Shape89.geometry = Sphere93
Scene26.addChildren([Shape89])

Shape94 = Shape()
Shape94.DEF = "TestShape2"

Appearance95 = Appearance()
Appearance95.DEF = "TestAppearance2"
# ArtDeco02Material prototype goes here... TODO ensure setContainerField is handled in exported Java 

ProtoInstance96 = ProtoInstance()
ProtoInstance96.DEF = "ArtDeco02MaterialDEF"
ProtoInstance96.name = "ArtDeco02Material"
# [HelloWorldProgram diagnostic] ArtDeco02ProtoInstance.getNodeType()=\"ERROR_UNKNOWN_EXTERNPROTODECLARE_NODE_TYPE: ExternProtoDeclare name='ArtDeco02Material' type cannot be remotely accessed at run time, TODO X3DJSAIL needs to add further capability.\" 

fieldValue97 = fieldValue()
fieldValue97.name = "description"
fieldValue97.value = "ArtDeco02Material can substitute for another Material node"
ProtoInstance96.addFieldValue([fieldValue97])
Appearance95.material = ProtoInstance96
Shape94.appearance = Appearance95

Cone98 = Cone(bottomRadius = 0.001, height = 0.001)
Shape94.geometry = Cone98
Scene26.addChildren([Shape94])

Shape99 = Shape()
Shape99.DEF = "TestShape3"

Appearance100 = Appearance()
Appearance100.DEF = "TestAppearance3"
# ArtDeco02Material ProtoInstance USE goes here... 

ProtoInstance101 = ProtoInstance()
ProtoInstance101.USE = "ArtDeco02MaterialDEF"
Appearance100.material = ProtoInstance101
Shape99.appearance = Appearance100

Cylinder102 = Cylinder(height = 0.001, radius = 0.001)
Shape99.geometry = Cylinder102
Scene26.addChildren([Shape99])

Inline103 = Inline()
Inline103.DEF = "inlineSceneDef"
Inline103.url = ["someOtherScene.x3d"]
Scene26.addChildren([Inline103])

IMPORT104 = IMPORT()
IMPORT104.AS = "WorldInfoDEF2"
IMPORT104.importedDEF = "WorldInfoDEF"
IMPORT104.inlineDEF = "inlineSceneDef"
Scene26.addChildren([IMPORT104])

EXPORT105 = EXPORT()
EXPORT105.AS = "WorldInfoDEF3"
EXPORT105.localDEF = "WorldInfoDEF"
Scene26.addChildren([EXPORT105])

ProtoDeclare106 = ProtoDeclare()
ProtoDeclare106.name = "MaterialModulator"
ProtoDeclare106.appinfo = "mimic a Material node and modulate fields as an animation effect"
ProtoDeclare106.documentation = "http://x3dgraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/MaterialModulatorIndex.html"

ProtoInterface107 = ProtoInterface()

field108 = field()
field108.name = "enabled"
field108.accessType = "inputOutput"
field108.type = "SFBool"
field108.value = "true"
ProtoInterface107.addField([field108])

field109 = field()
field109.name = "diffuseColor"
field109.accessType = "inputOutput"
field109.type = "SFColor"
field109.value = "0 0 0"
ProtoInterface107.addField([field109])

field110 = field()
field110.name = "emissiveColor"
field110.accessType = "inputOutput"
field110.type = "SFColor"
field110.value = "0.05 0.05 0.5"
ProtoInterface107.addField([field110])

field111 = field()
field111.name = "specularColor"
field111.accessType = "inputOutput"
field111.type = "SFColor"
field111.value = "0 0 0"
ProtoInterface107.addField([field111])

field112 = field()
field112.name = "transparency"
field112.accessType = "inputOutput"
field112.type = "SFFloat"
field112.value = "0.0"
ProtoInterface107.addField([field112])

field113 = field()
field113.name = "shininess"
field113.accessType = "inputOutput"
field113.type = "SFFloat"
field113.value = "0.0"
ProtoInterface107.addField([field113])

field114 = field()
field114.name = "ambientIntensity"
field114.accessType = "inputOutput"
field114.type = "SFFloat"
field114.value = "0.0"
ProtoInterface107.addField([field114])
ProtoDeclare106.protoInterface = ProtoInterface107

ProtoBody115 = ProtoBody()

Material116 = Material()
Material116.DEF = "MaterialNode"

IS117 = IS()

connect118 = connect()
connect118.nodeField = "diffuseColor"
connect118.protoField = "diffuseColor"
IS117.addConnect([connect118])

connect119 = connect()
connect119.nodeField = "emissiveColor"
connect119.protoField = "emissiveColor"
IS117.addConnect([connect119])

connect120 = connect()
connect120.nodeField = "specularColor"
connect120.protoField = "specularColor"
IS117.addConnect([connect120])

connect121 = connect()
connect121.nodeField = "transparency"
connect121.protoField = "transparency"
IS117.addConnect([connect121])

connect122 = connect()
connect122.nodeField = "shininess"
connect122.protoField = "shininess"
IS117.addConnect([connect122])

connect123 = connect()
connect123.nodeField = "ambientIntensity"
connect123.protoField = "ambientIntensity"
IS117.addConnect([connect123])
Material116.IS = IS117
ProtoBody115.addChildren([Material116])
# Only first node (the node type) is renderable, others are along for the ride 

Script124 = Script()
Script124.DEF = "MaterialModulatorScript"

field125 = field()
field125.name = "enabled"
field125.accessType = "inputOutput"
field125.type = "SFBool"
Script124.addField([field125])

field126 = field()
field126.name = "diffuseColor"
field126.accessType = "inputOutput"
field126.type = "SFColor"
Script124.addField([field126])

field127 = field()
field127.name = "newColor"
field127.accessType = "outputOnly"
field127.type = "SFColor"
Script124.addField([field127])

field128 = field()
field128.name = "clockTrigger"
field128.accessType = "inputOnly"
field128.type = "SFTime"
Script124.addField([field128])

IS129 = IS()

connect130 = connect()
connect130.nodeField = "enabled"
connect130.protoField = "enabled"
IS129.addConnect([connect130])

connect131 = connect()
connect131.nodeField = "diffuseColor"
connect131.protoField = "diffuseColor"
IS129.addConnect([connect131])
Script124.IS = IS129

Script124.setSourceCode('''\n"+
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
ProtoBody115.addChildren([Script124])
ProtoDeclare106.protoBody = ProtoBody115
Scene26.addChildren([ProtoDeclare106])
# Test success: declarative statement createDeclarativeShapeTests() 

Group132 = Group()
Group132.DEF = "DeclarativeGroupExample"

Shape133 = Shape()

MetadataString134 = MetadataString()
MetadataString134.DEF = "FindableMetadataStringTest"
MetadataString134.name = "findThisNameValue"
MetadataString134.value = ["test case"]
Shape133.metadata = MetadataString134

Appearance135 = Appearance()
Appearance135.DEF = "DeclarativeAppearanceExample"
# DeclarativeMaterialExample gets overridden by subsequently added MaterialModulator ProtoInstance 

ProtoInstance136 = ProtoInstance()
ProtoInstance136.DEF = "MyMaterialModulator"
ProtoInstance136.name = "MaterialModulator"
Appearance135.material = ProtoInstance136
Shape133.appearance = Appearance135

Cone137 = Cone(bottom = False, bottomRadius = 0.05, height = 0.1)
Shape133.geometry = Cone137
Group132.addChildren([Shape133])
# Test success: declarativeGroup.addChild() singleton pipeline method 
Scene26.addChildren([Group132])
# Test success: declarative statement addChild() 
# Test success: x3dModel.findNodeByDEF(DeclarativeAppearanceExample) = <Appearance DEF='DeclarativeAppearanceExample'/> i.e. <Appearance DEF='DeclarativeAppearanceExample'> <!- - DeclarativeMaterialExample gets overridden by subsequently added MaterialModulator ProtoInstance - -> <ProtoInstance DEF='MyMaterialModulator' name='MaterialModulator' containerField='material'/> </Appearance> 
# Test success: x3dModel.findElementByNameValue(findThisNameValue) = <MetadataString DEF='FindableMetadataStringTest' name='findThisNameValue' value='\"test case\"'/> 
# Test success: x3dModel.findElementByNameValue(\"ArtDeco01Material\", \"ProtoDeclare\") found 
# Test success: x3dModel.findElementByNameValue(\"MaterialModulator\", \"ProtoDeclare\") found 
# Test success: x3dModel.findElementByNameValue(\"MaterialModulator\", \"ProtoInstance\") found 

Group138 = Group()
Group138.DEF = "TestFieldObjectsGroup"
# testFieldObjects() results 
# SFBool default=true, true=true, false=false, negate()=true 
# MFBool default=, initial=true false true, negate()=false true false 
# SFFloat default=0.0, initial=1.0, setValue(2)=2.0, setValue(3.0f)=3.0, setValue(4.0)=4.0 
# MFFloat default=, initial=1 2 3, append(5)=1 2 3 5, inserts(3,4)(0,0)=0 1 2 3 4 5, append(6)=0 1 2 3 4 5 6, size()=7 
# ... get1Value[3]=3.0, remove[1]=0 2 3 4 5 6, set1Value(0,10)=10 2 3 4 5 6, multiply(2)=20 4 6 8 10 12, clear= 
# SFVec3f default=0 0 0, initial=1 2 3, setValue=4 5 6, multiply(2)=8 10 12, normalize()=0.45584232 0.5698029 0.68376344, regex matches()=true 
# regex test SFVec3f().matches(\"1 2 3\")=true, regex test SFVec3f().matches(\"1 2 3 4\")=false, regex test (SFRotationObject.matches(\"0 0 0 0\")=true, failure detecting illegal (zero axis) rotation value 
Scene26.addChildren([Group138])

Sound139 = Sound()
Sound139.location = [0,1.6,0]
# set sound-ellipsoid location height at 1.6m to match typical avatar height 

AudioClip140 = AudioClip()
AudioClip140.description = "chimes"
AudioClip140.url = ["chimes.wav","http://www.web3d.org/x3d/content/examples/ConformanceNist/Sounds/AudioClip/chimes.wav"]
# Scene example fragment from http://www.web3d.org/x3d/content/examples/ConformanceNist/Sounds/AudioClip/default.x3d 
Sound139.source = AudioClip140
Scene26.addChildren([Sound139])

Sound141 = Sound()
Sound141.location = [0,1.6,0]
# set sound-ellipsoid location height at 1.6m to match typical avatar height 

MovieTexture142 = MovieTexture()
MovieTexture142.description = "mpgsys.mpg from ConformanceNist suite"
MovieTexture142.url = ["mpgsys.mpg","http://www.web3d.org/x3d/content/examples/ConformanceNist/Appearance/MovieTexture/mpgsys.mpg"]
# Scene example fragment from http://www.web3d.org/x3d/content/examples/ConformanceNist/Appearance/MovieTexture/mpeg1-systems.x3d 
# Expected containerField='source', allowed containerField values=\"texture\" \"source\" \"back\" \"bottom\" \"front\" \"left\" \"right\" \"top\" \"backTexture\" \"bottomTexture\" \"frontTexture\" \"leftTexture\" \"rightTexture\" \"topTexture\" \"watchList\" 
Sound141.source = MovieTexture142
Scene26.addChildren([Sound141])
# Test success: AnchorObject.isNode()=true, siteAnchor.isNode()=true 
# Test success: AnchorObject.isStatement()=false, siteAnchor.isStatement()=false 
# Test success: ROUTEObject.isNode()=false, orbitPositionROUTE.isNode()=false 
# Test success: ROUTEObject.isStatement()=true, orbitPositionROUTE.isStatement()=true 
# Test success: CommentsBlock.isNode()=false, testComments.isNode()=false 
# Test failure: CommentsBlock.isStatement()=true, testComments.isStatement()=true 

Shape143 = Shape()
Shape143.DEF = "ExtrusionShape"
# ExampleExtrusion isCrossSectionClosed()=true, crossSection='[1.0, 1.0, 1.0, -1.0, -1.0, -1.0, -1.0, 1.0, 1.0, 1.0]' 
# ExampleExtrusion isSpineClosed()=false, spine='[0.0, 0.0, 0.0, 0.0, 1.0, 0.0]' 

Appearance144 = Appearance()
Appearance144.DEF = "TransparentAppearance"

Material145 = Material()
Material145.transparency = 1.0
Appearance144.material = Material145
Shape143.appearance = Appearance144

Extrusion146 = Extrusion()
Extrusion146.DEF = "ExampleExtrusion"
Shape143.geometry = Extrusion146
Scene26.addChildren([Shape143])
X3D0.scene = Scene26
