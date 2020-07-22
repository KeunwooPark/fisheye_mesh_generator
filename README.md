# Fisheye Mesh Generator
This is a fisheye projection mesh generator.
It generates mesh files (.obj) and you can use theses files to create a virtual fisheye camera in a Unity virtual environment.

This script is only for 180 degree camera. If you want a camera with larger degree, you can change the code to make it.

If you want to know more detail please check references.

## How to Use
Install dependent packages first.
```shcell
$ pip install -r requirements.txt
```
Then run the script.
```shell
$ run.py --model_type equidistance --res 64
```

### Model Type
This generator supports four fisheye projection model types.
* equidistance
* orthogonal
* stereographic
* equisolid

### Resolution
The higher number generates more fine mesh. Default value is 64. What it actually means is a number of grids that splits a side of a virtual cube.

## Output
The script will create two folders for square objects (```square_objs```) and fisheye objects (```fish_objs```). What you will use is the fisheye objects. It also creates ```fisheye.png```, which visualizes the created fisheye meshes.

# More Resources
## [Technical Document](https://www.notion.so/keunwoopark/Fisheye-Mesh-Generator-How-Does-It-Work-e7ccf209708041e4aec295d53567cced)
If you want to understand more about this code, please check this document.

## [Unity Example](https://github.com/KeunwooPark/Unity-Fisheye-Example)
If you want to create a fisheye camera using the mesh outputs, please check out this repository.

## References
Here are some great articles about fisheye camera for Unity.

* http://paulbourke.net/dome/unity3d/
* http://paulbourke.net/dome/unityfisheye/
