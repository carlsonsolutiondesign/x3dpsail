from X3Dpackage import *
X3D0 = X3D(profile="Immersive", version="3.3",    head1 = head(    # comment #1 
    # comment #2 
    # comment #3 
    # comment #4 

    component2 = component(name="Navigation", level=3), 
    component3 = component(name="Layering", level=1), 
    unit4 = unit(name="AngleUnitConversion", category="angle", conversionFactor=1.0), 
    unit5 = unit(name="LengthUnitConversion", category="length", conversionFactor=1.0), 
    meta6 = meta(name="title", content="HelloWorldProgramOutput.x3d"), 
    meta7 = meta(name="description", content="Example HelloWorldProgram creates an X3D model using the X3D Java Scene Access Interface (SAI) Library"), 
    meta8 = meta(name="reference", content="http://www.web3d.org/specifications/java/X3DJSAIL.html"), 
    meta9 = meta(name="generator", content="HelloWorldProgramOutput.java"), 
    meta10 = meta(name="created", content="6 September 2016"), 
    meta11 = meta(name="modified", content="10 September 2018"), 
    meta12 = meta(name="generator", content="X3D Java Scene Access Interface Library (X3DJSAIL)"), 
    meta13 = meta(name="generator", content="http://www.web3d.org/specifications/java/examples/HelloWorldProgram.java"), 
    meta14 = meta(name="generator", content="Netbeans http://www.netbeans.org"), 
    meta15 = meta(name="creator", content="Don Brutzman"), 
    meta16 = meta(name="reference", content="https://sourceforge.net/p/x3d/code/HEAD/tree/www.web3d.org/x3d/stylesheets/java/examples/HelloWorldProgramOutput.x3d"), 
    meta17 = meta(name="reference", content="Console output, ClassicVRML encoding, VRML97 encoding and pretty-print documentation:"), 
    meta18 = meta(name="reference", content="HelloWorldProgramOutput.txt"), 
    meta19 = meta(name="reference", content="HelloWorldProgramOutput.x3dv"), 
    meta20 = meta(name="reference", content="HelloWorldProgramOutput.wrl"), 
    meta21 = meta(name="reference", content="HelloWorldProgramOutput.html"), 
    meta22 = meta(name="X3dValidator", content="https://savage.nps.edu/X3dValidator?url=http://www.web3d.org/specifications/java/examples/HelloWorldProgramOutput.x3d"), 
    meta23 = meta(name="identifier", content="http://www.web3d.org/specifications/java/examples/HelloWorldProgramOutput.x3d"), 
    meta24 = meta(name="license", content="../license.html"), 
    meta25 = meta(name="SpecialTest", content="tested sat: name value cannot contain embedded space character")), 
   Scene26 = Scene(    ViewpointGroup27 = ViewpointGroup(description="Available viewpoints",      Viewpoint28 = Viewpoint(DEF="DefaultView", description="Hello X3DJSAIL"), 
     Viewpoint29 = Viewpoint(DEF="TopDownView", description="top-down view from above", orientation=[1,0,0,-1.570796], position=[0,100,0])), 
    WorldInfo30 = WorldInfo(DEF="WorldInfoDEF", title="HelloWorldProgram produced by X3D Java SAI Library (X3DJSAIL)"), 
    WorldInfo31 = WorldInfo(USE="WorldInfoDEF"), 
    WorldInfo32 = WorldInfo(USE="WorldInfoDEF"), 
    MetadataString33 = MetadataString(DEF="scene.addChildMetadata", name="test", value=["Top-level root Metadata node beneath Scene needs to be one of '-children' in JSON encoding"]), 
    LayerSet34 = LayerSet(DEF="scene.addChildLayerSetTest", order=[0]), 
    Transform35 = Transform(DEF="LogoGeometryTransform", translation=[0,1.5,0],      Anchor36 = Anchor(description="select for X3D Java SAI Library (X3DJSAIL) description", url=["../X3DJSAIL.html","http://www.web3d.org/specifications/java/X3DJSAIL.html"],       Shape37 = Shape(DEF="BoxShape",        Appearance38 = Appearance(        Material39 = Material(DEF="GreenMaterial", diffuseColor=[0,1,1], emissiveColor=[0.8,0,0], transparency=0.1), 
        ImageTexture40 = ImageTexture(url=["images/X3dJavaSceneAccessInterfaceSaiLibrary.png","http://www.web3d.org/specifications/java/examples/images/X3dJavaSceneAccessInterfaceSaiLibrary.png"])), 
       Box41 = Box(DEF="test-NMTOKEN_regex.0123456789", Class="untextured")))), 
    Shape42 = Shape(DEF="LineShape",      Appearance43 = Appearance(      Material44 = Material(emissiveColor=[0.6,0.19607843,0.8])), 
     IndexedLineSet45 = IndexedLineSet(coordIndex=[0,1,2,3,4,0],       # Coordinate 3-tuple point count: 6 

      Coordinate46 = Coordinate(point=[0,1.5,0,2,1.5,0,2,1.5,-2,-2,1.5,-2,-2,1.5,0,0,1.5,0]))), 
    PositionInterpolator47 = PositionInterpolator(DEF="BoxPathAnimator", key=[0,0.125,0.375,0.625,0.875,1], keyValue=[0,1.5,0,2,1.5,0,2,1.5,-2,-2,1.5,-2,-2,1.5,0,0,1.5,0]), 
    TimeSensor48 = TimeSensor(DEF="OrbitClock", cycleInterval=8.0, loop=True), 
    ROUTE49 = ROUTE(fromField="fraction_changed", fromNode="OrbitClock", toField="set_fraction", toNode="BoxPathAnimator"), 
    ROUTE50 = ROUTE(fromField="value_changed", fromNode="BoxPathAnimator", toField="set_translation", toNode="LogoGeometryTransform"), 
    Transform51 = Transform(DEF="TextTransform", translation=[0,-1.5,0],      Shape52 = Shape(      Appearance53 = Appearance(       Material54 = Material(USE="GreenMaterial")), 
      Text55 = Text(string=["X3D Java","SAI Library","X3DJSAIL"],        # Comment example A, plain quotation marks: He said, \"Immel did it!\" 
       # Comment example B, XML character entities: He said, &quot;Immel did it!&quot; 

       MetadataSet56 = MetadataSet(name="EscapedQuotationMarksMetadataSet",         MetadataString57 = MetadataString(name="quotesTestC", value=["MFString example C, backslash-escaped quotes: He said, \"Immel did it!\""]), 
        MetadataString58 = MetadataString(name="extraChildTest", value=["checks MetadataSetObject addValue() method"])), 
       FontStyle59 = FontStyle(family=["SERIF"], justify=["MIDDLE","MIDDLE"]))), 
     Collision60 = Collision(      # test containerField='proxy' 

      Shape61 = Shape(DEF="ProxyShape",        # alternative XML encoding: Text string='\"One, Two, Comment\" \"\" \"He said, \\&quot;Immel did it!\\&quot;\"' 
       # alternative XML encoding: Text string='\"One, Two, Comment\" \"\" \"He said, \\&quot;Immel did it!\\&quot;\" \"\"' 
       # alternative Java source: .setString(new String [] {\"One, Two, Comment\", \"\", \"He said, \\\"Immel did it!\\\"\"}) 
       # reference: http://www.web3d.org/x3d/content/examples/Basic/X3dSpecifications/StringArrayEncodingExamplesIndex.html 

       Text62 = Text(string=["One, Two, Text","","He said, \"Immel did it!\" \"\""]))),      # It's a beautiful world 
     # ... for you! 
     # https://en.wikipedia.org/wiki/Beautiful_World_(Devo_song) 
),     # repeatedly spin 180 degrees as a readable special effect 

    OrientationInterpolator63 = OrientationInterpolator(DEF="SpinInterpolator", key=[0,0.5,1], keyValue=[0,1,0,4.712389,0,1,0,0,0,1,0,1.5707964]), 
    TimeSensor64 = TimeSensor(DEF="SpinClock", cycleInterval=5.0, loop=True), 
    ROUTE65 = ROUTE(fromField="fraction_changed", fromNode="SpinClock", toField="set_fraction", toNode="SpinInterpolator"), 
    ROUTE66 = ROUTE(fromField="value_changed", fromNode="SpinInterpolator", toField="rotation", toNode="TextTransform"), 
    Group67 = Group(DEF="BackgroundGroup",      Background68 = Background(DEF="GradualBackground"), 
     Script69 = Script(DEF="colorTypeConversionScript",       field70 = field(name="colorInput", accessType="inputOnly", type="SFColor"), 
      field71 = field(name="colorsOutput", accessType="outputOnly", type="MFColor"),       sourceCode = '''\n"+
"ecmascript:\n"+
"\n"+
"function colorInput (eventValue) // Example source code\n"+
"{\n"+
"   colorsOutput = new MFColor(eventValue); // assigning value sends output event\n"+
"// Browser.print('colorInput=' + eventValue + ', colorsOutput=' + colorsOutput + '\\n');\n"+
"}\n"+
"''', ), 
     ColorInterpolator72 = ColorInterpolator(DEF="ColorAnimator", key=[0,0.5,1], keyValue=[0.9411765,1,1,0.29411766,0,0.50980395,0.9411765,1,1],       # AZURE to INDIGO and back again 
), 
     TimeSensor73 = TimeSensor(DEF="ColorClock", cycleInterval=60.0, loop=True), 
     ROUTE74 = ROUTE(fromField="colorsOutput", fromNode="colorTypeConversionScript", toField="skyColor", toNode="GradualBackground"), 
     ROUTE75 = ROUTE(fromField="value_changed", fromNode="ColorAnimator", toField="colorInput", toNode="colorTypeConversionScript"), 
     ROUTE76 = ROUTE(fromField="fraction_changed", fromNode="ColorClock", toField="set_fraction", toNode="ColorAnimator")), 
    ProtoDeclare77 = ProtoDeclare(name="ArtDeco01Material", appinfo="tooltip: ArtDeco01Material prototype is a Material node",      ProtoInterface78 = ProtoInterface(      field79 = field(name="description", accessType="inputOutput", appinfo="tooltip for descriptionField", type="SFString", value="ArtDeco01Material prototype is a Material node"), 
      field80 = field(name="enabled", accessType="inputOutput", type="SFBool", value="true")), 
     ProtoBody81 = ProtoBody(      # Initial node of ProtoBody determines prototype node type 

      Material82 = Material(ambientIntensity=0.25, diffuseColor=[0.282435,0.085159,0.134462], shininess=0.127273, specularColor=[0.276305,0.11431,0.139857]),       # [HelloWorldProgram diagnostic] should be connected to scene graph: ArtDeco01ProtoDeclare.getNodeType()=\"Material\" 
      # presence of follow-on TouchSensor shows that additional nodes are allowed in ProtoBody after initial node, regardless of node types 

      TouchSensor83 = TouchSensor(description="within ProtoBody",        IS84 = IS(        connect85 = connect(nodeField="description", protoField="description"), 
        connect86 = connect(nodeField="enabled", protoField="enabled"))))), 
    ExternProtoDeclare87 = ExternProtoDeclare(name="ArtDeco02Material", appinfo="this is a different Material node", url=["http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/ArtDecoPrototypesExcerpt.x3d#ArtDeco02Material","http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/ArtDecoPrototypesExcerpt.x3dv#ArtDeco02Material"],      # [HelloWorldProgram diagnostic] ArtDeco02ExternProtoDeclare.getNodeType()=\"ERROR_UNKNOWN_EXTERNPROTODECLARE_NODE_TYPE: ExternProtoDeclare name='ArtDeco02Material' type cannot be remotely accessed at run time, TODO X3DJSAIL needs to add further capability.\" 

     field88 = field(name="description", accessType="inputOutput", appinfo="tooltip for descriptionField", type="SFString")),     # Tested ArtDeco01ProtoInstance, ArtDeco02ProtoInstance for improper node type when ProtoInstance is added in wrong place 

    Shape89 = Shape(DEF="TestShape1",      Appearance90 = Appearance(DEF="TestAppearance1",       # ArtDeco01Material prototype goes here... TODO ensure setContainerField is handled in exported Java 

      ProtoInstance91 = ProtoInstance(name="ArtDeco01Material",        # [HelloWorldProgram diagnostic] ArtDeco01ProtoInstance.getNodeType()=\"Material\" 

       fieldValue92 = fieldValue(name="description", value="ArtDeco01Material can substitute for a Material node"))), 
     Sphere93 = Sphere(radius=0.001)), 
    Shape94 = Shape(DEF="TestShape2",      Appearance95 = Appearance(DEF="TestAppearance2",       # ArtDeco02Material prototype goes here... TODO ensure setContainerField is handled in exported Java 

      ProtoInstance96 = ProtoInstance(DEF="ArtDeco02MaterialDEF", name="ArtDeco02Material",        # [HelloWorldProgram diagnostic] ArtDeco02ProtoInstance.getNodeType()=\"ERROR_UNKNOWN_EXTERNPROTODECLARE_NODE_TYPE: ExternProtoDeclare name='ArtDeco02Material' type cannot be remotely accessed at run time, TODO X3DJSAIL needs to add further capability.\" 

       fieldValue97 = fieldValue(name="description", value="ArtDeco02Material can substitute for another Material node"))), 
     Cone98 = Cone(bottomRadius=0.001, height=0.001)), 
    Shape99 = Shape(DEF="TestShape3",      Appearance100 = Appearance(DEF="TestAppearance3",       # ArtDeco02Material ProtoInstance USE goes here... 

      ProtoInstance101 = ProtoInstance(USE="ArtDeco02MaterialDEF")), 
     Cylinder102 = Cylinder(height=0.001, radius=0.001)), 
    Inline103 = Inline(DEF="inlineSceneDef", url=["someOtherScene.x3d"]), 
    IMPORT104 = IMPORT(AS="WorldInfoDEF2", importedDEF="WorldInfoDEF", inlineDEF="inlineSceneDef"), 
    EXPORT105 = EXPORT(AS="WorldInfoDEF3", localDEF="WorldInfoDEF"), 
    ProtoDeclare106 = ProtoDeclare(name="MaterialModulator", appinfo="mimic a Material node and modulate fields as an animation effect", documentation="http://x3dgraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/MaterialModulatorIndex.html",      ProtoInterface107 = ProtoInterface(      field108 = field(name="enabled", accessType="inputOutput", type="SFBool", value="true"), 
      field109 = field(name="diffuseColor", accessType="inputOutput", type="SFColor", value="0 0 0"), 
      field110 = field(name="emissiveColor", accessType="inputOutput", type="SFColor", value="0.05 0.05 0.5"), 
      field111 = field(name="specularColor", accessType="inputOutput", type="SFColor", value="0 0 0"), 
      field112 = field(name="transparency", accessType="inputOutput", type="SFFloat", value="0.0"), 
      field113 = field(name="shininess", accessType="inputOutput", type="SFFloat", value="0.0"), 
      field114 = field(name="ambientIntensity", accessType="inputOutput", type="SFFloat", value="0.0")), 
     ProtoBody115 = ProtoBody(      Material116 = Material(DEF="MaterialNode",        IS117 = IS(        connect118 = connect(nodeField="diffuseColor", protoField="diffuseColor"), 
        connect119 = connect(nodeField="emissiveColor", protoField="emissiveColor"), 
        connect120 = connect(nodeField="specularColor", protoField="specularColor"), 
        connect121 = connect(nodeField="transparency", protoField="transparency"), 
        connect122 = connect(nodeField="shininess", protoField="shininess"), 
        connect123 = connect(nodeField="ambientIntensity", protoField="ambientIntensity"))),       # Only first node (the node type) is renderable, others are along for the ride 

      Script124 = Script(DEF="MaterialModulatorScript",        field125 = field(name="enabled", accessType="inputOutput", type="SFBool"), 
       field126 = field(name="diffuseColor", accessType="inputOutput", type="SFColor"), 
       field127 = field(name="newColor", accessType="outputOnly", type="SFColor"), 
       field128 = field(name="clockTrigger", accessType="inputOnly", type="SFTime"), 
       IS129 = IS(        connect130 = connect(nodeField="enabled", protoField="enabled"), 
        connect131 = connect(nodeField="diffuseColor", protoField="diffuseColor")),        sourceCode = '''\n"+
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
"''', ))),     # Test success: declarative statement createDeclarativeShapeTests() 

    Group132 = Group(DEF="DeclarativeGroupExample",      Shape133 = Shape(      MetadataString134 = MetadataString(DEF="FindableMetadataStringTest", name="findThisNameValue", value=["test case"]), 
      Appearance135 = Appearance(DEF="DeclarativeAppearanceExample",        # DeclarativeMaterialExample gets overridden by subsequently added MaterialModulator ProtoInstance 

       ProtoInstance136 = ProtoInstance(DEF="MyMaterialModulator", name="MaterialModulator")), 
      Cone137 = Cone(bottom=False, bottomRadius=0.05, height=0.1)),      # Test success: declarativeGroup.addChild() singleton pipeline method 
),     # Test success: declarative statement addChild() 
    # Test success: x3dModel.findNodeByDEF(DeclarativeAppearanceExample) = <Appearance DEF='DeclarativeAppearanceExample'/> i.e. <Appearance DEF='DeclarativeAppearanceExample'> <!- - DeclarativeMaterialExample gets overridden by subsequently added MaterialModulator ProtoInstance - -> <ProtoInstance DEF='MyMaterialModulator' name='MaterialModulator' containerField='material'/> </Appearance> 
    # Test success: x3dModel.findElementByNameValue(findThisNameValue) = <MetadataString DEF='FindableMetadataStringTest' name='findThisNameValue' value='\"test case\"'/> 
    # Test success: x3dModel.findElementByNameValue(\"ArtDeco01Material\", \"ProtoDeclare\") found 
    # Test success: x3dModel.findElementByNameValue(\"MaterialModulator\", \"ProtoDeclare\") found 
    # Test success: x3dModel.findElementByNameValue(\"MaterialModulator\", \"ProtoInstance\") found 

    Group138 = Group(DEF="TestFieldObjectsGroup",      # testFieldObjects() results 
     # SFBool default=true, true=true, false=false, negate()=true 
     # MFBool default=, initial=true false true, negate()=false true false 
     # SFFloat default=0.0, initial=1.0, setValue(2)=2.0, setValue(3.0f)=3.0, setValue(4.0)=4.0 
     # MFFloat default=, initial=1 2 3, append(5)=1 2 3 5, inserts(3,4)(0,0)=0 1 2 3 4 5, append(6)=0 1 2 3 4 5 6, size()=7 
     # ... get1Value[3]=3.0, remove[1]=0 2 3 4 5 6, set1Value(0,10)=10 2 3 4 5 6, multiply(2)=20 4 6 8 10 12, clear= 
     # SFVec3f default=0 0 0, initial=1 2 3, setValue=4 5 6, multiply(2)=8 10 12, normalize()=0.45584232 0.5698029 0.68376344, regex matches()=true 
     # regex test SFVec3f().matches(\"1 2 3\")=true, regex test SFVec3f().matches(\"1 2 3 4\")=false, regex test (SFRotationObject.matches(\"0 0 0 0\")=true, failure detecting illegal (zero axis) rotation value 
), 
    Sound139 = Sound(location=[0,1.6,0],      # set sound-ellipsoid location height at 1.6m to match typical avatar height 

     AudioClip140 = AudioClip(description="chimes", url=["chimes.wav","http://www.web3d.org/x3d/content/examples/ConformanceNist/Sounds/AudioClip/chimes.wav"],       # Scene example fragment from http://www.web3d.org/x3d/content/examples/ConformanceNist/Sounds/AudioClip/default.x3d 
)), 
    Sound141 = Sound(location=[0,1.6,0],      # set sound-ellipsoid location height at 1.6m to match typical avatar height 

     MovieTexture142 = MovieTexture(description="mpgsys.mpg from ConformanceNist suite", url=["mpgsys.mpg","http://www.web3d.org/x3d/content/examples/ConformanceNist/Appearance/MovieTexture/mpgsys.mpg"],       # Scene example fragment from http://www.web3d.org/x3d/content/examples/ConformanceNist/Appearance/MovieTexture/mpeg1-systems.x3d 
      # Expected containerField='source', allowed containerField values=\"texture\" \"source\" \"back\" \"bottom\" \"front\" \"left\" \"right\" \"top\" \"backTexture\" \"bottomTexture\" \"frontTexture\" \"leftTexture\" \"rightTexture\" \"topTexture\" \"watchList\" 
)),     # Test success: AnchorObject.isNode()=true, siteAnchor.isNode()=true 
    # Test success: AnchorObject.isStatement()=false, siteAnchor.isStatement()=false 
    # Test success: ROUTEObject.isNode()=false, orbitPositionROUTE.isNode()=false 
    # Test success: ROUTEObject.isStatement()=true, orbitPositionROUTE.isStatement()=true 
    # Test success: CommentsBlock.isNode()=false, testComments.isNode()=false 
    # Test failure: CommentsBlock.isStatement()=true, testComments.isStatement()=true 

    Shape143 = Shape(DEF="ExtrusionShape",      # ExampleExtrusion isCrossSectionClosed()=true, crossSection='[1.0, 1.0, 1.0, -1.0, -1.0, -1.0, -1.0, 1.0, 1.0, 1.0]' 
     # ExampleExtrusion isSpineClosed()=false, spine='[0.0, 0.0, 0.0, 0.0, 1.0, 0.0]' 

     Appearance144 = Appearance(DEF="TransparentAppearance",       Material145 = Material(transparency=1.0)), 
     Extrusion146 = Extrusion(DEF="ExampleExtrusion"))))
