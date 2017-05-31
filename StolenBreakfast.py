
"""
Your company delivers breakfast via autonomous quadcopter drones. And something mysterious has happened.
Each breakfast delivery is assigned a unique ID, a positive integer. When one of the company's 100 drones takes off with a delivery, the delivery's ID is added to a list, delivery_id_confirmations. When the drone comes back and lands, the ID is again added to the same list.

After breakfast this morning there were only 99 drones on the tarmac. One of the drones never made it back from a delivery. We suspect a secret agent from Amazon placed an order and stole one of our patented drones. To track them down, we need to find their delivery ID.

Given the list of IDs, which contains many duplicate integers and one unique integer, find the unique integer.
"""







x=[100,345,2,345,2,100,54,67,89,67,54,89,33]


def myunique(x):
  unique_id=0
  for i in x:
    unique_id^=i
  return unique_id
  
print(myunique(x)) # unique number is 33