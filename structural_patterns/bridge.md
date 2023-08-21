# Bridge is a structural design pattern that divides business logic or huge class into separate class hierarchies that can be developed independently.

## The abstraction is represented by the Shape class and its subclasses Circle and Square. The Shape class defines an abstract method draw() that all shapes must implement.

- Abstraction: Shapes
- Concrete Abstraction: Circle
- Concrete Abstraction: Square

## The implementation is represented by the Renderer interface and its concrete implementations VectorRenderer and RasterRenderer. The renderers define how the shapes are rendered in either vector or raster format.

- Implementation: Renderer
- Concrete Implementation: VectorRenderer
- Concrete Implementation: RasterRenderer

---

The Bridge pattern separates the abstraction of shapes from the implementation of rendering, allowing them to evolve independently. This way, you can add new shapes or rendering methods without modifying the existing code.

---

The primary reason for using the Bridge pattern is to separate the abstraction (high-level interface) from its implementation (how the actual work is done). This separation allows you to change and modify each part independently without affecting the other
