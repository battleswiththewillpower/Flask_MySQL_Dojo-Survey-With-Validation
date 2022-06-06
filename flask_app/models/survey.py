from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location= data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # @classmethod
    # def get_all(cls):
    #     query = "SELECT * FROM dojos;"
    #     results = connectToMySQL('dojo_survey_schema').query_db(query)
    #     dojos = []
    #     for dojo in results:
    #         dojos.append( cls(dojo) )
    #     return dojos

    # ... other class methods
    # class method to save our friend to the database
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO dojos ( name , location , comment , created_at, updated_at ) VALUES ( %(name)s , %(location)s , %(comment)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('dojo_survey_schema').query_db( query, data )


    @classmethod
    def get_one(cls):
        query = "SELECT * FROM dojos ORDER BY dojos.id DESC LIMIT 1;"
        result = connectToMySQL('dojo_survey_schema').query_db(query)
        return cls(result[0])

    @staticmethod
    def validate_dojo(dojo):
        is_valid = True
        if len(dojo['name']) < 3:
            is_valid = False
            flash("Name must be at least 3 characters!")
        if len(dojo['location']) < 1:
            is_valid = False
            flash("I told you at least 3 characters!")
        if 'language' not in dojo:
            is_valid = False
            flash("Must choose a favorite language.")
        if len(dojo['comment']) < 3:
            is_valid = False
            flash("You really don't listen HUH?")
            
        return is_valid