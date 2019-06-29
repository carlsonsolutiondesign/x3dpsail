import x3dpsail
X3D0 = x3dpsail.X3D()
X3D0.setProfile("Immersive")
X3D0.setVersion("3.3")
# x3dVersionComparisonTest for this model: supportsX3dVersion(X3DObject.VERSION_3_0)=true 
head1 = x3dpsail.head()
# comment #1 
# comment #2 
# comment #3 
# comment #4 
component2 = x3dpsail.component()
component2.setLevel(3)
component2.setName("Navigation")

head1.addComponent(component2)
component3 = x3dpsail.component()
component3.setLevel(1)
component3.setName("Shaders")

head1.addComponent(component3)
component4 = x3dpsail.component()
component4.setLevel(1)
component4.setName("Layering")

head1.addComponent(component4)
unit5 = x3dpsail.unit()
unit5.setCategory("angle")
unit5.setConversionFactor(1.0)
unit5.setName("AngleUnitConversion")

head1.addUnit(unit5)
unit6 = x3dpsail.unit()
unit6.setCategory("length")
unit6.setConversionFactor(1.0)
unit6.setName("LengthUnitConversion")

head1.addUnit(unit6)
meta7 = x3dpsail.meta()
meta7.setContent("HelloWorldProgramOutput.x3d")
meta7.setName("title")

head1.addMeta(meta7)
meta8 = x3dpsail.meta()
meta8.setContent("Example HelloWorldProgram creates an X3D model using the X3D Java Scene Access Interface Library (X3DJSAIL)")
meta8.setName("description")

head1.addMeta(meta8)
meta9 = x3dpsail.meta()
meta9.setContent("http://www.web3d.org/specifications/java/X3DJSAIL.html")
meta9.setName("reference")

head1.addMeta(meta9)
meta10 = x3dpsail.meta()
meta10.setContent("HelloWorldProgramOutput.java")
meta10.setName("generator")

head1.addMeta(meta10)
meta11 = x3dpsail.meta()
meta11.setContent("6 September 2016")
meta11.setName("created")

head1.addMeta(meta11)
meta12 = x3dpsail.meta()
meta12.setContent("27 December 2018")
meta12.setName("modified")

head1.addMeta(meta12)
meta13 = x3dpsail.meta()
meta13.setContent("X3D Java Scene Access Interface Library (X3DJSAIL)")
meta13.setName("generator")

head1.addMeta(meta13)
meta14 = x3dpsail.meta()
meta14.setContent("http://www.web3d.org/specifications/java/examples/HelloWorldProgram.java")
meta14.setName("generator")

head1.addMeta(meta14)
meta15 = x3dpsail.meta()
meta15.setContent("Netbeans http://www.netbeans.org")
meta15.setName("generator")

head1.addMeta(meta15)
meta16 = x3dpsail.meta()
meta16.setContent("Don Brutzman")
meta16.setName("creator")

head1.addMeta(meta16)
meta17 = x3dpsail.meta()
meta17.setContent("https://sourceforge.net/p/x3d/code/HEAD/tree/www.web3d.org/x3d/stylesheets/java/examples/HelloWorldProgramOutput.x3d")
meta17.setName("reference")

head1.addMeta(meta17)
meta18 = x3dpsail.meta()
meta18.setContent("Console output, ClassicVRML encoding, VRML97 encoding and pretty-print documentation:")
meta18.setName("reference")

head1.addMeta(meta18)
meta19 = x3dpsail.meta()
meta19.setContent("HelloWorldProgramOutput.txt")
meta19.setName("reference")

head1.addMeta(meta19)
meta20 = x3dpsail.meta()
meta20.setContent("HelloWorldProgramOutput.x3dv")
meta20.setName("reference")

head1.addMeta(meta20)
meta21 = x3dpsail.meta()
meta21.setContent("HelloWorldProgramOutput.wrl")
meta21.setName("reference")

head1.addMeta(meta21)
meta22 = x3dpsail.meta()
meta22.setContent("HelloWorldProgramOutput.html")
meta22.setName("reference")

head1.addMeta(meta22)
meta23 = x3dpsail.meta()
meta23.setContent("https://savage.nps.edu/X3dValidator?url=http://www.web3d.org/specifications/java/examples/HelloWorldProgramOutput.x3d")
meta23.setName("reference")

head1.addMeta(meta23)
meta24 = x3dpsail.meta()
meta24.setContent("http://www.web3d.org/specifications/java/examples/HelloWorldProgramOutput.x3d")
meta24.setName("identifier")

head1.addMeta(meta24)
meta25 = x3dpsail.meta()
meta25.setContent("../license.html")
meta25.setName("license")

head1.addMeta(meta25)

X3D0.setHead(head1)
Scene26 = x3dpsail.Scene()
ViewpointGroup27 = x3dpsail.ViewpointGroup()
ViewpointGroup27.setDescription("Available viewpoints")
Viewpoint28 = x3dpsail.Viewpoint()
Viewpoint28.setDEF("DefaultView")
Viewpoint28.setDescription("Hello X3DJSAIL")

