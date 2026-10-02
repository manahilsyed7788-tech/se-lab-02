def login(email, password):
    if email == "student@uet.edu.pk" and password == "12345":
        return "Login Successful!"
    else:
        return "Invalid email or password."

# Test the function
print(login("student@uet.edu.pk", "12345"))