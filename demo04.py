import os

def main():
    users = [{
        'name': 'john',
        'age': 25
    }, {
        'name': 'marry',
        'age': 32
    }, {
        'name': 'Simon',
        'age': 27
    }]
    print(users)
    # usernames = [user['name'] for user in users]
    # userage = [user['age']for user in users]
    for i in range(3):
      print(users[i])
   
    


           
        
        



if __name__ == '__main__':
    main()