ViewpointGroup27.addChildren(Viewpoint28)
Viewpoint29 = x3dpsail.Viewpoint()
Viewpoint29.setDEF("TopDownView")
Viewpoint29.setDescription("top-down view from above")
Viewpoint29.setOrientation([1,0,0,-1.570796])
Viewpoint29.setPosition([0,100,0])

ViewpointGroup27.addChildren(Viewpoint29)

Scene26.addChildren(ViewpointGroup27)
NavigationInfo30 = x3dpsail.NavigationInfo()
NavigationInfo30.setAvatarSize([0.25,1.6,0.75])
NavigationInfo30.setTransitionType(["LINEAR"])
NavigationInfo30.setType(["EXAMINE","FLY","ANY"])

Scene26.addChildren(NavigationInfo30)
WorldInfo31 = x3dpsail.WorldInfo()
WorldInfo31.setDEF("WorldInfoDEF")
WorldInfo31.setTitle("HelloWorldProgram produced by X3D Java SAI Library (X3DJSAIL)")

Scene26.addChildren(WorldInfo31)
WorldInfo32 = x3dpsail.WorldInfo()
WorldInfo32.setUSE("WorldInfoDEF")

Scene26.addChildren(WorldInfo32)
WorldInfo33 = x3dpsail.WorldInfo()
WorldInfo33.setUSE("WorldInfoDEF")

Scene26.addChildren(WorldInfo33)
MetadataString34 = x3dpsail.MetadataString()
MetadataString34.setDEF("scene.addChildMetadata")
MetadataString34.setName("test")
MetadataString34.setValue(["Top-level root Metadata node beneath Scene needs to be one of '-children' in JSON encoding"])

Scene26.addMetadata(MetadataString34)
LayerSet35 = x3dpsail.LayerSet()
LayerSet35.setDEF("scene.addChildLayerSetTest")
LayerSet35.setOrder([0])

Scene26.addLayerSet(LayerSet35)
Transform36 = x3dpsail.Transform()
Transform36.setDEF("LogoGeometryTransform")
Transform36.setTranslation([0,1.5,0])
Anchor37 = x3dpsail.Anchor()
Anchor37.setDescription("select for X3D Java SAI Library (X3DJSAIL) description")
Anchor37.setUrl(["../X3DJSAIL.html","http://www.web3d.org/specifications/java/X3DJSAIL.html"])
Shape38 = x3dpsail.Shape()
Shape38.setDEF("BoxShape")
Appearance39 = x3dpsail.Appearance()
Material40 = x3dpsail.Material()
Material40.setDEF("GreenMaterial")
Material40.setDiffuseColor([0,1,1])
Material40.setEmissiveColor([0.8,0,0])
Material40.setTransparency(0.1)

Appearance39.setMaterial(Material40)
ImageTexture41 = x3dpsail.ImageTexture()
ImageTexture41.setUrl(["images/X3dJavaSceneAccessInterfaceSaiLibrary.png","http://www.web3d.org/specifications/java/examples/images/X3dJavaSceneAccessInterfaceSaiLibrary.png"])

Appearance39.setTexture(ImageTexture41)

Shape38.setAppearance(Appearance39)
Box42 = x3dpsail.Box()
Box42.setDEF("test-NMTOKEN_regex.0123456789")
Box42.setCssClass("untextured")

Shape38.setGeometry(Box42)

Anchor37.addChildren(Shape38)

Transform36.addChildren(Anchor37)

Scene26.addChildren(Transform36)
Shape43 = x3dpsail.Shape()
Shape43.setDEF("LineShape")
Appearance44 = x3dpsail.Appearance()
Material45 = x3dpsail.Material()
Material45.setEmissiveColor([0.6,0.19607843,0.8])

Appearance44.setMaterial(Material45)

Shape43.setAppearance(Appearance44)
IndexedLineSet46 = x3dpsail.IndexedLineSet()
IndexedLineSet46.setCoordIndex([0,1,2,3,4,0])
# Coordinate 3-tuple point count: 6 
Coordinate47 = x3dpsail.Coordinate()
Coordinate47.setPoint([0,1.5,0,2,1.5,0,2,1.5,-2,-2,1.5,-2,-2,1.5,0,0,1.5,0])

IndexedLineSet46.setCoord(Coordinate47)

Shape43.setGeometry(IndexedLineSet46)

Scene26.addChildren(Shape43)
PositionInterpolator48 = x3dpsail.PositionInterpolator()
PositionInterpolator48.setDEF("BoxPathAnimator")
PositionInterpolator48.setKey([0,0.125,0.375,0.625,0.875,1])
PositionInterpolator48.setKeyValue([0,1.5,0,2,1.5,0,2,1.5,-2,-2,1.5,-2,-2,1.5,0,0,1.5,0])

Scene26.addChildren(PositionInterpolator48)
TimeSensor49 = x3dpsail.TimeSensor()
TimeSensor49.setDEF("OrbitClock")
TimeSensor49.setCycleInterval(8.0)
TimeSensor49.setLoop(True)

