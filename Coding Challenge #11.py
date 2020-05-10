# Create an algorithm for ATM software which will accept
# a withdraw amount and gives "Error" as an output
# if the amount is invalid else gives no of minimum
# notes needed
#  Notes: 50, 100, 200, 500, 2000


available_notes = [50, 100, 200, 500, 2000]

#
# def atm_withdraw(amount):
#     if amount % min(available_notes) != 0:
#        print('Invalid amount!')
#        exit(0)
#     counter = 0
#     while True:
#         if len(available_notes) == 0:
#             break
#         max_note = max(available_notes)
#         if amount >= max_note:
#             amount -= max_note
#             counter += 1
#         available_notes.pop()
#     print(amount, counter)


amount = 2750
counter = 0
#while len(available_notes) != 0 or amount != 0:
max_note = max(available_notes)
# while True:
#     # if amount < max_note:
#     #     print(amount)
#     #     available_notes.remove(max_note)
#     #     max_note = max(available_notes)
#     #     amount -= max_note
#     #     counter += 1
#     #     print(amount)
#     amount -= max_note
#     counter += 1
#     print(amount)
#     if amount == max_note or amount < 0:
#         amount -= max_note
#         counter += 1
#         break
# print(counter)
counter = 0
while max_note < amount:
    amount -= max_note
    while amount < max_note:
        available_notes.remove(max_note)
        max_note = max(available_notes)
    counter += 1

print(amount, counter)
#atm_withdraw(amount)
