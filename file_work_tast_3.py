with open("1.txt") as file:
  file_1 = [line.strip() for line in file.readlines()]

with open("2.txt") as file:
  file_2 = [line.strip() for line in file.readlines()]

with open("3.txt") as file:
  file_3 = [line.strip() for line in file.readlines()]

# print(len(file_1), len(file_2), len(file_3), sep="\n\n")

concat_file = [
    'Объединенный файл concated.txt',
    f'Количество строк объединенного файла {len(file_1) + len(file_2) + len(file_3)}'
]



if len(file_1) < len(file_2) and len(file_1) < len(file_3):
  concat_file += file_1
  if len(file_2) < len(file_3):
    concat_file += file_2
    concat_file += file_3
  elif len(file_3) < len(file_2):
    concat_file += file_3
    concat_file += file_2
elif len(file_2) < len(file_1) and len(file_2) < len(file_3):
  concat_file += file_2
  if len(file_1) < len(file_3):
    concat_file += file_1
    concat_file += file_3
  elif len(file_3) < len(file_1):
    concat_file += file_3
    concat_file += file_1
elif len(file_3) < len(file_1) and len(file_3) < len(file_2):
  concat_file += file_3
  if len(file_1) < len(file_2):
    concat_file += file_1
    concat_file += file_2
  elif len(file_2) < len(file_1):
    concat_file += file_2
    concat_file += file_1

print(concat_file)

with open("concated.txt", "w") as file:
  for line in concat_file:
    file.write(line + "\n")