Scene26.addChildren(TimeSensor49)
ROUTE50 = x3dpsail.ROUTE()
ROUTE50.setFromField("fraction_changed")
ROUTE50.setFromNode("OrbitClock")
ROUTE50.setToField("set_fraction")
ROUTE50.setToNode("BoxPathAnimator")

Scene26.addChildren(ROUTE50)
ROUTE51 = x3dpsail.ROUTE()
ROUTE51.setFromField("value_changed")
ROUTE51.setFromNode("BoxPathAnimator")
ROUTE51.setToField("set_translation")
ROUTE51.setToNode("LogoGeometryTransform")

Scene26.addChildren(ROUTE51)
Transform52 = x3dpsail.Transform()
Transform52.setDEF("TextTransform")
Transform52.setTranslation([0,-1.5,0])
Shape53 = x3dpsail.Shape()
Appearance54 = x3dpsail.Appearance()
Material55 = x3dpsail.Material()
Material55.setUSE("GreenMaterial")

Appearance54.setMaterial(Material55)

Shape53.setAppearance(Appearance54)
Text56 = x3dpsail.Text()
Text56.setString(["X3D Java","SAI Library","X3DJSAIL"])
# Comment example A, plain quotation marks: He said, \"Immel did it!\" 
# Comment example B, XML character entities: He said, &quot;Immel did it!&quot; 
MetadataSet57 = x3dpsail.MetadataSet()
MetadataSet57.setName("EscapedQuotationMarksMetadataSet")
MetadataString58 = x3dpsail.MetadataString()
MetadataString58.setName("quotesTestC")
MetadataString58.setValue(["MFString example C, backslash-escaped quotes: He said, \"Immel did it!\""])

MetadataSet57.setValue(MetadataString58)
MetadataString59 = x3dpsail.MetadataString()
MetadataString59.setName("extraChildTest")
MetadataString59.setValue(["checks MetadataSetObject addValue() method"])

MetadataSet57.setValue(MetadataString59)

Text56.setMetadata(MetadataSet57)
FontStyle60 = x3dpsail.FontStyle()
FontStyle60.setFamily(["SERIF"])
FontStyle60.setJustify(["MIDDLE","MIDDLE"])

Text56.setFontStyle(FontStyle60)

Shape53.setGeometry(Text56)

Transform52.addChildren(Shape53)
Collision61 = x3dpsail.Collision()
# test containerField='proxy' 
Shape62 = x3dpsail.Shape()
Shape62.setDEF("ProxyShape")
# alternative XML encoding: Text string='\"One, Two, Comment\" \"\" \"He said, \\&quot;Immel did it!\\&quot;\"' 
# alternative XML encoding: Text string='\"One, Two, Comment\" \"\" \"He said, \\&quot;Immel did it!\\&quot;\" \"\"' 
# alternative Java source: .setString(new String [] {\"One, Two, Comment\", \"\", \"He said, \\\"Immel did it!\\\"\"}) 
# reference: http://www.web3d.org/x3d/content/examples/Basic/X3dSpecifications/StringArrayEncodingExamplesIndex.html 
Text63 = x3dpsail.Text()
Text63.setString(["One, Two, Text","","He said, \"Immel did it!\" \"\""])

Shape62.setGeometry(Text63)

Collision61.setProxy(Shape62)

Transform52.addChildren(Collision61)
# It's a beautiful world 
# ... for you! 
# https://en.wikipedia.org/wiki/Beautiful_World_(Devo_song) 

Scene26.addChildren(Transform52)
# repeatedly spin 180 degrees as a readable special effect 
OrientationInterpolator64 = x3dpsail.OrientationInterpolator()
OrientationInterpolator64.setDEF("SpinInterpolator")
OrientationInterpolator64.setKey([0,0.5,1])
OrientationInterpolator64.setKeyValue([0,1,0,4.712389,0,1,0,0,0,1,0,1.5707964])

Scene26.addChildren(OrientationInterpolator64)
TimeSensor65 = x3dpsail.TimeSensor()
TimeSensor65.setDEF("SpinClock")
TimeSensor65.setCycleInterval(5.0)
TimeSensor65.setLoop(True)

Scene26.addChildren(TimeSensor65)
ROUTE66 = x3dpsail.ROUTE()
ROUTE66.setFromField("fraction_changed")
ROUTE66.setFromNode("SpinClock")
ROUTE66.setToField("set_fraction")
ROUTE66.setToNode("SpinInterpolator")

Scene26.addChildren(ROUTE66)
ROUTE67 = x3dpsail.ROUTE()
ROUTE67.setFromField("value_changed")
ROUTE67.setFromNode("SpinInterpolator")
ROUTE67.setToField("rotation")
ROUTE67.setToNode("TextTransform")

Scene26.addChildren(ROUTE67)
Group68 = x3dpsail.Group()
Group68.setDEF("BackgroundGroup")
Background69 = x3dpsail.Background()
Background69.setDEF("GradualBackground")

