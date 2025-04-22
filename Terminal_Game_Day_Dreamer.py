#Terminal Game Project

# Game Title in ASCII art

print("DDDDD     AAAAA   Y   Y         DDDDD   RRRRR   EEEEE  AAAAA  M   M  EEEEE  RRRRR")
print("D    D   A     A   Y Y          D    D  R   R   E      A     A MM MM  E      R   R")
print("D    D   AAAAAAA    Y     - -   D    D  RRRRR   EEEE   AAAAAAA M M M  EEEE   RRRRR")
print("D    D   A     A    Y           D    D  R  R    E      A     A M   M  E      R  R")
print("DDDDD    A     A    Y           DDDDD   R   R   EEEEE  A     A M   M  EEEEE  R   R")

#Libraries
import random

#Variables
Energy = 100
SleptLate = False
MissedBreakfast = False
Hungry = False
SugarOs = False
NewsAnxiety = False
RadioAnnoyed = False
BossAngry = False
LiarLiarPantsOnFire = False
Berated = False
ThrownCereal = False
MovieSpoiled = False
JesseFriendship = False
rain = False
birds = False
NightmareBoss = False
NightmarePolitician = False
NightmareTwoHead = False
NightmareSelf = False
NightmareCustomer=False
NightmareThreeHead=False
BossName="Nightmare"
BossHealth = 100

#Game Intro
print("")
print("Welcome to Day-Dreamer ")
print("Before the game starts, we have a simple question for you...")
print("")
print("what is your name?")
name=input("Enter your name: ")
print(f"Buzz! Buzz! Buzz! Your alarm clock is going off {name}") 
print("What will you do?")
#Q1 - Start of Day
print("")
print("1. Wake up and get out of bed")
print("2. Ignore the alarm and go back to sleep")
answer1=int(input("Enter 1 or 2: "))
while answer1 != 1 and answer1 != 2:
    print("Please enter a valid answer")
    answer1=int(input("Enter 1 or 2: "))
if answer1==1:
    print("You wake up and get out of bed, ready for a long day of work.")
elif answer1==2:
    print("You ignore the alarm and sleep in for an extra hour. You feel refreshed...But you are running late!")
    Energy += 25
    SleptLate = True

#Q2 - Morning Start (Slept Late)
print("") 
if SleptLate == True:
    print("There's no time for breakfast. You rush out the door and head to work.")
    MissedBreakfast = True
#Q2 - Morning Start (Did not sleep late)
if SleptLate == False:
    print("It's breakfast time! What will you eat?")
    print("1. Sugary cereal")
    print("2. Eggs and bacon")
    print("3. Just a cup of coffee")
    answer2=int(input("Enter 1, 2 or 3: "))
    while answer2 != 1 and answer2 != 2 and answer2 != 3:
        print("Please enter a valid answer")
        answer2=int(input("Enter 1, 2 or 3: "))
    if answer2==1:
        print("")
        print("You pour yourself a big bowl of Sugar-Os. While it's not the healthiest choice, it brings back a rush of memories from your childhood. You feel nostalgic. ")
        print("The Sugar-Os jingle from an old commercial plays in your head: 'You can't say no to Sugar-Os!'")
        Energy += 10
        SugarOs = True
    elif answer2==2:
        print("")
        print("You make yourself eggs and bacon. A breakfast classic.")
        print("You feel full and ready to take on the day.")
        Energy += 30
    elif answer2==3:
        print("")
        print("You drink a cup of coffee. It's not much, but it gives you a little boost.")
        print("'That's a damn good cup of coffee!' you say to yourself.")
        print("You feel a little more awake. But a little bit hungry")
        Energy += 15
        Hungry = True
#Q3 Morning Commute
print("")
print("You head out the door, and get into your car.")
print("As you turn your car on, you have an important decision to make.")
print("What radio station will you listen to?")
print("1. Tune into the News")
print("2. Listen to some music!")
answer3=int(input("Enter 1 or 2: "))
while answer3 != 1 and answer3 != 2:
    print("Please enter a valid answer")
    answer3=int(input("Enter 1 or 2: "))
if answer3==1:
    print("")
    print("You tune into the morning news show. The hosts are talking about the latest headlines.")
    print("A local politician has plans to make things worse for everyone.")
    print("You feel a sense of dread as they discuss the state of the world.")
    print("You pull into work.")
    NewsAnxiety = True
