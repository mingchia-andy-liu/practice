# Abstract Factory

## Intent

It defines an interface for creating all distinct products but leaves the actual product creation to concrete factory classes. Each factory type corresponds to a certain product variety.

## Applicability

- A system should be independent of how its products are created, composed, and represented.
- A system should be configured with one of multiple families of products.
- A family of related product objects is designed to be used together, and you need
to enforce this constraint.
- You want to provide a class library of products, and you want to reveal just their
interfaces, not their implementations

## Identification

The pattern is easy to recognize by methods, which return a factory object. Then, the factory is used for creating specific sub-components.


## Notes

- Normally a single instance of a `ConcreteFactory` class is created at run-time. This `ConcreteFactory` creates product objects having a particular implementation. To create different product objects, clients should use a different `ConcreteFactory`.
- `AbstractFactory` defers creation of product objects to its `ConcreteFactory` subclass.

## Elements

AbstractFactory
- declares an interface for methods that create abstract product objects.

ConcreteFactory
- implements the methods to create concrete product objects.

AbstractProduct
- declares an interface for a type of product object.

ConcreteProduct
- defines a product object to be created by the corresponding concrete
factory.
- implements the `AbstractProduct` interface.

Client
- uses only interfaces declared by `AbstractFactory` and `AbstractProduct` classes.

## Common Implementation

- Factories as singletons. An application typically needs only **one** instance of a ConcreteFactory per product family. So it's usually best implemented as a Singleton.


## Examples

1.
- `AbstractFactory`:
  - `CommunicationBaseFactory`
    - `initBluetooth`
    - `initWifi`
- `ConcreteFactory`: implements `AbstractFactory`
  - Prototype1 Factory
  - Prototype2 Factory
- `AbstractProduct`:
  - some product methods
- `ConcreteProduct`: implements `AbstractProduct`
  - Prototype1
    - `BluetoothCommunication`
    - `WifiCommunication`
  - Prototype2
    - `BluetoothV2Communication`
    - `WifiV2Communication`
- `Client`:
  - `var protoFactory1 = getPrototype(factory1)`
  - `var protoFactory2 = getPrototype(factory2)`