Group68.addChildren(Background69)
Script70 = x3dpsail.Script()
Script70.setDEF("colorTypeConversionScript")
field71 = x3dpsail.field()
field71.setAccessType("inputOnly")
field71.setName("colorInput")
field71.setType("SFColor")

Script70.addField(field71)
field72 = x3dpsail.field()
field72.setAccessType("outputOnly")
field72.setName("colorsOutput")
field72.setType("MFColor")

Script70.addField(field72)

Script70.setSourceCode('''\n"+
"ecmascript:\n"+
"\n"+
"function colorInput (eventValue) // Example source code\n"+
"{\n"+
"   colorsOutput = new MFColor(eventValue); // assigning value sends output event\n"+
"// Browser.print('colorInput=' + eventValue + ', colorsOutput=' + colorsOutput + '\\n');\n"+
"}\n"+
"''')

Group68.addChildren(Script70)
ColorInterpolator73 = x3dpsail.ColorInterpolator()
ColorInterpolator73.setDEF("ColorAnimator")
ColorInterpolator73.setKey([0,0.5,1])
ColorInterpolator73.setKeyValue([0.9411765,1,1,0.29411766,0,0.50980395,0.9411765,1,1])
# AZURE to INDIGO and back again 

Group68.addChildren(ColorInterpolator73)
TimeSensor74 = x3dpsail.TimeSensor()
TimeSensor74.setDEF("ColorClock")
TimeSensor74.setCycleInterval(60.0)
TimeSensor74.setLoop(True)

Group68.addChildren(TimeSensor74)
ROUTE75 = x3dpsail.ROUTE()
ROUTE75.setFromField("colorsOutput")
ROUTE75.setFromNode("colorTypeConversionScript")
ROUTE75.setToField("skyColor")
ROUTE75.setToNode("GradualBackground")

Group68.addChildren(ROUTE75)
ROUTE76 = x3dpsail.ROUTE()
ROUTE76.setFromField("value_changed")
ROUTE76.setFromNode("ColorAnimator")
ROUTE76.setToField("colorInput")
ROUTE76.setToNode("colorTypeConversionScript")

Group68.addChildren(ROUTE76)
ROUTE77 = x3dpsail.ROUTE()
ROUTE77.setFromField("fraction_changed")
ROUTE77.setFromNode("ColorClock")
ROUTE77.setToField("set_fraction")
ROUTE77.setToNode("ColorAnimator")

Group68.addChildren(ROUTE77)

Scene26.addChildren(Group68)
ProtoDeclare78 = x3dpsail.ProtoDeclare()
ProtoDeclare78.setAppinfo("tooltip: ArtDeco01Material prototype is a Material node")
ProtoDeclare78.setName("ArtDeco01Material")
ProtoInterface79 = x3dpsail.ProtoInterface()
field80 = x3dpsail.field()
field80.setAccessType("inputOutput")
field80.setAppinfo("tooltip for descriptionField")
field80.setName("description")
field80.setType("SFString")
field80.setValue("ArtDeco01Material prototype is a Material node")

ProtoInterface79.addField(field80)
field81 = x3dpsail.field()
field81.setAccessType("inputOutput")
field81.setName("enabled")
field81.setType("SFBool")
field81.setValue("true")

ProtoInterface79.addField(field81)

ProtoDeclare78.setProtoInterface(ProtoInterface79)
ProtoBody82 = x3dpsail.ProtoBody()
# Initial node of ProtoBody determines prototype node type 
Material83 = x3dpsail.Material()
Material83.setAmbientIntensity(0.25)
Material83.setDiffuseColor([0.282435,0.085159,0.134462])
Material83.setShininess(0.127273)
Material83.setSpecularColor([0.276305,0.11431,0.139857])

ProtoBody82.addChildren(Material83)
# [HelloWorldProgram diagnostic] should be connected to scene graph: artDeco01ProtoDeclare.getNodeType()=\"Material\" 
# presence of follow-on TouchSensor shows that additional nodes are allowed in ProtoBody after initial node, regardless of node types 
TouchSensor84 = x3dpsail.TouchSensor()
TouchSensor84.setDescription("within ProtoBody")
IS85 = x3dpsail.IS()
connect86 = x3dpsail.connect()
connect86.setNodeField("description")
connect86.setProtoField("description")

IS85.addConnect(connect86)
connect87 = x3dpsail.connect()
connect87.setNodeField("enabled")
connect87.setProtoField("enabled")

IS85.addConnect(connect87)

TouchSensor84.setIS(IS85)

ProtoBody82.addChildren(TouchSensor84)

ProtoDeclare78.setProtoBody(ProtoBody82)

