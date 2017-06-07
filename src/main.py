from xml.etree import ElementTree

class Cache:

    max_capacity = 20

    def __init__(self):
        all_students = ElementTree.parse('data.xml').findall('student')
        self.data = []
        for student in all_students:
            data_element = {
                'id': int(student.attrib['id']),
                'name': student.attrib['name'],
                'math_marks': int(student.attrib['math_marks']),
                'science_marks': int(student.attrib['science_marks']),
            }
            self.data.append(data_element)

    def run(self):
        keep_running = True
        while keep_running:
            choice = input("Enter your choice: ")

            if choice == 'Add':
                self.add_element()
            elif choice == 'Remove':
                self.remove_element()
            elif choice == 'Get':
                self.return_element()
            elif choice == 'CRUD':
                self.CRUD()
            elif choice == 'Help':
                self.display_help()
            elif choice == 'Exit':
                keep_running = False
            else:
                print("Invalid choice!")


def main():

    cache = Cache()
    cache.run()


if __name__ == "__main__":
    main()
