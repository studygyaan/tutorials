from django.contrib.auth.models import User

class CustomUser(User):
    class Meta:
        proxy = True

    def custom_method_username(self):
        # Example custom logic: Check if the user's username contains 'admin'
        if 'admin' in self.username.lower():
            return f"{self.username} is an admin user."
        else:
            return f"{self.username} is a regular user."
    
    def custom_method_birthdate(self):
        # Example custom logic: Calculate the user's age based on birthdate
        from datetime import date

        if self.birthdate:
            today = date.today()
            age = today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
            return f"{self.username} is {age} years old."
        else:
            return f"The birthdate for {self.username} is not available."