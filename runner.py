from users.FreeUser import FreeUser
from users.User_file import User
from users.PremiumUser import PremiumUser

bob= FreeUser('bob','bob@email.com',22)
bill= PremiumUser('bill','bill@email.com',22)
bob.add_post('Hello')
bob.add_post('Wow')
bob.add_post('Hello')

bill.add_post('Hello')
bill.add_post('Wow')
bill.add_post('Hello')
print(bob.historical_posts)
print(bill.historical_posts)
print(User.historical_posts)

