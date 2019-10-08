using System;

namespace day_1
{
    public class ConcreteFactory1: IAbstractFactory
    {
        // family A
        public IAbstractProductA CreateProductA() {
            return new ConcreteProductA1();
        }

        // family B
        public IAbstractProductB CreateProductB() {
            return new ConcreteProductB1();
        }
    }
}
