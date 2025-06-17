a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print("Равносторонний")
elif a == b != c or a == c != b or b == a != c or a != b == c:
    print("Равнобедренный")
elif a != b != c:
    print("Разносторонний")
