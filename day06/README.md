# Escaping the Maze

## Description
This program provides a solution to guide Reeborg, a robot navigating through a dark maze, to the exit using the right-hand rule algorithm. The right-hand rule instructs Reeborg to always keep its right hand on the wall and follow along the right edge until it reaches the exit.

## Problem Statement
Reeborg is lost in a dark maze with a dead flashlight battery. The task is to guide Reeborg out of the maze using a program that follows the right-hand rule.

## Solution Overview
The provided Python script employs a series of conditional statements within a while loop to navigate Reeborg through the maze. Here's a brief overview of how the solution works:

- Reeborg moves forward as long as the path ahead is clear.
- When Reeborg encounters a wall or a dead end, it turns left to start following along the right edge.
- Inside the main loop:
  - If there's a clear path to the right, Reeborg turns right and moves forward.
  - If the path to the right is blocked but there's a clear path ahead, Reeborg moves forward.
  - If both the right and front paths are blocked, Reeborg turns left, ensuring it continues following the right edge of the maze.
- The program continues executing until Reeborg reaches the exit.

## Credit
- 100 Days of Code: The Complete Python Pro Bootcamp
- Reeborg's world - https://reeborg.ca/
