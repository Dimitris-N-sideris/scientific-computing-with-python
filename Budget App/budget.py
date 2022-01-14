class Category:

  def __init__(self, type):
      self.name = type 
      self.ledger = []

  def deposit(self, amount, description = ''):
    self.ledger.append({"amount":amount, "description":description})

  def withdraw(self, amount, description = ''):  
    if(self.check_funds(amount)):
      self.ledger.append({"amount":amount*(-1), "description":description})    
      return True
    return False

  def get_balance(self):
    balance = 0 
    for transaction in self.ledger:
      balance += transaction["amount"]
    return balance

  def transfer(self, amount, category):
    if(self.withdraw(amount, 'Transfer to '+category.name )):
      category.deposit(amount, 'Transfer from ' + self.name)
      return True
    return False
  
  def check_funds(self, amount):
    if(self.get_balance() >= amount):
      return True
    return False

  def get_withdrawals(self):
    sumWidrawals = 0 
    for transaction in self.ledger:
      if(transaction['amount'] < 0):
        sumWidrawals += transaction['amount']
    return sumWidrawals

  def __str__(self):

    objectToString = f"{self.name:*^30}\n"
    for transaction in self.ledger:
      left_aligned = transaction['description']
      if(len(left_aligned) > 23):
        left_aligned = left_aligned[0:23]
      objectToString += f"{left_aligned:<23}{transaction['amount']:>7.2f}\n"

    objectToString += f"Total: {self.get_balance()}"
    return objectToString

def create_spend_chart(categories):
  withdrawals = []
  for i in range(len(categories)):
    withdrawals.append(categories[i].get_withdrawals())
  sumWidrawals = sum(withdrawals)
  withdrawals[:] = [(x / sumWidrawals)*100 for x in withdrawals]
  chart = 'Percentage spent by category\n'
  for i in range(100, -10, -10):
    chart += f'{i:>3}|'
    for x in withdrawals:
      if(x>i):
        chart += ' o '
      else:
        chart += '   '
    chart += ' \n'
  chart += '    '
  for x in range(len(withdrawals)):
    chart += '---'
  chart += '-'
  nameLst = [x.name for x in categories]
  for i in range(len(max(nameLst, key=len))):
    chart += '\n    '
    for x in range(len(nameLst)):
      name = nameLst[x]
      if(len(name) > i):
        chart += f' {name[i]} '
      else:
        chart += '   '
    chart += ' '
  return chart