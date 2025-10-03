# ejercicio 1
import os
import shutil

os.mkdir("dataset")
dir_names = ['train','test','validation']
for name in dir_names:
  os.makedirs(f"dataset/{name}", exist_ok=True)
print(os.listdir('dataset'))


# Ejercicio 2
with open('data.txt','w',encoding="utf-8") as f:
  f.write('sample data')

shutil.copy('data.txt','backup_data.txt')
shutil.move('backup_data.txt','dataset/train')
os.listdir('dataset/train')

# ejercicio 3
with open('dataset/test/test.txt','w',encoding="utf-8") as f:
  f.write('test file')

print(os.listdir('dataset/test'))

shutil.rmtree('dataset/test')
print(os.listdir('dataset'))