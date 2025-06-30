def greeting(name, course):
    print(f'Welcome {name} to {course}')

if __name__ == "__main__":
  guest_name = input('name: ')
  course = input('course: ')
  greeting(guest_name, course) 