# Fisheye Obj for Unity
This is dirty script for making fisheye projection objects for Unity.
If you want to make a fisheye camera in Unity, you can use the .obj files.
This script makes five object files(front, top, bottom, right, left).

This script is for 180 degree camera. If you want a camera with larger degree, you can change the code to make it.

If you want to know more detail please check references.
(The references are not my webpage)

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