Scene26.addChildren(ProtoDeclare78)
ExternProtoDeclare88 = x3dpsail.ExternProtoDeclare()
ExternProtoDeclare88.setAppinfo("this is a different Material node")
ExternProtoDeclare88.setName("ArtDeco02Material")
ExternProtoDeclare88.setUrl(["http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/ArtDecoPrototypesExcerpt.x3d#ArtDeco02Material","http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/ArtDecoPrototypesExcerpt.x3dv#ArtDeco02Material"])
# [HelloWorldProgram diagnostic] artDeco02ExternProtoDeclare.getNodeType()=\"ERROR_UNKNOWN_EXTERNPROTODECLARE_NODE_TYPE: ExternProtoDeclare name='ArtDeco02Material' type cannot be remotely accessed at run time. TODO X3DJSAIL needs to add further capability that retrieves the ExternProtoDeclare file.\" 
field89 = x3dpsail.field()
field89.setAccessType("inputOutput")
field89.setAppinfo("tooltip for descriptionField")
field89.setName("description")
field89.setType("SFString")

ExternProtoDeclare88.addField(field89)

Scene26.addChildren(ExternProtoDeclare88)
# Tested ArtDeco01ProtoInstance, ArtDeco02ProtoInstance for improper node type when ProtoInstance is added in wrong place 
Shape90 = x3dpsail.Shape()
Shape90.setDEF("TestShape1")
Appearance91 = x3dpsail.Appearance()
Appearance91.setDEF("TestAppearance1")
# ArtDeco01Material prototype goes here... TODO ensure setContainerField is handled in exported Java 
ProtoInstance92 = x3dpsail.ProtoInstance()
ProtoInstance92.setName("ArtDeco01Material")
# [HelloWorldProgram diagnostic] ArtDeco01ProtoInstance.getNodeType()=\"Material\" 
fieldValue93 = x3dpsail.fieldValue()
fieldValue93.setName("description")
fieldValue93.setValue("ArtDeco01Material can substitute for a Material node")

ProtoInstance92.addFieldValue(fieldValue93)

Appearance91.setMaterial(ProtoInstance92)

Shape90.setAppearance(Appearance91)
Sphere94 = x3dpsail.Sphere()
Sphere94.setRadius(0.001)

Shape90.setGeometry(Sphere94)

Scene26.addChildren(Shape90)
Shape95 = x3dpsail.Shape()
Shape95.setDEF("TestShape2")
Appearance96 = x3dpsail.Appearance()
Appearance96.setDEF("TestAppearance2")
# ArtDeco02Material prototype goes here... TODO ensure setContainerField is handled in exported Java 
ProtoInstance97 = x3dpsail.ProtoInstance()
ProtoInstance97.setDEF("ArtDeco02MaterialDEF")
ProtoInstance97.setName("ArtDeco02Material")
# [HelloWorldProgram diagnostic] ArtDeco02ProtoInstance.getNodeType()=\"ERROR_UNKNOWN_EXTERNPROTODECLARE_NODE_TYPE: ExternProtoDeclare name='ArtDeco02Material' type cannot be remotely accessed at run time. TODO X3DJSAIL needs to add further capability that retrieves the ExternProtoDeclare file.\" 
fieldValue98 = x3dpsail.fieldValue()
fieldValue98.setName("description")
fieldValue98.setValue("ArtDeco02Material can substitute for another Material node")

ProtoInstance97.addFieldValue(fieldValue98)

Appearance96.setMaterial(ProtoInstance97)

Shape95.setAppearance(Appearance96)
Cone99 = x3dpsail.Cone()
Cone99.setBottomRadius(0.001)
Cone99.setHeight(0.001)

Shape95.setGeometry(Cone99)

Scene26.addChildren(Shape95)
Shape100 = x3dpsail.Shape()
Shape100.setDEF("TestShape3")
Appearance101 = x3dpsail.Appearance()
Appearance101.setDEF("TestAppearance3")
# ArtDeco02Material ProtoInstance USE goes here. Note that name field is NOT defined as part of ProtoInstance USE. 
ProtoInstance102 = x3dpsail.ProtoInstance()
ProtoInstance102.setUSE("ArtDeco02MaterialDEF")

Appearance101.setMaterial(ProtoInstance102)

Shape100.setAppearance(Appearance101)
Cylinder103 = x3dpsail.Cylinder()
Cylinder103.setHeight(0.001)
Cylinder103.setRadius(0.001)

Shape100.setGeometry(Cylinder103)

Scene26.addChildren(Shape100)
Inline104 = x3dpsail.Inline()
Inline104.setDEF("inlineSceneDef")
Inline104.setUrl(["someOtherScene.x3d","http://www.web3d.org/specifications/java/examples/someOtherScene.x3d"])

Scene26.addChildren(Inline104)
IMPORT105 = x3dpsail.IMPORT()
IMPORT105.setAS("WorldInfoDEF2")
IMPORT105.setImportedDEF("WorldInfoDEF")
IMPORT105.setInlineDEF("inlineSceneDef")

Scene26.addChildren(IMPORT105)
EXPORT106 = x3dpsail.EXPORT()
EXPORT106.setAS("WorldInfoDEF3")
EXPORT106.setLocalDEF("WorldInfoDEF")

