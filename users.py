# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the users table from our database

class USER: 
    DB = 'users_cr_practice'
    def __init__(self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(cls.DB).query_db(query)
        # Create an empty list to append our instances of friends
        users = []
        # Iterate over the db results and create instances of friends with cls.
        for user in results:
            users.append( cls(user) )
        return users
    
    #route to save submitted data by adding it to our DB
    @classmethod
    def save(cls, data):
        query = """INSERT INTO users (first_name, last_name, email)
                VALUES (%(first_name)s, %(last_name)s, %(email)s );"""
        
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result
    

    # update edit action to save revised user data for a specific users id
    @classmethod
    def update(cls, data):
        #must correct on workbench first to insert correct query text*
        query = """
        UPDATE users
        SET first_name = %(first_name)s , last_name = %(last_name)s , email = %(email)s
        WHERE id = %(id)s ;
        """
        
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result
    
    # get_one action to view specific user id
    @classmethod
    def get_one(cls, data):
        #must correct on workbench first to insert correct query text*
        query = """SELECT * 
        FROM users
        WHERE id = %(id)s;"""
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(cls.DB).query_db(query, data)
        # Create an empty list to append our instances of single user
        singleUser = cls(results[0])
        
        return singleUser

    # action to delete specific user id
    @classmethod
    def delete(cls, data):
        query = """DELETE FROM users 
        WHERE id = %(id)s"""
        #temp dict to complete the query we have
        # data={'id':id}

        result = connectToMySQL(cls.DB).query_db(query, data)
        return result