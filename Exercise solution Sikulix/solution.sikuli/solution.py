#Solution for the exercise. Made for chrome, may not work everywhere.
tests = [0,0,0,0,0,0,0]

#TEST 1: WEBSITE HAS ALL NEEDED ELEMENTS:
if (not exists("1477510041399.png") or not exists("1477510051035.png") or not exists("1477510059831.png")):
    tests[0] = 1


#TEST 2: SITE SHOWS ERROR MESSAGE WHEN USER DOES NOT ACCEPT RULES:
click("1477510245598.png")
if(not exists("1477510263955.png")):
    tests[1] = 1


#TEST 3: SITE SHOWS ERROR MESSAGE WHEN REQUIRED FIELDS ARE EMPTY:
if (exists("1477510920069.png")):
    click("1477510925357.png")
    
click("1477510545400.png")
click("1477510563984.png")
if(not exists("1477510601320.png")):
    tests[2] = 1


#TEST 4: SITE SHOWS ERROR MESSAGE WHEN NAME IS A NUMBER:
if (exists("1477510920069.png")):
    click("1477510925357.png")

type("1477511178377.png","123456")
type("1477511434397.png","aaabbb")
type("1477511449445.png","NYC")
type("1477511478149.png","123")
click("1477510563984.png")
if(not exists("1477511333213.png")):
    tests[3] = 1

#TEST 5: SITE SHOWS ERROR MESSAGE WHEN AGE IS NOT A NUMBER:
if (exists("1477510920069.png")):
    click("1477510925357.png")
type("1477511571499.png",Key.HOME+Key.DELETE+Key.DELETE+Key.DELETE+Key.DELETE+Key.DELETE+Key.DELETE+"john bay")
click("1477510563984.png")
if(not exists("1477512005891.png")):
    tests[4] = 1


#TEST 6: SITE SHOWS ERROR MESSAGE WHEN COUNTRY IS A NUMBER:
if (exists("1477510920069.png")):
    click("1477510925357.png")
type("1477511896599.png",Key.HOME+Key.DELETE+Key.DELETE+Key.DELETE+Key.DELETE+Key.DELETE+Key.DELETE+"32")
click("1477510563984.png")
if(not exists("1477512084635.png")):
    tests[5] = 1


#TEST 7: SITE SHOWS SUCCESS MESSAGE AT THE END:
if (exists("1477510920069.png")):
    click("1477510925357.png")
type("1477512144995.png",Key.HOME+Key.DELETE+Key.DELETE+Key.DELETE+"usa")
click("1477510563984.png")
if(not exists("1477512184349.png")):
    tests[6] = 1


#SHOWING TEST RESULTS:
for n in range(7):
    if (tests[n] == 1):
        print "Test " + str(n+1) + " failed!"

       