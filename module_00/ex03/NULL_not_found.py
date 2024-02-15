def NULL_not_found(object: any) -> int:
    if type(object) is type(None):
        print("Nothing:", end=" ")
    elif type(object) is float:
        print("Cheese:", end=" ")
    elif type(object) is int:
        print("Zero:", end=" ")
    elif type(object) is str and not object:
        print("Empty:", end=" ")
    elif type(object) is bool:
        print("Fake:", end=" ")
    else:
        print("Type not Found")
        return 1
    print(f"{object} {type(object)}")
    return 0
