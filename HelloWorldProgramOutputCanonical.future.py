import x3dpsail


X3D0 = (x3dpsail.X3D().setProfile(x3dpsail.SFString("Immersive")).setVersion(x3dpsail.SFString("3.3"))
      # x3dVersionComparisonTest for this model: supportsX3dVersion(X3DObject.VERSION_3_0)=true 

      .setHead(x3dpsail.head()
        # comment #1 

        # comment #2 

        # comment #3 

        # comment #4 

        .addComponent(x3dpsail.component().setLevel(x3dpsail.SFInt32(3)).setName(x3dpsail.SFString("Navigation")))
        .addComponent(x3dpsail.component().setLevel(x3dpsail.SFInt32(1)).setName(x3dpsail.SFString("Shaders")))
        .addComponent(x3dpsail.component().setLevel(x3dpsail.SFInt32(1)).setName(x3dpsail.SFString("Layering")))
        .addUnit(x3dpsail.unit().setCategory(x3dpsail.SFString("angle")).setConversionFactor(x3dpsail.SFDouble(1.0)).setName(x3dpsail.SFString("AngleUnitConversion")))
        .addUnit(x3dpsail.unit().setCategory(x3dpsail.SFString("length")).setConversionFactor(x3dpsail.SFDouble(1.0)).setName(x3dpsail.SFString("LengthUnitConversion")))
        .addMeta(x3dpsail.meta().setContent(x3dpsail.SFString("HelloWorldProgramOutput.x3d")).setName(x3dpsail.SFString("title")))
        .addMeta(x3dpsail.meta().setContent(x3dpsail.SFString("Example HelloWorldProgram creates an X3D model using the X3D Java Scene Access Interface Library (X3DJSAIL)")).setName(x3dpsail.SFString("description")))
        .addMeta(x3dpsail.meta().setContent(x3dpsail.SFString("http://www.web3d.org/specifications/java/X3DJSAIL.html")).setName(x3dpsail.SFString("reference")))
        .addMeta(x3dpsail.meta().setContent(x3dpsail.SFString("HelloWorldProgramOutput.java")).setName(x3dpsail.SFString("generator")))
        .addMeta(x3dpsail.meta().setContent(x3dpsail.SFString("6 September 2016")).setName(x3dpsail.SFString("created")))
        .addMeta(x3dpsail.meta().setContent(x3dpsail.SFString("27 December 2018")).setName(x3dpsail.SFString("modified")))
        .addMeta(x3dpsail.meta().setContent(x3dpsail.SFString("X3D Java Scene Access Interface Library (X3DJSAIL)")).setName(x3dpsail.SFString("generator")))
        .addMeta(x3dpsail.meta().setContent(x3dpsail.SFString("http://www.web3d.org/specifications/java/examples/HelloWorldProgram.java")).setName(x3dpsail.SFString("generator")))
        .addMeta(x3dpsail.meta().setContent(x3dpsail.SFString("Netbeans http://www.netbeans.org")).setName(x3dpsail.SFString("generator")))
        .addMeta(x3dpsail.meta().setContent(x3dpsail.SFString("Don Brutzman")).setName(x3dpsail.SFString("creator")))
        .addMeta(x3dpsail.meta().setContent(x3dpsail.SFString("https://sourceforge.net/p/x3d/code/HEAD/tree/www.web3d.org/x3d/stylesheets/java/examples/HelloWorldProgramOutput.x3d")).setName(x3dpsail.SFString("reference")))
        .addMeta(x3dpsail.meta().setContent(x3dpsail.SFString("Console output, ClassicVRML encoding, VRML97 encoding and pretty-print documentation:")).setName(x3dpsail.SFString("reference")))
        .addMeta(x3dpsail.meta().setContent(x3dpsail.SFString("HelloWorldProgramOutput.txt")).setName(x3dpsail.SFString("reference")))
        .addMeta(x3dpsail.meta().setContent(x3dpsail.SFString("HelloWorldProgramOutput.x3dv")).setName(x3dpsail.SFString("reference")))
        .addMeta(x3dpsail.meta().setContent(x3dpsail.SFString("HelloWorldProgramOutput.wrl")).setName(x3dpsail.SFString("reference")))
        .addMeta(x3dpsail.meta().setContent(x3dpsail.SFString("HelloWorldProgramOutput.html")).setName(x3dpsail.SFString("reference")))
        .addMeta(x3dpsail.meta().setContent(x3dpsail.SFString("https://savage.nps.edu/X3dValidator?url=http://www.web3d.org/specifications/java/examples/HelloWorldProgramOutput.x3d")).setName(x3dpsail.SFString("reference")))
        .addMeta(x3dpsail.meta().setContent(x3dpsail.SFString("http://www.web3d.org/specifications/java/examples/HelloWorldProgramOutput.x3d")).setName(x3dpsail.SFString("identifier")))
        .addMeta(x3dpsail.meta().setContent(x3dpsail.SFString("../license.html")).setName(x3dpsail.SFString("license"))))
      .setScene(x3dpsail.Scene()
        .addChild(x3dpsail.ViewpointGroup().setDescription(x3dpsail.SFString("Available viewpoints"))
          .addChild(x3dpsail.Viewpoint().setDEF(x3dpsail.SFString("DefaultView")).setDescription(x3dpsail.SFString("Hello X3DJSAIL")))
          .addChild(x3dpsail.Viewpoint().setDEF(x3dpsail.SFString("TopDownView")).setDescription(x3dpsail.SFString("top-down view from above")).setOrientation(x3dpsail.SFRotation(1,0,0,-1.570796)).setPosition(x3dpsail.SFVec3f(0,100,0))))
        .addChild(x3dpsail.NavigationInfo().setAvatarSize(x3dpsail.MFFloat([0.25,1.6,0.75])).setTransitionType(x3dpsail.MFString(["LINEAR"])).setType(x3dpsail.MFString(["EXAMINE","FLY","ANY"])))
        .addChild(x3dpsail.WorldInfo().setDEF(x3dpsail.SFString("WorldInfoDEF")).setTitle(x3dpsail.SFString("HelloWorldProgram produced by X3D Java SAI Library (X3DJSAIL)")))
        .addChild(x3dpsail.WorldInfo().setUSE(x3dpsail.SFString("WorldInfoDEF")))
        .addChild(x3dpsail.WorldInfo().setUSE(x3dpsail.SFString("WorldInfoDEF")))
        .addMetadata(x3dpsail.MetadataString().setDEF(x3dpsail.SFString("scene.addChildMetadata")).setName(x3dpsail.SFString("test")).setValue(x3dpsail.MFString(["Top-level root Metadata node beneath Scene needs to be one of '-children' in JSON encoding"])))
        .addLayerSet(x3dpsail.LayerSet().setDEF(x3dpsail.SFString("scene.addChildLayerSetTest")).setOrder(x3dpsail.MFInt32([0])))
        .addChild(x3dpsail.Transform().setDEF(x3dpsail.SFString("LogoGeometryTransform")).setTranslation(x3dpsail.SFVec3f(0,1.5,0))
          .addChild(x3dpsail.Anchor().setDescription(x3dpsail.SFString("select for X3D Java SAI Library (X3DJSAIL) description")).setUrl(x3dpsail.MFString(["../X3DJSAIL.html","http://www.web3d.org/specifications/java/X3DJSAIL.html"]))
            .addChild(x3dpsail.Shape().setDEF(x3dpsail.SFString("BoxShape"))
              .setAppearance(x3dpsail.Appearance()
                .setMaterial(x3dpsail.Material().setDEF(x3dpsail.SFString("GreenMaterial")).setDiffuseColor(x3dpsail.SFColor(0,1,1)).setEmissiveColor(x3dpsail.SFColor(0.8,0,0)).setTransparency(x3dpsail.SFFloat(0.1)))
                .setTexture(x3dpsail.ImageTexture().setUrl(x3dpsail.MFString(["images/X3dJavaSceneAccessInterfaceSaiLibrary.png","http://www.web3d.org/specifications/java/examples/images/X3dJavaSceneAccessInterfaceSaiLibrary.png"]))))
              .setGeometry(x3dpsail.Box().setDEF(x3dpsail.SFString("test-NMTOKEN_regex.0123456789")).setCssClass(x3dpsail.SFString("untextured"))))))
        .addChild(x3dpsail.Shape().setDEF(x3dpsail.SFString("LineShape"))
          .setAppearance(x3dpsail.Appearance()
            .setMaterial(x3dpsail.Material().setEmissiveColor(x3dpsail.SFColor(0.6,0.19607843,0.8))))
          .setGeometry(x3dpsail.IndexedLineSet().setCoordIndex(x3dpsail.MFInt32([0,1,2,3,4,0]))
            # Coordinate 3-tuple point count: 6 

            .setCoord(x3dpsail.Coordinate().setPoint(x3dpsail.MFVec3f([0,1.5,0,2,1.5,0,2,1.5,-2,-2,1.5,-2,-2,1.5,0,0,1.5,0])))))
        .addChild(x3dpsail.PositionInterpolator().setDEF(x3dpsail.SFString("BoxPathAnimator")).setKey(x3dpsail.MFFloat([0,0.125,0.375,0.625,0.875,1])).setKeyValue(x3dpsail.MFVec3f([0,1.5,0,2,1.5,0,2,1.5,-2,-2,1.5,-2,-2,1.5,0,0,1.5,0])))
        .addChild(x3dpsail.TimeSensor().setDEF(x3dpsail.SFString("OrbitClock")).setCycleInterval(x3dpsail.SFTime(8.0)).setLoop(x3dpsail.SFBool(True)))
        .addChild(x3dpsail.ROUTE().setFromField(x3dpsail.SFString("fraction_changed")).setFromNode(x3dpsail.SFString("OrbitClock")).setToField(x3dpsail.SFString("set_fraction")).setToNode(x3dpsail.SFString("BoxPathAnimator")))
        .addChild(x3dpsail.ROUTE().setFromField(x3dpsail.SFString("value_changed")).setFromNode(x3dpsail.SFString("BoxPathAnimator")).setToField(x3dpsail.SFString("set_translation")).setToNode(x3dpsail.SFString("LogoGeometryTransform")))
        .addChild(x3dpsail.Transform().setDEF(x3dpsail.SFString("TextTransform")).setTranslation(x3dpsail.SFVec3f(0,-1.5,0))
          .addChild(x3dpsail.Shape()
            .setAppearance(x3dpsail.Appearance()
              .setMaterial(x3dpsail.Material().setUSE(x3dpsail.SFString("GreenMaterial"))))
            .setGeometry(x3dpsail.Text().setString(x3dpsail.MFString(["X3D Java","SAI Library","X3DJSAIL"]))
              # Comment example A, plain quotation marks: He said, \"Immel did it!\" 

              # Comment example B, XML character entities: He said, &quot;Immel did it!&quot; 

              .setMetadata(x3dpsail.MetadataSet().setName(x3dpsail.SFString("EscapedQuotationMarksMetadataSet"))
                .addValue(x3dpsail.MetadataString().setName(x3dpsail.SFString("quotesTestC")).setValue(x3dpsail.MFString(["MFString example C, backslash-escaped quotes: He said, \"Immel did it!\""])))
                .addValue(x3dpsail.MetadataString().setName(x3dpsail.SFString("extraChildTest")).setValue(x3dpsail.MFString(["checks MetadataSetObject addValue() method"]))))
              .setFontStyle(x3dpsail.FontStyle().setFamily(x3dpsail.MFString(["SERIF"])).setJustify(x3dpsail.MFString(["MIDDLE","MIDDLE"])))))
          .addChild(x3dpsail.Collision()
            # test containerField='proxy' 

            .setProxy(x3dpsail.Shape().setDEF(x3dpsail.SFString("ProxyShape"))
              # alternative XML encoding: Text string='\"One, Two, Comment\" \"\" \"He said, \\&quot;Immel did it!\\&quot;\"' 

              # alternative XML encoding: Text string='\"One, Two, Comment\" \"\" \"He said, \\&quot;Immel did it!\\&quot;\" \"\"' 

              # alternative Java source: .setString(new String [] {\"One, Two, Comment\", \"\", \"He said, \\\"Immel did it!\\\"\"}) 

              # reference: http://www.web3d.org/x3d/content/examples/Basic/X3dSpecifications/StringArrayEncodingExamplesIndex.html 

              .setGeometry(x3dpsail.Text().setString(x3dpsail.MFString(["One, Two, Text","","He said, \"Immel did it!\" \"\""])))))
          # It's a beautiful world 

          # ... for you! 

          # https://en.wikipedia.org/wiki/Beautiful_World_(Devo_song) 

          )
        # repeatedly spin 180 degrees as a readable special effect 

        .addChild(x3dpsail.OrientationInterpolator().setDEF(x3dpsail.SFString("SpinInterpolator")).setKey(x3dpsail.MFFloat([0,0.5,1])).setKeyValue(x3dpsail.MFRotation([0,1,0,4.712389,0,1,0,0,0,1,0,1.5707964])))
        .addChild(x3dpsail.TimeSensor().setDEF(x3dpsail.SFString("SpinClock")).setCycleInterval(x3dpsail.SFTime(5.0)).setLoop(x3dpsail.SFBool(True)))
        .addChild(x3dpsail.ROUTE().setFromField(x3dpsail.SFString("fraction_changed")).setFromNode(x3dpsail.SFString("SpinClock")).setToField(x3dpsail.SFString("set_fraction")).setToNode(x3dpsail.SFString("SpinInterpolator")))
        .addChild(x3dpsail.ROUTE().setFromField(x3dpsail.SFString("value_changed")).setFromNode(x3dpsail.SFString("SpinInterpolator")).setToField(x3dpsail.SFString("rotation")).setToNode(x3dpsail.SFString("TextTransform")))
        .addChild(x3dpsail.Group().setDEF(x3dpsail.SFString("BackgroundGroup"))
          .addChild(x3dpsail.Background().setDEF(x3dpsail.SFString("GradualBackground")))
          .addChild(x3dpsail.Script().setDEF(x3dpsail.SFString("colorTypeConversionScript"))
            .addField(x3dpsail.field().setAccessType(x3dpsail.SFString("inputOnly")).setName(x3dpsail.SFString("colorInput")).setType(x3dpsail.SFString("SFColor")))
            .addField(x3dpsail.field().setAccessType(x3dpsail.SFString("outputOnly")).setName(x3dpsail.SFString("colorsOutput")).setType(x3dpsail.SFString("MFColor"))).setSourceCode('''\n"+
"ecmascript:\n"+
"\n"+
"function colorInput (eventValue) // Example source code\n"+
"{\n"+
"   colorsOutput = new MFColor(eventValue); // assigning value sends output event\n"+
"// Browser.print('colorInput=' + eventValue + ', colorsOutput=' + colorsOutput + '\\n');\n"+
"}\n"+
"''')
)
          .addChild(x3dpsail.ColorInterpolator().setDEF(x3dpsail.SFString("ColorAnimator")).setKey(x3dpsail.MFFloat([0,0.5,1])).setKeyValue(x3dpsail.MFColor([0.9411765,1,1,0.29411766,0,0.50980395,0.9411765,1,1]))
            # AZURE to INDIGO and back again 

            )
          .addChild(x3dpsail.TimeSensor().setDEF(x3dpsail.SFString("ColorClock")).setCycleInterval(x3dpsail.SFTime(60.0)).setLoop(x3dpsail.SFBool(True)))
          .addChild(x3dpsail.ROUTE().setFromField(x3dpsail.SFString("colorsOutput")).setFromNode(x3dpsail.SFString("colorTypeConversionScript")).setToField(x3dpsail.SFString("skyColor")).setToNode(x3dpsail.SFString("GradualBackground")))
          .addChild(x3dpsail.ROUTE().setFromField(x3dpsail.SFString("value_changed")).setFromNode(x3dpsail.SFString("ColorAnimator")).setToField(x3dpsail.SFString("colorInput")).setToNode(x3dpsail.SFString("colorTypeConversionScript")))
          .addChild(x3dpsail.ROUTE().setFromField(x3dpsail.SFString("fraction_changed")).setFromNode(x3dpsail.SFString("ColorClock")).setToField(x3dpsail.SFString("set_fraction")).setToNode(x3dpsail.SFString("ColorAnimator"))))
        .addChild(x3dpsail.ProtoDeclare().setAppinfo(x3dpsail.SFString("tooltip: ArtDeco01Material prototype is a Material node")).setName(x3dpsail.SFString("ArtDeco01Material"))
          .setProtoInterface(x3dpsail.ProtoInterface()
            .addField(x3dpsail.field().setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("tooltip for descriptionField")).setName(x3dpsail.SFString("description")).setType(x3dpsail.SFString("SFString")).setValue(x3dpsail.SFString("ArtDeco01Material prototype is a Material node")))
            .addField(x3dpsail.field().setAccessType(x3dpsail.SFString("inputOutput")).setName(x3dpsail.SFString("enabled")).setType(x3dpsail.SFString("SFBool")).setValue(x3dpsail.SFString("true"))))
          .setProtoBody(x3dpsail.ProtoBody()
            # Initial node of ProtoBody determines prototype node type 

            .addChild(x3dpsail.Material().setAmbientIntensity(x3dpsail.SFFloat(0.25)).setDiffuseColor(x3dpsail.SFColor(0.282435,0.085159,0.134462)).setShininess(x3dpsail.SFFloat(0.127273)).setSpecularColor(x3dpsail.SFColor(0.276305,0.11431,0.139857)))
            # [HelloWorldProgram diagnostic] should be connected to scene graph: artDeco01ProtoDeclare.getNodeType()=\"Material\" 

            # presence of follow-on TouchSensor shows that additional nodes are allowed in ProtoBody after initial node, regardless of node types 

            .addChild(x3dpsail.TouchSensor().setDescription(x3dpsail.SFString("within ProtoBody"))
              .setIS(x3dpsail.IS()
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("description")).setProtoField(x3dpsail.SFString("description")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("enabled")).setProtoField(x3dpsail.SFString("enabled")))))))
        .addChild(x3dpsail.ExternProtoDeclare().setAppinfo(x3dpsail.SFString("this is a different Material node")).setName(x3dpsail.SFString("ArtDeco02Material")).setUrl(x3dpsail.MFString(["http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/ArtDecoPrototypesExcerpt.x3d#ArtDeco02Material","http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/ArtDecoPrototypesExcerpt.x3dv#ArtDeco02Material"]))
          # [HelloWorldProgram diagnostic] artDeco02ExternProtoDeclare.getNodeType()=\"ERROR_UNKNOWN_EXTERNPROTODECLARE_NODE_TYPE: ExternProtoDeclare name='ArtDeco02Material' type cannot be remotely accessed at run time. TODO X3DJSAIL needs to add further capability that retrieves the ExternProtoDeclare file.\" 

          .addField(x3dpsail.field().setAccessType(x3dpsail.SFString("inputOutput")).setAppinfo(x3dpsail.SFString("tooltip for descriptionField")).setName(x3dpsail.SFString("description")).setType(x3dpsail.SFString("SFString"))))
        # Tested ArtDeco01ProtoInstance, ArtDeco02ProtoInstance for improper node type when ProtoInstance is added in wrong place 

        .addChild(x3dpsail.Shape().setDEF(x3dpsail.SFString("TestShape1"))
          .setAppearance(x3dpsail.Appearance().setDEF(x3dpsail.SFString("TestAppearance1"))
            # ArtDeco01Material prototype goes here... TODO ensure setContainerField is handled in exported Java 

            .setMaterial(x3dpsail.ProtoInstance().setName(x3dpsail.SFString("ArtDeco01Material"))
              # [HelloWorldProgram diagnostic] ArtDeco01ProtoInstance.getNodeType()=\"Material\" 

              .addFieldValue(x3dpsail.fieldValue().setName(x3dpsail.SFString("description")).setValue(x3dpsail.SFString("ArtDeco01Material can substitute for a Material node")))))
          .setGeometry(x3dpsail.Sphere().setRadius(x3dpsail.SFFloat(0.001))))
        .addChild(x3dpsail.Shape().setDEF(x3dpsail.SFString("TestShape2"))
          .setAppearance(x3dpsail.Appearance().setDEF(x3dpsail.SFString("TestAppearance2"))
            # ArtDeco02Material prototype goes here... TODO ensure setContainerField is handled in exported Java 

            .setMaterial(x3dpsail.ProtoInstance().setDEF(x3dpsail.SFString("ArtDeco02MaterialDEF")).setName(x3dpsail.SFString("ArtDeco02Material"))
              # [HelloWorldProgram diagnostic] ArtDeco02ProtoInstance.getNodeType()=\"ERROR_UNKNOWN_EXTERNPROTODECLARE_NODE_TYPE: ExternProtoDeclare name='ArtDeco02Material' type cannot be remotely accessed at run time. TODO X3DJSAIL needs to add further capability that retrieves the ExternProtoDeclare file.\" 

              .addFieldValue(x3dpsail.fieldValue().setName(x3dpsail.SFString("description")).setValue(x3dpsail.SFString("ArtDeco02Material can substitute for another Material node")))))
          .setGeometry(x3dpsail.Cone().setBottomRadius(x3dpsail.SFFloat(0.001)).setHeight(x3dpsail.SFFloat(0.001))))
        .addChild(x3dpsail.Shape().setDEF(x3dpsail.SFString("TestShape3"))
          .setAppearance(x3dpsail.Appearance().setDEF(x3dpsail.SFString("TestAppearance3"))
            # ArtDeco02Material ProtoInstance USE goes here. Note that name field is NOT defined as part of ProtoInstance USE. 

            .setMaterial(x3dpsail.ProtoInstance().setUSE(x3dpsail.SFString("ArtDeco02MaterialDEF"))))
          .setGeometry(x3dpsail.Cylinder().setHeight(x3dpsail.SFFloat(0.001)).setRadius(x3dpsail.SFFloat(0.001))))
        .addChild(x3dpsail.Inline().setDEF(x3dpsail.SFString("inlineSceneDef")).setUrl(x3dpsail.MFString(["someOtherScene.x3d","http://www.web3d.org/specifications/java/examples/someOtherScene.x3d"])))
        .addChild(x3dpsail.IMPORT().setAS(x3dpsail.SFString("WorldInfoDEF2")).setImportedDEF(x3dpsail.SFString("WorldInfoDEF")).setInlineDEF(x3dpsail.SFString("inlineSceneDef")))
        .addChild(x3dpsail.EXPORT().setAS(x3dpsail.SFString("WorldInfoDEF3")).setLocalDEF(x3dpsail.SFString("WorldInfoDEF")))
        .addChild(x3dpsail.ProtoDeclare().setAppinfo(x3dpsail.SFString("mimic a Material node and modulate fields as an animation effect")).setDocumentation(x3dpsail.SFString("http://x3dgraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/MaterialModulatorIndex.html")).setName(x3dpsail.SFString("MaterialModulator"))
          .setProtoInterface(x3dpsail.ProtoInterface()
            .addField(x3dpsail.field().setAccessType(x3dpsail.SFString("inputOutput")).setName(x3dpsail.SFString("enabled")).setType(x3dpsail.SFString("SFBool")).setValue(x3dpsail.SFString("true")))
            .addField(x3dpsail.field().setAccessType(x3dpsail.SFString("inputOutput")).setName(x3dpsail.SFString("diffuseColor")).setType(x3dpsail.SFString("SFColor")).setValue(x3dpsail.SFString("0 0 0")))
            .addField(x3dpsail.field().setAccessType(x3dpsail.SFString("inputOutput")).setName(x3dpsail.SFString("emissiveColor")).setType(x3dpsail.SFString("SFColor")).setValue(x3dpsail.SFString("0.05 0.05 0.5")))
            .addField(x3dpsail.field().setAccessType(x3dpsail.SFString("inputOutput")).setName(x3dpsail.SFString("specularColor")).setType(x3dpsail.SFString("SFColor")).setValue(x3dpsail.SFString("0 0 0")))
            .addField(x3dpsail.field().setAccessType(x3dpsail.SFString("inputOutput")).setName(x3dpsail.SFString("transparency")).setType(x3dpsail.SFString("SFFloat")).setValue(x3dpsail.SFString("0.0")))
            .addField(x3dpsail.field().setAccessType(x3dpsail.SFString("inputOutput")).setName(x3dpsail.SFString("shininess")).setType(x3dpsail.SFString("SFFloat")).setValue(x3dpsail.SFString("0.0")))
            .addField(x3dpsail.field().setAccessType(x3dpsail.SFString("inputOutput")).setName(x3dpsail.SFString("ambientIntensity")).setType(x3dpsail.SFString("SFFloat")).setValue(x3dpsail.SFString("0.0"))))
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
              .addField(x3dpsail.field().setAccessType(x3dpsail.SFString("inputOutput")).setName(x3dpsail.SFString("enabled")).setType(x3dpsail.SFString("SFBool")))
              .addField(x3dpsail.field().setAccessType(x3dpsail.SFString("inputOutput")).setName(x3dpsail.SFString("diffuseColor")).setType(x3dpsail.SFString("SFColor")))
              .addField(x3dpsail.field().setAccessType(x3dpsail.SFString("outputOnly")).setName(x3dpsail.SFString("newColor")).setType(x3dpsail.SFString("SFColor")))
              .addField(x3dpsail.field().setAccessType(x3dpsail.SFString("inputOnly")).setName(x3dpsail.SFString("clockTrigger")).setType(x3dpsail.SFString("SFTime")))
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
            .setMetadata(x3dpsail.MetadataString().setDEF(x3dpsail.SFString("FindableMetadataStringTest")).setName(x3dpsail.SFString("findThisNameValue")).setValue(x3dpsail.MFString(["test case"])))
            .setAppearance(x3dpsail.Appearance().setDEF(x3dpsail.SFString("DeclarativeAppearanceExample"))
              # DeclarativeMaterialExample gets overridden by subsequently added MaterialModulator ProtoInstance 

              .setMaterial(x3dpsail.ProtoInstance().setDEF(x3dpsail.SFString("MyMaterialModulator")).setName(x3dpsail.SFString("MaterialModulator"))))
            .setGeometry(x3dpsail.Cone().setBottom(x3dpsail.SFBool(False)).setBottomRadius(x3dpsail.SFFloat(0.05)).setHeight(x3dpsail.SFFloat(0.1))))
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
        .addChild(x3dpsail.Sound().setLocation(x3dpsail.SFVec3f(0,1.6,0))
          # set sound-ellipsoid location height at 1.6m to match typical avatar height 

          .setSource(x3dpsail.AudioClip().setDescription(x3dpsail.SFString("chimes")).setUrl(x3dpsail.MFString(["chimes.wav","http://www.web3d.org/x3d/content/examples/ConformanceNist/Sounds/AudioClip/chimes.wav"]))
            # Scene example fragment from http://www.web3d.org/x3d/content/examples/ConformanceNist/Sounds/AudioClip/default.x3d 

            ))
        .addChild(x3dpsail.Sound().setLocation(x3dpsail.SFVec3f(0,1.6,0))
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
            .setMaterial(x3dpsail.Material().setTransparency(x3dpsail.SFFloat(1.0))))
          .setGeometry(x3dpsail.Extrusion().setDEF(x3dpsail.SFString("ExampleExtrusion"))))
        .addChild(x3dpsail.Group()
          # Test MFNode children array as an ordered list consisting of comments, statements, ProtoInstance and nodes 

          .addChild(x3dpsail.ProtoDeclare().setName(x3dpsail.SFString("NewWorldInfo"))
            .setProtoInterface(x3dpsail.ProtoInterface()
              .addField(x3dpsail.field().setAccessType(x3dpsail.SFString("initializeOnly")).setName(x3dpsail.SFString("description")).setType(x3dpsail.SFString("SFString"))))
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
              .addPrograms(x3dpsail.ShaderProgram().setDEF(x3dpsail.SFString("TestShader2"))))
            .addShaders(x3dpsail.ProtoInstance().setDEF(x3dpsail.SFString("TestShader3")).setName(x3dpsail.SFString("ShaderProto")))
            .addShaders(x3dpsail.ComposedShader().setDEF(x3dpsail.SFString("TestShader4"))
              .addParts(x3dpsail.ShaderPart().setDEF(x3dpsail.SFString("TestShader5"))))))))

X3D0.toFileX3D("HelloWorldProgramOutputCanonical_RoundTrip.x3d")
