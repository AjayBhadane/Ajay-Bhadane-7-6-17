from xml.etree import ElementTree

class Cache:

    max_capacity = 20

    def __init__(self):
        self.load_from_file()

    def load_from_file(self):
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
            choice = input('\nOptions are "Create", "Read", "Update", "Delete", "Exit" \nEnter your choice:')

            if choice == 'Create':
                self.add_element()
            elif choice == 'Read':
                self.read_element()
            elif choice == 'Update':
                self.update_element()
            elif choice == 'Delete':
                self.remove_element()
            elif choice == 'Exit':
                self.upload_to_file()
                keep_running = False
            else:
                print("Invalid choice!")

    def add_element(self):

        self.data.append({
            'id': int(input("Enter id:")),
            'name': input("Enter name:"),
            'math_marks': int(input("Enter math marks:")),
            'science_marks': int(input("Enter science marks")),
        })

    def upload_to_file(self):
        root = ElementTree.Element('students')

        for student in self.data:
            ElementTree.SubElement(root, "student", id=str(student['id']), name=student['name'],math_marks=str(student['math_marks']),science_marks=str(student['science_marks']))

        ElementTree.ElementTree(root).write("data.xml")

def main():

    cache = Cache()
    cache.run()


if __name__ == "__main__":
    main()
