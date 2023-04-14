import os

compile_file = ""
compile_lines = []
print_count = 0
print_str = ""
queries = []
program_counter = 0
new_query_add = ""
new_query_count = 0
query_log_count = 0
query_log_str = ""
query_log = 0
insert_addr_count = 0
insert_addr_str = ""
insert_addr = 0
insert_add_count = 0
insert_str = ""

os.system("clear")
while True:
  prompt = input("Type in file name (no format):  ")
  compile_file = open(f'src/{prompt}.sib', 'r')
  for line in compile_file:
    compile_lines.append(line.strip())
  for line in compile_lines:
    if compile_lines[program_counter].startswith("NEW QUERY"):
      new_query_count = 10
      for letter in range(len(compile_lines[program_counter]) - 10):
        new_query_add = new_query_add + compile_lines[program_counter][new_query_count]
        new_query_count += 1
      queries.append(new_query_add)
      print(f'Your new query {new_query_add} has been assigned at the index address {len(queries) - 1}.')
      new_query_add = ""
      new_query_count = 0
    elif compile_lines[program_counter].startswith("LOGS"):
      query_log_count = 5
      for letter in range(len(compile_lines[program_counter]) - 5):
        query_log_str = query_log_str + compile_lines[program_counter][query_log_count]
        query_log_count += 1
      query_log = int(query_log_str)
      print(queries[query_log])
      query_log = 0
      query_log_str = ""
      query_log_count = 0
    elif compile_lines[program_counter].startswith("INSERT AT"):
      insert_addr_count = 10
      while not compile_lines[program_counter][insert_addr_count] == " ":
        insert_addr_str = insert_addr_str + compile_lines[program_counter][insert_addr_count]
        insert_addr_count += 1
      insert_addr = int(insert_addr_str)
      insert_add_count = insert_addr_count + 1
      for letter in range(len(compile_lines[program_counter]) - insert_add_count):
        insert_str = insert_str + compile_lines[program_counter][insert_add_count]
        insert_add_count += 1
      queries[insert_addr] = insert_str
      print(f'Assigned data {insert_str} to address {insert_addr}.')
      insert_str = ""
      insert_addr = 0
      insert_addr_count = 0
      insert_add_count = 0
      insert_addr_str = ""
    program_counter += 1
  compile_lines.clear()
  queries.clear()
  program_counter = 0
