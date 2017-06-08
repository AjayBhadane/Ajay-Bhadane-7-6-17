from xml.etree import ElementTree


class Cache:
    max_capacity = 8

    def __init__(self):
        self.data = []
        self.__load_from_file()
        self.visit_paid = 0

    def __load_from_file(self):
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
            choice = input('\nOptions are "Create", "Read", "Update", "Delete", "Exit", ""Size \nEnter your choice:')

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

            elif choice == 'Size':

                print(len(self.data))

            else:
                print("Invalid choice!")

    def create_element(self, _id, name, math_marks, science_marks):
        if len(self.data) < self.max_capacity:
            self.__add_element(_id, name, math_marks, science_marks)
        else:
            foo = []
            for student in self.data:
                foo.append(student['visits_paid'])

            _min = min(foo)

            for i in range(0, len(self.data)):
                if self.data[i]['visits_paid'] == _min:
                    self.remove_element(self.data[i]['id'])
                    self.__add_element(_id, name, math_marks, science_marks)
                    break

    def __add_element(self, _id, name, math_marks, science_marks):
        try:
            self.data.append({
                'id': _id,
                'name': name,
                'math_marks': math_marks,
                'science_marks': science_marks,
                'visits_paid': 0
            })
        except ValueError:
            print('invalid input')

    def read_element(self, _id):
        self.visit_paid += 1
        for i in range(0, len(self.data)):
            if self.data[i]['id'] == _id:
                self.data[i]['visits_paid'] = int(self.visit_paid)
                print(self.data[i])
                return self.data[i]

        raise KeyError("No such id")

    def update_element(self, _id, name, math_marks, science_marks):
        self.visit_paid += 1
        for i in range(0, len(self.data)):
            if self.data[i]['id'] == _id:
                self.__add_element(_id, name, math_marks, science_marks)
                self.data[i]['visits_paid'] = self.visit_paid
                return

        raise KeyError("No such id")

    def remove_element(self, _id):
        for i in range(0, len(self.data)):
            if self.data[i]['id'] == _id:
                del self.data[i]
                return

        raise KeyError("No such id")

    def upload_to_file(self):
        root = ElementTree.Element('students')

        self.__sort()

        for student in self.data:
            ElementTree.SubElement(root, "student", id=str(student['id']), name=student['name'],
                                   math_marks=str(student['math_marks']), science_marks=str(student['science_marks']))

        ElementTree.ElementTree(root).write("data.xml")

    def __sort(self):
        foo = []
        for student in self.data:
            foo.append(student['math_marks'] + student['science_marks'])

        foo.sort()
        print(foo)
        self.__get_sorted_data(foo)

    def __get_sorted_data(self, foo):

        sorted_data = []

        for i in range(0, len(self.data)):
            for student in self.data:
                if foo[i] == (student['math_marks'] + student['science_marks']):
                    sorted_data.append(student)
                    break

        self.data = sorted_data



def main():
    cache = Cache()
    cache.run()


if __name__ == "__main__":
    main()
