"""
Given a robot cleaner in a room modeled as a grid.
Each cell in the grid can be empty or blocked.
The robot cleaner with 4 given APIs can move forward, turn left or turn right. Each turn it made is 90 degrees.
When it tries to move into a blocked cell, its bumper sensor detects the obstacle and it stays on the current cell.
Design an algorithm to clean the entire room using only the 4 given APIs shown below.

interface Robot {
  // returns true if next cell is open and robot moves into the cell.
  // returns false if next cell is obstacle and robot stays on the current cell.
  boolean move();

  // Robot will stay on the same cell after calling turnLeft/turnRight.
  // Each turn will be 90 degrees.
  void turnLeft();
  void turnRight();

  // Clean the current cell.
  void clean();
}
Example:

Input:
room = [
  [1,1,1,1,1,0,1,1],
  [1,1,1,1,1,0,1,1],
  [1,0,1,1,1,1,1,1],
  [0,0,0,1,0,0,0,0],
  [1,1,1,1,1,1,1,1]
],
row = 1,
col = 3

Explanation:
All grids in the room are marked by either 0 or 1.
0 means the cell is blocked, while 1 means the cell is accessible.
The robot initially starts at the position of row=1, col=3.
From the top left corner, its position is one row below and three columns right.
Notes:

The input is only given to initialize the room and the robot's position internally. 
You must solve this problem "blindfolded". 
In other words, you must control the robot using only the mentioned 4 APIs, without knowing the room layout and the initial robot's position.

The robot's initial position will always be in an accessible cell.
The initial direction of the robot will be facing up.
All accessible cells are connected, which means the all cells marked as 1 will be accessible by the robot.
Assume all four edges of the grid are all surrounded by wall.
"""


class Robot:
    def move(self):
        """
        Returns true if the cell in front is open and robot moves into the cell.
        Returns false if the cell in front is blocked and robot stays in the current cell.
        :rtype bool
        """
        pass

    def turnLeft(self):
        """
        Robot will stay in the same cell after calling turnLeft/turnRight.
        Each turn will be 90 degrees.
        :rtype void
        """
        pass

    def turnRight(self):
        """
        Robot will stay in the same cell after calling turnLeft/turnRight.
        Each turn will be 90 degrees.
        :rtype void
        """
        pass

    def clean(self):
        """
        Clean the current cell.
        :rtype void
        """
        pass


class Solution(object):
    def clear_room(self, robot):
        self.visited = set()
        self.robot = robot

    def walk(self, i, j, direction):

        def next_direction(direction):
            self.robot.turnLeft()
            return {"up": "left", "left": "down", "down": "right", "right": "left"}[direction]

        def next_coordinate(i, j, direction):
            return {"left": (i, j - 1), "up": (i - 1, j), "right": (i, j + 1), "down": (i + 1, j)}[direction]

        self.robot.clean()
        self.visited.add((i, j))

        for _ in range(4):
            ii, jj = next_coordinate(i, j, direction)
            if (ii, jj) not in self.visited or self.robot.move():  # 如果下一个坐标没有访问过，且可以到达
                direction = self.walk(ii, jj, direction)  # 前往下一个坐标
                # 从“一个”坐标返回
                direction = next_direction(direction)  
                direction = next_direction(direction)
                self.robot.move()
                # 还原朝向
                direction = next_direction(direction)
                direction = next_direction(direction)
            direction = next_direction(direction)
        return direction
            

