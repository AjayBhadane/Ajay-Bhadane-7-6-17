from xml.etree import ElementTree


class Cache:
    max_capacity = 20

    def __init__(self):
        self.data = []
        self.load_from_file()
        self.visit_paid = 0

    def load_from_file(self):
        all_students = ElementTree.parse('data.xml').findall('student')

        for student in all_students:
            data_element = {
                'id': int(student.attrib['id']),
                'name': student.attrib['name'],
                'math_marks': int(student.attrib['math_marks']),
                'science_marks': int(student.attrib['science_marks']),
                'visits_paid': 0,
            }
            self.data.append(data_element)

    def run(self):
        keep_running = True
        while keep_running:
            choice = input('\nOptions are "Create", "Read", "Update", "Delete", "Exit" \nEnter your choice:')

            if choice == 'Create':
                _id = int(input("Enter id:"))
                name = input("Enter name:")
                math_marks = int(input("Enter math marks:"))
                science_marks = int(input("Enter science marks:"))

                self.create_element(_id, name, math_marks, science_marks)
            elif choice == 'Read':

                _id = int(input("Enter id: "))

                self.read_element(_id)
            elif choice == 'Update':

                _id = int(input("Enter id: "))
                name = input("Enter name: ")
                math_marks = int(input("Enter math marks: "))
                science_marks = int(input("Enter science marks: "))

                self.update_element(_id, name, math_marks, science_marks)

            elif choice == 'Delete':

                _id = int(input("Enter id:"))
                self.remove_element(_id)

            elif choice == 'Exit':

                self.upload_to_file()
                keep_running = False

            else:
                print("Invalid choice!")

    def create_element(self, _id, name, math_marks, science_marks):
        if len(self.data) < 20:
            self.__add_element(_id, name, math_marks, science_marks)
        else:
            foo = []
            for student in self.data:
                foo.append(student['visits_paid'])

            _min = min(foo)

            for i in range(0, len(self.data)):
                if self.data[i]['visits_paid'] == _min:
                    self.remove_element(self.data[i])
                    break

    def __add_element(self, _id, name, math_marks, science_marks):
        self.data.append({
            'id': _id,
            'name': name,
            'math_marks': math_marks,
            'science_marks': science_marks,
        })

    def read_element(self, _id):

        for i in range(0, len(self.data)):
            if self.data[i]['id'] == _id:
                self.data[i]['visits_paid'] = int(self.visit_paid)
                print(self.data[i])
                return self.data[i]

        raise KeyError("No such id")

    def update_element(self, _id, name, math_marks, science_marks):
        for i in range(0, len(self.data)):
            if self.data[i]['id'] == _id:
                self.data[i]['name'] = name
                self.data[i]['math_marks'] = math_marks
                self.data[i]['science_marks'] = science_marks
                self.data[i]['visits_paid'] = self.visit_paid
                return

        raise KeyError("No such id")

    def remove_element(self, _id):
        for i in range(0, len(self.data)):
            if self.data[i]['id'] == _id:
                print(self.data[i])
                del self.data[i]
                return

        raise KeyError("No such id")

    def upload_to_file(self):
        root = ElementTree.Element('students')

        for student in self.data:
            ElementTree.SubElement(root, "student", id=str(student['id']), name=student['name'],
                                   math_marks=str(student['math_marks']), science_marks=str(student['science_marks']))

        ElementTree.ElementTree(root).write("data.xml")


def main():
    cache = Cache()
    cache.run()


if __name__ == "__main__":
    main()
