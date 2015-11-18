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
    print "Start:", start
    print "Successors 1: ", problem.getSuccessors(start)
    s1 = problem.getSuccessors(start)[0][0]
    print "Successors 2: ", problem.isGoalState(s1), problem.getSuccessors(s1)
    s2 = problem.getSuccessors(s1)[1][0]
    print "Successors 3: ", problem.isGoalState(s2), problem.getSuccessors(s2)
    s3 = problem.getSuccessors(s2)[1][0]
    print "Successors 4: ", problem.isGoalState(s3), problem.getSuccessors(s3)
    s4 = problem.getSuccessors(s3)[0][0]
    print "Successors 5: ", problem.isGoalState(s4), problem.getSuccessors(s4)
    s5 = problem.getSuccessors(s4)[1][0]
    print "Successors 6: ", problem.isGoalState(s5), problem.getSuccessors(s5)
    s6 = problem.getSuccessors(s5)[1][0]
    print "Successors 7: ", problem.isGoalState(s6), problem.getSuccessors(s6)
    s7 = problem.getSuccessors(s6)[1][0]
    print "Successors 8: ", problem.isGoalState(s7), problem.getSuccessors(s7)
    s8 = problem.getSuccessors(s7)[1][0]
    print "Successors 9: ", problem.isGoalState(s8), problem.getSuccessors(s8)

    s9 = problem.getSuccessors(s6)[0][0]
    print "Successors 11: ", problem.isGoalState(s9), problem.getSuccessors(s9)
    
    "list of nodes seen."
    openlist = []
    "list of nodes iterated. (Maybe we don't need this)"
    closedlist = []
    "the list of nodes that constitutes our path."
    path = []
    openlist.append((start,None,0))
    "Code gaat van triples uit."
    while len(openlist) > 0:
        currentnode = openlist[0]
        path.append(currentnode)
        closedlist.append(currentnode[0])
        if problem.isGoalState(currentnode[0]):
            break
        print "TEST: ", currentnode
        successors = filter(lambda x: x[0] not in closedlist, problem.getSuccessors(currentnode[0]))
        "successors = [node for node in problem.getSuccessors(currentnode[0]) if (node not in closedlist)]"
        print successors
        del openlist[0]
        if successors == []:
            for node in problem.getSuccessors(currentnode[0]):
                succs = filter(lambda x: x[0] not in closedlist, problem.getSuccessors(currentnode[0]))
        print successors
        del openlist[0]
        if successors == []:
            openlist.append(path[len(path)-2])
            path = path[:1]
            "Hier dingen uit path verwijderen."
            continue
        "We want to place the successors at the head of the openlist so that if the left most node leads to a deaden, it tries the next successor before travelling up the tree again."
        openlist = successors + openlist
    print path
    actionlist = [node[1] for node in path]
    util.raiseNotDefined()
    return actionlist

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
