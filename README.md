# Ajay-Bhadane-7-6-17

The Cache file in the src folder contains a class named Cache. That is my implementation of cache.

Data structure used
===
Data structure used here is a python Dictionary(Hash Table) to store the details of one student.
Such more instances of Dictionaries are stored in a list i.e for every student detail there is a object in the list.
All the above stated procedure is done at runtime
    
Where data is stored
===    
Offline the data is stored in a '.xml' file.
And it is loaded into the data structure when Cache class is instantiated.
For successful loading of data into the data structure the data file must be in the same directory as the file
containing the Cache file.
    
How to use the class
===    
Here is an implementation of the class.
---
    
1. This will run the cache.run() which is a CLI to add data to the file. 
2. Upon entering `Exit` all the data will be stored back to the `data.xml` file in a sorted manner.

```
def main():
    cache = Cache()
    cache.run()
    
if __name__ == "__main__":
    main()
```
    
    
    
    


