// Iterator is a behavioral design pattern that lets you traverse elements of a collection
// without exposing its underlying representation (list, stack, tree, etc.)

/*
1. Define the Iterator Interface , methods like `next()` `hasNext()`
2. Define the Aggregate Interface (represents collections of objects being iterated over)
3. Implement the Concrete Iterator 
4. Implement the Concrete Aggregate
5. Client Code → Use the iterator and aggregate classes in your client code to iterate over the collection without needing to know its internal structure.
 */

import java.util.ArrayList;
import java.util.List;

// Iterator interface
interface Iterator<T> {
    boolean hasNext();

    T next();
}

// ConcreteIterator implementing the Iterator interface
class ListIterator<T> implements Iterator<T> {
    private List<T> list;
    private int position = 0;

    public ListIterator(List<T> list) {
        this.list = list;
    }

    @Override
    public boolean hasNext() {
        return position < list.size();
    }

    @Override
    public T next() {
        if (hasNext()) {
            T element = list.get(position);
            position++;
            return element;
        }
        throw new IndexOutOfBoundsException("No more elements.");
    }
}

// Aggregate interface
interface IterableCollection<T> {
    Iterator<T> iterator();
}

// ConcreteAggregate implementing the IterableCollection interface
class ListCollection<T> implements IterableCollection<T> {
    private List<T> items = new ArrayList<>();

    public void addItem(T item) {
        items.add(item);
    }

    @Override
    public Iterator<T> iterator() {
        return new ListIterator<>(items);
    }
}

// Client code
public class IteratorPatternDemo {
    public static void main(String[] args) {
        ListCollection<String> collection = new ListCollection<>();
        collection.addItem("Item 1");
        collection.addItem("Item 2");
        collection.addItem("Item 3");

        Iterator<String> iterator = collection.iterator();
        while (iterator.hasNext()) {
            String item = iterator.next();
            System.out.println(item);
        }
    }
}