if answer3==2:
    print("")
    print("You feel like listening to some tunes! You tune the dial to your favorite station.")
    print("You catch the tail end of a song you love. The station breaks for commercials.")
    print("You change the station. Another commercial.")
    print("You change the station again. Yet another commercial.")
    print("You change the station for the last time. Your favourite song is starting!")
    print("...But you have arrived at work and have to turn off the radio.")
    print("You feel a little annoyed")
    RadioAnnoyed = True

#Q4 - Work
print("")
if SleptLate == True:
    print("You arrive at work and head straight to your desk.")
    print("A supervisor is waiting for you.")
    print("You're late! He says angrily. What's your excuse?")
    print("1. I overslept")
    print("2.[Lie] I was stuck in traffic.")
    print("3.[Lie] I'm actually early. I switched shifts with Wayne.")
    answer4=int(input("Enter 1, 2 or 3: "))
    while answer4 != 1 and answer4 != 2 and answer4 != 3:
        print("Please enter a valid answer")
        answer4=int(input("Enter 1, 2 or 3: "))
    if answer4==1:
        print("Your supervisor is annoyed, but appreciates your honesty. He tells you to get to work.")
    if answer4==2:
        print("Your supervisor can tell you're lying. He threatens to write you up, and tells you to get to work.")
        BossAngry = True
    if answer4==3:
        print("Your supervisor apologizes for being rude.")
        print("You get to work.")
        print("You feel a little guilty for lying.")
        LiarLiarPantsOnFire = True
if SleptLate == False:
    print("")
    print("You arrive at work and head straight to your desk.")
    print("Your supervisor is waiting for you.")
    print(f"Great to see you {name}! We have a lot of work to do, but I know you can handle it.")
    print("You get to work.")

#Q5 - Dealing with a Customer
print("")
print("A customer approaches you with a complaint.")
print("They are upset about a product they bought.")
print("They claim 'you' sold them a 'defective' product.")
print("They then pull out a nearly empty box of Sugar-Os cereal. Clealry they ate most of it")
#Q5 - Did Not Eat Sugar-Os
if SugarOs == False:
    print("")
    print("1. You want to return a box of cereal you've clearly eaten most of?")
    print("2. [Accept the return] 'Sure, I'll give you a refund.'")
    print("3. [Deny the return] 'Sorry, but I can't give you a refund for that.'")
    answer5=int(input("Enter 1, 2, or 3: "))
    while answer5 != 1 and answer5 != 2 and answer5 != 3:
        print("Please enter a valid answer")
        answer5=int(input("Enter 1, 2, or 3: "))
    if answer5==1:
       print("The customer says, 'Duh, that's why I'm here, genius! I swear, they hire some real idiots here.'")
       Berated = True
#Berated
    if Berated == True and SugarOs == False:
            print("")
            print("1. [Accept the return] 'Sure, I'll give you a refund.'")
            print("2. [Deny the return] 'Sorry, but I can't give you a refund for that.'")
            answer5=int(input("Enter 1 or 2: "))
            while answer5 != 1 and answer5 != 2:
                print("Please enter a valid answer")
                answer5=int(input("Enter 1 or 2: "))
            if answer5==1:
                print("")
                print("You give the customer a refund.")
                print("They leave, satisfied.")
                print("You feel a little bad for accepting it.")
                Energy -= 5
            if answer5==2:
                print("")
                print("You deny the return.")
                print("The customer gets angry and starts yelling at you.")
                print("They throw the cereal box at you.")
                print("It hits you in the face.")
                print("Security escorts the customer out of the store.")
                ThrownCereal = True

#Q5 - Ate Sugar-Os
else:
   print("")
   print("1. You want to return a box of cereal you've clearly eaten most of?")
   print("2. [Accept the return] 'Sure, I'll give you a refund.'")
   print("3. [Deny the return] 'Sorry, but I can't give you a refund for that.'")
   print("4. [Sing the Sugar-Os jingle] 'You can't say no to Sugar-Os!'")
   print("")
   answer5=int(input("Enter 1, 2, 3 or 4: "))
   while answer5 != 1 and answer5 != 2 and answer5 != 3 and answer5 != 4:
        print("Please enter a valid answer")
        answer5=int(input("Enter 1, 2, 3 or 4: "))
if answer5==1:
       print("The customer says, 'Duh, that's why I'm here, genius! I swear, they hire some real idiots here.'")
       Berated = True
