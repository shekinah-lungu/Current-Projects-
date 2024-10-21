def manage_stage_changes(changes):
  stack = []
  holder = ""
  for i in changes:
    if i[0] == "S":
      new_char = i.split(" ")
      stack.append(new_char[1])
    elif i == "Cancel":
      holder = stack.pop() 
    elif i[0] == "R":
      stack.append(holder)
  return stack

print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))  
print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"])) 
print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"])) 