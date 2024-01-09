#simple opp in Python
#This is very easy project

class Student:
    def __init__(self,id,name, department, course,skill):
        self.id = id
        self.name = name
        self.department = department
        self.course = course
        self.skill = skill

def record(id,name, department, course,skill):
    print("       -----------------------------------------------")
    print("  \n                   STUDENT RECORD")
    print("  \n              Student Number  :" , id)
    print("              FullName        :" , name)
    print("              Department      :", department)
    print("              Course          :", course)
    print("              Skill           :", skill)
    print("       ------------------------------------------------")

while True:
        student = ["JOHN DOE", 
                             "THOMAS BUTTON",
                             "THOMPSON WILL",
                             "SPONGEBOB SQUAREPANTS",
                             "PATRICK STAR"]
                             
        print("\n                 LIST OF STUDENT\n")
        
        for stud in student:
            print("                 ",stud)
          
       
        ch = input("\n              Enter Name with uppercase:")
       
        if ch == "JOHN DOE":
            Student1 = Student(1521, "John Doe", "CCJ", "BSCRIM","Hardware")
            record(Student1.id, 
            Student1.name, 
            Student1.department, 
            Student1.course, 
            Student1.skill)
       
        elif ch == "THOMAS BUTTON":
           Student2 = Student(1522, "Thomas Button", "CCJ", "BSCRIM", "Hardware")
           record(Student2.id,
           Student2.name,
           Student2.department,
           Student2.course,
           Student2.skill)
                  
        elif ch == "THOMPSON WILL":
           Student3 = Student(1523, "Thompson Will", "CCJ", "BSCRIM", "Hardware")
           record(Student3.id,
                   Student3.name,
                   Student3.department,
                   Student3.course,
                   Student3.skill)
              
        elif ch == "SPONGEBOB SQUAREPANTS":
             Student4 = Student(1524, "SpongeBob SquarePants","IT","BSIT","Design")
             record(Student4.id,
                           Student4.name,
                           Student4.department,
                           Student4.course,
                           Student4.skill)
                           
        elif ch == "PATRICK STAR":
            Student5 = Student(1525,"Patrick Star", "IT","BSIT","Programming")
            record(Student5.id,
                          Student5.name,
                          Student5.department,
                          Student5.course,
                          Student5.skill)
                          
     
        else:
           print("  \n         \t         No Record")