#Sugar-Os and Berated
if Berated == True and SugarOs == True:
    print("1. [Accept the return] 'Sure, I'll give you a refund.'")
    print("2. [Deny the return] 'Sorry, but I can't give you a refund for that.'")
    print("3. [Sing the Sugar-Os jingle] 'You can't say no to Sugar-Os!'")
    answer5=int(input("Enter 1, 2, or 3: "))
    while answer5 != 1 and answer5 != 2 and answer5 != 3:
        print("Please enter a valid answer")
        answer5=int(input("Enter 1, 2, or 3: "))
if answer5==1:
    print("You give the customer a refund.")
    print("They leave, satisfied.")
    print("You feel a little bad for accepting it.")
    Energy -= 5
if answer5==2:
    print("You deny the return.")
    print("The customer gets angry and starts yelling at you.")
    print("They throw the cereal box at you.")
    print("It hits you in the face.")
    print("Security escorts the customer out of the store.")
    ThrownCereal = True
if answer5==3:
    print("You start singing the Sugar-Os jingle.")
    print("The customer smiles, and sings along with you.")
    print("You both sing: 'You can't say no to Sugar-Os!' Oh you can't say no no no! You need them woah woah woah!")
    print("The customer suddenly forgets why they are there, and leave, satisfied.")
    Energy += 50
#else:
   #print("1. You want to return a box of cereal you've clearly eaten most of?")
   #print("2. [Accept the return] 'Sure, I'll give you a refund.'")
   #print("3. [Deny the return] 'Sorry, but I can't give you a refund for that.'")
   #answer5=int(input("Enter 1, 2, or 3: ")) 
   #while answer5 != 1 and answer5 != 2 and answer5 != 3:
          #print("Please enter a valid answer")
          #answer5=int(input("Enter 1, 2, or 3: "))
#if answer5==1:
       #print("The customer says, 'Duh, that's why I'm here, genius! I swear, they hire some real idiots here.'")
       #Berated = True
#if Berated == True and SugarOs == True:
    #print("1. [Accept the return] 'Sure, I'll give you a refund.'")
    #print("2. [Deny the return] 'Sorry, but I can't give you a refund for that.'")
    #answer5=int(input("Enter 1 or 2: "))
    #while answer5 != 1 and answer5 != 2:
        #print("Please enter a valid answer")
        #answer5=int(input("Enter 1 or 2: "))
#if answer5==1:
    #print("You give the customer a refund.")
    #print("They leave, satisfied.")
    #print("You feel a little bad for accepting it.")
    #Energy -= 5
#if answer5==2:       
    #print("You deny the return.") 
    #print("The customer gets angry  and starts yelling at you.")
    #print("They throw the cereal box at you.")
    #print("It hits you in the face.")
    #print("Security escorts the customer out of the store.")
    #ThrownCereal = True

#Q6 - Lunch with Coworkers
print("")
print("After dealing with a difficult customer, it's finally time for lunch.")
if Hungry == True:
    print("You are starving!")
print("You head to the break room, and sit down wih your coworkers.")
print("They are talking about a new horror movie that came out: 'Midnight Massacre.'")
print(f"Your co-worker Jesse turns to you and asks: 'Hey {name}, are you going to it?")
print("")
print("1. 'Yeah, I love horror movies!'")
print("2. 'No...horror movies aren't for me.'")
print("") 
answer6=int(input("Enter 1 or 2: "))
while answer6 != 1 and answer6 != 2:
    print("Please enter a valid answer")
    answer6=int(input("Enter 1 or 2: "))
if answer6==1:
    print("You tell Jesse that you love horror movies.")
    print("Jesse says: 'Awesome! You'll have to tell me about the part where the killer is actually...")
    print("Jesse proceeds to spoil the entire movie for you.")
    print("You feel a little annoyed.")
    Energy -= 10
    MovieSpoiled = True
if answer6==2:
    print("You tell Jesse that you don't like horror movies.")
    print("Jesse says: 'Ahh, are you too scared? Because...Actually I am too. They give me nightmares.'")
    print("You feel a connection with Jesse.")
    JesseFriendship = True
    Energy += 10
#Q7 - End of Workday
print("")
print("After lunch, you get back to work. A few hours go by. The shift is finally over")
print("After a long day of work, it's finally time to go home.")
if Berated == True:
    print("You feel a little drained after dealing with an angry customer.")
    Energy -= 10
