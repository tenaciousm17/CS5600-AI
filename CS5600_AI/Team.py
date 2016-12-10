"""
This pages focuses on taking the data from the read in and converting it to
the actual implementation for the classification algorithm. By using a dictionary
I can eaily track the many values being compared and stored. Also in the function,
I can can additinal features for testing accuracy on different aspects of the program
with soccer. Currently, I just have previous games as the only feature but
if you uncomment the othe sections you can add additional functionality for accuracy.

"""

class Team:
    def __init__(self,name):
        self.name = name
        self.scoresDict = dict() 
        self.scoresList = list()
        self.totalGames = 0
        self.totalWins = 0
        self.premier = False
#Tracks the recent games the team has been in

    def getRecentGames(self,num,d,m,y):
        temp = list()
        back = 0
        finds = 0
        listLength = len(self.scoresList)
        y = int(y)
        m = int(m)
        d = int(d)
        if listLength-1 > num: #useless if statement
            if num > back:
                i = listLength-1-back
                while back < num and i >=0:
                    print self.scoresList[i]
                    mon = int(self.scoresList[i][4])
                    day = int(self.scoresList[i][3]) 
                    yea = int(self.scoresList[i][5])
                    print "Current",mon,day,yea,"Finding",m,d,y
                    if yea <= y:
                        #print "Passed year"
                        #3 = d , 4 = m, 5 = y
                        #5th day of 3 month of 2012
                        #start at 2014, find 2012.
                        if mon <= m or yea != y:
                            #print "Passed Month" 
                        #find 3 month
                        #find games BEFORE 5th day
                            if day <=d or mon != m or yea != y:
                                #print "Passed day"
                                #Adding the result, game score, and opposing game score
                                #print "Matched"
                                temp+=self.scoresList[i][0],self.scoresList[i][6],self.scoresList[i][7]
                                finds+=1
                                back+=1
                                #if it is the first time, store the value and decrement the date
                                #used so that there is another iteration 
                    i-=1
            while finds < num:
                return None
        return temp
#Tracks the scores of recent games that the team has been in

    def getRecentTotalScores(self,num,d,m,y):
        temp = list()
        back = 0
        successes = 0
        listLength = len(self.scoresList)
        y = int(y)
        m = int(m)
        d = int(d)
        tScored = 0
        tScoredAgainst = 0
        if listLength-1 > num: #useless if statement
            if num > back:
                i = listLength-1-back
                while back < num and i >=0:
                    #print self.scoresList[i]
                    mon = int(self.scoresList[i][4])
                    day = int(self.scoresList[i][3]) 
                    yea = int(self.scoresList[i][5])
                    #print "Current",mon,day,yea,"Finding",m,d,y
                    if yea <= y:
                        #print "Passed year"
                        #3 = d , 4 = m, 5 = y
                        #5th day of 3 month of 2012
                        #start at 2014, find 2012.
                        if mon <= m or yea != y:
                            #print "Passed Month" 
                        #find 3 month
                        #find games BEFORE 5th day
                            if day <=d or mon != m or yea != y:
                                #print "Passed day"
                                #Adding the result, game score, and opposing game score
                                #print "Matched"
                                #temp+=self.scoresList[i][0],self.scoresList[i][6],self.scoresList[i][7]
                                tScored+=int(self.scoresList[i][6])
                                tScoredAgainst+=int(self.scoresList[i][7])
                                successes+=1
                                back+=1
                                #if it is the first time, store the value and decrement the date
                                #used so that there is another iteration 
                    i-=1
        if tScored == 0 or tScoredAgainst == 0:
            return None
        temp+=tScored,tScoredAgainst
        #print "------"
        return temp

        #This uses the stats of wins, losses, ties and scores for testing
    def currentStats(self,num,d,m,y): 
        temp = list()
        back = 0
        successes = 0
        listLength = len(self.scoresList)
        y = int(y)
        m = int(m)
        d = int(d) #no need to subtract by one because done already by getRecentGamesVS()
        win = 0.0
        loss = 0.0
        tie = 0.0
        total = 0.0
        if listLength-1 > num: #useless if statement
            if num > back:
                #temp+=self.scoresList[i][0],self.scoresList[i][6],self.scoresList[i][7]
                #back+=1
                i = listLength-1-back
                while back < num and i >=0:
                    #print self.scoresList[i]
                    mon = int(self.scoresList[i][4])
                    day = int(self.scoresList[i][3]) 
                    yea = int(self.scoresList[i][5])
                    #print "Current",mon,day,yea,"Finding",m,d,y
                    if yea <= y:
                        #print "Passed year"
                        #3 = d , 4 = m, 5 = y
                        #5th day of 3 month of 2012
                        #start at 2014, find 2012.
                        if mon <= m or yea != y:
                            #print "Passed Month" 
                        #find 3 month
                        #find games BEFORE 5th day
                            if day <=d or mon != m or yea != y:
                                #print "Passed day"
                                #Adding the result, game score, and opposing game score
                                
                                #temp+=self.scoresList[i][0],self.scoresList[i][6],self.scoresList[i][7]
                                res = int(self.scoresList[i][0])
                                #print "Matched",res
                                if res == 2:
                                    win+=1
                                    #print "won",win
                                elif res == 1:
                                    tie+=1
                                    #print "tie",tie
                                elif res == 0:
                                    loss+=1
                                    #print "loss",loss
                                total+=1
                                successes+=1
                                back+=1
                                #if it is the first time, store the value and decrement the date
                                #used so that there is another iteration
                    i-=1
        #print successes
        #print win,tie,total
        if successes == num and total != 0:
            temp+=[(win+(tie/2))/total]
        else:
            return None
        #print "------"
        return temp

