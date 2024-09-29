from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import xlwt
from xlwt import Workbook
from openpyxl import Workbook
import requests
def getListOfGames():
    url = "https://www.cbssports.com/nfl/scoreboard/"  # Replace with the target URL
    response = requests.get(url)
    print(response)
    soup = BeautifulSoup(response.content, 'html.parser')
    team_links = soup.find_all('a', class_='team-name-link')
    listOfTeams=[]
    for team in team_links:
        team_name = team.get_text(strip=True)
        listOfTeams.append(team_name)
        print(team_name)
    return listOfTeams
def getPregameOdds():
    url = "https://www.cbssports.com/nfl/scoreboard/"  # Replace with the target URL
    response = requests.get(url)
    print(response)
    soup = BeautifulSoup(response.content, 'html.parser')
    over_under = soup.find_all('td', class_="in-progress-odds in-progress-odds-away")
    spreads = soup.find_all('td', class_='in-progress-odds in-progress-odds-home')
    listofBetting =[]
    for a , b in zip(over_under, spreads):
        AwayOverUnder = a.get_text(strip=True)
        homeSpread = b.get_text(strip=True)
       # print(AwayOverUnder, " ", homeSpread)
        bets = {
            'over_under': AwayOverUnder,
            'spread': homeSpread
        }
        listofBetting.append(bets)
    return listofBetting
    # for a, b in over_under and spreads:
    #     AwayOverUnder = a.get_text(strip=True)
    #     homeSpread = b.get_text(strip=True)
    #     print('over-under: ', AwayOverUnder, 'spread ', homeSpread)

    #class="in-progress-odds in-progress-odds-away"

def getListofCompetition(listofTeams, odds):
    last_team =""
    listOfCompetions =[]
    for index, team in enumerate(listofTeams):
        if index % 2 == 0:  # Check if the index is even
            print('home team',team)  # Print team names at even indices
            last_team = team
        if index % 2 ==1:
            print('away team', team)
            competition = {
            'Home': team,
            'Away':last_team,
            }


def getListofCompetition(listofTeams, odds):
    last_team = ""
    listOfCompetitions = []

    for index, team in enumerate(listofTeams):
        if index % 2 == 0:  # Check if the index is even
            #print('home team', team)  # Print team names at even indices
            last_team = team
        elif index % 2 == 1:  # Check if the index is odd
            #print('away team', team)
            competition = {
                'Home': last_team,  # last_team is the home team
                'Away': team,  # current team is the away team
            }
            listOfCompetitions.append(competition)

    return listOfCompetitions


def getGames(teams, odds):
    listOfCompetitions = []

    # Iterate over the teams in pairs (home and away)
    for i in range(0, len(teams), 2):
        # Calculate the corresponding index in the odds list
        odds_index = i // 2

        # Check if there's a valid odds entry for this game
        if odds_index < len(odds):
            # Create a competition entry for this pair of teams and odds
            competition = {
                'home': teams[i],  # Home team
                'away': teams[i + 1],  # Away team
                'spread': odds[odds_index]['spread'],  # Corresponding spread
                'over_under': odds[odds_index]['over_under']  # Corresponding over/under
            }
            listOfCompetitions.append(competition)
        else:
            print(f"Warning: Not enough odds for game between {teams[i]} and {teams[i + 1]}")

    return listOfCompetitions

def printToExcel(data, weekNum):

    # Create a new Workbook and select the active sheet
    wb = Workbook()
    ws = wb.active

    # Optionally, you can set a title for the sheet
    ws.title = "My Items"

    # Write headers (optional)
    ws['A1'] = 'Away'  # Header for Column A
    ws['B1'] = 'Home'  # Header for Column B
    ws['C1'] = 'spread'
    ws['D1'] = 'Over Under'
    ws['E1'] ='Pops'
    ws['F1'] ='Anna'
    ws['G1'] = 'Gavin'
    ws['H1'] ='Winner'

    # Write data to column B starting from the second row
    for index, item in enumerate(data, start=1):  # Start from row 2
        ws[f'A{index+1}'] = item['home']  # Write away team
        ws[f'B{index+1}'] = item['away']  # Write home team
        ws[f'C{index+1}'] = item['spread']  # Write Spread
        ws[f'D{index+1}'] = item['over_under']  # Write Over Under

    # Save the workbook to a file
    excel_file_path = F"week{weekNum}.xlsx"
    wb.save(excel_file_path)

    print(f"Data written to {excel_file_path}")

def setUp():
    weekNumber =4
    teams = getListOfGames()
    odds = getPregameOdds()
    run = getGames(teams, odds)
    printToExcel(run, weekNumber)
setUp()
