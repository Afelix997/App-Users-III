from users.User_file import User

class FreeUser(User):
    
    def add_post(self,msg):
        
        if len(self.historical_posts) < 2:
            self.historical_posts.append(f'{self.name} said: "{msg}"')
            User.historical_posts.append(f'{self.name} said: "{msg}"')

            
        else:
            return print("You've reached your 2 post limit!")
        return f'{self.name} said: "{msg}"'


