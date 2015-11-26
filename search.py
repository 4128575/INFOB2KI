# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    start = problem.getStartState()
    "list of nodes seen."
    openlist = []
    "list of nodes iterated. (Maybe we don't need this)"
    closedlist = []
    "the list of nodes that constitutes our path."
    lijst = []
    "We slaan naast de positie, actie, cost ook nog het pad op in de vorm (currentnode, action). Dit is nog niet relevant voor de startstate."
    openlist.append(((start,None,0),(0,0)))
    "Code gaat van triples uit."
    while len(openlist) > 0:
        currentnode = openlist[0][0]
        lijst.append((currentnode[0],openlist[0][1],currentnode[1]))
        closedlist.append(currentnode[0])
        if problem.isGoalState(currentnode[0]):
            break
        successors = filter(lambda x: x[0] not in closedlist, problem.getSuccessors(currentnode[0]))
        succ = [(x,currentnode[0]) for x in successors]
        "successors = [node for node in problem.getSuccessors(currentnode[0]) if (node not in closedlist)]"
        del openlist[0]
        if successors == []:
            continue
        "We want to place the successors at the head of the openlist so that if the left most node leads to a deadend, it tries the next successor before travelling up the tree again."
        openlist = succ[::-1] + openlist
    actionlist = []
    pathnode = lijst[-1]
    while True:
        if pathnode[0] == start:
            break
        actionlist = [pathnode[2]] + actionlist
        for elem in lijst:
            if elem[0] == pathnode[1]:
                pathnode = elem
    return actionlist

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    start = problem.getStartState()
    openlist = []
    closedlist = []
    lijst = []
    openlist.append(((start,None,0),(0,0)))
    openlist2 = [start]
    while len(openlist) > 0:
        currentnode = openlist[0][0]
        lijst.append((currentnode[0],openlist[0][1],currentnode[1]))
        closedlist.append(currentnode[0])
        if problem.isGoalState(currentnode[0]):
            break
        successors = filter(lambda x: x[0] not in closedlist and x[0] not in openlist2, problem.getSuccessors(currentnode[0]))
        succ = [(x,currentnode[0]) for x in successors]
        del openlist[0]
        if successors == []:
            continue
        openlist = openlist + succ
        for elem in successors:
            openlist2.append(elem[0])
    actionlist = []
    pathnode = lijst[-1]
    while True:
        if pathnode[0] == start:
            break
        actionlist = [pathnode[2]] + actionlist
        for elem in lijst:
            if elem[0] == pathnode[1]:
                pathnode = elem
    return actionlist


def uniformCostSearch(problem):
    start = problem.getStartState()
    vertexlijst = [start]
    closedlist = []
    distdict = {start: 0}
    prevdict = {start: None}
    while len(vertexlijst) > 0:
        currentnode = vertexlijst[0]
        for node in vertexlijst:
            if distdict[node] < distdict[currentnode]:
                currentnode = node
        closedlist.append(currentnode)
        if problem.isGoalState(currentnode):
            goalnode = currentnode
            break
        successors = problem.getSuccessors(currentnode)
        succs = filter(lambda x: x[0] not in closedlist, successors)
        for elem in succs:
            if elem[0] not in distdict.keys():
                distdict[elem[0]] = float("inf")
                prevdict[elem[0]] = None
        vertexlijst = filter(lambda x: x != currentnode, vertexlijst)
        vertexlijst = [x[0] for x in succs] + vertexlijst
        for elem in successors:
            if elem[0] not in vertexlijst:
                continue
            else:
                altdist = distdict[currentnode] + elem[2]
                if altdist < distdict[elem[0]]:
                    distdict[elem[0]] = altdist
                    prevdict[elem[0]] = (currentnode,elem[1])
    path = []
    node = goalnode
    while prevdict[node] != None:
        path = [prevdict[node]] + path
        node = prevdict[node][0]
    actionlist = [x[1] for x in path]
    return actionlist

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    start = problem.getStartState()
    closedlist = []
    openlist = [start]
    camefrom = {}
    gscore = {start: 0}
    fscore = {start: gscore[start] + heuristic(start,problem)}
    while len(openlist) > 0:
        currentnode = openlist[0]
        for node in openlist:
            if fscore[node] < fscore[currentnode]:
                currentnode = node
        if problem.isGoalState(currentnode):
            goalnode = currentnode
            break
        openlist = filter(lambda x: x != currentnode, openlist)
        closedlist.append(currentnode)
        successors = problem.getSuccessors(currentnode)
        succs = [x[0] for x in successors]
        for elem in successors:
            if elem[0] in closedlist:
                continue
            tentativegscore = gscore[currentnode] + elem[2]
            if elem[0] not in openlist:
                openlist.append(elem[0])
            else:
                if tentativegscore >= gscore[elem[0]]:
                    continue
        
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
