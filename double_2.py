def double(val):
    if isinstance(val, list):
        x, double_x = val+val, list(map(lambda x: x*2 , val)) 
    else:
        if isinstance(val, int):
            x, double_x = [val,val], [2*val]
        else:
            if isinstance(val, float):
                x, double_x = val, 2*val
            else:
                x, double_x = "ERROR","Błędny typ danych"
    return x, double_x
        
