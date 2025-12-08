import copy
import heapq


globalp = 0


def myprint(state):
    for row in state:
      string = ""
      for col in row:
        string += str(col)
      print(string)
    print("")



def getkey(state):
    s = ""
    for row in state:
        for col in row:
            s += str(col)
    return s



def read_puzzle(id):
  global globalp
  if id == "puzzle1.txt":
    globalp = 1
  else:
    globalp = 2
  #begin to read
  f = open(id, "r")
  tem = []
  for line in f:
    line = line.strip()
    hehe = []
    for char in line:
      hehe.append(int(char))
    tem.append(hehe)
  check = [False,False,False,False,False]
  for x in range(0,5):
    for y in range(0,4):
      if tem[x][y] == 7:
        tem[x][y] = 4
      else:
        if tem[x][y] == 2 and (not check[0]):
          if y != 3 and tem[x][y] == tem[x][y+1]:
            tem[x][y] = 2
            tem[x][y+1] = 2
          elif x != 4 and tem[x][y] == tem[x+1][y]:
            tem[x][y] = 3
            tem[x+1][y] = 3
          check[0] = True
        if tem[x][y] == 3 and (not check[1]):
          if y != 3 and tem[x][y] == tem[x][y+1]:
            tem[x][y] = 2
            tem[x][y+1] = 2
          elif x != 4 and tem[x][y] == tem[x+1][y]:
            tem[x][y] = 3
            tem[x+1][y] = 3
          check[1] = True
        if tem[x][y] == 4 and (not check[2]):
          if y != 3 and tem[x][y] == tem[x][y+1]:
            tem[x][y] = 2
            tem[x][y+1] = 2
          elif x != 4 and tem[x][y] == tem[x+1][y]:
            tem[x][y] = 3
            tem[x+1][y] = 3
          check[2] = True
        if tem[x][y] == 5 and (not check[3]):
          if y != 3 and tem[x][y] == tem[x][y+1]:
            tem[x][y] = 2
            tem[x][y+1] = 2
          elif x != 4 and tem[x][y] == tem[x+1][y]:
            tem[x][y] = 3
            tem[x+1][y] = 3
          check[3] = True
        if tem[x][y] == 6 and (not check[4]):
          if y != 3 and tem[x][y] == tem[x][y+1]:
            tem[x][y] = 2
            tem[x][y+1] = 2
          elif x != 4 and tem[x][y] == tem[x+1][y]:
            tem[x][y] = 3
            tem[x+1][y] = 3
          check[4] = True 
  return tem


def is_goal(state):
  if state[3][1] == 1 and state[3][2] == 1 and state[4][1] == 1 and state[4][2] == 1:
    return True
  else:
    return False


