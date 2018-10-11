import math

# return volume of a ballon given its radius
def balloonVolume(radius):
    return (4/3)*math.pi*pow(radius, 3)
    
# return total volume of multiple balloons
def totalBalloonVolume(balloons):
    for i in range(0, len(balloons)):
        total += ballonVolume(balloons[i])

# returns the total volume of multiple balloons that have not been popped
# given a list of indices of popped balloons
def totalBalloonVolumeAfterPopped(balloons, popped):
    poppedVolume = 0
    for i in range(0, len(balloons)):
        if popped.count(i) > 0:
            poppedVolume = balloonVolume(balloons[i]) 
    return totalBalloonVolume(balloons) - poppedVolume
        

def main():
    balloonRadii = [4, 5, 9, 2, 10,]
    popped = [2, 4]
    print(totalBalloonVolume(balloonRadii))
    print(totalBalloonVolumeAfterPopped(balloonRadii, popped))
    
