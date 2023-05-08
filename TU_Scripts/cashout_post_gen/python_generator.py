#! python3

# importing modules
import os
import pandas as pd
import pyperclip

# 1. Read the data from the "data.csv" file in the same folder
filename = "data.csv"
current_path = os.path.dirname(__file__)
filepath = os.path.join(current_path, filename)

df = pd.read_csv(filepath)
output_str = ""  # final item to by copied into pyperclip
output_ls = []
# print(df['Username'])
# print(type(df['Username']))


# # 2. Print each line item in the CSV
for index, row in df.iterrows():
    line = ', '.join(row.astype(str).tolist())
    ls = line.split(', ')
    username, time, pv_amount, pct_char, cash_amount, charity_amount, count = ls[
        1], ls[3], ls[5], ls[6], ls[7], ls[8], ls[9]

    # tidy up the count NaN and decimal points
    if count == "nan":
        count = '0'
    count = str(int(float(count)))

    time = (time.split(":")[0]).split('T')[0]

    # tidy up the amount, charity, cash amounts
    pv_amount = f'{(int(pv_amount) * 0.01):.2f}'
    cash_amount = f'{(int(cash_amount) * 0.01):.2f}'
    charity_amount = f'{(int(charity_amount) * 0.01):.2f}'

    # print(username, time, pv_amount, pct_char,
    #       cash_amount, charity_amount, count)

    # adding fire / emoji logic
    fire = ':fire:'
    heart = ':heart:'
    decoration = ""

    if int(float(pv_amount)) > 1000:
        decoration = ''.join((decoration, (fire * 5)))
    elif int(float(pv_amount)) > 100:
        decoration = ''.join((decoration, (fire * 3)))
    else:
        decoration = ''.join((decoration, (fire * 1)))

    if float(pct_char) == 100:
        decoration = ''.join((decoration, (heart * 5)))
    elif float(pct_char) > 10:
        decoration = ''.join((decoration, (heart * 3)))

        # Formatting the string, and adding it to the final list
    message = f'**{username}** has cashed out **${pv_amount}** on {time}!! Winning ${cash_amount} in cash and donating ${charity_amount}({pct_char}%) to charity!{decoration}'

    output_str += f'{message}\n\n'


# print(output_str)
output_ls = output_str.split('\n')
filtered_ls = [item for item in output_ls if item != '']
filtered_ls.reverse()
output_str = '\n\n'.join(filtered_ls)
print(output_str)
pyperclip.copy(output_str)


# Additional todos;
# flip the ordering so its last in first out
