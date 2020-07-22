# Fisheye Mesh Generator
This is a script for making fisheye projection mesh objects for Unity.
It generates mesh files (.obj) and you can use theses files to create a virtual fisheye camera in a Unity virtual environment.

This script is only for 180 degree camera. If you want a camera with larger degree, you can change the code to make it.

If you want to know more detail please check references.

## How to use
```shell
$ run.py 'fisheye model type' 'resolution'
```
* fisheye model type
  * equidistance
  * orthogonal
  * stereographic
  * equisolid
* Resulotion
  * The number of face blocks that divides a side of square
  * ex) 8, 16, 32
* Example
   ```shell
   $ python run.py equidistance 256
   ```

## Outcome
The script will make folders for square objects and fisheye objects.

'Fisheye.png' will be created. It shows how squares are mapped with fisheye camera model.

## Dependencies

You need numpy and matplot.

## References
Here are some great articles about fisheye camera for Unity.

* http://paulbourke.net/dome/unity3d/
* http://paulbourke.net/dome/unityfisheye/
