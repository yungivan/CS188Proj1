# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util
from game import Directions
s=Directions.SOUTH
w=Directions.WEST
n=Directions.NORTH
e=Directions.EAST

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def GeneralSearch(problem, fringe):
    closed = set()
    #fringe = util.Stack()
    tup = (problem.getStartState(), [])
    fringe.push(tup)
    while True:
        if fringe.isEmpty():
            return []
        state, path = fringe.pop()
        if problem.isGoalState(state):
            #print "found path~~~~~~"
            #print path
            return path
        if state not in closed:
            closed.add(state)
            for child in problem.getSuccessors(state):
                pathalter = list(path)
                next_state, direction, cost = child
                pathalter.append(direction)
                tup = (next_state, pathalter)
                fringe.push(tup)

def GeneralSearchWithCost(problem, fringe):
    closed = set()
    #fringe = util.Stack()
    tup = (problem.getStartState(), [], 1)
    fringe.push(tup, 1)
    while True:
        if fringe.isEmpty():
            return []
        node = fringe.pop()

        state, path, parentcost = node
        #print "~~~~~~~~~~~"
        #print path
        #print "~~~~~~~"
        if problem.isGoalState(state):
            #print "found path~~~~~~"
            #print path
            return path
        if state not in closed:
            closed.add(state)
            for child in problem.getSuccessors(state):
                aggcost = parentcost
                pathalter = list(path)
                next_state, direction, cost = child
                pathalter.append(direction)
                tup = (next_state, pathalter, aggcost+cost)
                #print next_state, cost
                fringe.push(tup, aggcost+cost)

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())

    fringe keeps track of tuple to record state and path
    """
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()
    return GeneralSearch(problem, util.Stack())

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()
    return GeneralSearch(problem, util.Queue())

def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()
    return GeneralSearchWithCost(problem, util.PriorityQueue())


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
