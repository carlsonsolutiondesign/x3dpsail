from X3Dpackage import *
X3D0 = (X3D() 
   .setProfile("Immersive") 
   .setVersion("3.3") 
   .setHead(head()# comment #1 
# comment #2 
# comment #3 
# comment #4 
    .addComponent(component()     .setName("Navigation") 
     .setLevel(3) 
    ) 
    .addComponent(component()     .setName("Layering") 
     .setLevel(1) 
    ) 
    .addUnit(unit()     .setName("AngleUnitConversion") 
     .setConversionFactor(1.0) 
    ) 
    .addUnit(unit()     .setName("LengthUnitConversion") 
     .setConversionFactor(1.0) 
    ) 
    .addMeta(meta()     .setName("title") 
     .setContent("HelloWorldProgramOutput.x3d") 
    ) 
    .addMeta(meta()     .setName("description") 
     .setContent("Example HelloWorldProgram creates an X3D model using the X3D Java Scene Access Interface (SAI) Library") 
    ) 
    .addMeta(meta()     .setName("reference") 
     .setContent("http://www.web3d.org/specifications/java/X3DJSAIL.html") 
    ) 
    .addMeta(meta()     .setName("generator") 
     .setContent("HelloWorldProgramOutput.java") 
    ) 
    .addMeta(meta()     .setName("created") 
     .setContent("6 September 2016") 
    ) 
    .addMeta(meta()     .setName("modified") 
     .setContent("10 September 2018") 
    ) 
    .addMeta(meta()     .setName("generator") 
     .setContent("X3D Java Scene Access Interface Library (X3DJSAIL)") 
    ) 
    .addMeta(meta()     .setName("generator") 
     .setContent("http://www.web3d.org/specifications/java/examples/HelloWorldProgram.java") 
    ) 
    .addMeta(meta()     .setName("generator") 
     .setContent("Netbeans http://www.netbeans.org") 
    ) 
    .addMeta(meta()     .setName("creator") 
     .setContent("Don Brutzman") 
    ) 
    .addMeta(meta()     .setName("reference") 
     .setContent("https://sourceforge.net/p/x3d/code/HEAD/tree/www.web3d.org/x3d/stylesheets/java/examples/HelloWorldProgramOutput.x3d") 
    ) 
    .addMeta(meta()     .setName("reference") 
     .setContent("Console output, ClassicVRML encoding, VRML97 encoding and pretty-print documentation:") 
    ) 
    .addMeta(meta()     .setName("reference") 
     .setContent("HelloWorldProgramOutput.txt") 
    ) 
    .addMeta(meta()     .setName("reference") 
     .setContent("HelloWorldProgramOutput.x3dv") 
    ) 
    .addMeta(meta()     .setName("reference") 
     .setContent("HelloWorldProgramOutput.wrl") 
    ) 
    .addMeta(meta()     .setName("reference") 
     .setContent("HelloWorldProgramOutput.html") 
    ) 
    .addMeta(meta()     .setName("X3dValidator") 
     .setContent("https://savage.nps.edu/X3dValidator?url=http://www.web3d.org/specifications/java/examples/HelloWorldProgramOutput.x3d") 
    ) 
    .addMeta(meta()     .setName("identifier") 
     .setContent("http://www.web3d.org/specifications/java/examples/HelloWorldProgramOutput.x3d") 
    ) 
    .addMeta(meta()     .setName("license") 
     .setContent("../license.html") 
    ) 
    .addMeta(meta()     .setName("SpecialTest") 
     .setContent("tested sat: name value cannot contain embedded space character") 
    ) 
   ) 
   .setScene(Scene()    .addChildren([ViewpointGroup()     .setDescription("Available viewpoints") 
     .addChildren([Viewpoint()      .setDEF("DefaultView") 
      .setDescription("Hello X3DJSAIL") 
]     ) 
     .addChildren([Viewpoint()      .setDEF("TopDownView") 
      .setDescription("top-down view from above") 
      .setOrientation([1,0,0,-1.570796]) 
      .setPosition([0,100,0]) 
]     ) 
]    ) 
    .addChildren([WorldInfo()     .setDEF("WorldInfoDEF") 
     .setTitle("HelloWorldProgram produced by X3D Java SAI Library (X3DJSAIL)") 
]    ) 
    .addChildren([WorldInfo()     .setUSE("WorldInfoDEF") 
]    ) 
    .addChildren([WorldInfo()     .setUSE("WorldInfoDEF") 
]    ) 
    .addChildren([MetadataString()     .setDEF("scene.addChildMetadata") 
     .setName("test") 
     .setValue(["Top-level root Metadata node beneath Scene needs to be one of '-children' in JSON encoding"]) 
]    ) 
    .addLayerSet(LayerSet()     .setDEF("scene.addChildLayerSetTest") 
     .setOrder([0]) 
    ) 
    .addChildren([Transform()     .setDEF("LogoGeometryTransform") 
     .setTranslation([0,1.5,0]) 
     .addChildren([Anchor()      .setDescription("select for X3D Java SAI Library (X3DJSAIL) description") 
      .setUrl(["../X3DJSAIL.html","http://www.web3d.org/specifications/java/X3DJSAIL.html"]) 
      .addChildren([Shape()       .setDEF("BoxShape") 
       .setAppearance(Appearance()        .setMaterial(Material()         .setDEF("GreenMaterial") 
         .setDiffuseColor([0,1,1]) 
         .setEmissiveColor([0.8,0,0]) 
         .setTransparency(0.1) 
        ) 
        .setTexture(ImageTexture()         .setUrl(["images/X3dJavaSceneAccessInterfaceSaiLibrary.png","http://www.web3d.org/specifications/java/examples/images/X3dJavaSceneAccessInterfaceSaiLibrary.png"]) 
        ) 
       ) 
       .setGeometry(Box()        .setDEF("test-NMTOKEN_regex.0123456789") 
        .setClass("untextured") 
       ) 
]      ) 
]     ) 
]    ) 
    .addChildren([Shape()     .setDEF("LineShape") 
     .setAppearance(Appearance()      .setMaterial(Material()       .setEmissiveColor([0.6,0.19607843,0.8]) 
      ) 
     ) 
     .setGeometry(IndexedLineSet()# Coordinate 3-tuple point count: 6 
      .setCoord(Coordinate(coordIndex = [0,1,2,3,4,0])       .setPoint([0,1.5,0,2,1.5,0,2,1.5,-2,-2,1.5,-2,-2,1.5,0,0,1.5,0]) 
      ) 
     ) 
]    ) 
    .addChildren([PositionInterpolator()     .setDEF("BoxPathAnimator") 
     .setKey([0,0.125,0.375,0.625,0.875,1]) 
     .setKeyValue([0,1.5,0,2,1.5,0,2,1.5,-2,-2,1.5,-2,-2,1.5,0,0,1.5,0]) 
]    ) 
    .addChildren([TimeSensor()     .setDEF("OrbitClock") 
     .setCycleInterval(8.0) 
     .setLoop(True) 
]    ) 
    .addChildren([ROUTE()     .setFromField("fraction_changed") 
     .setFromNode("OrbitClock") 
     .setToField("set_fraction") 
     .setToNode("BoxPathAnimator") 
]    ) 
    .addChildren([ROUTE()     .setFromField("value_changed") 
     .setFromNode("BoxPathAnimator") 
     .setToField("set_translation") 
     .setToNode("LogoGeometryTransform") 
]    ) 
    .addChildren([Transform()     .setDEF("TextTransform") 
     .setTranslation([0,-1.5,0]) 
     .addChildren([Shape()      .setAppearance(Appearance()       .setMaterial(Material()        .setUSE("GreenMaterial") 
       ) 
      ) 
      .setGeometry(Text()       .setString(["X3D Java","SAI Library","X3DJSAIL"]) 
# Comment example A, plain quotation marks: He said, \"Immel did it!\" 
# Comment example B, XML character entities: He said, &quot;Immel did it!&quot; 
       .setMetadata(MetadataSet()        .setName("EscapedQuotationMarksMetadataSet") 
        .setValue(MetadataString()         .setName("quotesTestC") 
         .setValue(["MFString example C, backslash-escaped quotes: He said, \"Immel did it!\""]) 
        ) 
        .setValue(MetadataString()         .setName("extraChildTest") 
         .setValue(["checks MetadataSetObject addValue() method"]) 
        ) 
       ) 
       .setFontStyle(FontStyle()       ) 
      ) 
]     ) 
     .addChildren([Collision()# test containerField='proxy' 
      .setProxy(Shape()       .setDEF("ProxyShape") 
# alternative XML encoding: Text string='\"One, Two, Comment\" \"\" \"He said, \\&quot;Immel did it!\\&quot;\"' 
# alternative XML encoding: Text string='\"One, Two, Comment\" \"\" \"He said, \\&quot;Immel did it!\\&quot;\" \"\"' 
# alternative Java source: .setString(new String [] {\"One, Two, Comment\", \"\", \"He said, \\\"Immel did it!\\\"\"}) 
# reference: http://www.web3d.org/x3d/content/examples/Basic/X3dSpecifications/StringArrayEncodingExamplesIndex.html 
       .setGeometry(Text()        .setString(["One, Two, Text","","He said, \"Immel did it!\" \"\""]) 
       ) 
      ) 
]     ) 
# It's a beautiful world 
# ... for you! 
# https://en.wikipedia.org/wiki/Beautiful_World_(Devo_song) 
]    ) 
# repeatedly spin 180 degrees as a readable special effect 
    .addChildren([OrientationInterpolator()     .setDEF("SpinInterpolator") 
     .setKey([0,0.5,1]) 
     .setKeyValue([0,1,0,4.712389,0,1,0,0,0,1,0,1.5707964]) 
]    ) 
    .addChildren([TimeSensor()     .setDEF("SpinClock") 
     .setCycleInterval(5.0) 
     .setLoop(True) 
]    ) 
    .addChildren([ROUTE()     .setFromField("fraction_changed") 
     .setFromNode("SpinClock") 
     .setToField("set_fraction") 
     .setToNode("SpinInterpolator") 
]    ) 
    .addChildren([ROUTE()     .setFromField("value_changed") 
     .setFromNode("SpinInterpolator") 
     .setToField("rotation") 
     .setToNode("TextTransform") 
]    ) 
    .addChildren([Group()     .setDEF("BackgroundGroup") 
     .addChildren([Background()      .setDEF("GradualBackground") 
]     ) 
     .addChildren([Script()      .setDEF("colorTypeConversionScript") 
      .addField(field()       .setName("colorInput") 
       .setAccessType("inputOnly") 
       .setType("SFColor") 
      ) 
      .addField(field()       .setName("colorsOutput") 
       .setAccessType("outputOnly") 
       .setType("MFColor") 
      ) 
.setSourceCode('''\n"+
"ecmascript:\n"+
"\n"+
"function colorInput (eventValue) // Example source code\n"+
"{\n"+
"   colorsOutput = new MFColor(eventValue); // assigning value sends output event\n"+
"// Browser.print('colorInput=' + eventValue + ', colorsOutput=' + colorsOutput + '\\n');\n"+
"}\n"+
"''')
]     ) 
     .addChildren([ColorInterpolator()      .setDEF("ColorAnimator") 
      .setKey([0,0.5,1]) 
      .setKeyValue([0.9411765,1,1,0.29411766,0,0.50980395,0.9411765,1,1]) 
# AZURE to INDIGO and back again 
]     ) 
     .addChildren([TimeSensor()      .setDEF("ColorClock") 
      .setCycleInterval(60.0) 
      .setLoop(True) 
]     ) 
     .addChildren([ROUTE()      .setFromField("colorsOutput") 
      .setFromNode("colorTypeConversionScript") 
      .setToField("skyColor") 
      .setToNode("GradualBackground") 
]     ) 
     .addChildren([ROUTE()      .setFromField("value_changed") 
      .setFromNode("ColorAnimator") 
      .setToField("colorInput") 
      .setToNode("colorTypeConversionScript") 
]     ) 
     .addChildren([ROUTE()      .setFromField("fraction_changed") 
      .setFromNode("ColorClock") 
      .setToField("set_fraction") 
      .setToNode("ColorAnimator") 
]     ) 
]    ) 
    .addChildren([ProtoDeclare()     .setName("ArtDeco01Material") 
     .setAppinfo("tooltip: ArtDeco01Material prototype is a Material node") 
     .setProtoInterface(ProtoInterface()      .addField(field()       .setName("description") 
       .setAccessType("inputOutput") 
       .setAppinfo("tooltip for descriptionField") 
       .setType("SFString") 
       .setValue("ArtDeco01Material prototype is a Material node") 
      ) 
      .addField(field()       .setName("enabled") 
       .setAccessType("inputOutput") 
       .setType("SFBool") 
       .setValue("true") 
      ) 
     ) 
     .setProtoBody(ProtoBody()# Initial node of ProtoBody determines prototype node type 
      .addChildren([Material()       .setAmbientIntensity(0.25) 
       .setDiffuseColor([0.282435,0.085159,0.134462]) 
       .setShininess(0.127273) 
       .setSpecularColor([0.276305,0.11431,0.139857]) 
]      ) 
# [HelloWorldProgram diagnostic] should be connected to scene graph: ArtDeco01ProtoDeclare.getNodeType()=\"Material\" 
# presence of follow-on TouchSensor shows that additional nodes are allowed in ProtoBody after initial node, regardless of node types 
      .addChildren([TouchSensor()       .setDescription("within ProtoBody") 
       .setIS(IS()        .addConnect(connect()         .setNodeField("description") 
         .setProtoField("description") 
        ) 
        .addConnect(connect()         .setNodeField("enabled") 
         .setProtoField("enabled") 
        ) 
       ) 
]      ) 
     ) 
]    ) 
    .addChildren([ExternProtoDeclare()     .setName("ArtDeco02Material") 
     .setAppinfo("this is a different Material node") 
     .setUrl(["http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/ArtDecoPrototypesExcerpt.x3d#ArtDeco02Material","http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/ArtDecoPrototypesExcerpt.x3dv#ArtDeco02Material"]) 
# [HelloWorldProgram diagnostic] ArtDeco02ExternProtoDeclare.getNodeType()=\"ERROR_UNKNOWN_EXTERNPROTODECLARE_NODE_TYPE: ExternProtoDeclare name='ArtDeco02Material' type cannot be remotely accessed at run time, TODO X3DJSAIL needs to add further capability.\" 
     .addField(field()      .setName("description") 
      .setAccessType("inputOutput") 
      .setAppinfo("tooltip for descriptionField") 
      .setType("SFString") 
     ) 
]    ) 
# Tested ArtDeco01ProtoInstance, ArtDeco02ProtoInstance for improper node type when ProtoInstance is added in wrong place 
    .addChildren([Shape()     .setDEF("TestShape1") 
     .setAppearance(Appearance()      .setDEF("TestAppearance1") 
# ArtDeco01Material prototype goes here... TODO ensure setContainerField is handled in exported Java 
      .setMaterial(ProtoInstance()       .setName("ArtDeco01Material") 
# [HelloWorldProgram diagnostic] ArtDeco01ProtoInstance.getNodeType()=\"Material\" 
       .addFieldValue(fieldValue()        .setName("description") 
        .setValue("ArtDeco01Material can substitute for a Material node") 
       ) 
      ) 
     ) 
     .setGeometry(Sphere()     ) 
]    ) 
    .addChildren([Shape()     .setDEF("TestShape2") 
     .setAppearance(Appearance()      .setDEF("TestAppearance2") 
# ArtDeco02Material prototype goes here... TODO ensure setContainerField is handled in exported Java 
      .setMaterial(ProtoInstance()       .setDEF("ArtDeco02MaterialDEF") 
       .setName("ArtDeco02Material") 
# [HelloWorldProgram diagnostic] ArtDeco02ProtoInstance.getNodeType()=\"ERROR_UNKNOWN_EXTERNPROTODECLARE_NODE_TYPE: ExternProtoDeclare name='ArtDeco02Material' type cannot be remotely accessed at run time, TODO X3DJSAIL needs to add further capability.\" 
       .addFieldValue(fieldValue()        .setName("description") 
        .setValue("ArtDeco02Material can substitute for another Material node") 
       ) 
      ) 
     ) 
     .setGeometry(Cone()     ) 
]    ) 
    .addChildren([Shape()     .setDEF("TestShape3") 
     .setAppearance(Appearance()      .setDEF("TestAppearance3") 
# ArtDeco02Material ProtoInstance USE goes here... 
      .setMaterial(ProtoInstance()       .setUSE("ArtDeco02MaterialDEF") 
      ) 
     ) 
     .setGeometry(Cylinder()     ) 
]    ) 
    .addChildren([Inline()     .setDEF("inlineSceneDef") 
     .setUrl(["someOtherScene.x3d"]) 
]    ) 
    .addChildren([IMPORT()     .setAS("WorldInfoDEF2") 
     .setImportedDEF("WorldInfoDEF") 
     .setInlineDEF("inlineSceneDef") 
]    ) 
    .addChildren([EXPORT()     .setAS("WorldInfoDEF3") 
     .setLocalDEF("WorldInfoDEF") 
]    ) 
    .addChildren([ProtoDeclare()     .setName("MaterialModulator") 
     .setAppinfo("mimic a Material node and modulate fields as an animation effect") 
     .setDocumentation("http://x3dgraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/MaterialModulatorIndex.html") 
     .setProtoInterface(ProtoInterface()      .addField(field()       .setName("enabled") 
       .setAccessType("inputOutput") 
       .setType("SFBool") 
       .setValue("true") 
      ) 
      .addField(field()       .setName("diffuseColor") 
       .setAccessType("inputOutput") 
       .setType("SFColor") 
       .setValue("0 0 0") 
      ) 
      .addField(field()       .setName("emissiveColor") 
       .setAccessType("inputOutput") 
       .setType("SFColor") 
       .setValue("0.05 0.05 0.5") 
      ) 
      .addField(field()       .setName("specularColor") 
       .setAccessType("inputOutput") 
       .setType("SFColor") 
       .setValue("0 0 0") 
      ) 
      .addField(field()       .setName("transparency") 
       .setAccessType("inputOutput") 
       .setType("SFFloat") 
       .setValue("0.0") 
      ) 
      .addField(field()       .setName("shininess") 
       .setAccessType("inputOutput") 
       .setType("SFFloat") 
       .setValue("0.0") 
      ) 
      .addField(field()       .setName("ambientIntensity") 
       .setAccessType("inputOutput") 
       .setType("SFFloat") 
       .setValue("0.0") 
      ) 
     ) 
     .setProtoBody(ProtoBody()      .addChildren([Material()       .setDEF("MaterialNode") 
       .setIS(IS()        .addConnect(connect()         .setNodeField("diffuseColor") 
         .setProtoField("diffuseColor") 
        ) 
        .addConnect(connect()         .setNodeField("emissiveColor") 
         .setProtoField("emissiveColor") 
        ) 
        .addConnect(connect()         .setNodeField("specularColor") 
         .setProtoField("specularColor") 
        ) 
        .addConnect(connect()         .setNodeField("transparency") 
         .setProtoField("transparency") 
        ) 
        .addConnect(connect()         .setNodeField("shininess") 
         .setProtoField("shininess") 
        ) 
        .addConnect(connect()         .setNodeField("ambientIntensity") 
         .setProtoField("ambientIntensity") 
        ) 
       ) 
]      ) 
# Only first node (the node type) is renderable, others are along for the ride 
      .addChildren([Script()       .setDEF("MaterialModulatorScript") 
       .addField(field()        .setName("enabled") 
        .setAccessType("inputOutput") 
        .setType("SFBool") 
       ) 
       .addField(field()        .setName("diffuseColor") 
        .setAccessType("inputOutput") 
        .setType("SFColor") 
       ) 
       .addField(field()        .setName("newColor") 
        .setAccessType("outputOnly") 
        .setType("SFColor") 
       ) 
       .addField(field()        .setName("clockTrigger") 
        .setAccessType("inputOnly") 
        .setType("SFTime") 
       ) 
       .setIS(IS()        .addConnect(connect()         .setNodeField("enabled") 
         .setProtoField("enabled") 
        ) 
        .addConnect(connect()         .setNodeField("diffuseColor") 
         .setProtoField("diffuseColor") 
        ) 
       ) 
.setSourceCode('''\n"+
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
]      ) 
     ) 
]    ) 
# Test success: declarative statement createDeclarativeShapeTests() 
    .addChildren([Group()     .setDEF("DeclarativeGroupExample") 
     .addChildren([Shape()      .setMetadata(MetadataString()       .setDEF("FindableMetadataStringTest") 
       .setName("findThisNameValue") 
       .setValue(["test case"]) 
      ) 
      .setAppearance(Appearance()       .setDEF("DeclarativeAppearanceExample") 
# DeclarativeMaterialExample gets overridden by subsequently added MaterialModulator ProtoInstance 
       .setMaterial(ProtoInstance()        .setDEF("MyMaterialModulator") 
        .setName("MaterialModulator") 
       ) 
      ) 
      .setGeometry(Cone()      ) 
]     ) 
# Test success: declarativeGroup.addChild() singleton pipeline method 
]    ) 
# Test success: declarative statement addChild() 
# Test success: x3dModel.findNodeByDEF(DeclarativeAppearanceExample) = <Appearance DEF='DeclarativeAppearanceExample'/> i.e. <Appearance DEF='DeclarativeAppearanceExample'> <!- - DeclarativeMaterialExample gets overridden by subsequently added MaterialModulator ProtoInstance - -> <ProtoInstance DEF='MyMaterialModulator' name='MaterialModulator' containerField='material'/> </Appearance> 
# Test success: x3dModel.findElementByNameValue(findThisNameValue) = <MetadataString DEF='FindableMetadataStringTest' name='findThisNameValue' value='\"test case\"'/> 
# Test success: x3dModel.findElementByNameValue(\"ArtDeco01Material\", \"ProtoDeclare\") found 
# Test success: x3dModel.findElementByNameValue(\"MaterialModulator\", \"ProtoDeclare\") found 
# Test success: x3dModel.findElementByNameValue(\"MaterialModulator\", \"ProtoInstance\") found 
    .addChildren([Group()     .setDEF("TestFieldObjectsGroup") 
# testFieldObjects() results 
# SFBool default=true, true=true, false=false, negate()=true 
# MFBool default=, initial=true false true, negate()=false true false 
# SFFloat default=0.0, initial=1.0, setValue(2)=2.0, setValue(3.0f)=3.0, setValue(4.0)=4.0 
# MFFloat default=, initial=1 2 3, append(5)=1 2 3 5, inserts(3,4)(0,0)=0 1 2 3 4 5, append(6)=0 1 2 3 4 5 6, size()=7 
# ... get1Value[3]=3.0, remove[1]=0 2 3 4 5 6, set1Value(0,10)=10 2 3 4 5 6, multiply(2)=20 4 6 8 10 12, clear= 
# SFVec3f default=0 0 0, initial=1 2 3, setValue=4 5 6, multiply(2)=8 10 12, normalize()=0.45584232 0.5698029 0.68376344, regex matches()=true 
# regex test SFVec3f().matches(\"1 2 3\")=true, regex test SFVec3f().matches(\"1 2 3 4\")=false, regex test (SFRotationObject.matches(\"0 0 0 0\")=true, failure detecting illegal (zero axis) rotation value 
]    ) 
    .addChildren([Sound()     .setLocation([0,1.6,0]) 
# set sound-ellipsoid location height at 1.6m to match typical avatar height 
     .setSource(AudioClip()      .setDescription("chimes") 
      .setUrl(["chimes.wav","http://www.web3d.org/x3d/content/examples/ConformanceNist/Sounds/AudioClip/chimes.wav"]) 
# Scene example fragment from http://www.web3d.org/x3d/content/examples/ConformanceNist/Sounds/AudioClip/default.x3d 
     ) 
]    ) 
    .addChildren([Sound()     .setLocation([0,1.6,0]) 
# set sound-ellipsoid location height at 1.6m to match typical avatar height 
     .setSource(MovieTexture()      .setDescription("mpgsys.mpg from ConformanceNist suite") 
      .setUrl(["mpgsys.mpg","http://www.web3d.org/x3d/content/examples/ConformanceNist/Appearance/MovieTexture/mpgsys.mpg"]) 
# Scene example fragment from http://www.web3d.org/x3d/content/examples/ConformanceNist/Appearance/MovieTexture/mpeg1-systems.x3d 
# Expected containerField='source', allowed containerField values=\"texture\" \"source\" \"back\" \"bottom\" \"front\" \"left\" \"right\" \"top\" \"backTexture\" \"bottomTexture\" \"frontTexture\" \"leftTexture\" \"rightTexture\" \"topTexture\" \"watchList\" 
     ) 
]    ) 
# Test success: AnchorObject.isNode()=true, siteAnchor.isNode()=true 
# Test success: AnchorObject.isStatement()=false, siteAnchor.isStatement()=false 
# Test success: ROUTEObject.isNode()=false, orbitPositionROUTE.isNode()=false 
# Test success: ROUTEObject.isStatement()=true, orbitPositionROUTE.isStatement()=true 
# Test success: CommentsBlock.isNode()=false, testComments.isNode()=false 
# Test failure: CommentsBlock.isStatement()=true, testComments.isStatement()=true 
    .addChildren([Shape()     .setDEF("ExtrusionShape") 
# ExampleExtrusion isCrossSectionClosed()=true, crossSection='[1.0, 1.0, 1.0, -1.0, -1.0, -1.0, -1.0, 1.0, 1.0, 1.0]' 
# ExampleExtrusion isSpineClosed()=false, spine='[0.0, 0.0, 0.0, 0.0, 1.0, 0.0]' 
     .setAppearance(Appearance()      .setDEF("TransparentAppearance") 
      .setMaterial(Material()       .setTransparency(1.0) 
      ) 
     ) 
     .setGeometry(Extrusion()      .setDEF("ExampleExtrusion") 
     ) 
]    ) 
   ) 
)
