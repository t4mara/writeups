import copy
import math


class Node:
    def __init__(self, letter, y, x, previous, gscore=math.inf, fscore=math.inf):
        self.letter = letter
        self.previous = previous
        self.x = x
        self.y = y
        self.gscore = gscore
        self.fscore = fscore
        self.visited = False


fajl = open('matrica.txt', 'r')

matrica = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
           [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
           [], [], [], [], [], []]

i = 0
with fajl as file:
    while True:
        temp = file.readline().strip()

        if not temp:
            break

        list = []
        j = 0
        for slovo in temp:
            list.append(Node(slovo, i, j, None))
            j = j + 1

        matrica[i] = list
        i = i + 1

fajl.close()


# for i in range(len(matrica)):
#    for j in range(len(matrica[0])):
#        print(matrica[i][j].letter)

def valid(y, x, matrix):
    if y >= 0 and x >= 0 and x < len(matrix[0]) and y < len(matrix):
        if matrix[y][x].letter != '?':
            return True
    return False


def getvalid_teleport(node, matrix):
    temp = []
    y = node.y
    x = node.x
    if valid(y - 3, x, matrix):
        temp.append(matrix[y - 3][x])
    if valid(y + 3, x, matrix):
        temp.append(matrix[y + 3][x])
    if valid(y, x - 3, matrix):
        temp.append(matrix[y][x - 3])
    if valid(y, x + 3, matrix):
        temp.append(matrix[y][x + 3])
    validni = []

    for el in temp:
        if not inPath(node, el):
            validni.append(el)
    return validni


def getvalid(node, matrix):
    temp = []
    y = node.y
    x = node.x
    if valid(y - 1, x, matrix):
        temp.append(matrix[y - 1][x])
    if valid(y + 1, x, matrix):
        temp.append(matrix[y + 1][x])
    if valid(y, x - 1, matrix):
        temp.append(matrix[y][x - 1])
    if valid(y, x + 1, matrix):
        temp.append(matrix[y][x + 1])
    if valid(y + 1, x + 1, matrix):
        temp.append(matrix[y + 1][x + 1])
    if valid(y - 1, x - 1, matrix):
        temp.append(matrix[y - 1][x - 1])
    if valid(y + 1, x - 1, matrix):
        temp.append(matrix[y + 1][x - 1])
    if valid(y - 1, x + 1, matrix):
        temp.append(matrix[y - 1][x + 1])
    validni = []

    for el in temp:
        if not inPath(node, el):
            validni.append(el)
    return validni


def isTeleport(node):
    if node.x == node.previous.x + 3 or node.x == node.previous.x - 3 or node.y == node.previous.y - 3 or node.y == node.previous.y + 3:
        return True
    return False


def isDiag(node, prev):
    if node.x == prev.x - 1 and node.y == prev.y + 1:
        return True
    elif node.x == prev.x + 1 and node.y == prev.y - 1:
        return True
    elif node.x == prev.x + 1 and node.y == prev.y + 1:
        return True
    elif node.x == prev.x - 1 and node.y == prev.y - 1:
        return True
    return False


def inPath(node1, node2):
    while node1 is not None:
        if node1.previous == node2:
            return True
        node1 = node1.previous
    return False


def brojPrethodnika(node):
    broj = 0
    while node is not None:
        broj = broj + 1
        node = node.previous
    return broj


def h(node, goal):
    dx = abs(float(node.x) - float(goal.x))
    dy = abs(float(node.y) - float(goal.y))
    if isTeleport(node):
        return 30.0 * (dx + dy) + (14.0 - 20.0) * min(dx, dy)
    return 10.0 * (dx + dy) + (14.0 - 20.0) * min(dx, dy)


def azvezdica(start, end, matrix):
    # Manje od 120 poseta
    # Manje od 20 teleportova

    queue = set()
    queue.add(start)
    start.gscore = 0
    start.fscore = 0

    current = None

    while queue:

        current = min(queue, key=lambda x: x.fscore)
        current.visited = True

        brojpos = 0
        brojtele = 0

        savecurrent = copy.deepcopy(current)
        while savecurrent is not None:
            brojpos = brojpos + 1
            savecurrent = savecurrent.previous

        savecurrent2 = copy.deepcopy(current)
        while savecurrent2.previous is not None:
            if isTeleport(savecurrent2):
                brojtele = brojtele + 1
            savecurrent2 = savecurrent2.previous

        print("Trenutni: ")
        print(current.letter)

        if current == end:
            put = []
            while current is not None:
                put.append(current)
                current = current.previous
            return put

        queue.remove(current)

        validni = getvalid(current, matrix)

        print("Valid: ")
        for i in range(len(validni)):
            print(validni[i].letter + " (" + str(validni[i].y) + "," + str(validni[i].x) + ")")

        validni_tele = getvalid_teleport(current, matrix)

        if brojpos < 120:
            for el in validni:
                if isDiag(el, current):
                    tentative = current.gscore + 14
                else:
                    tentative = current.gscore + 10
                if tentative < el.gscore:
                    el.previous = current
                    el.gscore = tentative
                    el.fscore = el.gscore + h(el, end)
                    if el not in queue:
                        queue.add(el)

            if not validni and brojtele < 20:
                for el in validni_tele:
                    tentative = current.gscore + 30
                    if tentative < el.gscore:
                        el.previous = current
                        el.gscore = tentative
                        el.fscore = el.gscore + h(el, end)
                        if el not in queue:
                            queue.add(el)

        print("Queue: ")
        for i in queue:
            print(i.letter + " (" + str(i.y) + "," + str(i.x) + ")")
        print(brojpos)
        print(brojtele)

    print("Failed. Dobili smo:")
    feedback = []
    while current is not None:
        feedback.append(current)
        current = current.previous
    return feedback


printput = azvezdica(matrica[59][0], matrica[0][59], matrica)
flag = ''
printput.reverse()

for i in printput:
    flag = flag + i.letter
    # flag = flag + "(" + str(i.y) + "," + str(i.x) + ") "

print(flag)
