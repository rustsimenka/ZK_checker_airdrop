import csv

with open('my_wallets.txt', 'r') as my_wallets, \
        open('eligibility_list.csv', 'r') as wallets_eligible, \
        open('my_luck_wallets.txt', 'w', encoding='utf-8') as my_luck_wallets:
    eligible_wallets = {row[0]: row[1] for row in csv.reader(wallets_eligible)}
    count_luck_wallets = 0

    for line in my_wallets:
        if line.strip():
            wallet = line.strip().lower()
            if wallet in eligible_wallets:
                print(f'{count_luck_wallets + 1}. {wallet} \
                 одобрено {eligible_wallets[wallet]} монет', file=my_luck_wallets)
                count_luck_wallets += 1

    if count_luck_wallets == 0:
        print("Я всё проверил, Ваших кошельков нет в списке счастливчиков", file=my_luck_wallets)

print(f'Одобрено {count_luck_wallets} кошельков')
