import pandas as pd

def get_each_game_results(sRow):
    OutPutCol =6 #'G'
    winnerCol =5
    gavinPickCol = 3
    annaPickCol=4
    PopPickCol =2
    fileName = 'family.xlsx'
    df = pd.read_excel(fileName)
    popsWinCount = 0
    gavinWinCount =0
    AnnaWinCount =0
    for i in range(2, 14):
        popPick = df.iloc[i,PopPickCol]
        GavinPick = df.iloc[i, gavinPickCol]
        annaPick = df.iloc[i, annaPickCol]
        winnerPick = df.iloc[i, winnerCol]
        
        if(winnerPick.lower() == popPick.lower()):
            print('pops won game: ')
            popsWinCount = popsWinCount+1
        if (winnerPick.lower() == GavinPick.lower()):
            print('Gavin won game ')
            gavinWinCount = gavinWinCount +1
       # if(winnerPick.lower() == annaPick.lower()):
        #    print('Anna won game')
    
    print('Total wins for Gavin', gavinWinCount)
    print('Total wins for anna', AnnaWinCount)
    print('total wins for dad', popsWinCount)
    selected_data = df.iloc[2, PopPickCol]


    print(selected_data)
    print('ended')

def printResult(num, row):
    df = pd.read_excel('family.xlsx')
    outPutCol =6 #G

    # Update the cell (cell[0] is the row, cell[1] is the column)
    df.at[row, outPutCol] = num
    
    # Write the updated DataFrame back to the Excel file
    df.to_excel('family.xlsx', index=False)
    #print(f"Updated cell {cell[row]}{cell[outPutCol] + 1} with '{num}'.")
    print('Done')

get_each_game_results(46)
#printResult(num = 'blue', row =6)