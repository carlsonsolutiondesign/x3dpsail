from X3Dpackage import *
X3D0 = X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.3"

head1 = head()

meta2 = meta()
meta2.content = "HelloWorld.x3d"
meta2.name = "title"
head1.addMeta([meta2])

meta3 = meta()
meta3.content = "Simple X3D scene example: Hello World!"
meta3.name = "description"
head1.addMeta([meta3])

meta4 = meta()
meta4.content = "30 October 2000"
meta4.name = "created"
head1.addMeta([meta4])

meta5 = meta()
meta5.content = "28 July 2015"
meta5.name = "modified"
head1.addMeta([meta5])

meta6 = meta()
meta6.content = "Don Brutzman"
meta6.name = "creator"
head1.addMeta([meta6])

meta7 = meta()
meta7.content = "HelloWorld.tall.png"
meta7.name = "Image"
head1.addMeta([meta7])

meta8 = meta()
meta8.content = "http://en.wikipedia.org/wiki/Hello_world"
meta8.name = "reference"
head1.addMeta([meta8])

meta9 = meta()
meta9.content = "https://en.wikipedia.org/wiki/Hello#.22Hello.2C_World.22_computer_program"
meta9.name = "reference"
head1.addMeta([meta9])

meta10 = meta()
meta10.content = "https://en.wikipedia.org/wiki/\"Hello,_World!\"_program"
meta10.name = "reference"
head1.addMeta([meta10])

meta11 = meta()
meta11.content = "http://en.wikibooks.org/w/index.php?title=Computer_Programming/Hello_world"
meta11.name = "reference"
head1.addMeta([meta11])

meta12 = meta()
meta12.content = "http://www.HelloWorldExample.net"
meta12.name = "reference"
head1.addMeta([meta12])

meta13 = meta()
meta13.content = "http://www.web3D.org"
meta13.name = "reference"
head1.addMeta([meta13])

meta14 = meta()
meta14.content = "http://www.web3d.org/realtime-3d/news/internationalization-x3d"
meta14.name = "reference"
head1.addMeta([meta14])

meta15 = meta()
meta15.content = "http://www.web3d.org/x3d/content/examples/HelloWorld.x3d"
meta15.name = "reference"
head1.addMeta([meta15])

meta16 = meta()
meta16.content = "http://X3dGraphics.com/examples/X3dForAdvancedModeling/HelloWorldScenes"
meta16.name = "reference"
head1.addMeta([meta16])

meta17 = meta()
meta17.content = "http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter01TechnicalOverview/HelloWorld.x3d"
meta17.name = "identifier"
head1.addMeta([meta17])

meta18 = meta()
meta18.content = "http://www.web3d.org/x3d/content/examples/license.html"
meta18.name = "license"
head1.addMeta([meta18])

meta19 = meta()
meta19.content = "X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit"
meta19.name = "generator"
head1.addMeta([meta19])
# Alternate encodings: VRML97, X3D ClassicVRML Encoding, X3D Compressed Binary Encoding (CBE), X3DOM, JSON 

meta20 = meta()
meta20.content = "HelloWorld.wrl"
meta20.name = "reference"
head1.addMeta([meta20])

meta21 = meta()
meta21.content = "HelloWorld.x3dv"
meta21.name = "reference"
head1.addMeta([meta21])

meta22 = meta()
meta22.content = "HelloWorld.x3db"
meta22.name = "reference"
head1.addMeta([meta22])

meta23 = meta()
meta23.content = "HelloWorld.xhtml"
meta23.name = "reference"
head1.addMeta([meta23])

meta24 = meta()
meta24.content = "HelloWorld.json"
meta24.name = "reference"
head1.addMeta([meta24])
X3D0.head = head1

Scene25 = Scene()
# Example scene to illustrate X3D nodes and fields (XML elements and attributes) 

Group26 = Group()

Viewpoint27 = Viewpoint()
Viewpoint27.DEF = "ViewUpClose"
Viewpoint27.centerOfRotation = [0,-1,0]
Viewpoint27.description = "Hello world!"
Viewpoint27.position = [0,-1,7]
Group26.addChildren([Viewpoint27])

Transform28 = Transform()
Transform28.rotation = [0,1,0,3]

Shape29 = Shape()

Sphere30 = Sphere()
Shape29.geometry = Sphere30

Appearance31 = Appearance()

Material32 = Material()
Material32.DEF = "MaterialLightBlue"
Material32.diffuseColor = [0.1,0.5,1]
Appearance31.material = Material32

ImageTexture33 = ImageTexture()
ImageTexture33.DEF = "ImageCloudlessEarth"
ImageTexture33.url = ["earth-topo.png","earth-topo.jpg","earth-topo-small.gif","http://www.web3d.org/x3d/content/examples/Basic/earth-topo.png","http://www.web3d.org/x3d/content/examples/Basic/earth-topo.jpg","http://www.web3d.org/x3d/content/examples/Basic/earth-topo-small.gif"]
Appearance31.texture = ImageTexture33
Shape29.appearance = Appearance31
Transform28.addChildren([Shape29])
Group26.addChildren([Transform28])

Transform34 = Transform()
Transform34.translation = [0,-2,0]

Shape35 = Shape()

Text36 = Text()
Text36.DEF = "TextMessage"
Text36.string = ["Hello","world!"]

FontStyle37 = FontStyle(justify = ["MIDDLE","MIDDLE"])
Text36.fontStyle = FontStyle37
Shape35.geometry = Text36

Appearance38 = Appearance()

Material39 = Material()
Material39.USE = "MaterialLightBlue"
Appearance38.material = Material39
Shape35.appearance = Appearance38
Transform34.addChildren([Shape35])
Group26.addChildren([Transform34])
Scene25.addChildren([Group26])
X3D0.scene = Scene25
