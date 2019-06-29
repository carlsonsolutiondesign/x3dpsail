import X3Dpackage


X3D0 = (X3Dpackage.X3D().setProfile("Immersive").setVersion("3.3")
      # x3dVersionComparisonTest for this model: supportsX3dVersion(X3DObject.VERSION_3_0)=true 

      .setHead(X3Dpackage.head()
        # comment #1 

        # comment #2 

        # comment #3 

        # comment #4 

        .addComponent(X3Dpackage.component().setLevel(3).setName("Navigation"))
        .addComponent(X3Dpackage.component().setLevel(1).setName("Shaders"))
        .addComponent(X3Dpackage.component().setLevel(1).setName("Layering"))
        .addUnit(X3Dpackage.unit(setCategory = "angle").setConversionFactor(1.0).setName("AngleUnitConversion"))
        .addUnit(X3Dpackage.unit(setCategory = "length").setConversionFactor(1.0).setName("LengthUnitConversion"))
        .addMeta(X3Dpackage.meta().setContent("HelloWorldProgramOutput.x3d").setName("title"))
        .addMeta(X3Dpackage.meta().setContent("Example HelloWorldProgram creates an X3D model using the X3D Java Scene Access Interface Library (X3DJSAIL)").setName("description"))
        .addMeta(X3Dpackage.meta().setContent("http://www.web3d.org/specifications/java/X3DJSAIL.html").setName("reference"))
        .addMeta(X3Dpackage.meta().setContent("HelloWorldProgramOutput.java").setName("generator"))
        .addMeta(X3Dpackage.meta().setContent("6 September 2016").setName("created"))
        .addMeta(X3Dpackage.meta().setContent("27 December 2018").setName("modified"))
        .addMeta(X3Dpackage.meta().setContent("X3D Java Scene Access Interface Library (X3DJSAIL)").setName("generator"))
        .addMeta(X3Dpackage.meta().setContent("http://www.web3d.org/specifications/java/examples/HelloWorldProgram.java").setName("generator"))
        .addMeta(X3Dpackage.meta().setContent("Netbeans http://www.netbeans.org").setName("generator"))
        .addMeta(X3Dpackage.meta().setContent("Don Brutzman").setName("creator"))
        .addMeta(X3Dpackage.meta().setContent("https://sourceforge.net/p/x3d/code/HEAD/tree/www.web3d.org/x3d/stylesheets/java/examples/HelloWorldProgramOutput.x3d").setName("reference"))
        .addMeta(X3Dpackage.meta().setContent("Console output, ClassicVRML encoding, VRML97 encoding and pretty-print documentation:").setName("reference"))
        .addMeta(X3Dpackage.meta().setContent("HelloWorldProgramOutput.txt").setName("reference"))
        .addMeta(X3Dpackage.meta().setContent("HelloWorldProgramOutput.x3dv").setName("reference"))
        .addMeta(X3Dpackage.meta().setContent("HelloWorldProgramOutput.wrl").setName("reference"))
        .addMeta(X3Dpackage.meta().setContent("HelloWorldProgramOutput.html").setName("reference"))
        .addMeta(X3Dpackage.meta().setContent("https://savage.nps.edu/X3dValidator?url=http://www.web3d.org/specifications/java/examples/HelloWorldProgramOutput.x3d").setName("reference"))
        .addMeta(X3Dpackage.meta().setContent("http://www.web3d.org/specifications/java/examples/HelloWorldProgramOutput.x3d").setName("identifier"))
        .addMeta(X3Dpackage.meta().setContent("../license.html").setName("license")))
      .setScene(X3Dpackage.Scene()
        .addChildren(X3Dpackage.ViewpointGroup().setDescription("Available viewpoints")
          .addChildren(X3Dpackage.Viewpoint().setDEF("DefaultView").setDescription("Hello X3DJSAIL"))
          .addChildren(X3Dpackage.Viewpoint().setDEF("TopDownView").setDescription("top-down view from above").setOrientation([1,0,0,-1.570796]).setPosition([0,100,0])))
        .addChildren(X3Dpackage.NavigationInfo().setAvatarSize([0.25,1.6,0.75]).setTransitionType(["LINEAR"]).setType(["EXAMINE","FLY","ANY"]))
        .addChildren(X3Dpackage.WorldInfo().setDEF("WorldInfoDEF").setTitle("HelloWorldProgram produced by X3D Java SAI Library (X3DJSAIL)"))
        .addChildren(X3Dpackage.WorldInfo().setUSE("WorldInfoDEF"))
        .addChildren(X3Dpackage.WorldInfo().setUSE("WorldInfoDEF"))
        .addChildren(X3Dpackage.MetadataString().setDEF("scene.addChildMetadata").setName("test").setValue(["Top-level root Metadata node beneath Scene needs to be one of '-children' in JSON encoding"]))
        .addLayerSet(X3Dpackage.LayerSet(setOrder = [0]).setDEF("scene.addChildLayerSetTest"))
        .addChildren(X3Dpackage.Transform().setDEF("LogoGeometryTransform").setTranslation([0,1.5,0])
          .addChildren(X3Dpackage.Anchor().setDescription("select for X3D Java SAI Library (X3DJSAIL) description").setUrl(["../X3DJSAIL.html","http://www.web3d.org/specifications/java/X3DJSAIL.html"])
            .addChildren(X3Dpackage.Shape().setDEF("BoxShape")
              .setAppearance(X3Dpackage.Appearance()
                .setMaterial(X3Dpackage.Material().setDEF("GreenMaterial").setDiffuseColor([0,1,1]).setEmissiveColor([0.8,0,0]).setTransparency(0.1))
                .setTexture(X3Dpackage.ImageTexture().setUrl(["images/X3dJavaSceneAccessInterfaceSaiLibrary.png","http://www.web3d.org/specifications/java/examples/images/X3dJavaSceneAccessInterfaceSaiLibrary.png"])))
              .setGeometry(X3Dpackage.Box().setDEF("test-NMTOKEN_regex.0123456789").setClass("untextured")))))
        .addChildren(X3Dpackage.Shape().setDEF("LineShape")
          .setAppearance(X3Dpackage.Appearance()
            .setMaterial(X3Dpackage.Material().setEmissiveColor([0.6,0.19607843,0.8])))
          .setGeometry(X3Dpackage.IndexedLineSet(setCoordIndex = [0,1,2,3,4,0])
            # Coordinate 3-tuple point count: 6 

            .setCoord(X3Dpackage.Coordinate().setPoint([0,1.5,0,2,1.5,0,2,1.5,-2,-2,1.5,-2,-2,1.5,0,0,1.5,0]))))
        .addChildren(X3Dpackage.PositionInterpolator().setDEF("BoxPathAnimator").setKey([0,0.125,0.375,0.625,0.875,1]).setKeyValue([0,1.5,0,2,1.5,0,2,1.5,-2,-2,1.5,-2,-2,1.5,0,0,1.5,0]))
        .addChildren(X3Dpackage.TimeSensor().setDEF("OrbitClock").setCycleInterval(8.0).setLoop(True))
        .addChildren(X3Dpackage.ROUTE().setFromField("fraction_changed").setFromNode("OrbitClock").setToField("set_fraction").setToNode("BoxPathAnimator"))
        .addChildren(X3Dpackage.ROUTE().setFromField("value_changed").setFromNode("BoxPathAnimator").setToField("set_translation").setToNode("LogoGeometryTransform"))
        .addChildren(X3Dpackage.Transform().setDEF("TextTransform").setTranslation([0,-1.5,0])
          .addChildren(X3Dpackage.Shape()
            .setAppearance(X3Dpackage.Appearance()
              .setMaterial(X3Dpackage.Material().setUSE("GreenMaterial")))
            .setGeometry(X3Dpackage.Text().setString(["X3D Java","SAI Library","X3DJSAIL"])
              # Comment example A, plain quotation marks: He said, \"Immel did it!\" 

              # Comment example B, XML character entities: He said, &quot;Immel did it!&quot; 

              .setMetadata(X3Dpackage.MetadataSet().setName("EscapedQuotationMarksMetadataSet")
                .addValue(X3Dpackage.MetadataString().setName("quotesTestC").setValue(["MFString example C, backslash-escaped quotes: He said, \"Immel did it!\""]))
                .addValue(X3Dpackage.MetadataString().setName("extraChildTest").setValue(["checks MetadataSetObject addValue() method"])))
              .setFontStyle(X3Dpackage.FontStyle(setFamily = ["SERIF"], setJustify = ["MIDDLE","MIDDLE"]))))
          .addChildren(X3Dpackage.Collision()
            # test containerField='proxy' 

            .setProxy(X3Dpackage.Shape().setDEF("ProxyShape")
              # alternative XML encoding: Text string='\"One, Two, Comment\" \"\" \"He said, \\&quot;Immel did it!\\&quot;\"' 

              # alternative XML encoding: Text string='\"One, Two, Comment\" \"\" \"He said, \\&quot;Immel did it!\\&quot;\" \"\"' 

              # alternative Java source: .setString(new String [] {\"One, Two, Comment\", \"\", \"He said, \\\"Immel did it!\\\"\"}) 

              # reference: http://www.web3d.org/x3d/content/examples/Basic/X3dSpecifications/StringArrayEncodingExamplesIndex.html 

              .setGeometry(X3Dpackage.Text().setString(["One, Two, Text","","He said, \"Immel did it!\" \"\""]))))
          # It's a beautiful world 

          # ... for you! 

          # https://en.wikipedia.org/wiki/Beautiful_World_(Devo_song) 

          )
        # repeatedly spin 180 degrees as a readable special effect 

        .addChildren(X3Dpackage.OrientationInterpolator().setDEF("SpinInterpolator").setKey([0,0.5,1]).setKeyValue([0,1,0,4.712389,0,1,0,0,0,1,0,1.5707964]))
        .addChildren(X3Dpackage.TimeSensor().setDEF("SpinClock").setCycleInterval(5.0).setLoop(True))
        .addChildren(X3Dpackage.ROUTE().setFromField("fraction_changed").setFromNode("SpinClock").setToField("set_fraction").setToNode("SpinInterpolator"))
        .addChildren(X3Dpackage.ROUTE().setFromField("value_changed").setFromNode("SpinInterpolator").setToField("rotation").setToNode("TextTransform"))
        .addChildren(X3Dpackage.Group().setDEF("BackgroundGroup")
          .addChildren(X3Dpackage.Background().setDEF("GradualBackground"))
          .addChildren(X3Dpackage.Script().setDEF("colorTypeConversionScript")
            .addField(X3Dpackage.field().setAccessType("inputOnly").setName("colorInput").setType("SFColor"))
            .addField(X3Dpackage.field().setAccessType("outputOnly").setName("colorsOutput").setType("MFColor")).setSourceCode('''\n"+
"ecmascript:\n"+
"\n"+
"function colorInput (eventValue) // Example source code\n"+
"{\n"+
"   colorsOutput = new MFColor(eventValue); // assigning value sends output event\n"+
"// Browser.print('colorInput=' + eventValue + ', colorsOutput=' + colorsOutput + '\\n');\n"+
"}\n"+
"''')
)
          .addChildren(X3Dpackage.ColorInterpolator().setDEF("ColorAnimator").setKey([0,0.5,1]).setKeyValue([0.9411765,1,1,0.29411766,0,0.50980395,0.9411765,1,1])
            # AZURE to INDIGO and back again 

            )
          .addChildren(X3Dpackage.TimeSensor().setDEF("ColorClock").setCycleInterval(60.0).setLoop(True))
          .addChildren(X3Dpackage.ROUTE().setFromField("colorsOutput").setFromNode("colorTypeConversionScript").setToField("skyColor").setToNode("GradualBackground"))
          .addChildren(X3Dpackage.ROUTE().setFromField("value_changed").setFromNode("ColorAnimator").setToField("colorInput").setToNode("colorTypeConversionScript"))
          .addChildren(X3Dpackage.ROUTE().setFromField("fraction_changed").setFromNode("ColorClock").setToField("set_fraction").setToNode("ColorAnimator")))
        .addChildren(X3Dpackage.ProtoDeclare().setAppinfo("tooltip: ArtDeco01Material prototype is a Material node").setName("ArtDeco01Material")
          .setProtoInterface(X3Dpackage.ProtoInterface()
            .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("tooltip for descriptionField").setName("description").setType("SFString").setValue("ArtDeco01Material prototype is a Material node"))
            .addField(X3Dpackage.field().setAccessType("inputOutput").setName("enabled").setType("SFBool").setValue("true")))
          .setProtoBody(X3Dpackage.ProtoBody()
            # Initial node of ProtoBody determines prototype node type 

            .addChildren(X3Dpackage.Material().setAmbientIntensity(0.25).setDiffuseColor([0.282435,0.085159,0.134462]).setShininess(0.127273).setSpecularColor([0.276305,0.11431,0.139857]))
            # [HelloWorldProgram diagnostic] should be connected to scene graph: artDeco01ProtoDeclare.getNodeType()=\"Material\" 

            # presence of follow-on TouchSensor shows that additional nodes are allowed in ProtoBody after initial node, regardless of node types 

            .addChildren(X3Dpackage.TouchSensor().setDescription("within ProtoBody")
              .setIS(X3Dpackage.IS()
                .addConnect(X3Dpackage.connect().setNodeField("description").setProtoField("description"))
                .addConnect(X3Dpackage.connect().setNodeField("enabled").setProtoField("enabled"))))))
        .addChildren(X3Dpackage.ExternProtoDeclare().setAppinfo("this is a different Material node").setName("ArtDeco02Material").setUrl(["http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/ArtDecoPrototypesExcerpt.x3d#ArtDeco02Material","http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/ArtDecoPrototypesExcerpt.x3dv#ArtDeco02Material"])
          # [HelloWorldProgram diagnostic] artDeco02ExternProtoDeclare.getNodeType()=\"ERROR_UNKNOWN_EXTERNPROTODECLARE_NODE_TYPE: ExternProtoDeclare name='ArtDeco02Material' type cannot be remotely accessed at run time. TODO X3DJSAIL needs to add further capability that retrieves the ExternProtoDeclare file.\" 

          .addField(X3Dpackage.field().setAccessType("inputOutput").setAppinfo("tooltip for descriptionField").setName("description").setType("SFString")))
        # Tested ArtDeco01ProtoInstance, ArtDeco02ProtoInstance for improper node type when ProtoInstance is added in wrong place 

        .addChildren(X3Dpackage.Shape().setDEF("TestShape1")
          .setAppearance(X3Dpackage.Appearance().setDEF("TestAppearance1")
            # ArtDeco01Material prototype goes here... TODO ensure setContainerField is handled in exported Java 

            .setMaterial(X3Dpackage.ProtoInstance().setName("ArtDeco01Material")
              # [HelloWorldProgram diagnostic] ArtDeco01ProtoInstance.getNodeType()=\"Material\" 

              .addFieldValue(X3Dpackage.fieldValue().setName("description").setValue("ArtDeco01Material can substitute for a Material node"))))
          .setGeometry(X3Dpackage.Sphere(setRadius = 0.001)))
        .addChildren(X3Dpackage.Shape().setDEF("TestShape2")
          .setAppearance(X3Dpackage.Appearance().setDEF("TestAppearance2")
            # ArtDeco02Material prototype goes here... TODO ensure setContainerField is handled in exported Java 

            .setMaterial(X3Dpackage.ProtoInstance().setDEF("ArtDeco02MaterialDEF").setName("ArtDeco02Material")
              # [HelloWorldProgram diagnostic] ArtDeco02ProtoInstance.getNodeType()=\"ERROR_UNKNOWN_EXTERNPROTODECLARE_NODE_TYPE: ExternProtoDeclare name='ArtDeco02Material' type cannot be remotely accessed at run time. TODO X3DJSAIL needs to add further capability that retrieves the ExternProtoDeclare file.\" 

              .addFieldValue(X3Dpackage.fieldValue().setName("description").setValue("ArtDeco02Material can substitute for another Material node"))))
          .setGeometry(X3Dpackage.Cone(setBottomRadius = 0.001, setHeight = 0.001)))
        .addChildren(X3Dpackage.Shape().setDEF("TestShape3")
          .setAppearance(X3Dpackage.Appearance().setDEF("TestAppearance3")
            # ArtDeco02Material ProtoInstance USE goes here. Note that name field is NOT defined as part of ProtoInstance USE. 

            .setMaterial(X3Dpackage.ProtoInstance().setUSE("ArtDeco02MaterialDEF")))
          .setGeometry(X3Dpackage.Cylinder(setHeight = 0.001, setRadius = 0.001)))
        .addChildren(X3Dpackage.Inline().setDEF("inlineSceneDef").setUrl(["someOtherScene.x3d","http://www.web3d.org/specifications/java/examples/someOtherScene.x3d"]))
        .addChildren(X3Dpackage.IMPORT().setAS("WorldInfoDEF2").setImportedDEF("WorldInfoDEF").setInlineDEF("inlineSceneDef"))
        .addChildren(X3Dpackage.EXPORT().setAS("WorldInfoDEF3").setLocalDEF("WorldInfoDEF"))
        .addChildren(X3Dpackage.ProtoDeclare().setAppinfo("mimic a Material node and modulate fields as an animation effect").setDocumentation("http://x3dgraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/MaterialModulatorIndex.html").setName("MaterialModulator")
          .setProtoInterface(X3Dpackage.ProtoInterface()
            .addField(X3Dpackage.field().setAccessType("inputOutput").setName("enabled").setType("SFBool").setValue("true"))
            .addField(X3Dpackage.field().setAccessType("inputOutput").setName("diffuseColor").setType("SFColor").setValue("0 0 0"))
            .addField(X3Dpackage.field().setAccessType("inputOutput").setName("emissiveColor").setType("SFColor").setValue("0.05 0.05 0.5"))
            .addField(X3Dpackage.field().setAccessType("inputOutput").setName("specularColor").setType("SFColor").setValue("0 0 0"))
            .addField(X3Dpackage.field().setAccessType("inputOutput").setName("transparency").setType("SFFloat").setValue("0.0"))
            .addField(X3Dpackage.field().setAccessType("inputOutput").setName("shininess").setType("SFFloat").setValue("0.0"))
            .addField(X3Dpackage.field().setAccessType("inputOutput").setName("ambientIntensity").setType("SFFloat").setValue("0.0")))
          .setProtoBody(X3Dpackage.ProtoBody()
            .addChildren(X3Dpackage.Material().setDEF("MaterialNode")
              .setIS(X3Dpackage.IS()
                .addConnect(X3Dpackage.connect().setNodeField("diffuseColor").setProtoField("diffuseColor"))
                .addConnect(X3Dpackage.connect().setNodeField("emissiveColor").setProtoField("emissiveColor"))
                .addConnect(X3Dpackage.connect().setNodeField("specularColor").setProtoField("specularColor"))
                .addConnect(X3Dpackage.connect().setNodeField("transparency").setProtoField("transparency"))
                .addConnect(X3Dpackage.connect().setNodeField("shininess").setProtoField("shininess"))
                .addConnect(X3Dpackage.connect().setNodeField("ambientIntensity").setProtoField("ambientIntensity"))))
            # Only first node (the node type) is renderable, others are along for the ride 

            .addChildren(X3Dpackage.Script().setDEF("MaterialModulatorScript")
              .addField(X3Dpackage.field().setAccessType("inputOutput").setName("enabled").setType("SFBool"))
              .addField(X3Dpackage.field().setAccessType("inputOutput").setName("diffuseColor").setType("SFColor"))
              .addField(X3Dpackage.field().setAccessType("outputOnly").setName("newColor").setType("SFColor"))
              .addField(X3Dpackage.field().setAccessType("inputOnly").setName("clockTrigger").setType("SFTime"))
              .setIS(X3Dpackage.IS()
                .addConnect(X3Dpackage.connect().setNodeField("enabled").setProtoField("enabled"))
                .addConnect(X3Dpackage.connect().setNodeField("diffuseColor").setProtoField("diffuseColor"))).setSourceCode('''\n"+
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
)))
        # Test success: declarative statement createDeclarativeShapeTests() 

        .addChildren(X3Dpackage.Group().setDEF("DeclarativeGroupExample")
          .addChildren(X3Dpackage.Shape()
            .setMetadata(X3Dpackage.MetadataString().setDEF("FindableMetadataStringTest").setName("findThisNameValue").setValue(["test case"]))
            .setAppearance(X3Dpackage.Appearance().setDEF("DeclarativeAppearanceExample")
              # DeclarativeMaterialExample gets overridden by subsequently added MaterialModulator ProtoInstance 

              .setMaterial(X3Dpackage.ProtoInstance().setDEF("MyMaterialModulator").setName("MaterialModulator")))
            .setGeometry(X3Dpackage.Cone(setBottom = False, setBottomRadius = 0.05, setHeight = 0.1)))
          # Test success: declarativeGroup.addChild() singleton pipeline method 

          )
        # Test success: declarative statement addChild() 

        # Test success: x3dModel.findNodeByDEF(DeclarativeAppearanceExample) = <Appearance DEF='DeclarativeAppearanceExample'/> i.e. <Appearance DEF='DeclarativeAppearanceExample'> <!- - DeclarativeMaterialExample gets overridden by subsequently added MaterialModulator ProtoInstance - -> <ProtoInstance DEF='MyMaterialModulator' name='MaterialModulator' containerField='material'/> </Appearance> 

        # Test success: x3dModel.findElementByNameValue(findThisNameValue) = <MetadataString DEF='FindableMetadataStringTest' name='findThisNameValue' value='\"test case\"'/> 

        # Test success: x3dModel.findElementByNameValue(\"ArtDeco01Material\", \"ProtoDeclare\") found 

        # Test success: x3dModel.findElementByNameValue(\"MaterialModulator\", \"ProtoDeclare\") found 

        # Test success: x3dModel.findElementByNameValue(\"MaterialModulator\", \"ProtoInstance\") found 

        .addChildren(X3Dpackage.Group().setDEF("TestFieldObjectsGroup")
          # testFieldObjects() results 

          # SFBool default=true, true=true, false=false, negate()=true 

          # MFBool default=, initial=true false true, negate()=false true false 

          # SFFloat default=0.0, initial=1.0, setValue(2)=2.0, setValue(3.0f)=3.0, setValue(4.0)=4.0 

          # MFFloat default=, initial=1 2 3, append(5)=1 2 3 5, inserts(3,4)(0,0)=0 1 2 3 4 5, append(6)=0 1 2 3 4 5 6, size()=7 

          # ... get1Value[3]=3.0, remove[1]=0 2 3 4 5 6, set1Value(0,10)=10 2 3 4 5 6, multiply(2)=20 4 6 8 10 12, clear= 

          # SFVec3f default=0 0 0, initial=1 2 3, setValue=4 5 6, multiply(2)=8 10 12, normalize()=0.45584232 0.5698029 0.68376344, regex matches()=true 

          # regex test SFVec3f().matches(\"1 2 3\")=true, regex test SFVec3f().matches(\"1 2 3 4\")=false, regex test (SFRotationObject.matches(\"0 0 0 0\")=true, failure detecting illegal (zero axis) rotation value 

          )
        .addChildren(X3Dpackage.Sound().setLocation([0,1.6,0])
          # set sound-ellipsoid location height at 1.6m to match typical avatar height 

          .setSource(X3Dpackage.AudioClip().setDescription("chimes").setUrl(["chimes.wav","http://www.web3d.org/x3d/content/examples/ConformanceNist/Sounds/AudioClip/chimes.wav"])
            # Scene example fragment from http://www.web3d.org/x3d/content/examples/ConformanceNist/Sounds/AudioClip/default.x3d 

            ))
        .addChildren(X3Dpackage.Sound().setLocation([0,1.6,0])
          # set sound-ellipsoid location height at 1.6m to match typical avatar height 

          .setSource(X3Dpackage.MovieTexture().setDescription("mpgsys.mpg from ConformanceNist suite").setUrl(["mpgsys.mpg","http://www.web3d.org/x3d/content/examples/ConformanceNist/Appearance/MovieTexture/mpgsys.mpg"])
            # Scene example fragment from http://www.web3d.org/x3d/content/examples/ConformanceNist/Appearance/MovieTexture/mpeg1-systems.x3d 

            # Expected containerField='source', allowed containerField values=\"texture\" \"source\" \"back\" \"bottom\" \"front\" \"left\" \"right\" \"top\" \"backTexture\" \"bottomTexture\" \"frontTexture\" \"leftTexture\" \"rightTexture\" \"topTexture\" \"watchList\" 

            ))
        # Test success: AnchorObject.isNode()=true, siteAnchor.isNode()=true 

        # Test success: AnchorObject.isStatement()=false, siteAnchor.isStatement()=false 

        # Test success: ROUTEObject.isNode()=false, orbitPositionROUTE.isNode()=false 

        # Test success: ROUTEObject.isStatement()=true, orbitPositionROUTE.isStatement()=true 

        # Test success: CommentsBlock.isNode()=false, testComments.isNode()=false 

        # Test failure: CommentsBlock.isStatement()=true, testComments.isStatement()=true 

        .addChildren(X3Dpackage.Shape().setDEF("ExtrusionShape")
          # ExampleExtrusion isCrossSectionClosed()=true, crossSection='[1.0, 1.0, 1.0, -1.0, -1.0, -1.0, -1.0, 1.0, 1.0, 1.0]' 

          # ExampleExtrusion isSpineClosed()=false, spine='[0.0, 0.0, 0.0, 0.0, 1.0, 0.0]' 

          .setAppearance(X3Dpackage.Appearance().setDEF("TransparentAppearance")
            .setMaterial(X3Dpackage.Material().setTransparency(1.0)))
          .setGeometry(X3Dpackage.Extrusion().setDEF("ExampleExtrusion")))
        .addChildren(X3Dpackage.Group()
          # Test MFNode children array as an ordered list consisting of comments, statements, ProtoInstance and nodes 

          .addChildren(X3Dpackage.ProtoDeclare().setName("NewWorldInfo")
            .setProtoInterface(X3Dpackage.ProtoInterface()
              .addField(X3Dpackage.field().setAccessType("initializeOnly").setName("description").setType("SFString")))
            .setProtoBody(X3Dpackage.ProtoBody()
              .addChildren(X3Dpackage.WorldInfo())))
          .addChildren(X3Dpackage.ProtoInstance().setDEF("Proto1").setName("NewWorldInfo")
            .addFieldValue(X3Dpackage.fieldValue().setName("description").setValue("testing 1 2 3")))
          .addChildren(X3Dpackage.Group().setDEF("Node2")
            # intentionally empty 

            )
          .addChildren(X3Dpackage.ProtoInstance().setDEF("Proto3").setName("NewWorldInfo"))
          .addChildren(X3Dpackage.Transform().setDEF("Node4")
            # intentionally empty 

            )
          # Test satisfactorily creates MFNode children array as an ordered list with mixed content 

          )
        .addChildren(X3Dpackage.ProtoDeclare().setName("ShaderProto")
          .setProtoBody(X3Dpackage.ProtoBody()
            .addShaders(X3Dpackage.ProgramShader())))
        .addChildren(X3Dpackage.Shape()
          .setAppearance(X3Dpackage.Appearance()
            # Test MFNode shaders array as an ordered list consisting of comments, ProtoInstance and nodes 

            # Test satisfactorily creates MFNode shaders array as an ordered list with mixed content 

            .addShaders(X3Dpackage.ProgramShader().setDEF("TestShader1")
              .addPrograms(X3Dpackage.ShaderProgram().setDEF("TestShader2")))
            .addShaders(X3Dpackage.ProtoInstance().setDEF("TestShader3").setName("ShaderProto"))
            .addShaders(X3Dpackage.ComposedShader().setDEF("TestShader4")
              .addParts(X3Dpackage.ShaderPart().setDEF("TestShader5")))))))

