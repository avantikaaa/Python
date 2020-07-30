import os
'''from print_tree import *'''

def dict_making(startpath):
    root_content=[]
    for root, dirs, files in os.walk(startpath):
        for dir in dirs:
	    dir_content = {}
            go_inside = os.path.join(startpath, dir)
            dir_content[dir]=dict_making(go_inside)
            root_content.append(dir_content)
        for f in files:
            root_content.append(f)
        return root_content

