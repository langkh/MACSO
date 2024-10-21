import math

'''
Recently, Alisa learned about an interesting card game from Boris that tests memory and attention at the Russian School of Mathematics (RSM): 1. The first player shuffles two identical decks of cards, then removes one card from the combined set and gives the rest to the second player. 2. The second player must tell the first which card was removed.

Alisa enjoyed this game so much that she decided to play it with you during a break at RSM. She has already completed the first step of the game and handed you the set. Your task is to tell Alisa which card she removed.

Input
An odd number 0<n<8⋅106
 is given — the number of cards in the set. Then n
 integers 0≤ai≤109
 are given — the numerical characteristics of the cards in the set.

Output
Print one number — the numerical characteristic of the card Alisa removed.

Examples
InputCopy
5
9 11 8 9 8
OutputCopy
11
InputCopy
7
14 9 18 14 18 9 15
OutputCopy
15
Note
Second example:

1. The first player took one card out, and now in the total pile, there are cards with numbers 14, 9, 18, 14, 18, 9, 15.

2. Since you know that initially there were two identical decks, you can disregard cards with numbers that are present an even number of times. There are two of each: 14s, 9s, and 18s, and only one card with the number 15.

3. Now, you have only 15 left in the pile, since it appears only once ⟶
 this is your answer.

 '''
def cards():
    input()
    cards = input()
    cards = cards.split()
    
    #cards.pop(0)

    for i in cards:
        if cards.count(i) ==1:
            print(int(i))
        


'''
Andrew has always dreamed of becoming a programming Olympiad champion and winning all possible competitions, but he was always stopped by geometry problems, which prevented him from becoming a champion. Now, in his senior year at Brookline High School, at the very last Olympiad, he once again encountered a geometry problem. But this time, skipping it isn't an option — if he doesn't solve it, he won't make the podium and will lose his chance for guaranteed admission to either MIT or Harvard. The stakes couldn't be higher — failure would mean competing against thousands of applicants. You must help him!

This time, the organizers have come up with a very tricky problem: in the coordinate plane, two points are given. The first point is the center of a square, and the second is the center of one of the sides of this square. Around this square, the clever organizers drew a circle, and around this circle, they drew another square. What is the length of the side of the outer square?

Input
The first line contains the coordinate x
 of the first point. The second line contains the coordinate y
 of the first point. Similarly, the next two lines specify the second point. It is guaranteed that the coordinates of the points are distinct, are natural numbers, and are in the range: 0≤x1,y1,x2,y2≤107
.

Output
Output one number — the length of the side of the outer square with a precision of at least five decimal places.

Example
InputCopy
0
0
1
1
OutputCopy
2.8284271247461903
'''

def squares():
    coordOne = []
    coordTwo = []
    for i in range(2):
        num = input()
        coordOne.append(int(num))
    for i in range(2):
        num = input()
        coordTwo.append(int(num))

    dist = math.dist(coordOne,coordTwo)
    sideLen = math.sqrt(2)*dist*2    

    
    print(format(sideLen, '.6f'))
'''
E. Bitcoin Mining Detection
time limit per test2 seconds
memory limit per test256 megabytes
Airbnb apartment owner in Massachusetts is investigating illegal Bitcoin mining operations. Bitcoin mining is notorious for its high energy consumption, and one way to detect mining activities is to analyze the electricity usage over time. These energy consumptions are not good for our environment so the owner wants to find out who did it.

You are given an array electricity
 with length N
 where each element represents the amount of electricity (in kilowatt-hours) consumed during a certain period (it is the same for each of them). A suspected Bitcoin miner will have periods of consistently high electricity usage as they run their mining operations, which results in contiguous stretches of high electricity consumption.

Your task is to identify the largest (by the area) rectangular block (if you imagine the array electricity[] as a histogram, which is shown in the picture) of time where the electricity consumption was consistent, potentially indicating mining activity. The height of the rectangle represents the electricity usage during that time, and the width represents the number of contiguous periods.


Input
The input consists of multiple lines:

The first line contains a natural number N
 (1≤N≤100,000)
 – the number of measurments of the electricity;

The next N lines each contain one integer x
 (1≤N≤109)
 representing the amount of electricity consumed during the Nth time period;

Output
Return the numerical value of the area of the largest rectangular block in the histogram representing array electricity.

Examples
InputCopy
5
1 3 3 1 5
OutputCopy
6
InputCopy
7
60 20 50 40 10 50 60
OutputCopy
100

Note



Example:


'''
def bitcoin():
    len = int(input())
    nums = input()
    nums = nums.split()
    elecList = []
    for i in nums:
        elecList.append(int(i))


    diffHeights = []

    for i in range(1,len):
        if elecList[i-1]> elecList[i]:
            diffHeights.append(elecList[i])
            i+=1
        else:
            diffHeights.append(elecList[i-1])

    sortedHeights = list(set(diffHeights))
    sortedHeights.sort(reverse=True)
    
    areas = []
    
    for height in sortedHeights:
        width = diffHeights.count(height)+1

        area = height *width
        areas.append(area)

    print(max(areas))
    

'''
Hikers plan to conquer Mountain Washington, the highest peak in the Northeastern United States, located in New Hampshire's White Mountain National Forest. The mountain and its trail system can be represented as a graph tree, where nodes correspond to trail junctions, and edges represent hiking paths between them. Each edge (u,v)
 indicates that junction u
 is at a higher elevation than junction v
. The junction numbered 1 represents the summit of Mount Washington.

Junctions with no downward paths represent trailheads at the base of Mount Washington, where hikers can begin their trip. There are n
 junctions in total across the mountain.

Recently, the hikers received a weather forecast from the Mount Washington Observatory, known for its extreme and rapidly changing weather conditions. The forecast predicts severe weather events at q
 locations. These weather events, which could include sudden snowstorms, hurricane-force winds, or dense fog, occur near junctions. Once a severe weather event begins at one junction, it affects all lower-elevation areas that could be reached from that starting point. This means that all junctions below the node where the severe weather began, as well as the junction itself where it started, become too dangerous for hikers to pass through.

The task is to determine the number of trailheads at the base of Mount Washington from which hikers will be able to safely reach the summit, taking into account the information about junctions, trails, and locations of severe weather events. This calculation is crucial for hikers to plan their routes and for park rangers to manage safety on one of the most dangerous small mountains in the world.

Input
The first line of input contains the number n(2≤n≤105)
 — the number of trail junctions on Mount Washington.

Each of the next n−1
 lines describes a trail on the mountain. These lines contain numbers ui, vi(1≤ui, vi≤n, ui≠vi)
. It is guaranteed that the resulting graph represents a rooted tree with the root at junction number 1 (the summit of Mount Washington).

The next line contains the number q(1≤q≤n)
 — the number of junctions where severe weather events are expected.

Each of the following q
 lines contains a number ti(0≤ti≤n)
 — a junction near which a severe weather event is expected. It is guaranteed that all ti
 are distinct.

Output
Print out a single integer — the number of trailheads at the base of Mount Washington from which hikers can safely reach the summit after considering all the severe weather events.

Example
InputCopy
5
1 2
1 3
2 4
2 5
2
2
4
OutputCopy
1


0
4
3
4
1
0

'''
bitcoin()