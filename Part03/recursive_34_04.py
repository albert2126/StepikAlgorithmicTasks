"""
Task: https://stepik.org/lesson/862119/step/4?unit=866156

The Towers of Hanoi puzzle (try it online!) consists of three pegs, which we label from left to right as 1, 2, and 3,
and a number of disks of decreasing radius, each with a hole in the center. The disks are initially stacked on the left
peg (peg 1) so that smaller disks are on top of larger ones. The game is played by moving one disk at a time between
pegs. You are only allowed to place smaller disks on top of larger ones, and any disk may go onto an empty peg.
The puzzle is solved when all of the disks have been moved from peg 1 to peg 3.
Try our interactive puzzle Hanoi Towers to figure out how to move all disks from one peg to another.

HanoiTowers(n,fromPeg,toPeg)
     if n=1:
        output “Move disk from peg \text{fromPeg}fromPeg to peg \text{toPeg}toPeg”
        return
     unusedPeg←6−fromPeg−toPeg
     HanoiTowers(n−1,fromPeg,unusedPeg)
     output “Move disk from peg \text{fromPeg}fromPeg to peg \text{toPeg}toPeg”
     HanoiTowers(n−1,unusedPeg,toPeg)

"""