Scene26.addChildren(EXPORT106)
ProtoDeclare107 = x3dpsail.ProtoDeclare()
ProtoDeclare107.setAppinfo("mimic a Material node and modulate fields as an animation effect")
ProtoDeclare107.setDocumentation("http://x3dgraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/MaterialModulatorIndex.html")
ProtoDeclare107.setName("MaterialModulator")
ProtoInterface108 = x3dpsail.ProtoInterface()
field109 = x3dpsail.field()
field109.setAccessType("inputOutput")
field109.setName("enabled")
field109.setType("SFBool")
field109.setValue("true")

ProtoInterface108.addField(field109)
field110 = x3dpsail.field()
field110.setAccessType("inputOutput")
field110.setName("diffuseColor")
field110.setType("SFColor")
field110.setValue("0 0 0")

ProtoInterface108.addField(field110)
field111 = x3dpsail.field()
field111.setAccessType("inputOutput")
field111.setName("emissiveColor")
field111.setType("SFColor")
field111.setValue("0.05 0.05 0.5")

ProtoInterface108.addField(field111)
field112 = x3dpsail.field()
field112.setAccessType("inputOutput")
field112.setName("specularColor")
field112.setType("SFColor")
field112.setValue("0 0 0")

ProtoInterface108.addField(field112)
field113 = x3dpsail.field()
field113.setAccessType("inputOutput")
field113.setName("transparency")
field113.setType("SFFloat")
field113.setValue("0.0")

ProtoInterface108.addField(field113)
field114 = x3dpsail.field()
field114.setAccessType("inputOutput")
field114.setName("shininess")
field114.setType("SFFloat")
field114.setValue("0.0")

ProtoInterface108.addField(field114)
field115 = x3dpsail.field()
field115.setAccessType("inputOutput")
field115.setName("ambientIntensity")
field115.setType("SFFloat")
field115.setValue("0.0")

ProtoInterface108.addField(field115)

ProtoDeclare107.setProtoInterface(ProtoInterface108)
ProtoBody116 = x3dpsail.ProtoBody()
Material117 = x3dpsail.Material()
Material117.setDEF("MaterialNode")
IS118 = x3dpsail.IS()
connect119 = x3dpsail.connect()
connect119.setNodeField("diffuseColor")
connect119.setProtoField("diffuseColor")

IS118.addConnect(connect119)
connect120 = x3dpsail.connect()
connect120.setNodeField("emissiveColor")
connect120.setProtoField("emissiveColor")

IS118.addConnect(connect120)
connect121 = x3dpsail.connect()
connect121.setNodeField("specularColor")
connect121.setProtoField("specularColor")

IS118.addConnect(connect121)
connect122 = x3dpsail.connect()
connect122.setNodeField("transparency")
connect122.setProtoField("transparency")

IS118.addConnect(connect122)
connect123 = x3dpsail.connect()
connect123.setNodeField("shininess")
connect123.setProtoField("shininess")

IS118.addConnect(connect123)
connect124 = x3dpsail.connect()
connect124.setNodeField("ambientIntensity")
connect124.setProtoField("ambientIntensity")

IS118.addConnect(connect124)

Material117.setIS(IS118)

ProtoBody116.addChildren(Material117)
# Only first node (the node type) is renderable, others are along for the ride 
Script125 = x3dpsail.Script()
Script125.setDEF("MaterialModulatorScript")
field126 = x3dpsail.field()
field126.setAccessType("inputOutput")
field126.setName("enabled")
field126.setType("SFBool")

Script125.addField(field126)
field127 = x3dpsail.field()
field127.setAccessType("inputOutput")
field127.setName("diffuseColor")
field127.setType("SFColor")

Script125.addField(field127)
field128 = x3dpsail.field()
field128.setAccessType("outputOnly")
field128.setName("newColor")
field128.setType("SFColor")

Script125.addField(field128)
field129 = x3dpsail.field()
field129.setAccessType("inputOnly")
field129.setName("clockTrigger")
field129.setType("SFTime")

Script125.addField(field129)
IS130 = x3dpsail.IS()
connect131 = x3dpsail.connect()
connect131.setNodeField("enabled")
connect131.setProtoField("enabled")

IS130.addConnect(connect131)
connect132 = x3dpsail.connect()
connect132.setNodeField("diffuseColor")
connect132.setProtoField("diffuseColor")

IS130.addConnect(connect132)

Script125.setIS(IS130)

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

ProtoBody116.addChildren(Script125)

ProtoDeclare107.setProtoBody(ProtoBody116)

Scene26.addChildren(ProtoDeclare107)
# Test success: declarative statement createDeclarativeShapeTests() 
Group133 = x3dpsail.Group()
Group133.setDEF("DeclarativeGroupExample")
Shape134 = x3dpsail.Shape()
MetadataString135 = x3dpsail.MetadataString()
MetadataString135.setDEF("FindableMetadataStringTest")
MetadataString135.setName("findThisNameValue")
MetadataString135.setValue(["test case"])

