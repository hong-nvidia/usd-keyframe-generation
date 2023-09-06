# Omniverse USD Keyframe Animation Generation

This short document demonstrates the use of `SetAnimCurveKeys` command to generate keyframe animations in Omniverse.

## Example Result

![](result.gif)


## Code Snippets

First, open a USD stage and create a target of animation such as a cube. We then run the following script in the script editor

```
import omni
from pxr import Usd

target_prim_path = '/World/Cube'
target_xform_property = 'xformOp:translate|x'

keyframe_values = [0.0, 200.0, 0.0]
keyframe_timecodes = [0, 50, 100]
num_keyframes = len(keyframe_values)

for i in range(num_keyframes):
    omni.kit.commands.execute('SetAnimCurveKeys',
                              paths = [f'{target_prim_path}.{target_xform_property}'],
                              value = keyframe_values[i],
                              time  = Usd.TimeCode(keyframe_timecodes[i])
    )
```

Analogously, you can animate other xform properties by changing the `target_xform_property` to values such as `xformOp:rotate|y` or `xformOp:scale|z`