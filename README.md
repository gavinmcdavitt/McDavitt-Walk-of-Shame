# McDavitt-Walk-of-Shame
This will record the progress of the McDavitt Walk of Shame of 2024 - 2025. The basis of the project is my family and I will pick NFL football games. Loser has to walk the St Marks Tallahassee Trail. I wanted to use the data from this spreadsheet to build a website with a good UI, and can hold videos and photos from our event.

Documentation:
In this project we have these functions you can call.
## getListOfGames
## getPregameOdds
## getGames
## getNumOfGames
## printToExcel
## setUp
## ColorizePicks

### setUP:
In this function, it will call the underlying function:
 - getListOfGames
 - getPregameOdds
 - getGames
 - getGames
 - printToExcel

This will webscrape the data and allow us to write it to an excel spreadsheet.

### getListOfGames
In this function it scrapes each game and returns a list of teams,
this can grab teams that have already played so becareful.

### getPregameOdds
In this function it scrapes the betting odds for the two teams. It is in the same order,
as the games are. This is important as this is how I will match the games. It also will
return a list of json objects that can be called with: **over_under** and **spread**. Remember the spread
is for the home team to cover.

### getGames
In this function we will combine the results of **getListOfGames** and **getPregameOdds** 
It returns a list of json objects that can be called through:
- home
- away
- spread
- over_under
```
listOfObjects = getGames(competitions, odds)
listOfObjects[number][home] = "Steelers"
```

### getNumOfGames
Returns the list of games that have not started yet.

### printToExcel
Creates an excel sheet to write too. It will create one for each week. It will use
all the data we created earlier. It reutrns the file name that you wrote too.

### ColorizePicks
If everyone picks the same things then its green.
If two people have different picks then it is orange.
