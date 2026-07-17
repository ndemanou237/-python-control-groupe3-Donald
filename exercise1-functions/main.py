import statistics
def get_statistics(numbers):
    
    minimum = min(numbers)
    maximum = max(numbers)
    average = statistics.mean(numbers)
    print(f'le minimun est {minimum}, le maximum est {maximum}, et la moyenne est {average}')

def sum_all(*args):
    return sum(args)

def greet(name, greeting="Hello"):
    print(f'{greeting} {name}')  

def factorial(n):
    if(n <= 1):
        return 1
    else:
        return n * factorial(n-1)
      
def print_profile(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

def build_report(title, author="Unknown", *tags, status="draft", **extra_info):
    print(f'the title is {title}')
    print(f'author : {author}')
    print(f'les arg: {tags}')
    print(f'status: {status}')
    print(f'{extra_info}')
  


get_statistics([10,2,5])
# print(sum_all(12,2))  
# greet('donald')
# print(factorial(5))
# print_profile(name="Alice", age=20, city="Douala")
# build_report("stage")
# build_report("stage", author="donald")
# build_report("stage", status="completed")
# build_report("stage", city='bafoussam')
# build_report("stage", "ndem", "text")


