import numpy as np
import open3d as o3d
import matplotlib.pyplot as plt

if __name__ == '__main__':
	print(o3d.__version__)
	
	# cube = o3d.geometry.TriangleMesh.create_box().translate([0, 0, 0])
	# cube = o3d.t.geometry.TriangleMesh.from_legacy(cube)
	# torus = o3d.geometry.TriangleMesh.create_torus().translate([0, 0, 2])
	# torus = o3d.t.geometry.TriangleMesh.from_legacy(torus)
	# sphere = o3d.geometry.TriangleMesh.create_sphere(radius=0.5).translate(
	# 	[1, 2, 3])
	# sphere = o3d.t.geometry.TriangleMesh.from_legacy(sphere)
	#
	# scene = o3d.t.geometry.RaycastingScene()
	# scene.add_triangles(cube)
	# scene.add_triangles(torus)
	# _ = scene.add_triangles(sphere)
	# rays = o3d.t.geometry.RaycastingScene.create_rays_pinhole(
	# 	fov_deg=90,
	# 	center=[0, 0, 2],
	# 	eye=[2, 3, 0],
	# 	up=[0, 1, 0],
	# 	width_px=640,
	# 	height_px=480,
	# )
	# # We can directly pass the rays tensor to the cast_rays function.
	# ans = scene.cast_rays(rays)
	# print(ans['t_hit'])
	#
	# plt.imshow(ans['t_hit'].numpy())
	# plt.show()
	
	mesh_path = './data/prefabs/cube.fbx'
	mesh = o3d.io.read_triangle_mesh(mesh_path, True)
	mesh.translate([0, 0, 0])
	
	print(mesh)
	print('Vertices:')
	print(np.asarray(mesh.vertices))
	print('Triangles:')
	print(np.asarray(mesh.triangles))
	
	mesh_faces = mesh.triangles
	mesh_uvs = mesh.triangle_uvs
	texture = mesh.textures
	
	scene = o3d.t.geometry.RaycastingScene()
	mesh_id = scene.add_triangles(o3d.t.geometry.TriangleMesh.from_legacy(mesh))
	print(mesh_id)
	print(mesh.get_max_bound())
	
	# rays = o3d.core.Tensor([[-150, -150, -150, 150, 150, 150]], dtype=o3d.core.Dtype.Float32)
	# rays = scene.create_rays_pinhole(fov_deg=60,
	# 								 center=[0, 0, 0],
	# 								 eye=[-1, -1, -1],
	# 								 up=[0, 0, 1],
	# 								 width_px=480,
	# 								 height_px=360)
	# ans = scene.cast_rays(rays)
	# print(ans.keys())
	# print(ans['t_hit'])
	#
	# plt.imshow(ans['t_hit'].numpy())
	# plt.show()

# vis = o3d.visualization.Visualizer()
# vis.create_window(window_name='Mesh Visualizer', width=800, height=600)
#
# mesh.compute_vertex_normals()
# mesh.scale(1 / np.max(mesh.get_max_bound() - mesh.get_min_bound()), center=mesh.get_center())
# vis.add_geometry(mesh)
#
# vis.run()
# vis.destroy_window()
