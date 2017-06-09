from src.CacheImp.Cache import Cache

def main():
    cache = Cache()  # Make new Cache object
    student = cache.read_element(4)  # Get the element with id=1
    print(student['id'], student['name'], student['math_marks'], student['science_marks'])  # Print the details of students

    cache.update_element(4, 'Ajay', 85, 97)  # Update the element with id=1 with passed values
    student = cache.read_element(9)  # Fetch new values
    print(student['id'], student['name'], student['math_marks'], student['science_marks'])  # Print new values

    cache.remove_element(4)
    cache.upload_to_file()


if __name__ == "__main__":
    main()
