import csv

csv_file_path = r'C:\Users\april\Documents\April_Class\python-challenge\PyBank\Resources\budget_data.csv'

num_rows = 0
profit_loss = 0
monthly_diff = []
month1 = 0
month2 = 0
sum_month_diff = 0
greatest_inc = 0
greatest_dec = 0

with open(csv_file_path) as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    header = next(csv_reader)

    for row in csv_reader:

        num_rows = num_rows + 1

        profit_loss = profit_loss + int(row[1])

        if month1 == 0:
            month1=row[1]
        else:
                month2 = row[1]     
                diff_amount = int(month2) - int(month1) 
                if diff_amount < 0 and diff_amount < greatest_dec:
                    greatest_dec = diff_amount
                    greatest_dec_month = row[0]
                if diff_amount > 0 and diff_amount > greatest_inc:
                     greatest_inc = diff_amount
                     greatest_inc_month = row[0]
                sum_month_diff = sum_month_diff + diff_amount  
                monthly_diff.append(diff_amount)
                month1 = month2


profit_loss_ave = int(sum_month_diff)/int(len(monthly_diff))

print("Financial Analysis")

print("-----------------------------------------------------")

print(f"Total Months: {num_rows}")

print(f"Total: ${profit_loss}")

print(f"Average Change: ${profit_loss_ave:.2f}")

print(f"Greatest Increase in Profits: {greatest_inc_month} (${greatest_inc})")

print(f"Greatest Decrease in Profits: {greatest_dec_month} (${greatest_dec})")

output_path = r'C:\Users\april\Documents\April_Class\python-challenge\PyBank\analysis\analysis_Pybank.csv'

with open(output_path,'w') as csvfile2:

    csvwriter = csv.writer(csvfile2, delimiter = ',')

    csvwriter.writerow(['Financial Analysis'])

    csvwriter.writerow(['-----------------------------------------------------'])

    csvwriter.writerow([f'Total Months: {num_rows}'])

    csvwriter.writerow([f"Total: ${profit_loss}"])

    csvwriter.writerow([f"Average Change: ${profit_loss_ave:.2f}"])

    csvwriter.writerow([f"Greatest Increase in Profits: {greatest_inc_month} (${greatest_inc})"])

    csvwriter.writerow([f"Greatest Decrease in Profits: {greatest_dec_month} (${greatest_dec})"])
