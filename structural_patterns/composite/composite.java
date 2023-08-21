package composite;

//The Composite design pattern is a structural design pattern that is used to create hierarchical structures of objects while treating individual objects and compositions of objects uniformly.
//For tree-like structures 
import java.util.ArrayList;
import java.util.List;

interface OrganizationalUnit {
    void printDetails();
}

class Employee implements OrganizationalUnit {
    private String name;

    public Employee(String name) {
        this.name = name;
    }

    @Override
    public void printDetails() {
        System.out.println("Employee: " + name);
    }
}

class Department implements OrganizationalUnit {
    private String name;
    private List<OrganizationalUnit> units;

    public Department(String name) {
        this.name = name;
        units = new ArrayList<>();
    }

    public void addUnit(OrganizationalUnit unit) {
        units.add(unit);
    }

    @Override
    public void printDetails() {
        System.out.println("Department: " + name);
        for (OrganizationalUnit unit : units) {
            unit.printDetails();
        }
    }
}

public class composite {
    public static void main(String[] args) {
        Employee emp1 = new Employee("John");
        Employee emp2 = new Employee("Alice");
        Employee emp3 = new Employee("Bob");

        Department engineering = new Department("Engineering");
        engineering.addUnit(emp1);
        engineering.addUnit(emp2);

        Department sales = new Department("Sales");
        sales.addUnit(emp3);

        Department company = new Department("Our Company");
        company.addUnit(engineering);
        company.addUnit(sales);

        company.printDetails();
    }
}