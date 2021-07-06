from itertools import permutations
from functools import lru_cache

def is_perfect_cube(number):
    if int(number ** (1.0 / 3.0)) ** 3 == number or (int(number ** (1.0 / 3.0)) + 1) ** 3 == number:
        return True
    else:
        return False




def print_cubes(a, b):
    perfect_cubes = [x**3 for x in range(1,10001)]

    cube_list = []
    for x in perfect_cubes:
        if x >= a and x <= b:
            cube_list.append(str(x)) 
    return(', '.join(cube_list))   




@lru_cache(maxsize = None)
def smallest_number(): 
    perfect_cubes = [x**3 for x in range(1,10001)]
        
    for value in perfect_cubes:               
        p = [''.join(p) for p in permutations(str(value))]
        filtered = [x for x in set(list(map(int, p))) if len(str(x)) == len(str(value)) and is_perfect_cube(x)]
        if len(filtered) == 3:
            filtered.sort()
            return(filtered[0])



def menu():
    while True:  
        print("\nMAIN MENU")  
        print("1. Check if input is perfect cube")  
        print("2. Generate perfect cubes within a range")  
        print("3. Find the smallest perfect cube whose exactly 3 permutations are also cubes") 
        print("4. Exit") 
        choice = int(input("Enter Choice: "))  
        
        if choice == 1:
            num = int(input("Enter an integer between 1 and 1e12: ")) 
            if num >= 1 and num <= 1000000000000 :
                if is_perfect_cube(num):
                    print(str(int(num)) + " is a valid cube")
                else:
                    print(str(int(num)) + " is not a valid cube")
            else:
                print("Enter a valid input")
            
        elif choice == 2:
            m = int(input("Enter the starting integer of range (min is 1): "))
            n = int(input("Enter the ending integer of range (max is 1e12): "))
            if m >= 1 and m <= 1000000000000 and n >= 1 and n <= 1000000000000 :
                print("Perfect cubes in the given range are " + print_cubes(m,n))
            else:
                print("Enter a valid input")
            
        elif choice == 3: 
            print("Takes a while running for the first time")
            print(smallest_number())
        
        elif choice == 4:
            break
            
        else:
            print("Enter a valid choice")








