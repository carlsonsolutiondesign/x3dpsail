import x3dpsail as x3d


X3D0 = (x3d.X3D().setProfile("Immersive").setVersion("3.3")
      # x3dVersionComparisonTest for this model: supportsX3dVersion(X3DObject.VERSION_3_0)=true 

      .setHead(x3d.head()
        # comment #1 

        # comment #2 

        # comment #3 

        # comment #4 

        .addComponent(x3d.component().setName(x3d.SFString("Navigation")).setLevel(3))
        .addComponent(x3d.component().setName(x3d.SFString("Layering")).setLevel(1))
        .addComponent(x3d.component().setName(x3d.SFString("Shaders")).setLevel(1))
        .addComponent(x3d.component().setName(x3d.SFString("CADGeometry")).setLevel(2))
        .addComponent(x3d.component().setName(x3d.SFString("DIS")).setLevel(2))
        .addComponent(x3d.component().setName(x3d.SFString("H-Anim")).setLevel(1))
        .addUnit(x3d.unit().setName(x3d.SFString("AngleUnitConversion")).setCategory("angle").setConversionFactor(1.0))
        .addUnit(x3d.unit().setName(x3d.SFString("LengthUnitConversion")).setCategory("length").setConversionFactor(1.0))
        .addUnit(x3d.unit().setName(x3d.SFString("ForceFromPoundsToNewtons")).setCategory("force").setConversionFactor(4.4482))
        .addMeta(x3d.meta().setContent("HelloWorldProgramOutput.x3d").setName(x3d.SFString("title")))
        .addMeta(x3d.meta().setContent("continued development and testing in progress").setName(x3d.SFString("info")))
        .addMeta(x3d.meta().setContent("Example HelloWorldProgram creates an X3D model using the X3D Java Scene Access Interface Library (X3DJSAIL)").setName(x3d.SFString("description")))
        .addMeta(x3d.meta().setContent("http://www.web3d.org/specifications/java/X3DJSAIL.html").setName(x3d.SFString("reference")))
        .addMeta(x3d.meta().setContent("HelloWorldProgramOutput.java").setName(x3d.SFString("generator")))
        .addMeta(x3d.meta().setContent("6 September 2016").setName(x3d.SFString("created")))
        .addMeta(x3d.meta().setContent("19 June 2019").setName(x3d.SFString("modified")))
        .addMeta(x3d.meta().setContent("X3D Java Scene Access Interface Library (X3DJSAIL)").setName(x3d.SFString("generator")))
        .addMeta(x3d.meta().setContent("http://www.web3d.org/specifications/java/examples/HelloWorldProgram.java").setName(x3d.SFString("generator")))
        .addMeta(x3d.meta().setContent("Netbeans http://www.netbeans.org").setName(x3d.SFString("generator")))
        .addMeta(x3d.meta().setContent("Don Brutzman").setName(x3d.SFString("creator")))
        .addMeta(x3d.meta().setContent("https://sourceforge.net/p/x3d/code/HEAD/tree/www.web3d.org/x3d/stylesheets/java/examples/HelloWorldProgramOutput.x3d").setName(x3d.SFString("reference")))
        .addMeta(x3d.meta().setContent("Console output, ClassicVRML encoding, VRML97 encoding and pretty-print documentation:").setName(x3d.SFString("reference")))
        .addMeta(x3d.meta().setContent("HelloWorldProgramOutput.txt").setName(x3d.SFString("reference")))
        .addMeta(x3d.meta().setContent("HelloWorldProgramOutput.x3dv").setName(x3d.SFString("reference")))
        .addMeta(x3d.meta().setContent("HelloWorldProgramOutput.wrl").setName(x3d.SFString("reference")))
        .addMeta(x3d.meta().setContent("HelloWorldProgramOutput.html").setName(x3d.SFString("reference")))
        .addMeta(x3d.meta().setContent("https://savage.nps.edu/X3dValidator?url=http://www.web3d.org/specifications/java/examples/HelloWorldProgramOutput.x3d").setName(x3d.SFString("reference")))
        .addMeta(x3d.meta().setContent("http://www.web3d.org/specifications/java/examples/HelloWorldProgramOutput.x3d").setName(x3d.SFString("identifier")))
        .addMeta(x3d.meta().setContent("../license.html").setName(x3d.SFString("license"))))
      .setScene(x3d.Scene()
        .addChild(x3d.ViewpointGroup().setDescription(x3d.SFString("Available viewpoints"))
          .addChild(x3d.Viewpoint().setDEF(x3d.SFString("DefaultView")).setDescription(x3d.SFString("Hello X3DJSAIL")))
          .addChild(x3d.Viewpoint().setDEF(x3d.SFString("TopDownView")).setDescription(x3d.SFString("top-down view from above")).setOrientation(x3d.SFRotation([1,0,0,-1.570796])).setPosition(x3d.SFVec3f([0,100,0]))))
        .addChild(x3d.NavigationInfo().setAvatarSize([0.25,1.6,0.75]).setTransitionType(["LINEAR"]).setType(["EXAMINE","FLY","ANY"]))
        .addChild(x3d.WorldInfo().setDEF(x3d.SFString("WorldInfoDEF")).setTitle("HelloWorldProgram produced by X3D Java SAI Library (X3DJSAIL)"))
        .addChild(x3d.WorldInfo().setUSE(x3d.SFString("WorldInfoDEF")))
        .addChild(x3d.WorldInfo().setUSE(x3d.SFString("WorldInfoDEF")))
        .addMetadata(x3d.MetadataString().setDEF(x3d.SFString("scene.addChildMetadata")).setName(x3d.SFString("test")).setValue(x3d.MFString(["Top-level root Metadata node beneath Scene needs to be one of '-children' in JSON encoding"])))
        .addLayerSet(x3d.LayerSet().setDEF(x3d.SFString("scene.addChildLayerSetTest")).setOrder(x3d.MFInt32([0])))
        .addChild(x3d.Transform().setDEF(x3d.SFString("LogoGeometryTransform")).setTranslation(x3d.SFVec3f([0,1.5,0]))
          .addChild(x3d.Anchor().setDescription(x3d.SFString("select for X3D Java SAI Library (X3DJSAIL) description")).setUrl(x3d.MFString(["../X3DJSAIL.html","http://www.web3d.org/specifications/java/X3DJSAIL.html"]))
            .addChild(x3d.Shape().setDEF(x3d.SFString("BoxShape"))
              .setAppearance(x3d.Appearance()
                .setMaterial(x3d.Material().setDEF(x3d.SFString("GreenMaterial")).setDiffuseColor([0,1,1]).setEmissiveColor([0.8,0,0]).setTransparency(0.1))
                .setTexture(x3d.ImageTexture().setUrl(x3d.MFString(["images/X3dJavaSceneAccessInterfaceSaiLibrary.png","http://www.web3d.org/specifications/java/examples/images/X3dJavaSceneAccessInterfaceSaiLibrary.png"]))))
              .setGeometry(x3d.Box().setDEF(x3d.SFString("test-NMTOKEN_regex.0123456789")).setCssClass(x3d.SFString("untextured"))))))
        .addChild(x3d.Shape().setDEF(x3d.SFString("LineShape"))
          .setAppearance(x3d.Appearance()
            .setMaterial(x3d.Material().setEmissiveColor([0.6,0.19607843,0.8])))
          .setGeometry(x3d.IndexedLineSet().setCoordIndex([0,1,2,3,4,0])
            # Coordinate 3-tuple point count: 6 

            .setCoord(x3d.Coordinate().setPoint([0,1.5,0,2,1.5,0,2,1.5,-2,-2,1.5,-2,-2,1.5,0,0,1.5,0]))))
        .addChild(x3d.PositionInterpolator().setDEF(x3d.SFString("BoxPathAnimator")).setKey([0,0.125,0.375,0.625,0.875,1]).setKeyValue([0,1.5,0,2,1.5,0,2,1.5,-2,-2,1.5,-2,-2,1.5,0,0,1.5,0]))
        .addChild(x3d.TimeSensor().setDEF(x3d.SFString("OrbitClock")).setCycleInterval(8.0).setLoop(True))
        .addChild(x3d.ROUTE().setFromField("fraction_changed").setFromNode("OrbitClock").setToField("set_fraction").setToNode("BoxPathAnimator"))
        .addChild(x3d.ROUTE().setFromField("value_changed").setFromNode("BoxPathAnimator").setToField("set_translation").setToNode("LogoGeometryTransform"))
        .addChild(x3d.Transform().setDEF(x3d.SFString("TextTransform")).setTranslation(x3d.SFVec3f([0,-1.5,0]))
          .addChild(x3d.Shape()
            .setAppearance(x3d.Appearance()
              .setMaterial(x3d.Material().setUSE(x3d.SFString("GreenMaterial"))))
            .setGeometry(x3d.Text().setString(["X3D Java","SAI Library","X3DJSAIL"])
              # Comment example A, plain quotation marks: He said, \"Immel did it!\" 

              # Comment example B, XML character entities: He said, &quot;Immel did it!&quot; 

              .setMetadata(x3d.MetadataSet().setName(x3d.SFString("EscapedQuotationMarksMetadataSet"))
                .addValue(x3d.MetadataString().setName(x3d.SFString("quotesTestC")).setValue(x3d.MFString(["MFString example C, backslash-escaped quotes: He said, \"Immel did it!\""])))
                .addValue(x3d.MetadataString().setName(x3d.SFString("extraChildTest")).setValue(x3d.MFString(["checks MetadataSetObject addValue() method"]))))
              .setFontStyle(x3d.FontStyle().setFamily(["SERIF"]).setJustify(["MIDDLE","MIDDLE"]))))
          .addChild(x3d.Collision()
            # test containerField='proxy' 

            .setProxy(x3d.Shape().setDEF(x3d.SFString("ProxyShape"))
              # alternative XML encoding: Text string='\"One, Two, Comment\" \"\" \"He said, \\&quot;Immel did it!\\&quot;\"' 

              # alternative XML encoding: Text string='\"One, Two, Comment\" \"\" \"He said, \\&quot;Immel did it!\\&quot;\" \"\"' 

              # alternative Java source: .setString(new String [] {\"One, Two, Comment\", \"\", \"He said, \\\"Immel did it!\\\"\"}) 

              # reference: http://www.web3d.org/x3d/content/examples/Basic/X3dSpecifications/StringArrayEncodingExamplesIndex.html 

              .setGeometry(x3d.Text().setString(["One, Two, Text","","He said, \"Immel did it!\" \"\""]))))
          # It's a beautiful world 

          # ... for you! 

          # https://en.wikipedia.org/wiki/Beautiful_World_(Devo_song) 

          )
        # repeatedly spin 180 degrees as a readable special effect 

        .addChild(x3d.OrientationInterpolator().setDEF(x3d.SFString("SpinInterpolator")).setKey([0,0.5,1]).setKeyValue([0,1,0,4.712389,0,1,0,0,0,1,0,1.5707964]))
        .addChild(x3d.TimeSensor().setDEF(x3d.SFString("SpinClock")).setCycleInterval(5.0).setLoop(True))
        .addChild(x3d.ROUTE().setFromField("fraction_changed").setFromNode("SpinClock").setToField("set_fraction").setToNode("SpinInterpolator"))
        .addChild(x3d.ROUTE().setFromField("value_changed").setFromNode("SpinInterpolator").setToField("rotation").setToNode("TextTransform"))
        .addChild(x3d.Group().setDEF(x3d.SFString("BackgroundGroup"))
          .addChild(x3d.Background().setDEF(x3d.SFString("GradualBackground")))
          .addChild(x3d.Script().setDEF(x3d.SFString("colorTypeConversionScript"))
            .addField(x3d.field().setName(x3d.SFString("colorInput")).setAccessType("inputOnly").setType("SFColor"))
            .addField(x3d.field().setName(x3d.SFString("colorsOutput")).setAccessType("outputOnly").setType("MFColor")).setSourceCode('''\n"+
"ecmascript:\n"+
"\n"+
"function colorInput (eventValue) // Example source code\n"+
"{\n"+
"   colorsOutput = new MFColor(eventValue); // assigning value sends output event\n"+
"// Browser.print('colorInput=' + eventValue + ', colorsOutput=' + colorsOutput + '\\n');\n"+
"}\n"+
"''')
)
          .addChild(x3d.ColorInterpolator().setDEF(x3d.SFString("ColorAnimator")).setKey([0,0.5,1]).setKeyValue([0.9411765,1,1,0.29411766,0,0.50980395,0.9411765,1,1])
            # AZURE to INDIGO and back again 

            )
          .addChild(x3d.TimeSensor().setDEF(x3d.SFString("ColorClock")).setCycleInterval(60.0).setLoop(True))
          .addChild(x3d.ROUTE().setFromField("colorsOutput").setFromNode("colorTypeConversionScript").setToField("skyColor").setToNode("GradualBackground"))
          .addChild(x3d.ROUTE().setFromField("value_changed").setFromNode("ColorAnimator").setToField("colorInput").setToNode("colorTypeConversionScript"))
          .addChild(x3d.ROUTE().setFromField("fraction_changed").setFromNode("ColorClock").setToField("set_fraction").setToNode("ColorAnimator")))
        .addChild(x3d.ProtoDeclare().setName(x3d.SFString("ArtDeco01Material")).setAppinfo("tooltip: ArtDeco01Material prototype is a Material node")
          .setProtoInterface(x3d.ProtoInterface()
            .addField(x3d.field().setName(x3d.SFString("description")).setAccessType("inputOutput").setAppinfo("tooltip for descriptionField").setType("SFString").setValue(x3d.SFString("ArtDeco01Material prototype is a Material node")))
            .addField(x3d.field().setName(x3d.SFString("enabled")).setAccessType("inputOutput").setType("SFBool").setValue(x3d.SFString("true"))))
          .setProtoBody(x3d.ProtoBody()
            # Initial node of ProtoBody determines prototype node type 

            .addChild(x3d.Material().setAmbientIntensity(0.25).setDiffuseColor([0.282435,0.085159,0.134462]).setShininess(0.127273).setSpecularColor([0.276305,0.11431,0.139857]))
            # [HelloWorldProgram diagnostic] should be connected to scene graph: artDeco01ProtoDeclare.getNodeType()=\"Material\" 

            # presence of follow-on TouchSensor shows that additional nodes are allowed in ProtoBody after initial node, regardless of node types 

            .addChild(x3d.TouchSensor().setDescription(x3d.SFString("within ProtoBody"))
              .setIS(x3d.IS()
                .addConnect(x3d.connect().setNodeField(x3d.SFString("description")).setProtoField(x3d.SFString("description")))
                .addConnect(x3d.connect().setNodeField(x3d.SFString("enabled")).setProtoField(x3d.SFString("enabled")))))))
        .addChild(x3d.ExternProtoDeclare().setName(x3d.SFString("ArtDeco02Material")).setAppinfo("this is a different Material node").setUrl(x3d.MFString(["http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/ArtDecoPrototypesExcerpt.x3d#ArtDeco02Material","http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/ArtDecoPrototypesExcerpt.x3dv#ArtDeco02Material"]))
          # [HelloWorldProgram diagnostic] artDeco02ExternProtoDeclare.getNodeType()=\"ERROR_UNKNOWN_EXTERNPROTODECLARE_NODE_TYPE: ExternProtoDeclare name='ArtDeco02Material' type cannot be remotely accessed at run time. TODO X3DJSAIL needs to add further capability that retrieves the ExternProtoDeclare file.\" 

          .addField(x3d.field().setName(x3d.SFString("description")).setAccessType("inputOutput").setAppinfo("tooltip for descriptionField").setType("SFString")))
        # Tested ArtDeco01ProtoInstance, ArtDeco02ProtoInstance for improper node type when ProtoInstance is added in wrong place 

        .addChild(x3d.Shape().setDEF(x3d.SFString("TestShape1"))
          .setAppearance(x3d.Appearance().setDEF(x3d.SFString("TestAppearance1"))
            # ArtDeco01Material prototype goes here... TODO ensure setContainerField is handled in exported Java 

            .setMaterial(x3d.ProtoInstance().setName(x3d.SFString("ArtDeco01Material"))
              # [HelloWorldProgram diagnostic] ArtDeco01ProtoInstance.getNodeType()=\"Material\" 

              .addFieldValue(x3d.fieldValue().setName(x3d.SFString("description")).setValue(x3d.SFString("ArtDeco01Material can substitute for a Material node")))))
          .setGeometry(x3d.Sphere().setRadius(0.001)))
        .addChild(x3d.Shape().setDEF(x3d.SFString("TestShape2"))
          .setAppearance(x3d.Appearance().setDEF(x3d.SFString("TestAppearance2"))
            # ArtDeco02Material prototype goes here... TODO ensure setContainerField is handled in exported Java 

            .setMaterial(x3d.ProtoInstance().setDEF(x3d.SFString("ArtDeco02MaterialDEF")).setName(x3d.SFString("ArtDeco02Material"))
              # [HelloWorldProgram diagnostic] ArtDeco02ProtoInstance.getNodeType()=\"ERROR_UNKNOWN_EXTERNPROTODECLARE_NODE_TYPE: ExternProtoDeclare name='ArtDeco02Material' type cannot be remotely accessed at run time. TODO X3DJSAIL needs to add further capability that retrieves the ExternProtoDeclare file.\" 

              .addFieldValue(x3d.fieldValue().setName(x3d.SFString("description")).setValue(x3d.SFString("ArtDeco02Material can substitute for another Material node")))))
          .setGeometry(x3d.Cone().setBottomRadius(0.001).setHeight(0.001)))
        .addChild(x3d.Shape().setDEF(x3d.SFString("TestShape3"))
          .setAppearance(x3d.Appearance().setDEF(x3d.SFString("TestAppearance3"))
            # ArtDeco02Material ProtoInstance USE goes here. Note that name field is NOT defined as part of ProtoInstance USE. 

            .setMaterial(x3d.ProtoInstance().setUSE(x3d.SFString("ArtDeco02MaterialDEF"))))
          .setGeometry(x3d.Cylinder().setHeight(0.001).setRadius(0.001)))
        .addChild(x3d.Inline().setDEF(x3d.SFString("inlineSceneDef")).setUrl(x3d.MFString(["someOtherScene.x3d","http://www.web3d.org/specifications/java/examples/someOtherScene.x3d"])))
        .addChild(x3d.IMPORT().setAS("WorldInfoDEF2").setImportedDEF("WorldInfoDEF").setInlineDEF("inlineSceneDef"))
        .addChild(x3d.EXPORT().setAS("WorldInfoDEF3").setLocalDEF("WorldInfoDEF"))
        .addChild(x3d.ProtoDeclare().setName(x3d.SFString("MaterialModulator")).setAppinfo("mimic a Material node and modulate fields as an animation effect").setDocumentation("http://x3dgraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/MaterialModulatorIndex.html")
          .setProtoInterface(x3d.ProtoInterface()
            .addField(x3d.field().setName(x3d.SFString("enabled")).setAccessType("inputOutput").setType("SFBool").setValue(x3d.SFString("true")))
            .addField(x3d.field().setName(x3d.SFString("diffuseColor")).setAccessType("inputOutput").setType("SFColor").setValue(x3d.SFString("0 0 0")))
            .addField(x3d.field().setName(x3d.SFString("emissiveColor")).setAccessType("inputOutput").setType("SFColor").setValue(x3d.SFString("0.05 0.05 0.5")))
            .addField(x3d.field().setName(x3d.SFString("specularColor")).setAccessType("inputOutput").setType("SFColor").setValue(x3d.SFString("0 0 0")))
            .addField(x3d.field().setName(x3d.SFString("transparency")).setAccessType("inputOutput").setType("SFFloat").setValue(x3d.SFString("0.0")))
            .addField(x3d.field().setName(x3d.SFString("shininess")).setAccessType("inputOutput").setType("SFFloat").setValue(x3d.SFString("0.0")))
            .addField(x3d.field().setName(x3d.SFString("ambientIntensity")).setAccessType("inputOutput").setType("SFFloat").setValue(x3d.SFString("0.0"))))
          .setProtoBody(x3d.ProtoBody()
            .addChild(x3d.Material().setDEF(x3d.SFString("MaterialNode"))
              .setIS(x3d.IS()
                .addConnect(x3d.connect().setNodeField(x3d.SFString("diffuseColor")).setProtoField(x3d.SFString("diffuseColor")))
                .addConnect(x3d.connect().setNodeField(x3d.SFString("emissiveColor")).setProtoField(x3d.SFString("emissiveColor")))
                .addConnect(x3d.connect().setNodeField(x3d.SFString("specularColor")).setProtoField(x3d.SFString("specularColor")))
                .addConnect(x3d.connect().setNodeField(x3d.SFString("transparency")).setProtoField(x3d.SFString("transparency")))
                .addConnect(x3d.connect().setNodeField(x3d.SFString("shininess")).setProtoField(x3d.SFString("shininess")))
                .addConnect(x3d.connect().setNodeField(x3d.SFString("ambientIntensity")).setProtoField(x3d.SFString("ambientIntensity")))))
            # Only first node (the node type) is renderable, others are along for the ride 

            .addChild(x3d.Script().setDEF(x3d.SFString("MaterialModulatorScript"))
              .addField(x3d.field().setName(x3d.SFString("enabled")).setAccessType("inputOutput").setType("SFBool"))
              .addField(x3d.field().setName(x3d.SFString("diffuseColor")).setAccessType("inputOutput").setType("SFColor"))
              .addField(x3d.field().setName(x3d.SFString("newColor")).setAccessType("outputOnly").setType("SFColor"))
              .addField(x3d.field().setName(x3d.SFString("clockTrigger")).setAccessType("inputOnly").setType("SFTime"))
              .setIS(x3d.IS()
                .addConnect(x3d.connect().setNodeField(x3d.SFString("enabled")).setProtoField(x3d.SFString("enabled")))
                .addConnect(x3d.connect().setNodeField(x3d.SFString("diffuseColor")).setProtoField(x3d.SFString("diffuseColor")))).setSourceCode('''\n"+
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

        .addChild(x3d.Group().setDEF(x3d.SFString("DeclarativeGroupExample"))
          .addChild(x3d.Shape()
            .setMetadata(x3d.MetadataString().setDEF(x3d.SFString("FindableMetadataStringTest")).setName(x3d.SFString("findThisNameValue")).setValue(x3d.MFString(["test case"])))
            .setAppearance(x3d.Appearance().setDEF(x3d.SFString("DeclarativeAppearanceExample"))
              # DeclarativeMaterialExample gets overridden by subsequently added MaterialModulator ProtoInstance 

              .setMaterial(x3d.ProtoInstance().setDEF(x3d.SFString("MyMaterialModulator")).setName(x3d.SFString("MaterialModulator"))))
            .setGeometry(x3d.Cone().setBottom(False).setBottomRadius(0.05).setHeight(0.1)))
          # Test success: declarativeGroup.addChild() singleton pipeline method 

          )
        # Test success: declarative statement addChild() 

        # Test success: x3dModel.findNodeByDEF(DeclarativeAppearanceExample) = <Appearance DEF='DeclarativeAppearanceExample'/> i.e. <Appearance DEF='DeclarativeAppearanceExample'> <!- - DeclarativeMaterialExample gets overridden by subsequently added MaterialModulator ProtoInstance - -> <ProtoInstance DEF='MyMaterialModulator' name='MaterialModulator' containerField='material'/> </Appearance> 

        # Test success: x3dModel.findElementByNameValue(findThisNameValue) = <MetadataString DEF='FindableMetadataStringTest' name='findThisNameValue' value='\"test case\"'/> 

        # Test success: x3dModel.findElementByNameValue(\"ArtDeco01Material\", \"ProtoDeclare\") found 

        # Test success: x3dModel.findElementByNameValue(\"MaterialModulator\", \"ProtoDeclare\") found 

        # Test success: x3dModel.findElementByNameValue(\"MaterialModulator\", \"ProtoInstance\") found 

        .addChild(x3d.Group().setDEF(x3d.SFString("TestFieldObjectsGroup"))
          # testFieldObjects() results 

          # SFBool default=true, true=true, false=false, negate()=true 

          # MFBool default=, initial=true false true, negate()=false true false 

          # SFFloat default=0.0, initial=1.0, setValue(2)=2.0, setValue(3.0f)=3.0, setValue(4.0)=4.0 

          # MFFloat default=, initial=1 2 3, append(5)=1 2 3 5, inserts(3,4)(0,0)=0 1 2 3 4 5, append(6)=0 1 2 3 4 5 6, size()=7 

          # ... get1Value[3]=3.0, remove[1]=0 2 3 4 5 6, set1Value(0,10)=10 2 3 4 5 6, multiply(2)=20 4 6 8 10 12, clear= 

          # SFVec3f default=0 0 0, initial=1 2 3, setValue=4 5 6, multiply(2)=8 10 12, normalize()=0.45584232 0.5698029 0.68376344, regex matches()=true 

          # regex test SFVec3f().matches(\"1 2 3\")=true, regex test SFVec3f().matches(\"1 2 3 4\")=false, regex test (SFRotationObject.matches(\"0 0 0 0\")=true, failure detecting illegal (zero axis) rotation value 

          )
        .addChild(x3d.Sound().setLocation([0,1.6,0])
          # set sound-ellipsoid location height at 1.6m to match typical avatar height 

          .setSource(x3d.AudioClip().setDescription(x3d.SFString("chimes")).setUrl(x3d.MFString(["chimes.wav","http://www.web3d.org/x3d/content/examples/ConformanceNist/Sounds/AudioClip/chimes.wav"]))
            # Scene example fragment from http://www.web3d.org/x3d/content/examples/ConformanceNist/Sounds/AudioClip/default.x3d 

            ))
        .addChild(x3d.Sound().setLocation([0,1.6,0])
          # set sound-ellipsoid location height at 1.6m to match typical avatar height 

          .setSource(x3d.MovieTexture().setDescription(x3d.SFString("mpgsys.mpg from ConformanceNist suite")).setUrl(x3d.MFString(["mpgsys.mpg","http://www.web3d.org/x3d/content/examples/ConformanceNist/Appearance/MovieTexture/mpgsys.mpg"]))
            # Scene example fragment from http://www.web3d.org/x3d/content/examples/ConformanceNist/Appearance/MovieTexture/mpeg1-systems.x3d 

            # Expected containerField='source', allowed containerField values=\"texture\" \"source\" \"back\" \"bottom\" \"front\" \"left\" \"right\" \"top\" \"backTexture\" \"bottomTexture\" \"frontTexture\" \"leftTexture\" \"rightTexture\" \"topTexture\" \"watchList\" 

            ))
        # Test success: AnchorObject.isNode()=true, siteAnchor.isNode()=true 

        # Test success: AnchorObject.isStatement()=false, siteAnchor.isStatement()=false 

        # Test success: ROUTEObject.isNode()=false, orbitPositionROUTE.isNode()=false 

        # Test success: ROUTEObject.isStatement()=true, orbitPositionROUTE.isStatement()=true 

        # Test success: CommentsBlock.isNode()=false, testComments.isNode()=false 

        # Test failure: CommentsBlock.isStatement()=true, testComments.isStatement()=true 

        .addChild(x3d.Shape().setDEF(x3d.SFString("ExtrusionShape"))
          # ExampleExtrusion isCrossSectionClosed()=true, crossSection='[1.0, 1.0, 1.0, -1.0, -1.0, -1.0, -1.0, 1.0, 1.0, 1.0]' 

          # ExampleExtrusion isSpineClosed()=false, spine='[0.0, 0.0, 0.0, 0.0, 1.0, 0.0]' 

          .setAppearance(x3d.Appearance().setDEF(x3d.SFString("TransparentAppearance"))
            .setMaterial(x3d.Material().setTransparency(1.0)))
          .setGeometry(x3d.Extrusion().setDEF(x3d.SFString("ExampleExtrusion"))))
        .addChild(x3d.Group()
          # Test MFNode children array as an ordered list consisting of comments, statements, ProtoInstance and nodes 

          .addChild(x3d.ProtoDeclare().setName(x3d.SFString("NewWorldInfo"))
            .setProtoInterface(x3d.ProtoInterface()
              .addField(x3d.field().setName(x3d.SFString("description")).setAccessType("initializeOnly").setType("SFString")))
            .setProtoBody(x3d.ProtoBody()
              .addChild(x3d.WorldInfo())))
          .addChild(x3d.ProtoInstance().setDEF(x3d.SFString("Proto1")).setName(x3d.SFString("NewWorldInfo"))
            .addFieldValue(x3d.fieldValue().setName(x3d.SFString("description")).setValue(x3d.SFString("testing 1 2 3"))))
          .addChild(x3d.Group().setDEF(x3d.SFString("Node2"))
            # intentionally empty 

            )
          .addChild(x3d.ProtoInstance().setDEF(x3d.SFString("Proto3")).setName(x3d.SFString("NewWorldInfo")))
          .addChild(x3d.Transform().setDEF(x3d.SFString("Node4"))
            # intentionally empty 

            )
          # Test satisfactorily creates MFNode children array as an ordered list with mixed content 

          )
        .addChild(x3d.ProtoDeclare().setName(x3d.SFString("ShaderProto"))
          .setProtoBody(x3d.ProtoBody()
            .addChild(x3d.ProgramShader())))
        .addChild(x3d.Shape()
          .setAppearance(x3d.Appearance()
            # Test MFNode shaders array as an ordered list consisting of comments, ProtoInstance and nodes 

            # Test satisfactorily creates MFNode shaders array as an ordered list with mixed content 

            .addShaders(x3d.ProgramShader().setDEF(x3d.SFString("TestShader1"))
              .addPrograms(x3d.ShaderProgram().setDEF(x3d.SFString("TestShader2"))))
            .addChild(x3d.ProtoInstance().setDEF(x3d.SFString("TestShader3")).setName(x3d.SFString("ShaderProto")))
            .addShaders(x3d.ComposedShader().setDEF(x3d.SFString("TestShader4"))
              .addParts(x3d.ShaderPart().setDEF(x3d.SFString("TestShader5"))))))
        .addChild(x3d.Transform().setDEF(x3d.SFString("SpecialtyNodes"))
          .addChild(x3d.CADLayer()
            .addChild(x3d.CADAssembly()
              .addChild(x3d.CADPart()
                .addChild(x3d.CADFace()))))
          .addChild(x3d.EspduTransform().setGeoSystem(["GD","WE"]))
          .addChild(x3d.ReceiverPdu().setGeoSystem(["GD","WE"]))
          .addChild(x3d.SignalPdu().setGeoSystem(["GD","WE"]))
          .addChild(x3d.TransmitterPdu().setGeoSystem(["GD","WE"]))
          .addChild(x3d.DISEntityManager()
            .addMapping(x3d.DISEntityTypeMapping()))
          .addChild(x3d.HAnimHumanoid().setDEF(x3d.SFString("TestHumanoidDEF")).setName(x3d.SFString("TestHumanoid")).setVersion("2.0")))))

X3D0.toFileX3D("HelloWorldProgramOutput_RoundTrip.x3d")
