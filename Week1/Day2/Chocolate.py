name = input("Hello, You have decided to buy our chocolate... Thank you for your support. We just need one piece of information...What is your name? ")
print("New Email:\nHello " + name + ", \nThanks so much for your order. We will be shipping it tonight. It will have a special greeting of - " + name + " is super awesome, " + name +" is the best person in the whole wide world. \nSincerely, \nChocolates.co")
print("New Email:\nHello <NAME>,\nThanks so much for your order. We will be shipping it tonight. It will have a special greeting of - <NAME> is super awesome, <NAME> is the best person in the whole wide world. <NAME> is super awesome. <NAME> is super awesome. <NAME> is super awesome. <NAME> is super awesome. <NAME> is super awesome. <NAME> is super awesome. <NAME> is super awesome. <NAME> is super awesome.  \nSincerely, \nChocolates.co".replace("<NAME>",name))