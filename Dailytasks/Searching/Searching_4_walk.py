import os


os.chdir(os.pardir)

search_start_dir = os.getcwd()
print(search_start_dir)

gen = os.walk(search_start_dir)      
print(gen)






















