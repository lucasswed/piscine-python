def all_thing_is_obj(object: any) -> int:
    if type(object) == list:
        print('list :', end=' ')
    elif type(object) == tuple:
        print('tuple :', end=' ')
    elif type(object) == set:
        print('set :', end=' ')
    elif type(object) == dict:
        print('dict :', end=' ')
    elif type(object) == str:
        print(f'{object} is in the kitchen :', end=' ')
    else:
        print('Type not found')
        return 42
    print(type(object))

    return 42