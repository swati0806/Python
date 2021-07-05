def foo(L_foo):
    L_foo.append(1)
    print(L is L_foo)
    
L = [0]
print(f'L before: {L}')
foo(list(L))
print(f'L after: {L}')

