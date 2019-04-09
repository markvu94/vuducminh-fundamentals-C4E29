def is_inside(point,rectangle):
    result = False
    if rectangle[0] <= point[0] <= (rectangle[0] + rectangle[2]) and rectangle[1] <= point [1] <= (rectangle[1] +rectangle[3]):
        result = True
    return(result)
print(is_inside([200,120],[140,60,100,120]))




