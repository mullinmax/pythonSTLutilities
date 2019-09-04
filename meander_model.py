import re


def read_stl(name):
    file = open(name)
    lines = file.readlines()
    nums = []
    for line in lines:
        for num in re.finditer('[\+\-]{0,1}\d+.\d+e[\+\-]\d+', line):
            nums.append(num.group())
    verts = []
    for i in range(0, len(nums), 3):
        verts.append([float(nums[i]), float(nums[i+1]), float(nums[i+2])])
    faces = []
    for i in range(0, len(verts), 4):
        faces.append([verts[i], verts[i+1], verts[i+2], verts[i+3]])
    return faces


def write_stl(name, objs):
    file = open(name, 'w')
    obj_temp = '''solid ASCII{facets}
  endsolid
    '''

    facet_temp = '''
  facet normal {v0}
    outer loop
      vertex   {v1}
      vertex   {v2}
      vertex   {v3}
    endloop
  endfacet'''

    vert_temp = '''{x} {y} {z}'''

    for obj in objs:
        body = ''
        for f in obj:
            vs = []
            for v in f:
                vs.append(vert_temp.format(x=v[0], y=v[1], z=v[2]))
            facet = facet_temp.format(v0=vs[0], v1=vs[1], v2=vs[2], v3=vs[3])
            body = body + facet
        file.write(obj_temp.format(facets=body))


def translate(obj, x, y, z):
    out = []
    for face in obj:
        f = []
        f.append(face[1])
        for vert in face[1:]:
            f.append([vert[0] + x, vert[1] + y, vert[2] + z])
        out.append(f)
    return out


# def rotate(obj, axis, deg):
#     out = []
#     for f in obj:
#         vecs = []
#         for v in f:
#             vecs.append([v[]])


size = 5.1
tiles = []
tiles.append(read_stl('blank.stl'))
tiles.append(read_stl('horizontal.stl'))
tiles.append(read_stl('vertical.stl'))
tiles.append(read_stl('tl.stl'))
tiles.append(read_stl('tr.stl'))
tiles.append(read_stl('bl.stl'))
tiles.append(read_stl('br.stl'))

for i in range(len(tiles)):
    tiles[i] = translate(tiles[i], i*size, 0, 0)

write_stl('test.stl', tiles)

# 0 = v
# 1 = h
# 2 = tl
# 3 = tr
# 4 = bl
# 5 = br

[
    [5, 4, 5, 1, 4],
    [3, 4, 3, 2, 2],
    [4, 2, 5, 2, ],
    [],
    []
]
