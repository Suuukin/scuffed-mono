import random

joke_list = [
"What do you call a boomerang that won’t come back? A stick.",
"What does a cloud wear under his raincoat? Thunderwear.",
"Two pickles fell out of a jar onto the floor. What did one say to the other? Dill with it.",
"What time is it when the clock strikes 13? Time to get a new clock.",
"How does a cucumber become a pickle? It goes through a jarring experience.",
"What did one toilet say to the other? You look a bit flushed.",
"What do you think of that new diner on the moon? Food was good, but there really wasn’t much atmosphere.",
"Where would you find an elephant? The same place you lost her."
"What goes up and down but does not move?  Stairs " ,
"Where should a 500 pound alien go? On a diet ",
"What did one toilet say to the other?  You look a bit flushed. ",
"Why did the picture go to jail?  Because it was framed. ",
"What did one wall say to the other wall?  I'll meet you at the corner. ",
"What did the paper say to the pencil?  Write on! ",
"What do you call a boy named Lee that no one talks to?  Lonely ",
"What gets wetter the more it dries?  A towel. ",
"Why do bicycles fall over?  Because they are two-tired! ",
"Why do dragons sleep during the day?  So they can fight knights! ",
"What did Cinderella say when her photos did not show up?  Someday my prints will come! ",
"Why was the broom late?  It over swept! ",
"What part of the car is the laziest?  The wheels, because they are always tired! ",
"What did the stamp say to the envelope?  Stick with me and we will go places! ",
"What is blue and goes ding dong?  An Avon lady at the North Pole! ",
"Were you long in the hospital?  No, I was the same size I am now! " ,
"Why couldn't the pirate play cards?  Because he was sitting on the deck! ",
"What did the laundryman say to the impatient customer?  Keep your shirt on! ",
"What's the difference between a TV and a newspaper?  Ever tried swatting a fly with a TV? ",
"What did one elevator say to the other elevator?  I think I'm coming down with something! ",
"Why was the belt arrested?  Because it held up some pants! " ,
"Why was everyone so tired on April 1st?  They had just finished a March of 31 days. " ,
"Which hand is it better to write with?  Neither, it's best to write with a pen! " ,
"Why can't your nose be 12 inches long?  Because then it would be a foot! " ,
"What makes the calendar seem so popular?  Because it has a lot of dates! " ,
"Why did Mickey Mouse take a trip into space?  He wanted to find Pluto! " ,
"What is green and has yellow wheels?  Grass…..I lied about the wheels! " ,
"What is it that even the most careful person overlooks?  Her nose! " ,
"Did you hear about the robbery last night?  Two clothes pins held up a pair of pants! " ,
"Why do you go to bed every night?  Because the bed won't come to you! " ,
"Why did Billy go out with a prune?  Because he couldn't find a date! " ,
"Why do Inuit do their laundry in Tide?  Because it's too cold out-tide! " ,
"How do you cure a headache?  Put your head through a window and the pane will just disappear! " ,
"What has four wheels and flies?  A garbage truck! " ,
"What kind of car does Mickey Mouse's wife drive?  A minnie van! ",
"Why don't traffic lights ever go swimming?  Because they take too long to change! " ,
"Why did the man run around his bed?  To catch up on his sleep! ",
"Why did the robber take a bath before he stole from the bank?  He wanted to make a clean get away!"
    ]

want_joke = input('Want a joke (y/n)? ')

while want_joke == 'y':
    print(joke_list[random.randint(0,44)])
    want_joke = False
    want_joke = input('Want a joke (y/n)? ')

if want_joke == 'n':
    print('ok no joke')

    