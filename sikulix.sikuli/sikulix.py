# Open chrome, full screen, before running:
click("1477487238412.png")
paste("1477487255076.png", "jtrpinto.github.io/badboy/bbc.html")
type(Key.ENTER)
if (find("1477487566808.png")):
    type("1477488046153.png", "Kevin Pork")
    type("1477488052011.png", "23")
    type("1477488073035.png", "NYC")
    type("1477488106373.png", "USA")
    click("1477487715121.png")
    click("1477487784084.png")
    if (find("1477487830007.png")):
        print("Everything was ok!")
    else:
        print("Success message not shown!")
else:
    print("The page has items missing!")
