import os

compile_file = ""
compile_lines = []
print_count = 0
print_str = ""
tables = []
program_counter = 0
new_table_add = ""
new_table_count = 0

os.system("clear")
while True:
  prompt = input("Type in file name (no format):  ")
  compile_file = open(f'{prompt}.sb', 'r')
  for line in compile_file:
    compile_lines.append(line.strip())
  for line in compile_lines:
    if compile_lines[program_counter].startswith("NEW TABLE"):
      new_table_count = 10
      for letter in range(len(compile_lines[program_counter]) - 10):
        new_table_add = new_table_add + compile_lines[program_counter][new_table_count]
        new_table_count += 1
      tables.append(new_table_add)
      print(f'Your new table {new_table_add} has been assigned at the index address {len(tables) - 1}.')
      new_table_add = ""
      new_table_count = 0
    program_counter += 1
  compile_lines.clear()
  tables.clear()
  program_counter = 0
