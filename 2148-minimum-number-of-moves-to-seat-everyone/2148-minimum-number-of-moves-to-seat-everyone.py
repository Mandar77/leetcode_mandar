class Solution(object):
    def minMovesToSeat(self, seats, students):
        n=len(seats)
        seats.sort()
        students.sort()

        c=0

        for i in range (n):
            c += abs(students[i]-seats[i])
        return c
        