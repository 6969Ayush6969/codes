class user: 
    def __init__(self,username,name,email):
        self.username=username
        self.name=name
        self.email=email
    def __repr__(self) -> str:
        return 'user(name:{},username:{},email:{})'.format(self.name,self.username,self.email)
    def __str__(self) -> str:
        return self.__repr__()
class database:
    def __init__(self):
        self.users=[]
    def insert(self,user):
        l=0
        r=len(self.users)-1 
        while l<=r:  
            mid=(l+r)//2   
            if user.username<self.users[mid].username:
                r=mid-1
            elif user.username>self.users[mid].username:
                l=mid+1
            else:
                self.users.insert(mid,user)
                return 
        self.users.insert(l,user)
    def find(self,Username):
        l=0
        r=len(self.users)-1 
        while l<r :                   
            mid=(l+r)//2
            if self.users[mid].username>Username:
                r=mid-1
            elif self.users[mid].username<Username:
                l=mid+1
            else:
                return self.users[mid]
        return self.users[l]
    def update(self,user):
        search=self.find(user.username)
        search.name,search.email=user.name,user.email
    def list_all(self):
        return self.users
'''
                TEST CASES
database1=database()
hemanth = user('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = user('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = user('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
sonaksh = user('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
cheeku = user('cheeku', 'cheeku Goel', 'cheeku@example.com')

                INSERTION
database1.insert(hemanth)
database1.insert(jadhesh)
database1.insert(siddhant)
database1.insert(cheeku)

                FINDING
f=database1.find('siddhant')
print(f)

                UPDATING
database1.update(user('siddhant','ayush','ayush@gmail.com')) #username is same and cant be updated

                LISTING 
l=database1.list_all()   
print(l)  

'''