#!/usr/bin/python3
"""
This script returns information about his/her TOTO
list progress using a REST API
"""


from requests import get
from sys import argv

if __name__ == '__main__':
    main_url = 'https://jsonplaceholder.typicode.com'
    parm_todo = main_url + "/user/{}/todos".format(argv[1])
    parm_name = main_url + "/users/{}".format(argv[1])
    output_todo = get(parm_todo).json()
    output_name = get(parm_name).json()

    num_todo = len(output_todo)
    all_todo = len([todo for todo in output_todo
                    if todo.get("completed")])
    name = output_name.get("name")
    print("Employee {} is done with tasks({}/{}):"
          .format(name, all_todo, num_todo))
    for todo in output_todo:
        if (todo.get("completed")):
            print("\t {}".format(todo.get("title")))