Shape134.setMetadata(MetadataString135)
Appearance136 = x3dpsail.Appearance()
Appearance136.setDEF("DeclarativeAppearanceExample")
# DeclarativeMaterialExample gets overridden by subsequently added MaterialModulator ProtoInstance 
ProtoInstance137 = x3dpsail.ProtoInstance()
ProtoInstance137.setDEF("MyMaterialModulator")
ProtoInstance137.setName("MaterialModulator")

Appearance136.setMaterial(ProtoInstance137)

Shape134.setAppearance(Appearance136)
Cone138 = x3dpsail.Cone()
Cone138.setBottom(False)
Cone138.setBottomRadius(0.05)
Cone138.setHeight(0.1)

Shape134.setGeometry(Cone138)

Group133.addChildren(Shape134)
# Test success: declarativeGroup.addChild() singleton pipeline method 

Scene26.addChildren(Group133)
# Test success: declarative statement addChild() 
# Test success: x3dModel.findNodeByDEF(DeclarativeAppearanceExample) = <Appearance DEF='DeclarativeAppearanceExample'/> i.e. <Appearance DEF='DeclarativeAppearanceExample'> <!- - DeclarativeMaterialExample gets overridden by subsequently added MaterialModulator ProtoInstance - -> <ProtoInstance DEF='MyMaterialModulator' name='MaterialModulator' containerField='material'/> </Appearance> 
# Test success: x3dModel.findElementByNameValue(findThisNameValue) = <MetadataString DEF='FindableMetadataStringTest' name='findThisNameValue' value='\"test case\"'/> 
# Test success: x3dModel.findElementByNameValue(\"ArtDeco01Material\", \"ProtoDeclare\") found 
# Test success: x3dModel.findElementByNameValue(\"MaterialModulator\", \"ProtoDeclare\") found 
# Test success: x3dModel.findElementByNameValue(\"MaterialModulator\", \"ProtoInstance\") found 
Group139 = x3dpsail.Group()
Group139.setDEF("TestFieldObjectsGroup")
# testFieldObjects() results 
# SFBool default=true, true=true, false=false, negate()=true 
# MFBool default=, initial=true false true, negate()=false true false 
# SFFloat default=0.0, initial=1.0, setValue(2)=2.0, setValue(3.0f)=3.0, setValue(4.0)=4.0 
# MFFloat default=, initial=1 2 3, append(5)=1 2 3 5, inserts(3,4)(0,0)=0 1 2 3 4 5, append(6)=0 1 2 3 4 5 6, size()=7 
# ... get1Value[3]=3.0, remove[1]=0 2 3 4 5 6, set1Value(0,10)=10 2 3 4 5 6, multiply(2)=20 4 6 8 10 12, clear= 
# SFVec3f default=0 0 0, initial=1 2 3, setValue=4 5 6, multiply(2)=8 10 12, normalize()=0.45584232 0.5698029 0.68376344, regex matches()=true 
# regex test SFVec3f().matches(\"1 2 3\")=true, regex test SFVec3f().matches(\"1 2 3 4\")=false, regex test (SFRotationObject.matches(\"0 0 0 0\")=true, failure detecting illegal (zero axis) rotation value 

Scene26.addChildren(Group139)
Sound140 = x3dpsail.Sound()
Sound140.setLocation([0,1.6,0])
# set sound-ellipsoid location height at 1.6m to match typical avatar height 
AudioClip141 = x3dpsail.AudioClip()
AudioClip141.setDescription("chimes")
AudioClip141.setUrl(["chimes.wav","http://www.web3d.org/x3d/content/examples/ConformanceNist/Sounds/AudioClip/chimes.wav"])
# Scene example fragment from http://www.web3d.org/x3d/content/examples/ConformanceNist/Sounds/AudioClip/default.x3d 

Sound140.setSource(AudioClip141)

Scene26.addChildren(Sound140)
Sound142 = x3dpsail.Sound()
Sound142.setLocation([0,1.6,0])
# set sound-ellipsoid location height at 1.6m to match typical avatar height 
MovieTexture143 = x3dpsail.MovieTexture()
MovieTexture143.setDescription("mpgsys.mpg from ConformanceNist suite")
MovieTexture143.setUrl(["mpgsys.mpg","http://www.web3d.org/x3d/content/examples/ConformanceNist/Appearance/MovieTexture/mpgsys.mpg"])
# Scene example fragment from http://www.web3d.org/x3d/content/examples/ConformanceNist/Appearance/MovieTexture/mpeg1-systems.x3d 
# Expected containerField='source', allowed containerField values=\"texture\" \"source\" \"back\" \"bottom\" \"front\" \"left\" \"right\" \"top\" \"backTexture\" \"bottomTexture\" \"frontTexture\" \"leftTexture\" \"rightTexture\" \"topTexture\" \"watchList\" 

Sound142.setSource(MovieTexture143)

