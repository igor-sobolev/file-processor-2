import os
path_to_root = '/home/igor/workspace/awtg/documents_all/'

directories = [os.path.join(path_to_root, subitem)
    for subitem in os.listdir(path_to_root)
    if os.path.isdir(os.path.join(path_to_root, subitem))]

directories_shortnames = filter(
    lambda x:
        os.path.isdir(os.path.join(path_to_root, x)), os.listdir(path_to_root)
)

print(directories)
print(list(directories_shortnames))
