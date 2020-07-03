# function for DIMENSION

def get_surface_area(*, height:float=2,width:float=5,length:float=10) -> float:
    return float(length*height*2 + width*height*2)
