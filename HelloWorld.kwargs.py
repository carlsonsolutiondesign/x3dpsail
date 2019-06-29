from X3Dpackage import *
X3D0 = X3D(profile="Immersive", version="3.3",    head1 = head(    meta2 = meta(content="HelloWorld.x3d", name="title"), 
    meta3 = meta(content="Simple X3D scene example: Hello World!", name="description"), 
    meta4 = meta(content="30 October 2000", name="created"), 
    meta5 = meta(content="14 April 2017", name="modified"), 
    meta6 = meta(content="Don Brutzman", name="creator"), 
    meta7 = meta(content="HelloWorld.tall.png", name="Image"), 
    meta8 = meta(content="http://en.wikipedia.org/wiki/Hello_world", name="reference"), 
    meta9 = meta(content="https://en.wikipedia.org/wiki/Hello#.22Hello.2C_World.22_computer_program", name="reference"), 
    meta10 = meta(content="https://en.wikipedia.org/wiki/\"Hello,_World!\"_program", name="reference"), 
    meta11 = meta(content="http://en.wikibooks.org/w/index.php?title=Computer_Programming/Hello_world", name="reference"), 
    meta12 = meta(content="http://www.HelloWorldExample.net", name="reference"), 
    meta13 = meta(content="http://www.web3D.org", name="reference"), 
    meta14 = meta(content="http://www.web3d.org/realtime-3d/news/internationalization-x3d", name="reference"), 
    meta15 = meta(content="http://www.web3d.org/x3d/content/examples/HelloWorld.x3d", name="reference"), 
    meta16 = meta(content="http://X3dGraphics.com/examples/X3dForAdvancedModeling/HelloWorldScenes", name="reference"), 
    meta17 = meta(content="http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter01TechnicalOverview/HelloWorld.x3d", name="identifier"), 
    meta18 = meta(content="http://www.web3d.org/x3d/content/examples/license.html", name="license"), 
    meta19 = meta(content="X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit", name="generator"),     # Alternate encodings: VRML97, X3D ClassicVRML Encoding, X3D Compressed Binary Encoding (CBE), X3DOM, JSON 

    meta20 = meta(content="HelloWorld.wrl", name="reference"), 
    meta21 = meta(content="HelloWorld.x3dv", name="reference"), 
    meta22 = meta(content="HelloWorld.x3db", name="reference"), 
    meta23 = meta(content="HelloWorld.xhtml", name="reference"), 
    meta24 = meta(content="HelloWorld.json", name="reference")), 
   Scene25 = Scene(    # Example scene to illustrate X3D nodes and fields (XML elements and attributes) 

    WorldInfo26 = WorldInfo(title="Hello world!"), 
    Group27 = Group(     Viewpoint28 = Viewpoint(DEF="ViewUpClose", centerOfRotation=[0,-1,0], description="Hello world!", position=[0,-1,7]), 
     Transform29 = Transform(rotation=[0,1,0,3],       Shape30 = Shape(       Sphere31 = Sphere(), 
       Appearance32 = Appearance(        Material33 = Material(DEF="MaterialLightBlue", diffuseColor=[0.1,0.5,1]), 
        ImageTexture34 = ImageTexture(DEF="ImageCloudlessEarth", url=["earth-topo.png","earth-topo.jpg","earth-topo-small.gif","http://www.web3d.org/x3d/content/examples/Basic/earth-topo.png","http://www.web3d.org/x3d/content/examples/Basic/earth-topo.jpg","http://www.web3d.org/x3d/content/examples/Basic/earth-topo-small.gif"])))), 
     Transform35 = Transform(translation=[0,-2,0],       Shape36 = Shape(       Text37 = Text(DEF="TextMessage", string=["Hello","world!"],         FontStyle38 = FontStyle(justify=["MIDDLE","MIDDLE"])), 
       Appearance39 = Appearance(        Material40 = Material(USE="MaterialLightBlue")))))))
