from X3Dpackage import *
X3D0 = X3D(profile="Immersive", version="3.3",    # x3dVersionComparisonTest for this model: supportsX3dVersion(X3DObject.VERSION_3_0)=true 

   head1 = head(    # comment #1 
    # comment #2 
    # comment #3 
    # comment #4 

    component2 = component(level=3, name="Navigation"), 
    component3 = component(level=1, name="Shaders"), 
    component4 = component(level=1, name="Layering"), 
    unit5 = unit(category="angle", conversionFactor=1.0, name="AngleUnitConversion"), 
    unit6 = unit(category="length", conversionFactor=1.0, name="LengthUnitConversion"), 
    meta7 = meta(content="HelloWorldProgramOutput.x3d", name="title"), 
    meta8 = meta(content="Example HelloWorldProgram creates an X3D model using the X3D Java Scene Access Interface Library (X3DJSAIL)", name="description"), 
    meta9 = meta(content="http://www.web3d.org/specifications/java/X3DJSAIL.html", name="reference"), 
    meta10 = meta(content="HelloWorldProgramOutput.java", name="generator"), 
    meta11 = meta(content="6 September 2016", name="created"), 
    meta12 = meta(content="27 December 2018", name="modified"), 
    meta13 = meta(content="X3D Java Scene Access Interface Library (X3DJSAIL)", name="generator"), 
    meta14 = meta(content="http://www.web3d.org/specifications/java/examples/HelloWorldProgram.java", name="generator"), 
    meta15 = meta(content="Netbeans http://www.netbeans.org", name="generator"), 
    meta16 = meta(content="Don Brutzman", name="creator"), 
    meta17 = meta(content="https://sourceforge.net/p/x3d/code/HEAD/tree/www.web3d.org/x3d/stylesheets/java/examples/HelloWorldProgramOutput.x3d", name="reference"), 
    meta18 = meta(content="Console output, ClassicVRML encoding, VRML97 encoding and pretty-print documentation:", name="reference"), 
    meta19 = meta(content="HelloWorldProgramOutput.txt", name="reference"), 
    meta20 = meta(content="HelloWorldProgramOutput.x3dv", name="reference"), 
    meta21 = meta(content="HelloWorldProgramOutput.wrl", name="reference"), 
    meta22 = meta(content="HelloWorldProgramOutput.html", name="reference"), 
    meta23 = meta(content="https://savage.nps.edu/X3dValidator?url=http://www.web3d.org/specifications/java/examples/HelloWorldProgramOutput.x3d", name="reference"), 
    meta24 = meta(content="http://www.web3d.org/specifications/java/examples/HelloWorldProgramOutput.x3d", name="identifier"), 
    meta25 = meta(content="../license.html", name="license")), 
   Scene26 = Scene(    ViewpointGroup27 = ViewpointGroup(description="Available viewpoints",      Viewpoint28 = Viewpoint(DEF="DefaultView", description="Hello X3DJSAIL"), 
     Viewpoint29 = Viewpoint(DEF="TopDownView", description="top-down view from above", orientation=[1,0,0,-1.570796], position=[0,100,0])), 
    NavigationInfo30 = NavigationInfo(avatarSize=[0.25,1.6,0.75], transitionType=["LINEAR"], type=["EXAMINE","FLY","ANY"]), 
    WorldInfo31 = WorldInfo(DEF="WorldInfoDEF", title="HelloWorldProgram produced by X3D Java SAI Library (X3DJSAIL)"), 
    WorldInfo32 = WorldInfo(USE="WorldInfoDEF"), 
    WorldInfo33 = WorldInfo(USE="WorldInfoDEF"), 
    MetadataString34 = MetadataString(DEF="scene.addChildMetadata", name="test", value=["Top-level root Metadata node beneath Scene needs to be one of '-children' in JSON encoding"]), 
    LayerSet35 = LayerSet(DEF="scene.addChildLayerSetTest", order=[0]), 
    Transform36 = Transform(DEF="LogoGeometryTransform", translation=[0,1.5,0],      Anchor37 = Anchor(description="select for X3D Java SAI Library (X3DJSAIL) description", url=["../X3DJSAIL.html","http://www.web3d.org/specifications/java/X3DJSAIL.html"],       Shape38 = Shape(DEF="BoxShape",        Appearance39 = Appearance(        Material40 = Material(DEF="GreenMaterial", diffuseColor=[0,1,1], emissiveColor=[0.8,0,0], transparency=0.1), 
        ImageTexture41 = ImageTexture(url=["images/X3dJavaSceneAccessInterfaceSaiLibrary.png","http://www.web3d.org/specifications/java/examples/images/X3dJavaSceneAccessInterfaceSaiLibrary.png"])), 
       Box42 = Box(DEF="test-NMTOKEN_regex.0123456789", Class="untextured")))), 
    Shape43 = Shape(DEF="LineShape",      Appearance44 = Appearance(      Material45 = Material(emissiveColor=[0.6,0.19607843,0.8])), 
     IndexedLineSet46 = IndexedLineSet(coordIndex=[0,1,2,3,4,0],       # Coordinate 3-tuple point count: 6 

      Coordinate47 = Coordinate(point=[0,1.5,0,2,1.5,0,2,1.5,-2,-2,1.5,-2,-2,1.5,0,0,1.5,0]))), 
    PositionInterpolator48 = PositionInterpolator(DEF="BoxPathAnimator", key=[0,0.125,0.375,0.625,0.875,1], keyValue=[0,1.5,0,2,1.5,0,2,1.5,-2,-2,1.5,-2,-2,1.5,0,0,1.5,0]), 
    TimeSensor49 = TimeSensor(DEF="OrbitClock", cycleInterval=8.0, loop=True), 
    ROUTE50 = ROUTE(fromField="fraction_changed", fromNode="OrbitClock", toField="set_fraction", toNode="BoxPathAnimator"), 
    ROUTE51 = ROUTE(fromField="value_changed", fromNode="BoxPathAnimator", toField="set_translation", toNode="LogoGeometryTransform"), 
    Transform52 = Transform(DEF="TextTransform", translation=[0,-1.5,0],      Shape53 = Shape(      Appearance54 = Appearance(       Material55 = Material(USE="GreenMaterial")), 
      Text56 = Text(string=["X3D Java","SAI Library","X3DJSAIL"],        # Comment example A, plain quotation marks: He said, \"Immel did it!\" 
       # Comment example B, XML character entities: He said, &quot;Immel did it!&quot; 

       MetadataSet57 = MetadataSet(name="EscapedQuotationMarksMetadataSet",         MetadataString58 = MetadataString(name="quotesTestC", value=["MFString example C, backslash-escaped quotes: He said, \"Immel did it!\""]), 
        MetadataString59 = MetadataString(name="extraChildTest", value=["checks MetadataSetObject addValue() method"])), 
       FontStyle60 = FontStyle(family=["SERIF"], justify=["MIDDLE","MIDDLE"]))), 
     Collision61 = Collision(      # test containerField='proxy' 

      Shape62 = Shape(DEF="ProxyShape",        # alternative XML encoding: Text string='\"One, Two, Comment\" \"\" \"He said, \\&quot;Immel did it!\\&quot;\"' 
       # alternative XML encoding: Text string='\"One, Two, Comment\" \"\" \"He said, \\&quot;Immel did it!\\&quot;\" \"\"' 
       # alternative Java source: .setString(new String [] {\"One, Two, Comment\", \"\", \"He said, \\\"Immel did it!\\\"\"}) 
       # reference: http://www.web3d.org/x3d/content/examples/Basic/X3dSpecifications/StringArrayEncodingExamplesIndex.html 

       Text63 = Text(string=["One, Two, Text","","He said, \"Immel did it!\" \"\""]))),      # It's a beautiful world 
     # ... for you! 
     # https://en.wikipedia.org/wiki/Beautiful_World_(Devo_song) 
),     # repeatedly spin 180 degrees as a readable special effect 

    OrientationInterpolator64 = OrientationInterpolator(DEF="SpinInterpolator", key=[0,0.5,1], keyValue=[0,1,0,4.712389,0,1,0,0,0,1,0,1.5707964]), 
    TimeSensor65 = TimeSensor(DEF="SpinClock", cycleInterval=5.0, loop=True), 
    ROUTE66 = ROUTE(fromField="fraction_changed", fromNode="SpinClock", toField="set_fraction", toNode="SpinInterpolator"), 
    ROUTE67 = ROUTE(fromField="value_changed", fromNode="SpinInterpolator", toField="rotation", toNode="TextTransform"), 
    Group68 = Group(DEF="BackgroundGroup",      Background69 = Background(DEF="GradualBackground"), 
     Script70 = Script(DEF="colorTypeConversionScript",       field71 = field(accessType="inputOnly", name="colorInput", type="SFColor"), 
      field72 = field(accessType="outputOnly", name="colorsOutput", type="MFColor"),       sourceCode = '''
ecmascript:

function colorInput (eventValue) // Example source code
{
   colorsOutput = new MFColor(eventValue); // assigning value sends output event
// Browser.print('colorInput=' + eventValue + ', colorsOutput=' + colorsOutput + '\\n');
}
''', ), 
     ColorInterpolator73 = ColorInterpolator(DEF="ColorAnimator", key=[0,0.5,1], keyValue=[0.9411765,1,1,0.29411766,0,0.50980395,0.9411765,1,1],       # AZURE to INDIGO and back again 
), 
     TimeSensor74 = TimeSensor(DEF="ColorClock", cycleInterval=60.0, loop=True), 
     ROUTE75 = ROUTE(fromField="colorsOutput", fromNode="colorTypeConversionScript", toField="skyColor", toNode="GradualBackground"), 
     ROUTE76 = ROUTE(fromField="value_changed", fromNode="ColorAnimator", toField="colorInput", toNode="colorTypeConversionScript"), 
     ROUTE77 = ROUTE(fromField="fraction_changed", fromNode="ColorClock", toField="set_fraction", toNode="ColorAnimator")), 
    ProtoDeclare78 = ProtoDeclare(appinfo="tooltip: ArtDeco01Material prototype is a Material node", name="ArtDeco01Material",      ProtoInterface79 = ProtoInterface(      field80 = field(accessType="inputOutput", appinfo="tooltip for descriptionField", name="description", type="SFString", value="ArtDeco01Material prototype is a Material node"), 
      field81 = field(accessType="inputOutput", name="enabled", type="SFBool", value="true")), 
     ProtoBody82 = ProtoBody(      # Initial node of ProtoBody determines prototype node type 

      Material83 = Material(ambientIntensity=0.25, diffuseColor=[0.282435,0.085159,0.134462], shininess=0.127273, specularColor=[0.276305,0.11431,0.139857]),       # [HelloWorldProgram diagnostic] should be connected to scene graph: artDeco01ProtoDeclare.getNodeType()=\"Material\" 
      # presence of follow-on TouchSensor shows that additional nodes are allowed in ProtoBody after initial node, regardless of node types 

      TouchSensor84 = TouchSensor(description="within ProtoBody",        IS85 = IS(        connect86 = connect(nodeField="description", protoField="description"), 
        connect87 = connect(nodeField="enabled", protoField="enabled"))))), 
    ExternProtoDeclare88 = ExternProtoDeclare(appinfo="this is a different Material node", name="ArtDeco02Material", url=["http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/ArtDecoPrototypesExcerpt.x3d#ArtDeco02Material","http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/ArtDecoPrototypesExcerpt.x3dv#ArtDeco02Material"],      # [HelloWorldProgram diagnostic] artDeco02ExternProtoDeclare.getNodeType()=\"ERROR_UNKNOWN_EXTERNPROTODECLARE_NODE_TYPE: ExternProtoDeclare name='ArtDeco02Material' type cannot be remotely accessed at run time. TODO X3DJSAIL needs to add further capability that retrieves the ExternProtoDeclare file.\" 

     field89 = field(accessType="inputOutput", appinfo="tooltip for descriptionField", name="description", type="SFString")),     # Tested ArtDeco01ProtoInstance, ArtDeco02ProtoInstance for improper node type when ProtoInstance is added in wrong place 

    Shape90 = Shape(DEF="TestShape1",      Appearance91 = Appearance(DEF="TestAppearance1",       # ArtDeco01Material prototype goes here... TODO ensure setContainerField is handled in exported Java 

      ProtoInstance92 = ProtoInstance(name="ArtDeco01Material",        # [HelloWorldProgram diagnostic] ArtDeco01ProtoInstance.getNodeType()=\"Material\" 

       fieldValue93 = fieldValue(name="description", value="ArtDeco01Material can substitute for a Material node"))), 
     Sphere94 = Sphere(radius=0.001)), 
    Shape95 = Shape(DEF="TestShape2",      Appearance96 = Appearance(DEF="TestAppearance2",       # ArtDeco02Material prototype goes here... TODO ensure setContainerField is handled in exported Java 

      ProtoInstance97 = ProtoInstance(DEF="ArtDeco02MaterialDEF", name="ArtDeco02Material",        # [HelloWorldProgram diagnostic] ArtDeco02ProtoInstance.getNodeType()=\"ERROR_UNKNOWN_EXTERNPROTODECLARE_NODE_TYPE: ExternProtoDeclare name='ArtDeco02Material' type cannot be remotely accessed at run time. TODO X3DJSAIL needs to add further capability that retrieves the ExternProtoDeclare file.\" 

       fieldValue98 = fieldValue(name="description", value="ArtDeco02Material can substitute for another Material node"))), 
     Cone99 = Cone(bottomRadius=0.001, height=0.001)), 
    Shape100 = Shape(DEF="TestShape3",      Appearance101 = Appearance(DEF="TestAppearance3",       # ArtDeco02Material ProtoInstance USE goes here. Note that name field is NOT defined as part of ProtoInstance USE. 

      ProtoInstance102 = ProtoInstance(USE="ArtDeco02MaterialDEF")), 
     Cylinder103 = Cylinder(height=0.001, radius=0.001)), 
    Inline104 = Inline(DEF="inlineSceneDef", url=["someOtherScene.x3d","http://www.web3d.org/specifications/java/examples/someOtherScene.x3d"]), 
    IMPORT105 = IMPORT(AS="WorldInfoDEF2", importedDEF="WorldInfoDEF", inlineDEF="inlineSceneDef"), 
    EXPORT106 = EXPORT(AS="WorldInfoDEF3", localDEF="WorldInfoDEF"), 
    ProtoDeclare107 = ProtoDeclare(appinfo="mimic a Material node and modulate fields as an animation effect", documentation="http://x3dgraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/MaterialModulatorIndex.html", name="MaterialModulator",      ProtoInterface108 = ProtoInterface(      field109 = field(accessType="inputOutput", name="enabled", type="SFBool", value="true"), 
      field110 = field(accessType="inputOutput", name="diffuseColor", type="SFColor", value="0 0 0"), 
      field111 = field(accessType="inputOutput", name="emissiveColor", type="SFColor", value="0.05 0.05 0.5"), 
      field112 = field(accessType="inputOutput", name="specularColor", type="SFColor", value="0 0 0"), 
      field113 = field(accessType="inputOutput", name="transparency", type="SFFloat", value="0.0"), 
      field114 = field(accessType="inputOutput", name="shininess", type="SFFloat", value="0.0"), 
      field115 = field(accessType="inputOutput", name="ambientIntensity", type="SFFloat", value="0.0")), 
     ProtoBody116 = ProtoBody(      Material117 = Material(DEF="MaterialNode",        IS118 = IS(        connect119 = connect(nodeField="diffuseColor", protoField="diffuseColor"), 
        connect120 = connect(nodeField="emissiveColor", protoField="emissiveColor"), 
        connect121 = connect(nodeField="specularColor", protoField="specularColor"), 
        connect122 = connect(nodeField="transparency", protoField="transparency"), 
        connect123 = connect(nodeField="shininess", protoField="shininess"), 
        connect124 = connect(nodeField="ambientIntensity", protoField="ambientIntensity"))),       # Only first node (the node type) is renderable, others are along for the ride 

      Script125 = Script(DEF="MaterialModulatorScript",        field126 = field(accessType="inputOutput", name="enabled", type="SFBool"), 
       field127 = field(accessType="inputOutput", name="diffuseColor", type="SFColor"), 
       field128 = field(accessType="outputOnly", name="newColor", type="SFColor"), 
       field129 = field(accessType="inputOnly", name="clockTrigger", type="SFTime"), 
       IS130 = IS(        connect131 = connect(nodeField="enabled", protoField="enabled"), 
        connect132 = connect(nodeField="diffuseColor", protoField="diffuseColor")),        sourceCode = '''
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

    Group133 = Group(DEF="DeclarativeGroupExample",      Shape134 = Shape(      MetadataString135 = MetadataString(DEF="FindableMetadataStringTest", name="findThisNameValue", value=["test case"]), 
      Appearance136 = Appearance(DEF="DeclarativeAppearanceExample",        # DeclarativeMaterialExample gets overridden by subsequently added MaterialModulator ProtoInstance 

       ProtoInstance137 = ProtoInstance(DEF="MyMaterialModulator", name="MaterialModulator")), 
      Cone138 = Cone(bottom=False, bottomRadius=0.05, height=0.1)),      # Test success: declarativeGroup.addChild() singleton pipeline method 
),     # Test success: declarative statement addChild() 
    # Test success: x3dModel.findNodeByDEF(DeclarativeAppearanceExample) = <Appearance DEF='DeclarativeAppearanceExample'/> i.e. <Appearance DEF='DeclarativeAppearanceExample'> <!- - DeclarativeMaterialExample gets overridden by subsequently added MaterialModulator ProtoInstance - -> <ProtoInstance DEF='MyMaterialModulator' name='MaterialModulator' containerField='material'/> </Appearance> 
    # Test success: x3dModel.findElementByNameValue(findThisNameValue) = <MetadataString DEF='FindableMetadataStringTest' name='findThisNameValue' value='\"test case\"'/> 
    # Test success: x3dModel.findElementByNameValue(\"ArtDeco01Material\", \"ProtoDeclare\") found 
    # Test success: x3dModel.findElementByNameValue(\"MaterialModulator\", \"ProtoDeclare\") found 
    # Test success: x3dModel.findElementByNameValue(\"MaterialModulator\", \"ProtoInstance\") found 

    Group139 = Group(DEF="TestFieldObjectsGroup",      # testFieldObjects() results 
     # SFBool default=true, true=true, false=false, negate()=true 
     # MFBool default=, initial=true false true, negate()=false true false 
     # SFFloat default=0.0, initial=1.0, setValue(2)=2.0, setValue(3.0f)=3.0, setValue(4.0)=4.0 
     # MFFloat default=, initial=1 2 3, append(5)=1 2 3 5, inserts(3,4)(0,0)=0 1 2 3 4 5, append(6)=0 1 2 3 4 5 6, size()=7 
     # ... get1Value[3]=3.0, remove[1]=0 2 3 4 5 6, set1Value(0,10)=10 2 3 4 5 6, multiply(2)=20 4 6 8 10 12, clear= 
     # SFVec3f default=0 0 0, initial=1 2 3, setValue=4 5 6, multiply(2)=8 10 12, normalize()=0.45584232 0.5698029 0.68376344, regex matches()=true 
     # regex test SFVec3f().matches(\"1 2 3\")=true, regex test SFVec3f().matches(\"1 2 3 4\")=false, regex test (SFRotationObject.matches(\"0 0 0 0\")=true, failure detecting illegal (zero axis) rotation value 
), 
    Sound140 = Sound(location=[0,1.6,0],      # set sound-ellipsoid location height at 1.6m to match typical avatar height 

     AudioClip141 = AudioClip(description="chimes", url=["chimes.wav","http://www.web3d.org/x3d/content/examples/ConformanceNist/Sounds/AudioClip/chimes.wav"],       # Scene example fragment from http://www.web3d.org/x3d/content/examples/ConformanceNist/Sounds/AudioClip/default.x3d 
)), 
    Sound142 = Sound(location=[0,1.6,0],      # set sound-ellipsoid location height at 1.6m to match typical avatar height 

     MovieTexture143 = MovieTexture(description="mpgsys.mpg from ConformanceNist suite", url=["mpgsys.mpg","http://www.web3d.org/x3d/content/examples/ConformanceNist/Appearance/MovieTexture/mpgsys.mpg"],       # Scene example fragment from http://www.web3d.org/x3d/content/examples/ConformanceNist/Appearance/MovieTexture/mpeg1-systems.x3d 
      # Expected containerField='source', allowed containerField values=\"texture\" \"source\" \"back\" \"bottom\" \"front\" \"left\" \"right\" \"top\" \"backTexture\" \"bottomTexture\" \"frontTexture\" \"leftTexture\" \"rightTexture\" \"topTexture\" \"watchList\" 
)),     # Test success: AnchorObject.isNode()=true, siteAnchor.isNode()=true 
    # Test success: AnchorObject.isStatement()=false, siteAnchor.isStatement()=false 
    # Test success: ROUTEObject.isNode()=false, orbitPositionROUTE.isNode()=false 
    # Test success: ROUTEObject.isStatement()=true, orbitPositionROUTE.isStatement()=true 
    # Test success: CommentsBlock.isNode()=false, testComments.isNode()=false 
    # Test failure: CommentsBlock.isStatement()=true, testComments.isStatement()=true 

    Shape144 = Shape(DEF="ExtrusionShape",      # ExampleExtrusion isCrossSectionClosed()=true, crossSection='[1.0, 1.0, 1.0, -1.0, -1.0, -1.0, -1.0, 1.0, 1.0, 1.0]' 
     # ExampleExtrusion isSpineClosed()=false, spine='[0.0, 0.0, 0.0, 0.0, 1.0, 0.0]' 

     Appearance145 = Appearance(DEF="TransparentAppearance",       Material146 = Material(transparency=1.0)), 
     Extrusion147 = Extrusion(DEF="ExampleExtrusion")), 
    Group148 = Group(     # Test MFNode children array as an ordered list consisting of comments, statements, ProtoInstance and nodes 

     ProtoDeclare149 = ProtoDeclare(name="NewWorldInfo",       ProtoInterface150 = ProtoInterface(       field151 = field(accessType="initializeOnly", name="description", type="SFString")), 
      ProtoBody152 = ProtoBody(       WorldInfo153 = WorldInfo())), 
     ProtoInstance154 = ProtoInstance(DEF="Proto1", name="NewWorldInfo",       fieldValue155 = fieldValue(name="description", value="testing 1 2 3")), 
     Group156 = Group(DEF="Node2",       # intentionally empty 
), 
     ProtoInstance157 = ProtoInstance(DEF="Proto3", name="NewWorldInfo"), 
     Transform158 = Transform(DEF="Node4",       # intentionally empty 
),      # Test satisfactorily creates MFNode children array as an ordered list with mixed content 
), 
    ProtoDeclare159 = ProtoDeclare(name="ShaderProto",      ProtoBody160 = ProtoBody(      ProgramShader161 = ProgramShader())), 
    Shape162 = Shape(     Appearance163 = Appearance(      # Test MFNode shaders array as an ordered list consisting of comments, ProtoInstance and nodes 
      # Test satisfactorily creates MFNode shaders array as an ordered list with mixed content 

      ProgramShader164 = ProgramShader(DEF="TestShader1",        ShaderProgram165 = ShaderProgram(DEF="TestShader2")), 
      ProtoInstance166 = ProtoInstance(DEF="TestShader3", name="ShaderProto"), 
      ComposedShader167 = ComposedShader(DEF="TestShader4",        ShaderPart168 = ShaderPart(DEF="TestShader5"))))))
