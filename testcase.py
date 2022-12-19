import numpy as np
import time

def file():
    input_file = input("Enter the filename: ")
    file = open(input_file)    
    first_line = file.readline()
    arr = first_line.split(' ')
    arr[3]= arr[3].split('\n')[0]
    arr = [int(x) for x in arr]
    
    num_vertices = arr[0]
    num_edges = arr[1]
    num_faces = arr[2]
    num_tetrahedrons = arr[3] 
    
    print("no of vertices are:", num_vertices)
    print("no of edges are:", num_edges)
    print("no of faces are:", num_faces)
    print("no of tetrahedrons are:", num_tetrahedrons)

    coordinates = []
    vertices = []
    edges = []
    faces= []
    tetrahedrons = []

    for i in range(0, num_vertices):
        coordinate = file.readline()
        coordinates.append(coordinate)

    for i in range(0, num_vertices):
        vertices.append(i+1)

    for i in range(0, num_edges):
        j = file.readline()
        edge = list(map(int, j.split(' ')))
        edges.append(edge)
    
    for i in range(0, num_faces):
        j = file.readline()
        face = list(map(int, j.split(' ')))
        faces.append(face)

    for i in range(0, num_tetrahedrons):
        j = file.readline()
        tetra = list(map(int, j.split(' ')))
        tetrahedrons.append(tetra)

    temp=[]
    temp.append(num_faces)
    temp.append(edges)
    temp.append(faces)
    temp.append(vertices)
    temp.append(tetrahedrons)
    return temp

def image_space_delta_2(vertices, faces, edges):
    # f1 = []
    # for i in faces:
    #     e = []
    #     for j in i:
    #         e.append(edges[j-1])
    #     f1.append(e)
    # print(f1)
    f1 = []
    tmp = []
    for i in faces:
        e = []
        for j in i:
            if edges[j-1] not in tmp:
                e.append(edges[j-1])
                tmp.append(edges[j-1])
            else:
                e.append(edges[j-1][::-1])
                tmp.append(edges[j-1][::-1])
            
        f1.append(e)

    ed = []
    for i in range(0,len(vertices)):
        for j in range(i+1,len(vertices)):
            ed.append([vertices[i],vertices[j]][::-1])
    
    del2 = []
    for i in f1:
        c1 = []
        for j in ed:
            if j in i:
                c1.append(1)
            elif j[::-1] in i:
                c1.append(-1)
            else:
                c1.append(0)
        del2.append(c1)
    
        # for j in i:
        #     if j in ed:
        #         c1.append(1)
        #     elif j[::-1] in ed:
        #         c1.append(-1)
        #     else:
        #         c1.append(0)
    
    del2 = np.transpose(del2)
    del2 = del2[~ np.all(del2 == 0, axis=1)]
    #print(del2)
    return np.linalg.matrix_rank(del2)

def image_space_delta_3(faces, tetrahedrons):
    arr = [[0]*len(tetrahedrons) for i in range(len(faces))]
    count=0
    for i in range(0,len(tetrahedrons)):
        f1 = tetrahedrons[i][0]
        x1 = faces[f1 - 1][0]
        y1 = faces[f1 - 1][1]
        z1 = faces[f1 - 1][2]

        f2 = tetrahedrons[i][1]
        x2 = faces[f2 - 1][0]
        y2 = faces[f2 - 1][1]
        z2 = faces[f2 - 1][2]

        f3 = tetrahedrons[i][2]
        x3 = faces[f3 - 1][0]
        y3 = faces[f3 - 1][1]
        z3 = faces[f3 - 1][2]

        f4 = tetrahedrons[i][3]
        x4 = faces[f4 - 1][0]
        y4 = faces[f4 - 1][1]
        z4 = faces[f4 - 2][2]

        arr[f1 - 1][count] = 1 
            
        if(x1 == y2 or x1 == z2 or y1 == x2 or y1 == z2 or z1 == x2 or z1 == y2):
            arr[f2 - 1][count] = -1
        else:
            arr[f2 - 1][count] = 1
            
        if(x1 == y3 or x1 == z3 or y1 == z3 or y1 == x3 or z1 == x3 or z1 == y3):
            arr[f3 - 1][count] = -1
        else:
            arr[f3 - 1][count] = 1

        if(x1 == y4 or x1 == z4 or y1 == x4 or y1 == z4 or z1 == x4 or z1 == y4):
            arr[f4 - 1][count] = -1
        else:
            arr[f4 - 1][count] = 1
        count += 1
    
    arr = np.transpose(arr)
    arr = np.transpose(arr)
    #print(arr)
    return(np.linalg.matrix_rank(arr))


def main():
    temp = file()
    num_faces = temp[0]
    edges = temp[1]
    faces = temp[2]
    vertices = temp[3]
    tetrahedrons = temp[4]

    begin = time.time()
    image_delta2 = image_space_delta_2(vertices, faces,edges)
    
    if tetrahedrons == []:
        image_delta3 = 0
    else:
        image_delta3 = image_space_delta_3(faces, tetrahedrons)
    
    print("\nImage of betti_2 = ", image_delta2)
    print("Kernel of betti_2 = ", num_faces - image_delta2)
    print("Image of betti_3 = ", image_delta3)
    
    betti_2 = num_faces - image_delta2 - image_delta3
    end = time.time()

    print("")
    print("+-------------+")
    print("|betti_2 = ", betti_2, "|")
    print("+-------------+")
    print("\nexecution time:", end - begin)

main()