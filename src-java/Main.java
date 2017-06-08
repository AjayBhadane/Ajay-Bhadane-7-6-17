
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