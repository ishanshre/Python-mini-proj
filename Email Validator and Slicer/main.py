import re


def validate_email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    if re.fullmatch(regex, email):
        return email
    else:
        return None


def get_domain(email):
    email = validate_email(email)
    if email:
        try:
            
            domain = email[email.index("@")+1:]
            return domain
        except ValueError:
            print("Please enter the correct email")
    else:
        print("please enter a valid email")

def main():
    while True:
        email = input("Enter your email address: ")
        domain = get_domain(email)
        if domain:
            print(f"domain = {domain}")
            break;

if __name__ == "__main__":
    main()