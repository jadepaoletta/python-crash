class User(object):

    def __init__(self, first_name, last_name, email, summary):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.summary = summary
        self.login_attempts = 0


    def describe_user(self):
        """Prints user's name and summary"""
        print "{} {}: {}".format(self.first_name, self.last_name, self.summary)


    def greet_user(self):
        """Prints a personalized greeting to the user"""
        print "Hello {} {}, it's so nice to meet you!".format(self.first_name, self.last_name)


    def get_login_attempts(self):
        """Returns the number of login attempts for the user"""
        return self.login_attempts


    def increment_login_attempts(self):
        """Increments the number of login attempts by 1"""
        self.login_attempts += 1


    def reset_login_attempts(self):
        """Resets the value of login attempts to 0"""
        self.login_attempts = 0


class Admin(User):
    priveleges = ["Can delete users", "Can add post", "Can add post"]
    
    def __init__(self, first_name, last_name, email, summary):
        super(Admin, self).__init__(first_name, last_name, email, summary)


    def show_priveleges(self):
        """prints a list of admin priveleges"""
        for privelege in self.priveleges:
            print privelege


