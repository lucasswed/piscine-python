def all_thing_is_obj(object: any) -> int:
    if type(object) is list:
        print('list :', end=' ')
    elif type(object) is tuple:
        print('tuple :', end=' ')
    elif type(object) is set:
        print('set :', end=' ')
    elif type(object) is dict:
        print('dict :', end=' ')
    elif type(object) is str:
        print(f'{object} is in the kitchen :', end=' ')
    else:
        print('Type not found')
        return 42
    print(type(object))

    return 42