#This is for testing recent games scores and whether they were wins or losses or ties
    def getRecentGamesVS(self,d,m,y,num,opposing):
        temp = list()
        #ensures values are initialized
        label = 9999
        i = len(self.scoresList)-1
        first = True
        if self.scoresList[i][4] == "mon" or self.scoresList[i][5] == "yea":
            return None
        y = int(y)
        m = int(m)
        d = int(d)
        #decrements from the back, as well as checking for the
        #number of head to head games planned to record
        while i >= 0 and num > 0:
            #hacky way to prevent the mon error, does not read the mon line
            mon = int(self.scoresList[i][4])
            day = int(self.scoresList[i][3])
            yea = int(self.scoresList[i][5])

            #print m,d,y,mon,day,yea
            if yea <= y:
                #3 = d , 4 = m, 5 = y
                #5th day of 3 month of 2012
                #start at 2014, find 2012.
                #print "pass y"
                if mon <= m or yea != y:
                    #print "pass m" 
                #find 3 month
                #find games BEFORE 5th day
                    if day <=d or mon != m or yea != y:
                        #print "pass d"
                        #print self.scoresList[i][2],opposing
                        if self.scoresList[i][2] == opposing and not first:
                            #Adding the result, game score, and opposing game score
                            #temp+=self.scoresList[i][0],self.scoresList[i][6],self.scoresList[i][7]

                            #more complicated
                            #print self.scoresList[i]
                            #label,goals scored,opposing goals scored
                            temp+=self.scoresList[i][0],self.scoresList[i][6],self.scoresList[i][7]

                            #shots opposing shots
                            #temp+=self.scoresList[i][8],self.scoresList[i][9]
                            
                            #shots on target, opposing shots on target
                            #temp+=self.scoresList[i][10],self.scoresList[i][11]
                            

                            num-=1
                            #if it is the first time, store the value and decrement the date
                            #used so that there is another iteration
                        elif first and self.scoresList[i][2] == opposing:
                            #print "got label"
                            label = self.scoresList[i][0]
                            #print m,d,y,mon,day,yea
                            first = False
                            m = mon
                            d = day-1
                            y = yea
                               
                #check if opposing is correct
                #add into list
                #otherwise decrement
            i-=1
        #print "================================"
        if not num == 0:
            #print "Not enough data"
            return None
        if label == 9999 or temp == None:
            return None

        #This is the section that can add functionality of testing accuracy as needed
        """temp = list()
        
        if self.currentStats(5,d,m,y) == None:
            return None
        else:
            temp+=self.currentStats(5,d,m,y)
        
        if self.getRecentTotalScores(5,d,m,y) == None:
            return None
        else:
            temp+=self.getRecentTotalScores(5,d,m,y)

        if self.getRecentGames(5,d,m,y) == None:
            return None
        else:
            temp+=self.getRecentGames(5,d,m,y)"""

        return label,temp


                    
def makeTeam(name):
    team = Team(name)
    return team