if RadioAnnoyed == True:
    print("You can't help but be annoyed after what happened on the radio this morning.")
    Energy -= 5
print("Do you take a long walk in the park to decompress, or go straight home?")
print("")
print("1. Take a walk in the park.")
print("2. Go straight home.")
answer8=int(input("Enter 1 or 2: "))

while answer8 != 1 and answer8 != 2:
    print("Please enter a valid answer")
    answer8=int(input("1. Take a walk in the park. 2. Go straight home: "))
    print("")
if answer8==1:
    print("You take a long walk in the park.")
    print("You hear birds chriping above you.")
    print("You feel a sense of peace and tranquility.")
    birds = True
    Energy += 20
if answer8==2:
    print("You go straight home.")
    print("You feel a little tired, but ready to relax.")
    Energy += 10

#Q8 - Evening Routine
print("")
print("You get home and go through the regular evening routine: dinner, shower, brushing your teeth.")
print("It's finally time for bed.")
print("Before you fall asleep, you put on some audio to help you sleep.")
print("You have a few options.")
print("")
print("1. The sound of rain")
print("2. White noise")
print("3. The sounds of birds chirping")
answer7=int(input("Enter 1, 2 or 3: "))
while answer7 != 1 and answer7 != 2 and answer7 != 3:
    print("Please enter a valid answer")
    answer7=int(input("Enter 1, 2 or 3: "))
if answer7==1:
    print("You put on the sound of rain.")
    print("It relaxes you into a gentle slumber, as visions of rain drops dance in your head.")
    energy=+ 25
    rain=True
if answer7==2:
    print("You put on white noise.")
    print("You don't know why, but it helps you fall asleep")
    energy=+ 10
if answer7==3:
    print("You put on the sounds of birds chirping.")
    print("You feel one with nature. You imagine yourself flying with the birds.")
    print("You fall asleep.")
    energy=+ 15
    birds=True

#Q9 - Dream Sequence
print("")
print("zzzzz")
print("You look around, and can't quite place where you are.")
print("Everything feels familair and foreign at the same time.")
print("Then it hits you: you're dreaming!")
print("")
#Environment
print("You study your surroundings.")
if MovieSpoiled == True:
    print("You see what looks like the setting of the movie Jesse described")
else:
    print("You see what looks like a mixture of your house and your workplace.")
print("")
if rain == True:
    print("You look up, and see the rain falling down.")
    print("Yet, you feel dry.")
    print("")
elif birds == True:
    print("You look up, and see the birds flying around.")
    print("Their chirping brings you comfort")
    print("")
elif rain == False and birds == False:
    print("You look up, and can't tell if it is day or night.")
    print("It's beaituful, yet eerie.")
    print("")
else:
    print("You look up, and see the sky is a deep shade of purple.")
    print("The clouds are swirling around, and you feel a sense of unease.")
    print("")
#Nightmare begins
print("Suddenly, you hear a loud noise.")
print("You turn around, and see a giant shadow.")
print("You can't quite make out what it is, but you sense it getting closer.")
print("You feel a sense of dread wash over you.")
print("You realize this isn't just a dream, it's a nightmare.")
print("")
#Nightmare Boss reveal
print("Suddenly, the shadow takes form.")
if BossAngry == True and NewsAnxiety == False:
    print("It's your boss!")
    print("He looks angry, and is yelling at you.")
    print("You try to run away, but your legs feel heavy.")
    print("You can't escape.")
    print("You have to stay and fight.")
    print("")
    NightmareBoss=True
    BossName="Nightmare Manager"
elif NewsAnxiety==True and BossAngry==False:
    print("It's the local politician you heard on the news!")
    print("They are stating their horrible political platform")
    print("You try to run away, but your legs feel heavy.")
    print("You can't escape.")
    print("You have to stay and fight.")
    print("")
    NightmarePolitician=True
    BossName="Nightmare Politician"
elif NewsAnxiety==True and BossAngry==True:
    print("It's a two headed monster")
    print("One head is your boss, and the other is the local politician from the news.")
    print("This really is a nightmare!")
    print("You try to run away, but your legs feel heavy.")
    print("You can't escape.")
    print("You have to stay and fight.")
    print("")
    NightmareTwoHead=True
    BossName="Nightmare Two-Headed Monster"
