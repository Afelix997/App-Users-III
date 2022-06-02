class User:

    historical_posts= []
    
    def __init__(self,name,email,age):
        self.historical_posts=[]
        self.name= name
        self.email= email
        self.age= age

    def add_post(self,msg):
        self.historical_posts.append(f'{self.name} said: "{msg}"')
        User.historical_posts.append(f'{self.name} said: "{msg}"')
        return f'{self.name} said: "{msg}"'

