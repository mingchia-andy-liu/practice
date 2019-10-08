using System;

namespace day_1
{
    public class ConcreteFactory2: IAbstractFactory
    {
        // family A
        public IAbstractProductA CreateProductA() {
            return new ConcreteProductA2();
        }

        // family B
        public IAbstractProductB CreateProductB() {
            return new ConcreteProductB2();
        }
    }
}