def get_successors(state):
  successors = []
  twoblank = []
  for x in range(0,5):
    for y in range(0,4):
      if state[x][y] == 0:
        point = (x,y)
        twoblank.append(point)
  #onesquare
  for e in twoblank:
    x = e[0]
    y = e[1]
    if x != 0:
      if state[x-1][y] == 4:
        tem = copy.deepcopy(state)
        tem[x-1][y] = 0
        tem[x][y] = 4
        successors.append(tem)
      elif state[x-1][y] == 3:
        tem = copy.deepcopy(state)
        tem[x-2][y] = 0
        tem[x][y] = 3
        successors.append(tem)
    if x != 4:
      if state[x+1][y] == 4:
        tem = copy.deepcopy(state)
        tem[x+1][y] = 0
        tem[x][y] = 4
        successors.append(tem)
      elif state[x+1][y] == 3:
        tem = copy.deepcopy(state)
        tem[x+2][y] = 0
        tem[x][y] = 3
        successors.append(tem)
    if y != 0:
      if state[x][y-1] == 4:
        tem = copy.deepcopy(state)
        tem[x][y-1] = 0
        tem[x][y] = 4
        successors.append(tem)
      elif state[x][y-1] == 2:
        tem = copy.deepcopy(state)
        tem[x][y-2] = 0
        tem[x][y] = 2
        successors.append(tem)
    if y != 3:
      if state[x][y+1] == 4:
        tem = copy.deepcopy(state)
        tem[x][y+1] = 0
        tem[x][y] = 4
        successors.append(tem)
      elif state[x][y+1] == 2:
        tem = copy.deepcopy(state)
        tem[x][y+2] = 0
        tem[x][y] = 2
        successors.append(tem)
  #twosquares
  x1 = twoblank[0][0]
  y1 = twoblank[0][1]
  x2 = twoblank[1][0]
  y2 = twoblank[1][1]
  if x1 == x2 and y2 - y1 == 1:
    if x1 != 0:
      if state[x1-1][y1] == 2 and state[x1-1][y2] == 2:
        if y1 == 0 or y2 == 3:
          tem = copy.deepcopy(state)
          tem[x1-1][y1] = 0
          tem[x2-1][y2] = 0
          tem[x1][y1] = 2
          tem[x2][y2] = 2
          successors.append(tem)
        elif state[x1-1][y1-1] != 2 or state[x1-1][y2+1] != 2:
          tem = copy.deepcopy(state)
          tem[x1-1][y1] = 0
          tem[x2-1][y2] = 0
          tem[x1][y1] = 2
          tem[x2][y2] = 2
          successors.append(tem)
      elif state[x1-1][y1] == 1 and state[x1-1][y2] == 1:
        tem = copy.deepcopy(state)
        tem[x1-2][y1] = 0
        tem[x2-2][y2] = 0
        tem[x1][y1] = 1
        tem[x2][y2] = 1
        successors.append(tem)
    if x1 != 4:
      if state[x1+1][y1] == 2 and state[x1+1][y2] == 2:
        if y1 == 0 or y2 == 3:
          tem = copy.deepcopy(state)
          tem[x1+1][y1] = 0
          tem[x2+1][y2] = 0
          tem[x1][y1] = 2
          tem[x2][y2] = 2
          successors.append(tem)
        elif state[x1+1][y1-1] != 2 or state[x1+1][y2+1] != 2:
          tem = copy.deepcopy(state)
          tem[x1+1][y1] = 0
          tem[x2+1][y2] = 0
          tem[x1][y1] = 2
          tem[x2][y2] = 2
          successors.append(tem)
      elif state[x1+1][y1] == 1 and state[x1+1][y2] == 1:
        tem = copy.deepcopy(state)
        tem[x1+2][y1] = 0
        tem[x2+2][y2] = 0
        tem[x1][y1] = 1
        tem[x2][y2] = 1
        successors.append(tem)
  if y1 == y2 and x2 - x1 == 1:
    if y1 != 0:
      if state[x1][y1-1] == 3 and state[x2][y2-1] == 3:
        if x1 == 0 or x2 == 4:
          tem = copy.deepcopy(state)
          tem[x1][y1-1] = 0
          tem[x2][y2-1] = 0
          tem[x1][y1] = 3
          tem[x2][y2] = 3
          successors.append(tem)
        elif state[x1-1][y1-1] != 3 or state[x2+1][y2-1] != 3:
          tem = copy.deepcopy(state)
          tem[x1][y1-1] = 0
          tem[x2][y2-1] = 0
          tem[x1][y1] = 3
          tem[x2][y2] = 3
          successors.append(tem)
      elif state[x1][y1-1] == 1 and state[x2][y2-1] == 1:
        tem = copy.deepcopy(state)
        tem[x1][y1-2] = 0
        tem[x2][y2-2] = 0
        tem[x1][y1] = 1
        tem[x2][y2] = 1
        successors.append(tem)
    if y1 != 3:
      if state[x1][y1+1] == 3 and state[x2][y2+1] == 3:
        if x1 == 0 or x2 == 4:
          tem = copy.deepcopy(state)
          tem[x1][y1+1] = 0
          tem[x2][y2+1] = 0
          tem[x1][y1] = 3
          tem[x2][y2] = 3
          successors.append(tem)
        elif state[x1-1][y1+1] != 3 or state[x2+1][y2+1] != 3:
          tem = copy.deepcopy(state)
          tem[x1][y1+1] = 0
          tem[x2][y2+1] = 0
          tem[x1][y1] = 3
          tem[x2][y2] = 3
          successors.append(tem)
      elif state[x1][y1+1] == 1 and state[x2][y2+1] == 1:
        tem = copy.deepcopy(state)
        tem[x1][y1+2] = 0
        tem[x2][y2+2] = 0
        tem[x1][y1] = 1
        tem[x2][y2] = 1
        successors.append(tem)
  return successors



def get_cost(path):
  return len(path) - 1



def get_heuristic(state):
  point = (0,0)
  for x in range(0,5):
    for y in range(0,4):
      if state[x][y] == 1:
          point = (x,y)
  h = abs(4 - point[0]) + abs(2 - point[1])
  return h



