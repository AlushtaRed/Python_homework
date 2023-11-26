from math import pi
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
def find_farthest_orbit(list_of_orbits):
    
   
    
    max_area = max([pi*i[0]*i[1]  for i in list_of_orbits if i[0] !=i[1]])
   
    final_res = list(filter(lambda x: max_area == pi*x[0]*x[1], list_of_orbits))
    # for i in list_of_orbits:
    #     if i[0] !=i[1]:
            
    #         if (pi*i[0]*i[1]) > max_area:
    #             max_area = pi*i[0]*i[1]
    #             result = i
    return final_res[0]


print(find_farthest_orbit(orbits))