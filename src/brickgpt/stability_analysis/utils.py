import numpy as np


def construct_world_grid(bricks, world_dimension, brick_library):
    world_grid = np.zeros(world_dimension)
    for key in bricks.keys():
        brick = bricks[key]
        brick_id = str(brick["brick_id"])
        if brick["ori"] == 0:
            h = brick_library[brick_id]["height"]
            w = brick_library[brick_id]["width"]
        else:
            w = brick_library[brick_id]["height"]
            h = brick_library[brick_id]["width"]
        brick_x = brick["x"]
        brick_y = brick["y"]
        brick_z = brick["z"]
        for i in range(brick_x, brick_x + h):
            for j in range(brick_y, brick_y + w):
                world_grid[i, j, brick_z] = 1
    return world_grid


def gen_key(x, y, z):
    return "X: " + str(x) + ", Y: " + str(y) + ", Z: " + str(z)


def out_boundary(pt, brick_x, brick_y, h, w):
    x = pt[0]
    y = pt[1]
    if x < brick_x or x >= brick_x + h or y < brick_y or y >= brick_y + w:
        return True
    return False