elif NewsAnxiety==True and BossAngry==True and Berated == True and ThrownCereal == True:
    print("It's...It's a three headed monster!")
    print("One head is your boss, one is that customer from earlier, and the other is the local politician from the news.")
    print("This really is a nightmare!")
    print("You try to run away, but your legs feel heavy.")
    print("You can't escape.")
    print("You have to stay and fight.")
    print("")
    NightmareThreeHead=True
    BossName="Ultimate Nightmare"
elif NewsAnxiety==True and BossAngry==True and Berated == True and ThrownCereal == True:
    print("It's...It's a three headed monster!")
    print("One head is your boss, one os that customer from earlier, and the other is the local politician from the news.")
    print("This really is a nightmare!")
    print("You try to run away, but your legs feel heavy.")
    print("You can't escape.")
    print("You have to stay and fight.")
    print("")
    NightmareThreeHead=True
    BossName="Ultimate Nightmare"
else:
    print("It's...You!")
    print("You figure this is a metaphor for your own self-doubt.")
    print("You have no choice but to face it...or rather, face yourself.")
    NightmareSelf = True
    BossName=f"Nightmare {name}"
#Nightmare Fight (All Options)
print("")
print(f"You get ready to fight the {BossName}.")
print("You have a few options.")
#Nightmare Fight (All Options)
    #Battle Loop
while BossHealth>0 and Energy>0:
     print("")
     print("Choose your attack")
     print("1. Punch")
     if rain == True:
        print("2. Use a water attack")
     if birds == True:
        print("3. Command the bird to attack")
     if JesseFriendship == True:
        print("4. Call Jesse for help")
     if ThrownCereal == True:
        print("5. Throw a cereal box")
        print("")
     Attack=int(input("Enter 1, 2, 3, 4 or 5: "))
     while Attack != 1 and Attack != 2 and Attack != 3 and Attack != 4 and Attack != 5:
        print("Please enter a valid answer")
        Attack=int(input("Enter 1, 2, 3, 4 or 5: "))
     if Attack==1:
        print("You punch the nightmare in the face.")
        num=random.randint(1, 10)
        print(f"you do {num} damage")
        print("")
        BossHealth -= num
        print(f"{BossName} has {BossHealth} health left.")
     if Attack==2:
        print(f"You use your connection with the rain to splash {BossName}.")
        num=random.randint(5, 20)
        print(f"You do {num} damage")
        BossHealth -= num
        print(f"{BossName} has {BossHealth} health left.")
        print("")
     if Attack==3:
        print(f"You command the birds to attack {BossName}.")
        num=random.randint(5, 20)
        print(f"You do {num} damage")
        BossHealth -= num
        print(f"{BossName} has {BossHealth} health left.")
        print("")
     if Attack==4:
        print(f"You call Jesse for help.")
        print("Jesse shows up and punches the nightmare in the face.")
        num=random.randint(5, 20)
        print(f"You do {num} damage")
        BossHealth -= num
        print(f"{BossName} has {BossHealth} health left.")
        print("")
     if Attack==5:
        print(f"You throw a cereal box at {BossName}.")
        num=random.randint(5, 20)
        print(f"You do {num} damage")
        BossHealth -= num
        print(f"{BossName} has {BossHealth} health left.")
        print("")
     num=random.randint(1, 2)
     if num==1:
        print(f"{BossName} attacks you!")
        num=random.randint(1, 10)
        print(f"You take {num} damage.")
        print("")
        Energy -= num
        print(f"You have {Energy} energy left.")
        print("")
     if num==2:
        print(f"{BossName} tries to attack you...but misses!")
     
if BossHealth<=0:
        print(f"You defeated {BossName}!")
        print("You wake up, feeling refreshed.")
        print("You feel like you can take on the world.")
        print("You win!")
if Energy<=0:  
        print("You wake up from the nightmare")
        print("You feel uneasy and tired.")
        print("That definitely was not a good sleep.")

#Credits
print("")
print("Thanks for playing Day-Dreamer!")
print("Created by Zach Butler")
print("TTTTT  H   H  EEEEE       EEEEE  N   N  DDDD")
print("  T    H   H  E           E      NN  N  D   D")
print("  T    HHHHH  EEEE   - -  EEEE   N N N  D   D")
print("  T    H   H  E           E      N  NN  D   D")
print("  T    H   H  EEEEE       EEEEE  N   N  DDDD")
        

