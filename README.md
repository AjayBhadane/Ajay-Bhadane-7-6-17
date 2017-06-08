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
Here is another way to use it
---

1. The Cache class has all the CRUD methods
2. Methods-->
    
    run() : Runs the CLI to interact with database
    
    `create_element(id,name,math_marks,science_marks)`: Creates a new element in the cache and stores the passes values 
    into the cache.If the the list size exceeds 20 elements the least accessed element is deleted and new element is 
    added at the end of the list.
      
    `read_element(id)`: Returns the element with the given id back.
    
    `update_element(id, name, math_marks, science_marks)` : Updates the element with the passed id with the passed data. 
     
    `remove_element(id)` : Removes the element with the given id.
    
    `upload_to_file()` : Sorts the cache according to the total of marks and stores the result back to file.
     
     Here is an example:
     ---             
     ````
     def main():
        cache = Cache() #Make new Cache object 
        student = cache.read_element(1) #Get the element with id=1
        print(student['id'], student['name'], student['math_marks'], student['science_marks']) #Print the details of 
        students
         
        cache.update_element(1, 'Ajay', 85, 97) #Update the element with id=1 with passed values
        student = cache.read_element(1) #Fetch new values
        print(student['id'], student['name'], student['math_marks'], student['science_marks']) #Print new values
        
        cache.remove_element(5)
        cache.upload_to_file()
        
    if __name__ == "__main__":
        main()
     ````
   

How the data is sorted
===
Data is sorted as the total of the marks of both the subjects arranged in ascending order.
    
    
    
    


