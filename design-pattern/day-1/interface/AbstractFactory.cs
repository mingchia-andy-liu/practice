using System;

namespace day_1
{
    // The Abstract Factory interface declares a set of methods that return
    // different abstract products. These products are called a family and are
    // related by a high-level theme or concept.
    public interface IAbstractFactory
    {
        // family A
        IAbstractProductA CreateProductA();

        // family B
        IAbstractProductB CreateProductB();
    }
}
