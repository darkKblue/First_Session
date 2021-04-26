def counter(vorodi):
    string=int()
    Dict=int()
    Set=int()
    List=int()
    Tuple=int()
    output=dict()

    for index in vorodi:
        if type(index)==type(str()):
            string+=1
        elif type(index)==type(dict()):
            Dict+=1
        elif type(index)==type(tuple()):
            Tuple+=1
        elif type(index)==type(set()):
            Set+=1
        elif type(index)==type(list()):
            List+=1
    output={"string": string,"Tuple": Tuple,"Dict": Dict,"Set": Set,"List": List}
    return output
 
