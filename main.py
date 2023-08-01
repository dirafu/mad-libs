import random
storyNumber=int(input('choose story template (1, 2 or 3)\n'))
if storyNumber == 1:
    wordList=[]
    numberList=[]
    adjectiveList=[]
    nounList=[]
    partofthebodyList=[]
    verbList=[]

    numberList.append(input('Input a number:'))
    wordList.append(input('Measure of time:'))
    wordList.append(input('Mode of transportation:'))
    adjectiveList.append(input('Input adjective:'))
    adjectiveList.append(input('Input adjective again:'))
    nounList.append(input('Input a noun:'))
    wordList.append(input('Input a color:'))
    partofthebodyList.append(input('Part of the body:'))
    verbList.append(input('Input a verb:'))
    numberList.append(input('Input a number again:'))
    nounList.append(input('Input a noun again:'))
    nounList.append(input('Input a noun again:'))
    partofthebodyList.append(input('Input a part of the body again:'))
    verbList.append(input('Input a verb:'))
    nounList.append(input('Input a noun:'))
    adjectiveList.append(input('Input an adjective:'))
    wordList.append(input('Input a silly word:'))
    nounList.append(input('Input a noun again:'))

    random.shuffle(numberList)
    random.shuffle(adjectiveList)
    random.shuffle(nounList)
    random.shuffle(partofthebodyList)
    random.shuffle(verbList)

    storyText=f'It was about {numberList[0]} {wordList[0]} ago when I arrived at the hospital in a {wordList[1]}. The hospital is a/an {adjectiveList[0]} place, there are a lot of {adjectiveList[1]} {nounList[0]} here. There are nurses here who have {wordList[2]} {partofthebodyList[0]}. If someone wants to come into my room I told them that they have to {verbList[0]} first. I’ve decorated my room with {numberList[1]} {nounList[1]}. Today I talked to a doctor and they were wearing a {nounList[2]} on their {partofthebodyList[1]}. I heard that all doctors {verbList[1]} {nounList[3]} every day for breakfast. The most {adjectiveList[2]} thing about being in the hospital is the {wordList[3]} {nounList[4]} !'
    print(storyText)
elif storyNumber == 2:
    wordList=[]
    nounList=[]
    adjectiveList=[]
    verbList=[]
    colorList=[]
    numberList=[]
    animalList=[]

    wordList.append(input('Input Person Name:'))
    nounList.append(input('input noun:'))
    adjectiveList.append(input('Input adjective (feeling):'))
    verbList.append(input('Input verb:'))
    adjectiveList.append(input('Input adjective (feeling):'))
    animalList.append(input('Input an animal:'))
    verbList.append(input('Input a verb:'))
    colorList.append(input('Input a color:'))
    wordList.append(input('Input a verb + ing:'))
    wordList.append(input('Input a adverb + ly:'))
    numberList.append(input('Input a number:'))
    wordList.append(input('Measure of time:'))
    colorList.append(input('Input a color:'))
    animalList.append(input('Input an animal:'))
    numberList.append(input('Input a number:'))
    wordList.append(input('Input a silly word:'))
    nounList.append(input('Input a noun again:'))

    random.shuffle(nounList)
    random.shuffle(adjectiveList)
    random.shuffle(verbList)
    random.shuffle(colorList)
    random.shuffle(numberList)
    random.shuffle(animalList)

    storyText=f'This weekend I am going camping with {wordList[0]}. I packed my lantern, sleeping bag, and {nounList[0]}. I am so {adjectiveList[0]} to {verbList[0]} in a tent. I am {adjectiveList[1]} we might see a(n) {animalList[0]}, I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and {verbList[1]}. I have heard that the {colorList[0]} lake is great for {wordList[1]}. Then we will {wordList[2]} hike through the forest for {numberList[0]} {wordList[3]}. If I see a {colorList[1]} {animalList[1]} while hiking, I am going to bring it home as a pet! At night we will tell {numberList[1]} {wordList[4]} stories and roast {nounList[1]} around the campfire!!'
    print(storyText)
elif storyNumber == 3:
    wordList=[]
    adjectiveList=[]
    magicalcreatureList=[]
    nounList=[]
    pluralnounList=[]

    wordList.append(input('Input Person Name:'))
    adjectiveList.append(input('Input an adjective:'))
    wordList.append(input('Input a color:'))
    wordList.append(input('Input an animal:'))
    wordList.append(input('Input a place:'))
    adjectiveList.append(input('Input an adjective:'))
    magicalcreatureList.append(input('Input a magical creature (plural):'))
    adjectiveList.append(input('Input an adjective:'))
    magicalcreatureList.append(input('Input a magical creature (plural):'))
    wordList.append(input('Input a room in the house:'))
    nounList.append(input('Input a noun:'))
    nounList.append(input('Input a noun:'))
    pluralnounList.append(input('Input a noun (plural):'))
    adjectiveList.append(input('Input an adjective:'))
    pluralnounList.append(input('Input a noun (plural):'))
    wordList.append(input('Input a number:'))
    wordList.append(input('Measure of time:'))
    wordList.append(input('Input a verb + ing:'))
    adjectiveList.append(input('Input an adjective:'))
    nounList.append(input('Input a noun:'))

    random.shuffle(adjectiveList)
    random.shuffle(magicalcreatureList)
    random.shuffle(nounList)
    random.shuffle(pluralnounList)

    storyText=f'Dear {wordList[0]}, I am writing to you from a {adjectiveList[0]} castle in an enchanted forest. I found myself here one day after going for a ride on a {wordList[1]} {wordList[2]} in {wordList[3]}. There are {adjectiveList[1]} {magicalcreatureList[0]} and {adjectiveList[2]} {magicalcreatureList[1]} here! In the {wordList[4]} there is a pool full of {nounList[0]}. I fall asleep each night on a {nounList[1]} of {pluralnounList[0]} and dream of {adjectiveList[3]} {pluralnounList[1]}. It feels as though I have lived here for {wordList[5]} {wordList[6]}. I hope one day you can visit, although the only way to get here now is {wordList[7]} on a {adjectiveList[4]} {nounList[2]}!!'
    print(storyText)