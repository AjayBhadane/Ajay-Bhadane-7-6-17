Ajay-Bhadane-7-6-2017
===

Assumptions
---
1. The initial size of the Map is 20 elements
2. The Map is a Hash-map.
 
 Implementation
 ===
 The class is a generic one. It has two data-type inputs a Key and a Value.
 
 Hereon Key = K, Value = V
 
 Methods:
 ---
 1. `public synchronized V get(K key)`: This method returns the value associated with the given Key.
 2. `public synchronized void put(K key, V value)`: This method stores the value in the element of the map matching the Key.
 3. `public int getSize()`:Returns the current size of the Map
 4. `public Set<K> keySet()`: Returns a Set object with all the keys inside it.
 5. `public void removeKey(K key)`:Removes the element corresponding to the given Key.
 6. `public void saveMap(String path)`:Saves the map on the disk with location string provided in path.
 7. `public Map<K, V> retrieveMap(String path)`:returns the map object from the file path specified

Here is a simple example:
---
````
public class Main {

    public static void main(String[] args) {
        Map<Integer, String> map = new Map<>();
        map.put(1,"one");
        map.put(2,"two");

        System.out.println(map.get(1));
        map.saveMap("map.ser");
        map = map.retrieveMap("map.ser");
        System.out.println(map.get(2));
    }
}
````
The output is:

one

two

The above code creates a `Map` object called `map`.
 
First the put method is called twice on the object to add two elements 'one' and 'two' with Keys '1' and '2'.

The map is then saved on the disk and retrieved again and the value of the second element is printed.