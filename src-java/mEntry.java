import java.io.Serializable;

/**
 * Created by Ajay on 6/8/2017.
 */
public class mEntry<K, V> implements Serializable{
    private K key;
    private V value;

    public mEntry(K key, V value){
        this.key = key;
        this.value = value;
    }

    public K getKey(){
        return this.key;
    }

    public V getValue(){
        return this.value;
    }

    public void setValue(V value){
        this.value = value;
    }
}
