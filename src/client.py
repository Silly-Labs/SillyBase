import os
import random
import sys
import time
from time import sleep

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
compile_to_count = 0
selected = 0
selected_str = ""
select_count = 0

# lmao what are these names :skull:
random_names = ["cosmic-cat", "silly-string", "voloptous-table", "stainless-stain", "rusted-ownership", "weakly-typed", "goober-energy", "descriptive-soda", "abstractive-star", "unbiased-home", "fishy-existence", "mossy-water", "meal-rock", "fried-brick"]

os.system("clear")

"""
SillyBase Client - By HaxeFloppa/epok_gamer
"""

print("SILLYBASE CLIENT --------- By HaxeFloppa/epok_gamer\n")
print("=======================================================")
while True:
  prompt = input("Type in file name (no format):  ")
  if prompt == "exit()":
    os.system("clear")
    print("Thank you for using SillyBase. Sillying out.")
    time.sleep(1.5)
    os.system("clear")
    sys.exit()
  else:
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
      if query_log_str == "SELECTED":
        print(queries[selected])
        selected = 0
      else:
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
    elif compile_lines[program_counter] == "SAVE FILE":
      with open(f'result/{random_names[random.randint(0,len(random_names) - 1)]}.html', 'a') as static_file:
        static_file.write("<table>\n")
        static_file.write("  <tr>\n")
        compile_to_count = 0
        while compile_to_count < len(queries):
          static_file.write(f'    <td>{queries[compile_to_count]}</td>\n')
          compile_to_count += 1
        static_file.write("  </tr>\n")
        static_file.write("</table>")
        print("Queries written to static HTML.")
    elif compile_lines[program_counter].startswith("SELECT"):
      select_count = 7
      for letter in range(len(compile_lines[program_counter]) - 7):
        selected_str = selected_str + compile_lines[program_counter][select_count]
        select_count += 1
      selected = int(selected_str)
      select_count = 0
      selected_str = ""
    program_counter += 1
  compile_lines.clear()
  queries.clear()
  program_counter = 0
  compile_to_count = 0