def a_star(initial_state):
  visited = set()
  frontier = []
  path = []
  midstate = (initial_state,path)
  f = get_cost(midstate[1]) + get_heuristic(midstate[0])
  pair = (f,midstate)
  heapq.heappush(frontier,pair)
  Expanded = 0
  Generated = 0
  visited.add(getkey(initial_state))
  while len(frontier) != 0:
    tem  = frontier[0][1]
    heapq.heappop(frontier)
    Expanded += 1
    if is_goal(tem[0]):
      tem[1].append(tem[0])
      #write to output
      out = open("puzzle"+str(globalp)+"sol_astar.txt","w+")
      #begin to write
      out.write("Initial state:\n")
      for row in initial_state:
        temstr = ""
        for col in row:
          temstr += str(col)
        out.write(temstr)
        out.write("\n")
      out.write("\n")
      #write other states
      out.write("Cost of the optimal solution: ")
      out.write(str(len(tem[1]) - 1))
      out.write("\n\n")
      out.write("Number of states expanded: ")
      out.write(str(Expanded))
      out.write("\n")
      out.write("Number of states generated: ")
      out.write(str(Generated))
      out.write("\n\n")
      out.write("Optimal solution:")
      out.write("\n")
      i = 0
      for each in tem[1]:
        out.write(str(i))
        i += 1
        out.write("\n")
        for row in each:
          string = ""
          for col in row:
            string += str(col)
          out.write(string)
          out.write("\n")
        out.write("\n")
      out.close()
      return tem
    successors = get_successors(tem[0])
    for each in successors:
      if not(getkey(each) in visited):
        visited.add(getkey(each))
        newpath = copy.deepcopy(tem[1])
        newpath.append(tem[0])
        mid = (each,newpath)
        f = get_cost(mid[1]) + get_heuristic(each)
        pair = (f,mid)
        heapq.heappush(frontier,pair)
        Generated += 1


def bfs(initial_state):
  visited = set()
  frontier = []
  path = []
  midstate = (initial_state,path)
  f = 0
  pair = (f,midstate)
  heapq.heappush(frontier,pair)
  Expanded = 0
  Generated = 0
  visited.add(getkey(initial_state))
  while len(frontier) != 0:
    tem  = frontier[0][1]
    heapq.heappop(frontier)
    Expanded += 1
    if is_goal(tem[0]):
      tem[1].append(tem[0])
      #write to output
      out = open("puzzle"+str(globalp)+"sol_bfs.txt","w+")
      #begin to write
      out.write("Initial state:\n")
      for row in initial_state:
        temstr = ""
        for col in row:
          temstr += str(col)
        out.write(temstr)
        out.write("\n")
      out.write("\n")
      #write other states
      out.write("Cost of the optimal solution: ")
      out.write(str(len(tem[1]) - 1))
      out.write("\n\n")
      out.write("Number of states expanded: ")
      out.write(str(Expanded))
      out.write("\n")
      out.write("Number of states generated: ")
      out.write(str(Generated))
      out.write("\n\n")
      out.write("Optimal solution:\n")
      out.write("\n")
      i = 0
      for each in tem[1]:
        out.write(str(i))
        i += 1
        out.write("\n")
        for row in each:
          string = ""
          for col in row:
            string += str(col)
          out.write(string)
          out.write("\n")
        out.write("\n")
      out.close()
      return tem
    successors = get_successors(tem[0])
    for each in successors:
      if not(getkey(each) in visited):
        visited.add(getkey(each))
        newpath = copy.deepcopy(tem[1])
        newpath.append(tem[0])
        mid = (each,newpath)
        f += 1
        pair = (f,mid)
        heapq.heappush(frontier,pair)
        Generated += 1


def dfs(initial_state):
  visited = set()
  frontier = []
  path = []
  frontier.append(initial_state)
  Expanded = 0
  Generated = 0
  visited.add(getkey(initial_state))
  while len(frontier) != 0:
    tem  = frontier[-1]
    frontier.pop()
    Expanded += 1
    path.append(copy.deepcopy(tem))
    if is_goal(tem):
      #write to output
      out = open("puzzle"+str(globalp)+"sol_dfs.txt","w+")
      #begin to write
      out.write("Initial state:\n")
      for row in initial_state:
        temstr = ""
        for col in row:
          temstr += str(col)
        out.write(temstr)
        out.write("\n")
      out.write("\n")
      #write other states
      out.write("Cost of the solution: ")
      out.write(str(len(path) - 1))
      out.write("\n\n")
      out.write("Number of states expanded: ")
      out.write(str(Expanded))
      out.write("\n")
      out.write("Number of states generated: ")
      out.write(str(Generated))
      out.write("\n\n")
      out.write("Solution:\n")
      out.write("\n")
      i = 0
      for each in path:
        out.write(str(i))
        i += 1
        out.write("\n")
        for row in each:
          string = ""
          for col in row:
            string += str(col)
          out.write(string)
          out.write("\n")
        out.write("\n")
      out.close()
      return tem
    successors = get_successors(tem)
    count = 0
    for each in successors:
      if not(getkey(each) in visited):
        count += 1
        visited.add(getkey(each))
        frontier.append(each)
        Generated += 1
    if count == 0:
      path.pop()

a_star(read_puzzle("puzzle1.txt"))
a_star(read_puzzle("puzzle2.txt"))
