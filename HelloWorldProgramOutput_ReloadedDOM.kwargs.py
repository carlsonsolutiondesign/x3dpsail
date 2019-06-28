from X3Dpackage import *
X3D0 = X3D(profile="Immersive", version="3.3",    # x3dVersionComparisonTest for this model: supportsX3dVersion(X3DObject.VERSION_3_0)=true 

   head1 = head(    # comment #1 
    # comment #2 
    # comment #3 
    # comment #4 

    component2 = component(name="Navigation", level=3), 
    component3 = component(name="Layering", level=1), 
    component4 = component(name="Shaders", level=1), 
    component5 = component(name="CADGeometry", level=2), 
    component6 = component(name="DIS", level=2), 
    component7 = component(name="H-Anim", level=1), 
    unit8 = unit(name="AngleUnitConversion", category="angle", conversionFactor=1.0), 
    unit9 = unit(name="LengthUnitConversion", category="length", conversionFactor=1.0), 
    unit10 = unit(name="ForceFromPoundsToNewtons", category="force", conversionFactor=4.4482), 
    meta11 = meta(content="HelloWorldProgramOutput.x3d", name="title"), 
    meta12 = meta(content="continued development and testing in progress", name="info"), 
    meta13 = meta(content="Example HelloWorldProgram creates an X3D model using the X3D Java Scene Access Interface Library (X3DJSAIL)", name="description"), 
    meta14 = meta(content="http://www.web3d.org/specifications/java/X3DJSAIL.html", name="reference"), 
    meta15 = meta(content="HelloWorldProgramOutput.java", name="generator"), 
    meta16 = meta(content="6 September 2016", name="created"), 
    meta17 = meta(content="19 June 2019", name="modified"), 
    meta18 = meta(content="X3D Java Scene Access Interface Library (X3DJSAIL)", name="generator"), 
    meta19 = meta(content="http://www.web3d.org/specifications/java/examples/HelloWorldProgram.java", name="generator"), 
    meta20 = meta(content="Netbeans http://www.netbeans.org", name="generator"), 
    meta21 = meta(content="Don Brutzman", name="creator"), 
    meta22 = meta(content="https://sourceforge.net/p/x3d/code/HEAD/tree/www.web3d.org/x3d/stylesheets/java/examples/HelloWorldProgramOutput.x3d", name="reference"), 
    meta23 = meta(content="Console output, ClassicVRML encoding, VRML97 encoding and pretty-print documentation:", name="reference"), 
    meta24 = meta(content="HelloWorldProgramOutput.txt", name="reference"), 
    meta25 = meta(content="HelloWorldProgramOutput.x3dv", name="reference"), 
    meta26 = meta(content="HelloWorldProgramOutput.wrl", name="reference"), 
    meta27 = meta(content="HelloWorldProgramOutput.html", name="reference"), 
    meta28 = meta(content="https://savage.nps.edu/X3dValidator?url=http://www.web3d.org/specifications/java/examples/HelloWorldProgramOutput.x3d", name="reference"), 
    meta29 = meta(content="http://www.web3d.org/specifications/java/examples/HelloWorldProgramOutput.x3d", name="identifier"), 
    meta30 = meta(content="../license.html", name="license")), 
   Scene31 = Scene(    ViewpointGroup32 = ViewpointGroup(description="Available viewpoints",      Viewpoint33 = Viewpoint(DEF="DefaultView", description="Hello X3DJSAIL"), 
     Viewpoint34 = Viewpoint(DEF="TopDownView", description="top-down view from above", orientation=[1,0,0,-1.570796], position=[0,100,0])), 
    NavigationInfo35 = NavigationInfo(avatarSize=[0.25,1.6,0.75], transitionType=["LINEAR"], type=["EXAMINE","FLY","ANY"]), 
    WorldInfo36 = WorldInfo(DEF="WorldInfoDEF", title="HelloWorldProgram produced by X3D Java SAI Library (X3DJSAIL)"), 
    WorldInfo37 = WorldInfo(USE="WorldInfoDEF"), 
    WorldInfo38 = WorldInfo(USE="WorldInfoDEF"), 
    MetadataString39 = MetadataString(DEF="scene.addChildMetadata", name="test", value=["Top-level root Metadata node beneath Scene needs to be one of '-children' in JSON encoding"]), 
    LayerSet40 = LayerSet(DEF="scene.addChildLayerSetTest", order=[0]), 
    Transform41 = Transform(DEF="LogoGeometryTransform", translation=[0,1.5,0],      Anchor42 = Anchor(description="select for X3D Java SAI Library (X3DJSAIL) description", url=["../X3DJSAIL.html","http://www.web3d.org/specifications/java/X3DJSAIL.html"],       Shape43 = Shape(DEF="BoxShape",        Appearance44 = Appearance(        Material45 = Material(DEF="GreenMaterial", diffuseColor=[0,1,1], emissiveColor=[0.8,0,0], transparency=0.1), 
        ImageTexture46 = ImageTexture(url=["images/X3dJavaSceneAccessInterfaceSaiLibrary.png","http://www.web3d.org/specifications/java/examples/images/X3dJavaSceneAccessInterfaceSaiLibrary.png"])), 
       Box47 = Box(DEF="test-NMTOKEN_regex.0123456789", Class="untextured")))), 
    Shape48 = Shape(DEF="LineShape",      Appearance49 = Appearance(      Material50 = Material(emissiveColor=[0.6,0.19607843,0.8])), 
     IndexedLineSet51 = IndexedLineSet(coordIndex=[0,1,2,3,4,0],       # Coordinate 3-tuple point count: 6 

      Coordinate52 = Coordinate(point=[0,1.5,0,2,1.5,0,2,1.5,-2,-2,1.5,-2,-2,1.5,0,0,1.5,0]))), 
    PositionInterpolator53 = PositionInterpolator(DEF="BoxPathAnimator", key=[0,0.125,0.375,0.625,0.875,1], keyValue=[0,1.5,0,2,1.5,0,2,1.5,-2,-2,1.5,-2,-2,1.5,0,0,1.5,0]), 
    TimeSensor54 = TimeSensor(DEF="OrbitClock", cycleInterval=8.0, loop=True), 
    ROUTE55 = ROUTE(fromField="fraction_changed", fromNode="OrbitClock", toField="set_fraction", toNode="BoxPathAnimator"), 
    ROUTE56 = ROUTE(fromField="value_changed", fromNode="BoxPathAnimator", toField="set_translation", toNode="LogoGeometryTransform"), 
    Transform57 = Transform(DEF="TextTransform", translation=[0,-1.5,0],      Shape58 = Shape(      Appearance59 = Appearance(       Material60 = Material(USE="GreenMaterial")), 
      Text61 = Text(string=["X3D Java","SAI Library","X3DJSAIL"],        # Comment example A, plain quotation marks: He said, \"Immel did it!\" 
       # Comment example B, XML character entities: He said, &quot;Immel did it!&quot; 

       MetadataSet62 = MetadataSet(name="EscapedQuotationMarksMetadataSet",         MetadataString63 = MetadataString(name="quotesTestC", value=["MFString example C, backslash-escaped quotes: He said, \"Immel did it!\""]), 
        MetadataString64 = MetadataString(name="extraChildTest", value=["checks MetadataSetObject addValue() method"])), 
       FontStyle65 = FontStyle(family=["SERIF"], justify=["MIDDLE","MIDDLE"]))), 
     Collision66 = Collision(      # test containerField='proxy' 

      Shape67 = Shape(DEF="ProxyShape",        # alternative XML encoding: Text string='\"One, Two, Comment\" \"\" \"He said, \\&quot;Immel did it!\\&quot;\"' 
       # alternative XML encoding: Text string='\"One, Two, Comment\" \"\" \"He said, \\&quot;Immel did it!\\&quot;\" \"\"' 
       # alternative Java source: .setString(new String [] {\"One, Two, Comment\", \"\", \"He said, \\\"Immel did it!\\\"\"}) 
       # reference: http://www.web3d.org/x3d/content/examples/Basic/X3dSpecifications/StringArrayEncodingExamplesIndex.html 

       Text68 = Text(string=["One, Two, Text","","He said, \"Immel did it!\" \"\""]))),      # It's a beautiful world 
     # ... for you! 
     # https://en.wikipedia.org/wiki/Beautiful_World_(Devo_song) 
),     # repeatedly spin 180 degrees as a readable special effect 

    OrientationInterpolator69 = OrientationInterpolator(DEF="SpinInterpolator", key=[0,0.5,1], keyValue=[0,1,0,4.712389,0,1,0,0,0,1,0,1.5707964]), 
    TimeSensor70 = TimeSensor(DEF="SpinClock", cycleInterval=5.0, loop=True), 
    ROUTE71 = ROUTE(fromField="fraction_changed", fromNode="SpinClock", toField="set_fraction", toNode="SpinInterpolator"), 
    ROUTE72 = ROUTE(fromField="value_changed", fromNode="SpinInterpolator", toField="rotation", toNode="TextTransform"), 
    Group73 = Group(DEF="BackgroundGroup",      Background74 = Background(DEF="GradualBackground"), 
     Script75 = Script(DEF="colorTypeConversionScript",       field76 = field(name="colorInput", accessType="inputOnly", type="SFColor"), 
      field77 = field(name="colorsOutput", accessType="outputOnly", type="MFColor"),       sourceCode = '''
ecmascript:

function colorInput (eventValue) // Example source code
{
   colorsOutput = new MFColor(eventValue); // assigning value sends output event
// Browser.print('colorInput=' + eventValue + ', colorsOutput=' + colorsOutput + '\\n');
}
''', ), 
     ColorInterpolator78 = ColorInterpolator(DEF="ColorAnimator", key=[0,0.5,1], keyValue=[0.9411765,1,1,0.29411766,0,0.50980395,0.9411765,1,1],       # AZURE to INDIGO and back again 
), 
     TimeSensor79 = TimeSensor(DEF="ColorClock", cycleInterval=60.0, loop=True), 
     ROUTE80 = ROUTE(fromField="colorsOutput", fromNode="colorTypeConversionScript", toField="skyColor", toNode="GradualBackground"), 
     ROUTE81 = ROUTE(fromField="value_changed", fromNode="ColorAnimator", toField="colorInput", toNode="colorTypeConversionScript"), 
     ROUTE82 = ROUTE(fromField="fraction_changed", fromNode="ColorClock", toField="set_fraction", toNode="ColorAnimator")), 
    ProtoDeclare83 = ProtoDeclare(name="ArtDeco01Material", appinfo="tooltip: ArtDeco01Material prototype is a Material node",      ProtoInterface84 = ProtoInterface(      field85 = field(name="description", accessType="inputOutput", appinfo="tooltip for descriptionField", type="SFString", value="ArtDeco01Material prototype is a Material node"), 
      field86 = field(name="enabled", accessType="inputOutput", type="SFBool", value="true")), 
     ProtoBody87 = ProtoBody(      # Initial node of ProtoBody determines prototype node type 

      Material88 = Material(ambientIntensity=0.25, diffuseColor=[0.282435,0.085159,0.134462], shininess=0.127273, specularColor=[0.276305,0.11431,0.139857]),       # [HelloWorldProgram diagnostic] should be connected to scene graph: artDeco01ProtoDeclare.getNodeType()=\"Material\" 
      # presence of follow-on TouchSensor shows that additional nodes are allowed in ProtoBody after initial node, regardless of node types 

      TouchSensor89 = TouchSensor(description="within ProtoBody",        IS90 = IS(        connect91 = connect(nodeField="description", protoField="description"), 
        connect92 = connect(nodeField="enabled", protoField="enabled"))))), 
    ExternProtoDeclare93 = ExternProtoDeclare(name="ArtDeco02Material", appinfo="this is a different Material node", url=["http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/ArtDecoPrototypesExcerpt.x3d#ArtDeco02Material","http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/ArtDecoPrototypesExcerpt.x3dv#ArtDeco02Material"],      # [HelloWorldProgram diagnostic] artDeco02ExternProtoDeclare.getNodeType()=\"ERROR_UNKNOWN_EXTERNPROTODECLARE_NODE_TYPE: ExternProtoDeclare name='ArtDeco02Material' type cannot be remotely accessed at run time. TODO X3DJSAIL needs to add further capability that retrieves the ExternProtoDeclare file.\" 

     field94 = field(name="description", accessType="inputOutput", appinfo="tooltip for descriptionField", type="SFString")),     # Tested ArtDeco01ProtoInstance, ArtDeco02ProtoInstance for improper node type when ProtoInstance is added in wrong place 

    Shape95 = Shape(DEF="TestShape1",      Appearance96 = Appearance(DEF="TestAppearance1",       # ArtDeco01Material prototype goes here... TODO ensure setContainerField is handled in exported Java 

      ProtoInstance97 = ProtoInstance(name="ArtDeco01Material",        # [HelloWorldProgram diagnostic] ArtDeco01ProtoInstance.getNodeType()=\"Material\" 

       fieldValue98 = fieldValue(name="description", value="ArtDeco01Material can substitute for a Material node"))), 
     Sphere99 = Sphere(radius=0.001)), 
    Shape100 = Shape(DEF="TestShape2",      Appearance101 = Appearance(DEF="TestAppearance2",       # ArtDeco02Material prototype goes here... TODO ensure setContainerField is handled in exported Java 

      ProtoInstance102 = ProtoInstance(DEF="ArtDeco02MaterialDEF", name="ArtDeco02Material",        # [HelloWorldProgram diagnostic] ArtDeco02ProtoInstance.getNodeType()=\"ERROR_UNKNOWN_EXTERNPROTODECLARE_NODE_TYPE: ExternProtoDeclare name='ArtDeco02Material' type cannot be remotely accessed at run time. TODO X3DJSAIL needs to add further capability that retrieves the ExternProtoDeclare file.\" 

       fieldValue103 = fieldValue(name="description", value="ArtDeco02Material can substitute for another Material node"))), 
     Cone104 = Cone(bottomRadius=0.001, height=0.001)), 
    Shape105 = Shape(DEF="TestShape3",      Appearance106 = Appearance(DEF="TestAppearance3",       # ArtDeco02Material ProtoInstance USE goes here. Note that name field is NOT defined as part of ProtoInstance USE. 

      ProtoInstance107 = ProtoInstance(USE="ArtDeco02MaterialDEF")), 
     Cylinder108 = Cylinder(height=0.001, radius=0.001)), 
    Inline109 = Inline(DEF="inlineSceneDef", url=["someOtherScene.x3d","http://www.web3d.org/specifications/java/examples/someOtherScene.x3d"]), 
    IMPORT110 = IMPORT(AS="WorldInfoDEF2", importedDEF="WorldInfoDEF", inlineDEF="inlineSceneDef"), 
    EXPORT111 = EXPORT(AS="WorldInfoDEF3", localDEF="WorldInfoDEF"), 
    ProtoDeclare112 = ProtoDeclare(name="MaterialModulator", appinfo="mimic a Material node and modulate fields as an animation effect", documentation="http://x3dgraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/MaterialModulatorIndex.html",      ProtoInterface113 = ProtoInterface(      field114 = field(name="enabled", accessType="inputOutput", type="SFBool", value="true"), 
      field115 = field(name="diffuseColor", accessType="inputOutput", type="SFColor", value="0 0 0"), 
      field116 = field(name="emissiveColor", accessType="inputOutput", type="SFColor", value="0.05 0.05 0.5"), 
      field117 = field(name="specularColor", accessType="inputOutput", type="SFColor", value="0 0 0"), 
      field118 = field(name="transparency", accessType="inputOutput", type="SFFloat", value="0.0"), 
      field119 = field(name="shininess", accessType="inputOutput", type="SFFloat", value="0.0"), 
      field120 = field(name="ambientIntensity", accessType="inputOutput", type="SFFloat", value="0.0")), 
     ProtoBody121 = ProtoBody(      Material122 = Material(DEF="MaterialNode",        IS123 = IS(        connect124 = connect(nodeField="diffuseColor", protoField="diffuseColor"), 
        connect125 = connect(nodeField="emissiveColor", protoField="emissiveColor"), 
        connect126 = connect(nodeField="specularColor", protoField="specularColor"), 
        connect127 = connect(nodeField="transparency", protoField="transparency"), 
        connect128 = connect(nodeField="shininess", protoField="shininess"), 
        connect129 = connect(nodeField="ambientIntensity", protoField="ambientIntensity"))),       # Only first node (the node type) is renderable, others are along for the ride 

      Script130 = Script(DEF="MaterialModulatorScript",        field131 = field(name="enabled", accessType="inputOutput", type="SFBool"), 
       field132 = field(name="diffuseColor", accessType="inputOutput", type="SFColor"), 
       field133 = field(name="newColor", accessType="outputOnly", type="SFColor"), 
       field134 = field(name="clockTrigger", accessType="inputOnly", type="SFTime"), 
       IS135 = IS(        connect136 = connect(nodeField="enabled", protoField="enabled"), 
        connect137 = connect(nodeField="diffuseColor", protoField="diffuseColor")),        sourceCode = '''
ecmascript:
function initialize ()
{
    newColor = diffuseColor; // start with correct color
}
function set_enabled (newValue)
{
	enabled = newValue;
}
function clockTrigger (timeValue)
{
    if (!enabled) return;
    red   = newColor.r;
    green = newColor.g;
    blue  = newColor.b;
    
    // note different modulation rates for each color component, % is modulus operator
    newColor = new SFColor ((red + 0.02) % 1, (green + 0.03) % 1, (blue + 0.04) % 1);
	if (enabled)
	{
		Browser.print ('diffuseColor=(' + red + ',' + green + ',' + blue + ') newColor=' + newColor.toString() + '\\n');
	}
}
''', ))),     # Test success: declarative statement createDeclarativeShapeTests() 

    Group138 = Group(DEF="DeclarativeGroupExample",      Shape139 = Shape(      MetadataString140 = MetadataString(DEF="FindableMetadataStringTest", name="findThisNameValue", value=["test case"]), 
      Appearance141 = Appearance(DEF="DeclarativeAppearanceExample",        # DeclarativeMaterialExample gets overridden by subsequently added MaterialModulator ProtoInstance 

       ProtoInstance142 = ProtoInstance(DEF="MyMaterialModulator", name="MaterialModulator")), 
      Cone143 = Cone(bottom=False, bottomRadius=0.05, height=0.1)),      # Test success: declarativeGroup.addChild() singleton pipeline method 
),     # Test success: declarative statement addChild() 
    # Test success: x3dModel.findNodeByDEF(DeclarativeAppearanceExample) = <Appearance DEF='DeclarativeAppearanceExample'/> i.e. <Appearance DEF='DeclarativeAppearanceExample'> <!- - DeclarativeMaterialExample gets overridden by subsequently added MaterialModulator ProtoInstance - -> <ProtoInstance DEF='MyMaterialModulator' name='MaterialModulator' containerField='material'/> </Appearance> 
    # Test success: x3dModel.findElementByNameValue(findThisNameValue) = <MetadataString DEF='FindableMetadataStringTest' name='findThisNameValue' value='\"test case\"'/> 
    # Test success: x3dModel.findElementByNameValue(\"ArtDeco01Material\", \"ProtoDeclare\") found 
    # Test success: x3dModel.findElementByNameValue(\"MaterialModulator\", \"ProtoDeclare\") found 
    # Test success: x3dModel.findElementByNameValue(\"MaterialModulator\", \"ProtoInstance\") found 

    Group144 = Group(DEF="TestFieldObjectsGroup",      # testFieldObjects() results 
     # SFBool default=true, true=true, false=false, negate()=true 
     # MFBool default=, initial=true false true, negate()=false true false 
     # SFFloat default=0.0, initial=1.0, setValue(2)=2.0, setValue(3.0f)=3.0, setValue(4.0)=4.0 
     # MFFloat default=, initial=1 2 3, append(5)=1 2 3 5, inserts(3,4)(0,0)=0 1 2 3 4 5, append(6)=0 1 2 3 4 5 6, size()=7 
     # ... get1Value[3]=3.0, remove[1]=0 2 3 4 5 6, set1Value(0,10)=10 2 3 4 5 6, multiply(2)=20 4 6 8 10 12, clear= 
     # SFVec3f default=0 0 0, initial=1 2 3, setValue=4 5 6, multiply(2)=8 10 12, normalize()=0.45584232 0.5698029 0.68376344, regex matches()=true 
     # regex test SFVec3f().matches(\"1 2 3\")=true, regex test SFVec3f().matches(\"1 2 3 4\")=false, regex test (SFRotationObject.matches(\"0 0 0 0\")=true, failure detecting illegal (zero axis) rotation value 
), 
    Sound145 = Sound(location=[0,1.6,0],      # set sound-ellipsoid location height at 1.6m to match typical avatar height 

     AudioClip146 = AudioClip(description="chimes", url=["chimes.wav","http://www.web3d.org/x3d/content/examples/ConformanceNist/Sounds/AudioClip/chimes.wav"],       # Scene example fragment from http://www.web3d.org/x3d/content/examples/ConformanceNist/Sounds/AudioClip/default.x3d 
)), 
    Sound147 = Sound(location=[0,1.6,0],      # set sound-ellipsoid location height at 1.6m to match typical avatar height 

     MovieTexture148 = MovieTexture(description="mpgsys.mpg from ConformanceNist suite", url=["mpgsys.mpg","http://www.web3d.org/x3d/content/examples/ConformanceNist/Appearance/MovieTexture/mpgsys.mpg"],       # Scene example fragment from http://www.web3d.org/x3d/content/examples/ConformanceNist/Appearance/MovieTexture/mpeg1-systems.x3d 
      # Expected containerField='source', allowed containerField values=\"texture\" \"source\" \"back\" \"bottom\" \"front\" \"left\" \"right\" \"top\" \"backTexture\" \"bottomTexture\" \"frontTexture\" \"leftTexture\" \"rightTexture\" \"topTexture\" \"watchList\" 
)),     # Test success: AnchorObject.isNode()=true, siteAnchor.isNode()=true 
    # Test success: AnchorObject.isStatement()=false, siteAnchor.isStatement()=false 
    # Test success: ROUTEObject.isNode()=false, orbitPositionROUTE.isNode()=false 
    # Test success: ROUTEObject.isStatement()=true, orbitPositionROUTE.isStatement()=true 
    # Test success: CommentsBlock.isNode()=false, testComments.isNode()=false 
    # Test failure: CommentsBlock.isStatement()=true, testComments.isStatement()=true 

    Shape149 = Shape(DEF="ExtrusionShape",      # ExampleExtrusion isCrossSectionClosed()=true, crossSection='[1.0, 1.0, 1.0, -1.0, -1.0, -1.0, -1.0, 1.0, 1.0, 1.0]' 
     # ExampleExtrusion isSpineClosed()=false, spine='[0.0, 0.0, 0.0, 0.0, 1.0, 0.0]' 

     Appearance150 = Appearance(DEF="TransparentAppearance",       Material151 = Material(transparency=1.0)), 
     Extrusion152 = Extrusion(DEF="ExampleExtrusion")), 
    Group153 = Group(     # Test MFNode children array as an ordered list consisting of comments, statements, ProtoInstance and nodes 

     ProtoDeclare154 = ProtoDeclare(name="NewWorldInfo",       ProtoInterface155 = ProtoInterface(       field156 = field(name="description", accessType="initializeOnly", type="SFString")), 
      ProtoBody157 = ProtoBody(       WorldInfo158 = WorldInfo())), 
     ProtoInstance159 = ProtoInstance(DEF="Proto1", name="NewWorldInfo",       fieldValue160 = fieldValue(name="description", value="testing 1 2 3")), 
     Group161 = Group(DEF="Node2",       # intentionally empty 
), 
     ProtoInstance162 = ProtoInstance(DEF="Proto3", name="NewWorldInfo"), 
     Transform163 = Transform(DEF="Node4",       # intentionally empty 
),      # Test satisfactorily creates MFNode children array as an ordered list with mixed content 
), 
    ProtoDeclare164 = ProtoDeclare(name="ShaderProto",      ProtoBody165 = ProtoBody(      ProgramShader166 = ProgramShader())), 
    Shape167 = Shape(     Appearance168 = Appearance(      # Test MFNode shaders array as an ordered list consisting of comments, ProtoInstance and nodes 
      # Test satisfactorily creates MFNode shaders array as an ordered list with mixed content 

      ProgramShader169 = ProgramShader(DEF="TestShader1",        ShaderProgram170 = ShaderProgram(DEF="TestShader2")), 
      ProtoInstance171 = ProtoInstance(DEF="TestShader3", name="ShaderProto"), 
      ComposedShader172 = ComposedShader(DEF="TestShader4",        ShaderPart173 = ShaderPart(DEF="TestShader5")))), 
    Transform174 = Transform(DEF="SpecialtyNodes",      CADLayer175 = CADLayer(      CADAssembly176 = CADAssembly(       CADPart177 = CADPart(        CADFace178 = CADFace()))), 
     EspduTransform179 = EspduTransform(geoSystem=["GD","WE"]), 
     ReceiverPdu180 = ReceiverPdu(geoSystem=["GD","WE"]), 
     SignalPdu181 = SignalPdu(geoSystem=["GD","WE"]), 
     TransmitterPdu182 = TransmitterPdu(geoSystem=["GD","WE"]), 
     DISEntityManager183 = DISEntityManager(      DISEntityTypeMapping184 = DISEntityTypeMapping()), 
     HAnimHumanoid185 = HAnimHumanoid(DEF="TestHumanoidDEF", name="TestHumanoid", version="2.0"))))
