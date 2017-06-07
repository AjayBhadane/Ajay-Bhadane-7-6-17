class Cache:

    max_capacity = 20

    def __init__(self):
        self.data_element = {
            'id': 1,
            'name': "Ajay Bhadane",
            'math_marks': 100,
            'science_marks': 100,
        }

    def run(self):
        print(self.data_element['name'])


def main():

    cache = Cache()
    cache.run()


if __name__ == "__main__":
    main()
