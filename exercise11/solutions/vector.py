from dataclasses import dataclass


def apply_binary_operator(operator: str, operand1: float,
                          operand2: float) -> float:
    match operator:
        case "+":
            return operand1 + operand2
        case "-":
            return operand1 - operand2
        case "*":
            return operand1 * operand2
    raise ValueError(f"Unknown binary operator: {operator}")


@dataclass
class Vector:
    """
    Represents an n-dimensional vector.

    Invariants:
        len(values) > 0

    """
    __values: list[float]

    def __post_init__(self):
        self.__dim = len(self.__values)
        self.__length = sum(x ** 2 for x in self.__values) ** 0.5
        assert self.dim > 0, 'Vector must have at least one dimension'

    @property
    def dim(self) -> int:
        return self.__dim

    @property
    def length(self) -> float:
        return self.__length

    @property
    def values(self) -> list[float]:
        return self.__values

    def operate_binary(self, operator: str,
                       other: 'Vector | float') -> 'Vector':
        match other:
            case Vector():
                assert self.dim == other.dim, (
                    f"Vector dimension mismatch: {self.dim} != {other.dim}")
                return Vector([apply_binary_operator(operator, x, y)
                               for x, y in zip(self.__values, other.__values)])
            case float() | int():
                return Vector([apply_binary_operator(operator, x, other)
                               for x in self.__values])
        raise TypeError(f"Cannot perform operation {operator} "
                        f"between Vector and {type(other)}")

    def __str__(self) -> str:
        return str(self.dim) + "D vector: " + str(self.__values)

    def __pos__(self) -> 'Vector':
        return self

    def __neg__(self) -> 'Vector':
        return Vector([-x for x in self.__values])

    def __add__(self, other: 'Vector | float') -> 'Vector':
        return self.operate_binary("+", other)

    def __sub__(self, other: 'Vector | float') -> 'Vector':
        return self.operate_binary("-", other)

    def __mul__(self, other: 'Vector | float') -> 'Vector':
        return self.operate_binary("*", other)

    def __radd__(self, other: 'Vector | float') -> 'Vector':
        return self.operate_binary("+", other)

    def __rsub__(self, other: 'Vector | float') -> 'Vector':
        return -self.operate_binary("-", other)

    def __rmul__(self, other: 'Vector | float') -> 'Vector':
        return self.operate_binary("*", other)


if __name__ == "__main__":
    print(apply_binary_operator("-", 5, 3))
    v1 = Vector([1, 2, 3])
    print(v1)
    v1 + 6
