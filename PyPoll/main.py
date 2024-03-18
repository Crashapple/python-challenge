import csv

csv_file_path = r'C:\Users\april\Documents\April_Class\python-challenge\PyPoll\Resources\election_data.csv'

total_votes = 0 #used to tally the total number of votes
candidates = [] #list of all individual candidates
candidate_results = {} #dictionary of votes per candidate
winner = 0 #individual candidate with the most votes
winner_name = "" #Name of candidate with the most votes

#Open CSV File
with open(csv_file_path) as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    header = next(csv_reader)

    #initiatlize candidate_vote to zero
    candidate_vote = 0


    #loop through csv file to get candidate names and votes
    for row in csv_reader:

        total_votes = total_votes +1

        candidate_name = row[2]

        if candidate_name not in candidates:
            candidates.append(candidate_name)    
            candidate_results[candidate_name]=1
        else:
            candidate_results[candidate_name] = candidate_results[candidate_name]+1

#create output file with results
output_path = r'C:\Users\april\Documents\April_Class\python-challenge\PyPoll\analysis\analysis_Pypoll.csv'

with open(output_path,'w') as csvfile2: 

    csvwriter = csv.writer(csvfile2, delimiter = ',')

    print("Election Results")

    csvwriter.writerow(['Election Results']) 

    print("------------------------------")

    csvwriter.writerow(['------------------------------'])

    print(f"Total Votes: {total_votes}")    

    csvwriter.writerow([f"Total Votes: {total_votes}"])

    print("------------------------------")

    csvwriter.writerow(['------------------------------'])
   
   #determine winner
    for candidate in candidates:

        candidate_percent = candidate_results[candidate]/total_votes

        format_candidate_percent = f"{candidate_percent: .3%}"

        if candidate_results[candidate] > winner:

            winner = candidate_results[candidate] 
            winner_name = candidate

        print(f'{candidate}: {format_candidate_percent} ({candidate_results[candidate]})')

        csvwriter.writerow([f'{candidate}: {format_candidate_percent} ({candidate_results[candidate]})'])

    print("------------------------------")

    csvwriter.writerow(['------------------------------'])

    print(f"Winner: {winner_name}")

    csvwriter.writerow([f"Winner: {winner_name}"])

    print("------------------------------")

    csvwriter.writerow(['------------------------------'])