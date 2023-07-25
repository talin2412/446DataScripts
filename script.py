import csv
import json

with open('bad-words.csv', 'r') as badWords:
    with open('words_pos.csv', 'r') as allWords:

        readerBadWords = csv.reader(badWords)
        readerAllWords = csv.reader(allWords)


        bad = list(readerBadWords)
        good = list(readerAllWords)

        returnData = []
        match = False

        for row in good:
            for rowBad in bad:
                if row[0] == rowBad[0]:
                    match = True
                    print("Ss")
                    break
            if not match:
                returnData.append(row[0])
            match = False

        with open('clarityWords.json', 'w') as output:
            output.write(json.dumps(returnData, indent=4))
        
        
        
        # with open('clarityWords.csv', 'w') as csvfile:
        #     csv_writer = csv.writer(csvfile)
        #     # Write the data to the CSV file
        #     csv_writer.writerows(returnData)