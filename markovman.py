#!/usr/bin/env python3

import pprint
import sys
import random

TRAINING_DATA = [
    "Florida Man Shooting at Target in Backyard Hits Neighbor Sitting at Dining Room Table",
    "Florida Man Doesn't Get Straw, Attacks McDonald's Employee",
    "Florida Man Arrested at Mar-a-lago, Says He Came to Talk to Trump About His $6.3 Trillion",
    "Florida Man Arrested After Hitting Dad with Pizza Because He Was Mad He Helped Birth Him",
    "Florida Man Killed Ex-Girlfriend While Trying to Get Rid of the Devil",
    "Florida Man Intentionally Drove Ferrari 360 Into Ocean At Top Speed",
    "Florida Man Denies Syringes Found in Rectum Are His",
    "Florida Man Arrested After Argument Over Cheesesteak",
    "Florida Man Accused of Burning Son to Teach Him Lesson About Fire",
    "Florida Man Allegedly Fooled Family Into Believing Murdered Wife Was Still Alive",
    "Florida Man Chews Up Police Car Seat After Cocaine Arrest",
    "Florida Man Finds Boa Constrictor in His Car Engine",
    "Florida Man Harasses People in the Park",
    "Florida Man Threatens to Kill Man With Kindness, Uses Machete Named Kindness"
    "Florida Man Causes Highway Crash, Steals Good Samaritan’s Truck Who Stopped To Help",
    "Florida Man Who Drove Ferrari Into Water Said, Jesus Told Him To",
    "Florida Man Accused of Luring Kids Tells Cops He Can't Recall As He Drinks 18-20 Beers Before Talking to Children",
    "Florida Man Accused Of Throwing Chair Across Steak 'n Shake",
    "Florida Man And Woman Run Over By Patrol Car While Lying in Road to Watch Eclipse",
    "Florida Man Caught Exposing Himself in Walmart Pillow Aisle",
    "Florida Man Beat, Pepper Sprayed Mom Because She Was a Narcissist",
    "Florida Man Driving Unregistered ATV Ran Over Dog",
    "Florida Man Finds a WWII Grenade, Places It in His Truck, Drives to Taco Bell",
    "Florida Man Learns Hard Way He Stole Laxatives, Not Opioids",
    "Florida Man Accused of Robbing Chinese Restaurant at Finger Point",
    "Florida Man Spent Weeks in Jail for Heroin That Was Actually Detergent",
    "Florida Man Attacked Sister, Bit Cop After Someone Touched His Cigar",
    "Florida Men Accused of Smearing Feces on Crunch Fitness Bathroom, Sauna",
    "Florida Man Tried to Run Over Son Because He Didn't Want to Take a Bath",
    "Florida Man Dances Through DUI Sobriety Test",
    "Florida Man Caught on Camera Licking Doorbell",
    "Florida Man Throws Pizza Slice at Mom During Argument",
    "Florida Man Arrested for Allegedly Throwing Cookie at Girlfriend",
    "Florida Man Sprayed Other Inmates with Urine",
    "Florida Man Who Allegedly Threatened Family with Coldplay Lyrics Ends Standoff After SWAT Promises Him Pizza",
    "Florida Man Sentenced to 10 Days For Dragging Shark Behind Boat",
    "Florida Man Rescues Grandma Floating Away on Ice Throne",
    "Florida Man Arrested After Fight About Tupac Shakur",
    "Florida Man Arrested with Cocaine-Stuffed Lunchables",
    "Florida Man Throws Toilet Through School Board Building Window in Illinois, Is Arrested Sitting on Another",
    "Florida Man Charged with Death of Grandma Found in Maggot-Infested Bed",
    "Florida Man Actually Tried to Board a Flight to Orlando With a Fake Grenade",
    "Florida Man Goes Viral for Crushing Dance Routine to Post Malone Song",
    "Florida Man Arrested After Fight Over Beachfront Wedding Pictures",
    "Florida Man Who Attacked McDonald's Worker Over Straw Sentenced to Jail",
    "Florida Man Accused of Intentionally Pressure Washing His Neighbor",
    "Florida Man in Spider-Man Mask Steals Bottles From Liquor Store",
    "Florida Man Hit Pregnant Girlfriend With Bag of Tortilla Chips Over Baby's Paternity",
    "Florida Man Finds Bright Green Iguana in Toilet, Calls 911",
    "Florida Man Breaks into Store, Flips off Security Camera",
    "Florida Man Who Burned Caged Cat, Fed it to Dogs Gets No Jail Time",
    "Florida Man Accused of Throwing Pancake Batter at Woman Arrested",
    "Florida Man Accused of Exposing Himself to Sammy's Exotic Dancer",
    "Florida Man Shoved Woman Because He Wanted to Eat Egg Rolls in Her House",
    "Florida Man Googles Self to Find Out Which Florida Man He Is",
    "Florida Man Steals Hot Air Balloon From Indiana During Florida Man Challenge",
    "Florida Man Electrocuted Trying to Remove Bird From Power Line",
    "Florida Man Calls 911 to Get Out of His Fast Food Shift, Cops Say",
    "Florida Man Job Application Led to His Arrest in a 1998 Cold Case",
    "Florida Man Shoots and Kills Pet Zebra He Did Not Have a Permit For After Animal Escapes",
    "Florida Man Accused of Attacking Mom When She Wouldn't Dress his Mannequin",
    "Florida Man Arrested For Stealing Nearly $6,000 Worth of Sunglasses"
]

if len(sys.argv) < 2:
    print("USAGE: [{}] <number of sentences> [debug]".format(sys.argv[0]))
    exit(-1)
debug = "debug" in sys.argv
num = int(sys.argv[1])

for i in range(len(TRAINING_DATA)):
    TRAINING_DATA[i] = TRAINING_DATA[i].lower()
    TRAINING_DATA[i] += "."

DATA_SET = {}
for headline in TRAINING_DATA:
    for i, word in enumerate(headline.split()):
        if(i < len(headline.split()) - 1):
            if word in DATA_SET:
                if (headline.split())[i+1] in DATA_SET[word]:
                    DATA_SET[word][(headline.split())[i+1]] += 1
                else:
                    DATA_SET[word][(headline.split())[i+1]] = 1
            else:
                DATA_SET[word] = {}
                DATA_SET[word][(headline.split())[i+1]] = 1

pp = pprint.PrettyPrinter(indent=4)
if debug:
    print("TRAINING_DATA:")
    pp.pprint(TRAINING_DATA)
    print("DATA SET:")
    pp.pprint(DATA_SET)

for i in range(num):
    sentence = []
    sentence.append("florida")
    sentence.append("man")
    i = 2
    cont = True
    while(cont):
        summ = 0
        for k, v in DATA_SET[sentence[i - 1]].items():
            summ += v
        choice = random.randint(0, summ)
        j = 0
        newsumm = 0
        for k, v in DATA_SET[sentence[i - 1]].items():
            if newsumm == choice:
                break
            newsumm += v
            j += 1
        j -= 1
        if('.' in list(DATA_SET[sentence[i - 1]].keys())[j]):
            cont = False
        sentence.append(list(DATA_SET[sentence[i - 1]].keys())[j])
        i += 1
    sentence[0] = "Florida"
    print(" ".join(sentence))