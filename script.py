from pxr import Usd, UsdGeom, Gf, Sdf


stage = Usd.Stage.CreateNew('keyframe.usda')
stage.DefinePrim('/World', 'Xform')
stage.SetMetadata('defaultPrim', 'World')
stage.SetMetadata('startTimeCode', 0)
stage.SetMetadata('endTimeCode', 100)
stage.SetMetadata('timeCodesPerSecond', 60)
stage.SetMetadata('metersPerUnit', 0.01)
stage.SetMetadata('upAxis', 'Y')


target_prim_path = '/World/Cube'
cube_extent = [(-50, -50, -50), (50, 50, 50)]
cube_size = 100
initial_rotation = (0, 0, 0)
initial_scale = (1, 1, 1)
initial_translation = (0, 0, 0)

cube_prim = UsdGeom.Cube.Define(stage, target_prim_path).GetPrim()
cube_prim.CreateAttribute('extent', Sdf.ValueTypeNames.Float3Array).Set(cube_extent)
cube_prim.CreateAttribute('size', Sdf.ValueTypeNames.Double).Set(cube_size)
cube_prim.CreateAttribute('xformOp:rotateXYZ', Sdf.ValueTypeNames.Double3).Set(initial_rotation)
cube_prim.CreateAttribute('xformOp:scale', Sdf.ValueTypeNames.Double3).Set(initial_scale)
cube_prim.CreateAttribute('xformOp:translate', Sdf.ValueTypeNames.Double3).Set(initial_translation)
cube_prim.CreateAttribute('xformOpOrder', Sdf.ValueTypeNames.TokenArray).Set([
    'xformOp:translate', 'xformOp:rotateXYZ', 'xformOp:scale'
])


og_prim = stage.DefinePrim('/World/PushGraph', 'OmniGraph')
og_prim.CreateAttribute('evaluationMode', Sdf.ValueTypeNames.Token).Set('Automatic')
og_prim.CreateAttribute('evaluator:type', Sdf.ValueTypeNames.Token).Set('push')
og_prim.CreateAttribute('fabricCacheBacking', Sdf.ValueTypeNames.Token).Set('Shared')
og_prim.CreateAttribute('fileFormatVersion', Sdf.ValueTypeNames.Int2,).Set(Gf.Vec2i(1, 6))
og_prim.CreateAttribute('pipelineStage', Sdf.ValueTypeNames.Token).Set('pipelineStageSimulation')


node_prim = stage.DefinePrim('/World/PushGraph/CubeCurveNode', 'OmniGraphNode')
node_prim.CreateRelationship('inputs:Prim').SetTargets([target_prim_path])
node_prim.CreateAttribute('inputs:Time', Sdf.ValueTypeNames.TimeCode,).Set(Sdf.TimeCode(0))
node_prim.CreateAttribute('inputs:UseGlobalTime', Sdf.ValueTypeNames.Bool).Set(True)
node_prim.CreateAttribute('node:type', Sdf.ValueTypeNames.Token).Set('omni.anim.curve.AnimCurve')
node_prim.CreateAttribute('node:typeVersion', Sdf.ValueTypeNames.Int).Set(5)


x_axis_values = [0, 200, 0]
keyframe_times = [0, 100000000, 200000000]

node_prim.CreateAttribute('xformOp:translate:x:defaultTangentType', Sdf.ValueTypeNames.Token).Set('auto')
node_prim.CreateAttribute('xformOp:translate:x:inTangentTimes', Sdf.ValueTypeNames.Int64Array).Set([0, 0, -0])
node_prim.CreateAttribute('xformOp:translate:x:inTangentTypes', Sdf.ValueTypeNames.TokenArray).Set(['auto', 'auto', 'auto'])
node_prim.CreateAttribute('xformOp:translate:x:inTangentValues', Sdf.ValueTypeNames.DoubleArray).Set([0, 0, 0])
node_prim.CreateAttribute('xformOp:translate:x:outTangentTimes', Sdf.ValueTypeNames.Int64Array).Set([0, 0, 0])
node_prim.CreateAttribute('xformOp:translate:x:outTangentTypes', Sdf.ValueTypeNames.TokenArray).Set(['auto', 'auto', 'auto'])
node_prim.CreateAttribute('xformOp:translate:x:outTangentValues', Sdf.ValueTypeNames.DoubleArray).Set([0, 0, 0])
node_prim.CreateAttribute('xformOp:translate:x:postInfinityType', Sdf.ValueTypeNames.Token).Set('constant')
node_prim.CreateAttribute('xformOp:translate:x:preInfinityType', Sdf.ValueTypeNames.Token).Set('constant')
node_prim.CreateAttribute('xformOp:translate:x:tangentBrokens', Sdf.ValueTypeNames.BoolArray).Set([0, 0, 0])
node_prim.CreateAttribute('xformOp:translate:x:tangentWeighteds', Sdf.ValueTypeNames.BoolArray).Set([0, 0, 0])
node_prim.CreateAttribute('xformOp:translate:x:times', Sdf.ValueTypeNames.Int64Array).Set(keyframe_times)
node_prim.CreateAttribute('xformOp:translate:x:values', Sdf.ValueTypeNames.DoubleArray).Set(x_axis_values)

stage.Save()