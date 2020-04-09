import os

module_dir = os.path.dirname(__file__)
modules_folder = os.path.join(module_dir, 'modules')
os.makedirs(modules_folder, exist_ok=True)

template_module = '''
class MyClass():
    
    def __init__(self):
        print('Hello from', __class__)

if __name__ == '__main__':
    MyClass()
'''

for idx in range(1, 6):
    new_file = os.path.join(modules_folder, 'Module' + str(idx) + '.py')
    with open(new_file, 'w') as file:
        file.writelines(template_module)


print(os.listdir(modules_folder))


















