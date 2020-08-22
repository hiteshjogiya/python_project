import re
class Validation:
    def validateemail(self,email):
        pattern = re.compile(r"[.A-Za-z0-9-]+@[A-Za-z.-]+[.A-Za-z0-9.-]")
        if(pattern.match(email)):
            return email
        else:
            print("Invalid Email...")
            return False
    def validatemobile(self,mo):
        pattern = re.compile(r"\d{10}")
        if(pattern.match(mo)):
            return mo
        else:
            print("Invalid Mobile Number...")
            return False
