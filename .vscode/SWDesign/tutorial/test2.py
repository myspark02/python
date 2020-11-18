from address import Address
from course import Course
from enroll import Enroll
from professor import Professor
from student import Student

address = Address('Korea', "KB", "Daegu", "Bukgu", "754023  ")
std = Student('P', 'SC', 1974, '010-123', address)    
professor = Professor('SC', 'Park', 1974, '010-223', address, 8000)

course = Course('Python', 'p12', 200, 30, professor)    
enroll = Enroll(std, course)