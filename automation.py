import time
import random

start_time = time.time()

print("Welcome")
print("I Will Remind You To Take A 15 Minute Break every 30 Minute")
print("And Help You The Steps To Have Better Eye Sight")

def excerciseSteps():
    start_time = time.time
    print("OK Time To Take A Break")
    print("Step Number 1 Roll Your Eyes from Left To Right 5 Times and Right to Left 5 Times,")
    print("Repeate The Same For 3 Times And Close Your Eyes For 5 Seconds")
    print(".")
    print("Step Number 2 Move Your Eyes Up And Down 10 Times And Move Your Eyes Left And Right For Another 10 Times.")
    print("Remember Not To move Your Neck !")
    print(".")
    print("Step Number 3 Look At The Wall And Blink  Every 30 Seconds For 10 Times")
    print(".")
    print("Step Number 4 Move Your Eyes To The Left For 3 Seconds And Look In Front For A Second")
    print("And Move Your Eyes To The Right For 3 Seconds And Look In Front For A Second, Repeat This 10 Times")
    print(".")
    print("Step Number 5 Start To Move Your Eyes Up and Down As Fast As You Can For 10 Times")
    print("Then Take A 5 Second Break And Repeat This For 10 Times")
    
def main():
    while (True):
        if((time.time()-start_time) >= 5):
            excerciseSteps()

main()