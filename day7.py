instr = []
with open("day7.txt") as f:
  instr = f.readlines()

STEP = 'Step ([A-Z]) must be finished before step ([A-Z]) can begin\.'

steps = {}

import re

for i in instr:
  step = re.search(STEP, i).groups()
  parent = step[0]
  child = step[1]
  if steps.get(parent, None) != None:
    steps[parent].add(child)
  else:
    steps[parent] = set(child)
  if steps.get(child, None) == None:
    steps[child] = set()

def get_all_children(steps):
  result = set()
  for c in steps.values():
    result = result.union(c)
  return result

def find_next_step(steps):
  desired_step = 'ZZ'
  for s in steps.keys():
    cs = get_all_children(steps)
    if s not in cs and s < desired_step:
      desired_step = s
  return desired_step

def find_next_steps(steps):
  next_steps = []
  for s in steps.keys():
    cs = get_all_children(steps)
    if s not in cs:
      next_steps.append(s)
  next_steps.sort()
  return next_steps

parents = {}
for s, cs in steps.items():
  for c in cs:
    if parents.get(c, None) == None:
      parents[c] = set([s])
    else:
      parents[c].add(s)
 
# result = ''
# while steps:
#  next = find_next_step(steps)
#  del steps[next]
#  result += next

# print(result)

from queue import Queue

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
workers = {}
finished = set()
q = Queue()
time = 0
num_workers = 5
addtl_time = 60

print(parents)
while True:
  # decrement time left on the workers
  workers = {s: max(workers[s] - 1, 0) for s in workers.keys()}

  # removed finished jobs from workers and
  # add them to 'finished'
  finished |= set([s for s in workers.keys() if workers[s] == 0])
  workers = {s: workers[s] for s in workers.keys() if s not in finished}
  
  # get next steps that can be done in parallel
  # and add them to the queue
  next_steps = find_next_steps(steps)
  print("next_steps:", next_steps)
  for ns in next_steps:
    if parents.get(ns) == None or parents[ns].issubset(finished):
      q.put(ns)
      del steps[ns]

  # give jobs to workers from the queue
  while not q.empty() and len(workers) < num_workers:
    step = q.get()
    print("step:", step)
    workers[step] = addtl_time + alpha.index(step) + 1

  print("time:", time, "workers:", workers)
  if len(workers) == 0:
    break

  time += 1
  
print(time)
