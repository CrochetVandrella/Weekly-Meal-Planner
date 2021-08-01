import random

def Cook():
    taste = ["sweet", "sour", "tangy", "spicy", "grilled", "baked", "fried", "plain"]
    cuisine = ["Mediteranian", "American", "Chinese", "Italian", "Mexican", "Japanese", "Indian"]
    meat = ["pork", "fish", "chicken", "beef"]
    color = ["red", "orange", "yellow", "green", "no", "mixed"]
    side = ["nothing", "mashed potatoes", "white rice", "fried rice", "noodles"]
    food = [taste, cuisine, meat, color, side]

    picked = []
    for everything in food:
        picked.append(random.choice(everything))
    sentence = ", we will have "+ picked[0] +" " + picked[1] +" " + picked[2] +" " + "with "+ picked[3] +" " + "veggies on a bed of " + picked[4]
    return sentence

def TakeOut():
    fastFood = ["Taco Bell", "McDonalds", "Wendys", "Burger King", "Chickfila", "Bojangles", "Chinese takeout", "Arbys", "Kashin (if on weekend)", "DoorDash night"]
    picked = random.choice(fastFood)
    sentence = ", we're eating " + picked
    return sentence
    
def main():
    week = ( "Sunday","Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
    phrase = ""
    for day in week:
        eating = random.randint(1,3)
        if  eating == 1:
            phrase = Cook()
            print("On", day, phrase)
        elif eating == 2:
            phrase = TakeOut()
            print("On", day, phrase)
        else:
            print("On", day, "we're eating leftovers")

main()