Scene26.addChildren(Sound142)
# Test success: AnchorObject.isNode()=true, siteAnchor.isNode()=true 
# Test success: AnchorObject.isStatement()=false, siteAnchor.isStatement()=false 
# Test success: ROUTEObject.isNode()=false, orbitPositionROUTE.isNode()=false 
# Test success: ROUTEObject.isStatement()=true, orbitPositionROUTE.isStatement()=true 
# Test success: CommentsBlock.isNode()=false, testComments.isNode()=false 
# Test failure: CommentsBlock.isStatement()=true, testComments.isStatement()=true 
Shape144 = x3dpsail.Shape()
Shape144.setDEF("ExtrusionShape")
# ExampleExtrusion isCrossSectionClosed()=true, crossSection='[1.0, 1.0, 1.0, -1.0, -1.0, -1.0, -1.0, 1.0, 1.0, 1.0]' 
# ExampleExtrusion isSpineClosed()=false, spine='[0.0, 0.0, 0.0, 0.0, 1.0, 0.0]' 
Appearance145 = x3dpsail.Appearance()
Appearance145.setDEF("TransparentAppearance")
Material146 = x3dpsail.Material()
Material146.setTransparency(1.0)

Appearance145.setMaterial(Material146)

Shape144.setAppearance(Appearance145)
Extrusion147 = x3dpsail.Extrusion()
Extrusion147.setDEF("ExampleExtrusion")

Shape144.setGeometry(Extrusion147)

Scene26.addChildren(Shape144)
Group148 = x3dpsail.Group()
# Test MFNode children array as an ordered list consisting of comments, statements, ProtoInstance and nodes 
ProtoDeclare149 = x3dpsail.ProtoDeclare()
ProtoDeclare149.setName("NewWorldInfo")
ProtoInterface150 = x3dpsail.ProtoInterface()
field151 = x3dpsail.field()
field151.setAccessType("initializeOnly")
field151.setName("description")
field151.setType("SFString")

ProtoInterface150.addField(field151)

ProtoDeclare149.setProtoInterface(ProtoInterface150)
ProtoBody152 = x3dpsail.ProtoBody()
WorldInfo153 = x3dpsail.WorldInfo()

ProtoBody152.addChildren(WorldInfo153)

ProtoDeclare149.setProtoBody(ProtoBody152)

Group148.addChildren(ProtoDeclare149)
ProtoInstance154 = x3dpsail.ProtoInstance()
ProtoInstance154.setDEF("Proto1")
ProtoInstance154.setName("NewWorldInfo")
fieldValue155 = x3dpsail.fieldValue()
fieldValue155.setName("description")
fieldValue155.setValue("testing 1 2 3")

ProtoInstance154.addFieldValue(fieldValue155)

Group148.addChildren(ProtoInstance154)
Group156 = x3dpsail.Group()
Group156.setDEF("Node2")
# intentionally empty 

Group148.addChildren(Group156)
ProtoInstance157 = x3dpsail.ProtoInstance()
ProtoInstance157.setDEF("Proto3")
ProtoInstance157.setName("NewWorldInfo")

Group148.addChildren(ProtoInstance157)
Transform158 = x3dpsail.Transform()
Transform158.setDEF("Node4")
# intentionally empty 

Group148.addChildren(Transform158)
# Test satisfactorily creates MFNode children array as an ordered list with mixed content 

Scene26.addChildren(Group148)
ProtoDeclare159 = x3dpsail.ProtoDeclare()
ProtoDeclare159.setName("ShaderProto")
ProtoBody160 = x3dpsail.ProtoBody()
ProgramShader161 = x3dpsail.ProgramShader()

ProtoBody160.addShaders(ProgramShader161)

ProtoDeclare159.setProtoBody(ProtoBody160)

Scene26.addChildren(ProtoDeclare159)
Shape162 = x3dpsail.Shape()
Appearance163 = x3dpsail.Appearance()
# Test MFNode shaders array as an ordered list consisting of comments, ProtoInstance and nodes 
# Test satisfactorily creates MFNode shaders array as an ordered list with mixed content 
ProgramShader164 = x3dpsail.ProgramShader()
ProgramShader164.setDEF("TestShader1")
ShaderProgram165 = x3dpsail.ShaderProgram()
ShaderProgram165.setDEF("TestShader2")

ProgramShader164.addPrograms(ShaderProgram165)

Appearance163.addShaders(ProgramShader164)
ProtoInstance166 = x3dpsail.ProtoInstance()
ProtoInstance166.setDEF("TestShader3")
ProtoInstance166.setName("ShaderProto")

Appearance163.addShaders(ProtoInstance166)
ComposedShader167 = x3dpsail.ComposedShader()
ComposedShader167.setDEF("TestShader4")
ShaderPart168 = x3dpsail.ShaderPart()
ShaderPart168.setDEF("TestShader5")

ComposedShader167.addParts(ShaderPart168)

Appearance163.addShaders(ComposedShader167)

Shape162.setAppearance(Appearance163)

Scene26.addChildren(Shape162)

X3D0.setScene(Scene26)
X3D0.toFileX3D("HelloWorldProgramOutputCanonical_RoundTrip.x3d")
