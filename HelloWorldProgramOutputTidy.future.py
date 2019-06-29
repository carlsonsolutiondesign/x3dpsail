import x3dpsail


X3D0 = (x3dpsail.X3D().setProfile("Immersive").setVersion("3.3")
      # x3dVersionComparisonTest for this model: supportsX3dVersion(X3DObject.VERSION_3_0)=true 

      .setHead(x3dpsail.head()
        # comment #1 

        # comment #2 

        # comment #3 

        # comment #4 

        .addComponent(x3dpsail.component().setLevel(3).setName(x3dpsail.SFString("Navigation")))
        .addComponent(x3dpsail.component().setLevel(1).setName(x3dpsail.SFString("Layering")))
        .addComponent(x3dpsail.component().setLevel(1).setName(x3dpsail.SFString("Shaders")))
        .addComponent(x3dpsail.component().setLevel(2).setName(x3dpsail.SFString("CADGeometry")))
        .addComponent(x3dpsail.component().setLevel(2).setName(x3dpsail.SFString("DIS")))
        .addComponent(x3dpsail.component().setLevel(1).setName(x3dpsail.SFString("H-Anim")))
        .addUnit(x3dpsail.unit().setConversionFactor(1.0).setName(x3dpsail.SFString("AngleUnitConversion")).setCategory("angle"))
        .addUnit(x3dpsail.unit().setConversionFactor(1.0).setName(x3dpsail.SFString("LengthUnitConversion")).setCategory("length"))
        .addUnit(x3dpsail.unit().setConversionFactor(4.4482).setName(x3dpsail.SFString("ForceFromPoundsToNewtons")).setCategory("force"))
        .addMeta(x3dpsail.meta().setContent("HelloWorldProgramOutput.x3d").setName(x3dpsail.SFString("title")))
        .addMeta(x3dpsail.meta().setContent("continued development and testing in progress").setName(x3dpsail.SFString("info")))
        .addMeta(x3dpsail.meta().setContent("Example HelloWorldProgram creates an X3D model using the X3D Java Scene Access Interface Library (X3DJSAIL)").setName(x3dpsail.SFString("description")))
        .addMeta(x3dpsail.meta().setContent("http://www.web3d.org/specifications/java/X3DJSAIL.html").setName(x3dpsail.SFString("reference")))
        .addMeta(x3dpsail.meta().setContent("HelloWorldProgramOutput.java").setName(x3dpsail.SFString("generator")))
        .addMeta(x3dpsail.meta().setContent("6 September 2016").setName(x3dpsail.SFString("created")))
        .addMeta(x3dpsail.meta().setContent("19 June 2019").setName(x3dpsail.SFString("modified")))
        .addMeta(x3dpsail.meta().setContent("X3D Java Scene Access Interface Library (X3DJSAIL)").setName(x3dpsail.SFString("generator")))
        .addMeta(x3dpsail.meta().setContent("http://www.web3d.org/specifications/java/examples/HelloWorldProgram.java").setName(x3dpsail.SFString("generator")))
        .addMeta(x3dpsail.meta().setContent("Netbeans http://www.netbeans.org").setName(x3dpsail.SFString("generator")))
        .addMeta(x3dpsail.meta().setContent("Don Brutzman").setName(x3dpsail.SFString("creator")))
        .addMeta(x3dpsail.meta().setContent("https://sourceforge.net/p/x3d/code/HEAD/tree/www.web3d.org/x3d/stylesheets/java/examples/HelloWorldProgramOutput.x3d").setName(x3dpsail.SFString("reference")))
        .addMeta(x3dpsail.meta().setContent("Console output, ClassicVRML encoding, VRML97 encoding and pretty-print documentation:").setName(x3dpsail.SFString("reference")))
        .addMeta(x3dpsail.meta().setContent("HelloWorldProgramOutput.txt").setName(x3dpsail.SFString("reference")))
        .addMeta(x3dpsail.meta().setContent("HelloWorldProgramOutput.x3dv").setName(x3dpsail.SFString("reference")))
        .addMeta(x3dpsail.meta().setContent("HelloWorldProgramOutput.wrl").setName(x3dpsail.SFString("reference")))
        .addMeta(x3dpsail.meta().setContent("HelloWorldProgramOutput.html").setName(x3dpsail.SFString("reference")))
        .addMeta(x3dpsail.meta().setContent("https://savage.nps.edu/X3dValidator?url=http://www.web3d.org/specifications/java/examples/HelloWorldProgramOutput.x3d").setName(x3dpsail.SFString("reference")))
        .addMeta(x3dpsail.meta().setContent("http://www.web3d.org/specifications/java/examples/HelloWorldProgramOutput.x3d").setName(x3dpsail.SFString("identifier")))
        .addMeta(x3dpsail.meta().setContent("../license.html").setName(x3dpsail.SFString("license"))))
      .setScene(x3dpsail.Scene()
        .addChild(x3dpsail.ViewpointGroup().setDescription(x3dpsail.SFString("Available viewpoints"))
          .addChild(x3dpsail.Viewpoint().setDEF(x3dpsail.SFString("DefaultView")).setDescription(x3dpsail.SFString("Hello X3DJSAIL")))
          .addChild(x3dpsail.Viewpoint().setDEF(x3dpsail.SFString("TopDownView")).setPosition(x3dpsail.SFVec3f([0,100,0])).setOrientation(x3dpsail.SFRotation([1,0,0,-1.570796])).setDescription(x3dpsail.SFString("top-down view from above"))))
        .addChild(x3dpsail.NavigationInfo().setType(["EXAMINE","FLY","ANY"]))
        .addChild(x3dpsail.WorldInfo().setDEF(x3dpsail.SFString("WorldInfoDEF")).setTitle("HelloWorldProgram produced by X3D Java SAI Library (X3DJSAIL)"))
        .addChild(x3dpsail.WorldInfo().setUSE(x3dpsail.SFString("WorldInfoDEF")))
        .addChild(x3dpsail.WorldInfo().setUSE(x3dpsail.SFString("WorldInfoDEF")))
        .addMetadata(x3dpsail.MetadataString().setDEF(x3dpsail.SFString("scene.addChildMetadata")).setValue(x3dpsail.MFString(["Top-level root Metadata node beneath Scene needs to be one of '-children' in JSON encoding"])).setName(x3dpsail.SFString("test")))
        .addLayerSet(x3dpsail.LayerSet().setDEF(x3dpsail.SFString("scene.addChildLayerSetTest")))
        .addChild(x3dpsail.Transform().setDEF(x3dpsail.SFString("LogoGeometryTransform")).setTranslation(x3dpsail.SFVec3f([0,1.5,0]))
          .addChild(x3dpsail.Anchor().setDescription(x3dpsail.SFString("select for X3D Java SAI Library (X3DJSAIL) description")).setUrl(x3dpsail.MFString(["../X3DJSAIL.html","http://www.web3d.org/specifications/java/X3DJSAIL.html"]))
            .addChild(x3dpsail.Shape().setDEF(x3dpsail.SFString("BoxShape"))
              .setAppearance(x3dpsail.Appearance()
                .setMaterial(x3dpsail.Material().setDEF(x3dpsail.SFString("GreenMaterial")).setDiffuseColor([0,1,1]).setTransparency(0.1).setEmissiveColor([0.8,0,0]))
                .setTexture(x3dpsail.ImageTexture().setUrl(x3dpsail.MFString(["images/X3dJavaSceneAccessInterfaceSaiLibrary.png","http://www.web3d.org/specifications/java/examples/images/X3dJavaSceneAccessInterfaceSaiLibrary.png"]))))
              .setGeometry(x3dpsail.Box().setDEF(x3dpsail.SFString("test-NMTOKEN_regex.0123456789")).setCssClass(x3dpsail.SFString("untextured"))))))
        .addChild(x3dpsail.Shape().setDEF(x3dpsail.SFString("LineShape"))
          .setAppearance(x3dpsail.Appearance()
            .setMaterial(x3dpsail.Material().setEmissiveColor([0.6,0.19607843,0.8])))
          .setGeometry(x3dpsail.IndexedLineSet().setCoordIndex([0,1,2,3,4,0])
            # Coordinate 3-tuple point count: 6 

            .setCoord(x3dpsail.Coordinate().setPoint([0,1.5,0,2,1.5,0,2,1.5,-2,-2,1.5,-2,-2,1.5,0,0,1.5,0]))))
        .addChild(x3dpsail.PositionInterpolator().setDEF(x3dpsail.SFString("BoxPathAnimator")).setKey([0,0.125,0.375,0.625,0.875,1]).setKeyValue([0,1.5,0,2,1.5,0,2,1.5,-2,-2,1.5,-2,-2,1.5,0,0,1.5,0]))
        .addChild(x3dpsail.TimeSensor().setDEF(x3dpsail.SFString("OrbitClock")).setCycleInterval(8.0).setLoop(True))
        .addChild(x3dpsail.ROUTE().setFromField("fraction_changed").setFromNode("OrbitClock").setToField("set_fraction").setToNode("BoxPathAnimator"))
        .addChild(x3dpsail.ROUTE().setFromField("value_changed").setFromNode("BoxPathAnimator").setToField("set_translation").setToNode("LogoGeometryTransform"))
        .addChild(x3dpsail.Transform().setDEF(x3dpsail.SFString("TextTransform")).setTranslation(x3dpsail.SFVec3f([0,-1.5,0]))
          .addChild(x3dpsail.Shape()
            .setAppearance(x3dpsail.Appearance()
              .setMaterial(x3dpsail.Material().setUSE(x3dpsail.SFString("GreenMaterial"))))
            .setGeometry(x3dpsail.Text().setString(["X3D Java","SAI Library","X3DJSAIL"])
              # Comment example A, plain quotation marks: He said, \"Immel did it!\" 

              # Comment example B, XML character entities: He said, &quot;Immel did it!&quot; 

              .setMetadata(x3dpsail.MetadataSet().setName(x3dpsail.SFString("EscapedQuotationMarksMetadataSet"))
                .addValue(x3dpsail.MetadataString().setValue(x3dpsail.MFString(["MFString example C, backslash-escaped quotes: He said, \"Immel did it!\""])).setName(x3dpsail.SFString("quotesTestC")))
                .addValue(x3dpsail.MetadataString().setValue(x3dpsail.MFString(["checks MetadataSetObject addValue() method"])).setName(x3dpsail.SFString("extraChildTest"))))
              .setFontStyle(x3dpsail.FontStyle().setJustify(["MIDDLE","MIDDLE"]))))
          .addChild(x3dpsail.Collision()
            # test containerField='proxy' 

            .setProxy(x3dpsail.Shape().setDEF(x3dpsail.SFString("ProxyShape"))
              # alternative XML encoding: Text string='\"One, Two, Comment\" \"\" \"He said, \\&quot;Immel did it!\\&quot;\"' 

              # alternative XML encoding: Text string='\"One, Two, Comment\" \"\" \"He said, \\&quot;Immel did it!\\&quot;\" \"\"' 

              # alternative Java source: .setString(new String [] {\"One, Two, Comment\", \"\", \"He said, \\\"Immel did it!\\\"\"}) 

              # reference: http://www.web3d.org/x3d/content/examples/Basic/X3dSpecifications/StringArrayEncodingExamplesIndex.html 

              .setGeometry(x3dpsail.Text().setString(["One, Two, Text","","He said, \"Immel did it!\" \"\""]))))
          # It's a beautiful world 

          # ... for you! 

          # https://en.wikipedia.org/wiki/Beautiful_World_(Devo_song) 

          )
        # repeatedly spin 180 degrees as a readable special effect 

        .addChild(x3dpsail.OrientationInterpolator().setDEF(x3dpsail.SFString("SpinInterpolator")).setKey([0,0.5,1]).setKeyValue([0,1,0,4.712389,0,1,0,0,0,1,0,1.5707964]))
        .addChild(x3dpsail.TimeSensor().setDEF(x3dpsail.SFString("SpinClock")).setCycleInterval(5.0).setLoop(True))
        .addChild(x3dpsail.ROUTE().setFromField("fraction_changed").setFromNode("SpinClock").setToField("set_fraction").setToNode("SpinInterpolator"))
        .addChild(x3dpsail.ROUTE().setFromField("value_changed").setFromNode("SpinInterpolator").setToField("rotation").setToNode("TextTransform"))
        .addChild(x3dpsail.Group().setDEF(x3dpsail.SFString("BackgroundGroup"))
          .addChild(x3dpsail.Background().setDEF(x3dpsail.SFString("GradualBackground")))
          .addChild(x3dpsail.Script().setDEF(x3dpsail.SFString("colorTypeConversionScript"))
            .addField(x3dpsail.field().setAccessType("inputOnly").setName(x3dpsail.SFString("colorInput")).setType("SFColor"))
            .addField(x3dpsail.field().setAccessType("outputOnly").setName(x3dpsail.SFString("colorsOutput")).setType("MFColor")).setSourceCode('''\n"+
"ecmascript:\n"+
"\n"+
"function colorInput (eventValue) // Example source code\n"+
"{\n"+
"   colorsOutput = new MFColor(eventValue); // assigning value sends output event\n"+
"// Browser.print('colorInput=' + eventValue + ', colorsOutput=' + colorsOutput + '\\n');\n"+
"}\n"+
"''')
)
          .addChild(x3dpsail.ColorInterpolator().setDEF(x3dpsail.SFString("ColorAnimator")).setKey([0,0.5,1]).setKeyValue([0.9411765,1,1,0.29411766,0,0.50980395,0.9411765,1,1])
            # AZURE to INDIGO and back again 

            )
          .addChild(x3dpsail.TimeSensor().setDEF(x3dpsail.SFString("ColorClock")).setCycleInterval(60.0).setLoop(True))
          .addChild(x3dpsail.ROUTE().setFromField("colorsOutput").setFromNode("colorTypeConversionScript").setToField("skyColor").setToNode("GradualBackground"))
          .addChild(x3dpsail.ROUTE().setFromField("value_changed").setFromNode("ColorAnimator").setToField("colorInput").setToNode("colorTypeConversionScript"))
          .addChild(x3dpsail.ROUTE().setFromField("fraction_changed").setFromNode("ColorClock").setToField("set_fraction").setToNode("ColorAnimator")))
        .addChild(x3dpsail.ProtoDeclare().setAppinfo("tooltip: ArtDeco01Material prototype is a Material node").setName(x3dpsail.SFString("ArtDeco01Material"))
          .setProtoInterface(x3dpsail.ProtoInterface()
            .addField(x3dpsail.field().setAccessType("inputOutput").setAppinfo("tooltip for descriptionField").setName(x3dpsail.SFString("description")).setType("SFString").setValue(x3dpsail.SFString("ArtDeco01Material prototype is a Material node")))
            .addField(x3dpsail.field().setAccessType("inputOutput").setName(x3dpsail.SFString("enabled")).setType("SFBool").setValue(x3dpsail.SFString("true"))))
          .setProtoBody(x3dpsail.ProtoBody()
            # Initial node of ProtoBody determines prototype node type 

            .addChild(x3dpsail.Material().setShininess(0.127273).setAmbientIntensity(0.25).setSpecularColor([0.276305,0.11431,0.139857]).setDiffuseColor([0.282435,0.085159,0.134462]))
            # [HelloWorldProgram diagnostic] should be connected to scene graph: artDeco01ProtoDeclare.getNodeType()=\"Material\" 

            # presence of follow-on TouchSensor shows that additional nodes are allowed in ProtoBody after initial node, regardless of node types 

            .addChild(x3dpsail.TouchSensor().setDescription(x3dpsail.SFString("within ProtoBody"))
              .setIS(x3dpsail.IS()
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("description")).setProtoField(x3dpsail.SFString("description")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("enabled")).setProtoField(x3dpsail.SFString("enabled")))))))
        .addChild(x3dpsail.ExternProtoDeclare().setAppinfo("this is a different Material node").setName(x3dpsail.SFString("ArtDeco02Material")).setUrl(x3dpsail.MFString(["http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/ArtDecoPrototypesExcerpt.x3d#ArtDeco02Material","http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/ArtDecoPrototypesExcerpt.x3dv#ArtDeco02Material"]))
          # [HelloWorldProgram diagnostic] artDeco02ExternProtoDeclare.getNodeType()=\"ERROR_UNKNOWN_EXTERNPROTODECLARE_NODE_TYPE: ExternProtoDeclare name='ArtDeco02Material' type cannot be remotely accessed at run time. TODO X3DJSAIL needs to add further capability that retrieves the ExternProtoDeclare file.\" 

          .addField(x3dpsail.field().setAccessType("inputOutput").setAppinfo("tooltip for descriptionField").setName(x3dpsail.SFString("description")).setType("SFString")))
        # Tested ArtDeco01ProtoInstance, ArtDeco02ProtoInstance for improper node type when ProtoInstance is added in wrong place 

        .addChild(x3dpsail.Shape().setDEF(x3dpsail.SFString("TestShape1"))
          .setAppearance(x3dpsail.Appearance().setDEF(x3dpsail.SFString("TestAppearance1"))
            # ArtDeco01Material prototype goes here... TODO ensure setContainerField is handled in exported Java 

            .setMaterial(x3dpsail.ProtoInstance().setName(x3dpsail.SFString("ArtDeco01Material"))
              # [HelloWorldProgram diagnostic] ArtDeco01ProtoInstance.getNodeType()=\"Material\" 

              .addFieldValue(x3dpsail.fieldValue().setName(x3dpsail.SFString("description")).setValue(x3dpsail.SFString("ArtDeco01Material can substitute for a Material node")))))
          .setGeometry(x3dpsail.Sphere().setRadius(0.001)))
        .addChild(x3dpsail.Shape().setDEF(x3dpsail.SFString("TestShape2"))
          .setAppearance(x3dpsail.Appearance().setDEF(x3dpsail.SFString("TestAppearance2"))
            # ArtDeco02Material prototype goes here... TODO ensure setContainerField is handled in exported Java 

            .setMaterial(x3dpsail.ProtoInstance().setDEF(x3dpsail.SFString("ArtDeco02MaterialDEF")).setName(x3dpsail.SFString("ArtDeco02Material"))
              # [HelloWorldProgram diagnostic] ArtDeco02ProtoInstance.getNodeType()=\"ERROR_UNKNOWN_EXTERNPROTODECLARE_NODE_TYPE: ExternProtoDeclare name='ArtDeco02Material' type cannot be remotely accessed at run time. TODO X3DJSAIL needs to add further capability that retrieves the ExternProtoDeclare file.\" 

              .addFieldValue(x3dpsail.fieldValue().setName(x3dpsail.SFString("description")).setValue(x3dpsail.SFString("ArtDeco02Material can substitute for another Material node")))))
          .setGeometry(x3dpsail.Cone().setBottomRadius(0.001).setHeight(0.001)))
        .addChild(x3dpsail.Shape().setDEF(x3dpsail.SFString("TestShape3"))
          .setAppearance(x3dpsail.Appearance().setDEF(x3dpsail.SFString("TestAppearance3"))
            # ArtDeco02Material ProtoInstance USE goes here. Note that name field is NOT defined as part of ProtoInstance USE. 

            .setMaterial(x3dpsail.ProtoInstance().setUSE(x3dpsail.SFString("ArtDeco02MaterialDEF"))))
          .setGeometry(x3dpsail.Cylinder().setHeight(0.001).setRadius(0.001)))
        .addChild(x3dpsail.Inline().setDEF(x3dpsail.SFString("inlineSceneDef")).setUrl(x3dpsail.MFString(["someOtherScene.x3d","http://www.web3d.org/specifications/java/examples/someOtherScene.x3d"])))
        .addChild(x3dpsail.IMPORT().setImportedDEF("WorldInfoDEF").setInlineDEF("inlineSceneDef").setAS("WorldInfoDEF2"))
        .addChild(x3dpsail.EXPORT().setLocalDEF("WorldInfoDEF").setAS("WorldInfoDEF3"))
        .addChild(x3dpsail.ProtoDeclare().setAppinfo("mimic a Material node and modulate fields as an animation effect").setName(x3dpsail.SFString("MaterialModulator")).setDocumentation("http://x3dgraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/MaterialModulatorIndex.html")
          .setProtoInterface(x3dpsail.ProtoInterface()
            .addField(x3dpsail.field().setAccessType("inputOutput").setName(x3dpsail.SFString("enabled")).setType("SFBool").setValue(x3dpsail.SFString("true")))
            .addField(x3dpsail.field().setAccessType("inputOutput").setName(x3dpsail.SFString("diffuseColor")).setType("SFColor").setValue(x3dpsail.SFString("0 0 0")))
            .addField(x3dpsail.field().setAccessType("inputOutput").setName(x3dpsail.SFString("emissiveColor")).setType("SFColor").setValue(x3dpsail.SFString("0.05 0.05 0.5")))
            .addField(x3dpsail.field().setAccessType("inputOutput").setName(x3dpsail.SFString("specularColor")).setType("SFColor").setValue(x3dpsail.SFString("0 0 0")))
            .addField(x3dpsail.field().setAccessType("inputOutput").setName(x3dpsail.SFString("transparency")).setType("SFFloat").setValue(x3dpsail.SFString("0.0")))
            .addField(x3dpsail.field().setAccessType("inputOutput").setName(x3dpsail.SFString("shininess")).setType("SFFloat").setValue(x3dpsail.SFString("0.0")))
            .addField(x3dpsail.field().setAccessType("inputOutput").setName(x3dpsail.SFString("ambientIntensity")).setType("SFFloat").setValue(x3dpsail.SFString("0.0"))))
          .setProtoBody(x3dpsail.ProtoBody()
            .addChild(x3dpsail.Material().setDEF(x3dpsail.SFString("MaterialNode"))
              .setIS(x3dpsail.IS()
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("diffuseColor")).setProtoField(x3dpsail.SFString("diffuseColor")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("emissiveColor")).setProtoField(x3dpsail.SFString("emissiveColor")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("specularColor")).setProtoField(x3dpsail.SFString("specularColor")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("transparency")).setProtoField(x3dpsail.SFString("transparency")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("shininess")).setProtoField(x3dpsail.SFString("shininess")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("ambientIntensity")).setProtoField(x3dpsail.SFString("ambientIntensity")))))
            # Only first node (the node type) is renderable, others are along for the ride 

            .addChild(x3dpsail.Script().setDEF(x3dpsail.SFString("MaterialModulatorScript"))
              .addField(x3dpsail.field().setAccessType("inputOutput").setName(x3dpsail.SFString("enabled")).setType("SFBool"))
              .addField(x3dpsail.field().setAccessType("inputOutput").setName(x3dpsail.SFString("diffuseColor")).setType("SFColor"))
              .addField(x3dpsail.field().setAccessType("outputOnly").setName(x3dpsail.SFString("newColor")).setType("SFColor"))
              .addField(x3dpsail.field().setAccessType("inputOnly").setName(x3dpsail.SFString("clockTrigger")).setType("SFTime"))
              .setIS(x3dpsail.IS()
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("enabled")).setProtoField(x3dpsail.SFString("enabled")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("diffuseColor")).setProtoField(x3dpsail.SFString("diffuseColor")))).setSourceCode('''\n"+
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

        .addChild(x3dpsail.Group().setDEF(x3dpsail.SFString("DeclarativeGroupExample"))
          .addChild(x3dpsail.Shape()
            .setMetadata(x3dpsail.MetadataString().setDEF(x3dpsail.SFString("FindableMetadataStringTest")).setValue(x3dpsail.MFString(["test case"])).setName(x3dpsail.SFString("findThisNameValue")))
            .setAppearance(x3dpsail.Appearance().setDEF(x3dpsail.SFString("DeclarativeAppearanceExample"))
              # DeclarativeMaterialExample gets overridden by subsequently added MaterialModulator ProtoInstance 

              .setMaterial(x3dpsail.ProtoInstance().setDEF(x3dpsail.SFString("MyMaterialModulator")).setName(x3dpsail.SFString("MaterialModulator"))))
            .setGeometry(x3dpsail.Cone().setBottomRadius(0.05).setHeight(0.1).setBottom(False)))
          # Test success: declarativeGroup.addChild() singleton pipeline method 

          )
        # Test success: declarative statement addChild() 

        # Test success: x3dModel.findNodeByDEF(DeclarativeAppearanceExample) = <Appearance DEF='DeclarativeAppearanceExample'/> i.e. <Appearance DEF='DeclarativeAppearanceExample'> <!- - DeclarativeMaterialExample gets overridden by subsequently added MaterialModulator ProtoInstance - -> <ProtoInstance DEF='MyMaterialModulator' name='MaterialModulator' containerField='material'/> </Appearance> 

        # Test success: x3dModel.findElementByNameValue(findThisNameValue) = <MetadataString DEF='FindableMetadataStringTest' name='findThisNameValue' value='\"test case\"'/> 

        # Test success: x3dModel.findElementByNameValue(\"ArtDeco01Material\", \"ProtoDeclare\") found 

        # Test success: x3dModel.findElementByNameValue(\"MaterialModulator\", \"ProtoDeclare\") found 

        # Test success: x3dModel.findElementByNameValue(\"MaterialModulator\", \"ProtoInstance\") found 

        .addChild(x3dpsail.Group().setDEF(x3dpsail.SFString("TestFieldObjectsGroup"))
          # testFieldObjects() results 

          # SFBool default=true, true=true, false=false, negate()=true 

          # MFBool default=, initial=true false true, negate()=false true false 

          # SFFloat default=0.0, initial=1.0, setValue(2)=2.0, setValue(3.0f)=3.0, setValue(4.0)=4.0 

          # MFFloat default=, initial=1 2 3, append(5)=1 2 3 5, inserts(3,4)(0,0)=0 1 2 3 4 5, append(6)=0 1 2 3 4 5 6, size()=7 

          # ... get1Value[3]=3.0, remove[1]=0 2 3 4 5 6, set1Value(0,10)=10 2 3 4 5 6, multiply(2)=20 4 6 8 10 12, clear= 

          # SFVec3f default=0 0 0, initial=1 2 3, setValue=4 5 6, multiply(2)=8 10 12, normalize()=0.45584232 0.5698029 0.68376344, regex matches()=true 

          # regex test SFVec3f().matches(\"1 2 3\")=true, regex test SFVec3f().matches(\"1 2 3 4\")=false, regex test (SFRotationObject.matches(\"0 0 0 0\")=true, failure detecting illegal (zero axis) rotation value 

          )
        .addChild(x3dpsail.Sound().setLocation([0,1.6,0])
          # set sound-ellipsoid location height at 1.6m to match typical avatar height 

          .setSource(x3dpsail.AudioClip().setDescription(x3dpsail.SFString("chimes")).setUrl(x3dpsail.MFString(["chimes.wav","http://www.web3d.org/x3d/content/examples/ConformanceNist/Sounds/AudioClip/chimes.wav"]))
            # Scene example fragment from http://www.web3d.org/x3d/content/examples/ConformanceNist/Sounds/AudioClip/default.x3d 

            ))
        .addChild(x3dpsail.Sound().setLocation([0,1.6,0])
          # set sound-ellipsoid location height at 1.6m to match typical avatar height 

          .setSource(x3dpsail.MovieTexture().setDescription(x3dpsail.SFString("mpgsys.mpg from ConformanceNist suite")).setUrl(x3dpsail.MFString(["mpgsys.mpg","http://www.web3d.org/x3d/content/examples/ConformanceNist/Appearance/MovieTexture/mpgsys.mpg"]))
            # Scene example fragment from http://www.web3d.org/x3d/content/examples/ConformanceNist/Appearance/MovieTexture/mpeg1-systems.x3d 

            # Expected containerField='source', allowed containerField values=\"texture\" \"source\" \"back\" \"bottom\" \"front\" \"left\" \"right\" \"top\" \"backTexture\" \"bottomTexture\" \"frontTexture\" \"leftTexture\" \"rightTexture\" \"topTexture\" \"watchList\" 

            ))
        # Test success: AnchorObject.isNode()=true, siteAnchor.isNode()=true 

        # Test success: AnchorObject.isStatement()=false, siteAnchor.isStatement()=false 

        # Test success: ROUTEObject.isNode()=false, orbitPositionROUTE.isNode()=false 

        # Test success: ROUTEObject.isStatement()=true, orbitPositionROUTE.isStatement()=true 

        # Test success: CommentsBlock.isNode()=false, testComments.isNode()=false 

        # Test failure: CommentsBlock.isStatement()=true, testComments.isStatement()=true 

        .addChild(x3dpsail.Shape().setDEF(x3dpsail.SFString("ExtrusionShape"))
          # ExampleExtrusion isCrossSectionClosed()=true, crossSection='[1.0, 1.0, 1.0, -1.0, -1.0, -1.0, -1.0, 1.0, 1.0, 1.0]' 

          # ExampleExtrusion isSpineClosed()=false, spine='[0.0, 0.0, 0.0, 0.0, 1.0, 0.0]' 

          .setAppearance(x3dpsail.Appearance().setDEF(x3dpsail.SFString("TransparentAppearance"))
            .setMaterial(x3dpsail.Material().setTransparency(1.0)))
          .setGeometry(x3dpsail.Extrusion().setDEF(x3dpsail.SFString("ExampleExtrusion"))))
        .addChild(x3dpsail.Group()
          # Test MFNode children array as an ordered list consisting of comments, statements, ProtoInstance and nodes 

          .addChild(x3dpsail.ProtoDeclare().setName(x3dpsail.SFString("NewWorldInfo"))
            .setProtoInterface(x3dpsail.ProtoInterface()
              .addField(x3dpsail.field().setAccessType("initializeOnly").setName(x3dpsail.SFString("description")).setType("SFString")))
            .setProtoBody(x3dpsail.ProtoBody()
              .addChild(x3dpsail.WorldInfo())))
          .addChild(x3dpsail.ProtoInstance().setDEF(x3dpsail.SFString("Proto1")).setName(x3dpsail.SFString("NewWorldInfo"))
            .addFieldValue(x3dpsail.fieldValue().setName(x3dpsail.SFString("description")).setValue(x3dpsail.SFString("testing 1 2 3"))))
          .addChild(x3dpsail.Group().setDEF(x3dpsail.SFString("Node2"))
            # intentionally empty 

            )
          .addChild(x3dpsail.ProtoInstance().setDEF(x3dpsail.SFString("Proto3")).setName(x3dpsail.SFString("NewWorldInfo")))
          .addChild(x3dpsail.Transform().setDEF(x3dpsail.SFString("Node4"))
            # intentionally empty 

            )
          # Test satisfactorily creates MFNode children array as an ordered list with mixed content 

          )
        .addChild(x3dpsail.ProtoDeclare().setName(x3dpsail.SFString("ShaderProto"))
          .setProtoBody(x3dpsail.ProtoBody()
            .addShaders(x3dpsail.ProgramShader())))
        .addChild(x3dpsail.Shape()
          .setAppearance(x3dpsail.Appearance()
            # Test MFNode shaders array as an ordered list consisting of comments, ProtoInstance and nodes 

            # Test satisfactorily creates MFNode shaders array as an ordered list with mixed content 

            .addShaders(x3dpsail.ProgramShader().setDEF(x3dpsail.SFString("TestShader1"))
              .setPrograms(x3dpsail.ShaderProgram().setDEF(x3dpsail.SFString("TestShader2"))))
            .addShaders(x3dpsail.ProtoInstance().setDEF(x3dpsail.SFString("TestShader3")).setName(x3dpsail.SFString("ShaderProto")))
            .addShaders(x3dpsail.ComposedShader().setDEF(x3dpsail.SFString("TestShader4"))
              .setParts(x3dpsail.ShaderPart().setDEF(x3dpsail.SFString("TestShader5"))))))
        .addChild(x3dpsail.Transform().setDEF(x3dpsail.SFString("SpecialtyNodes"))
          .addChild(x3dpsail.CADLayer()
            .addChild(x3dpsail.CADAssembly()
              .addChild(x3dpsail.CADPart()
                .addChild(x3dpsail.CADFace()))))
          .addChild(x3dpsail.EspduTransform())
          .addChild(x3dpsail.ReceiverPdu().setReceivedPower(0.0))
          .addChild(x3dpsail.SignalPdu())
          .addChild(x3dpsail.TransmitterPdu().setRelativeAntennaLocation([0,0,0]).setTransmitFrequencyBandwidth(0.0))
          .addChild(x3dpsail.DISEntityManager()
            .addMapping(x3dpsail.DISEntityTypeMapping()))
          .addChild(x3dpsail.HAnimHumanoid().setDEF(x3dpsail.SFString("TestHumanoidDEF")).setVersion("2.0").setName(x3dpsail.SFString("TestHumanoid"))))))

X3D0.toFileX3D("HelloWorldProgramOutputTidy_RoundTrip.x3d")
