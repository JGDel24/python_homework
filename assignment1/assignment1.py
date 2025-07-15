# Write your code here.
def hello():
    return 'Hello!'

def greet(name):
    return f"Hello, {name}!"

def calc(val1, val2, operation='multiply'):
    try:
        match operation:
            case 'add':
                return val1 + val2
            case 'subtract':
                return val1 - val2
            case 'multiply':
                return val1 * val2
            case 'divide':
                return val1 / val2
            case 'modulo':
                return val1 % val2
            case 'int_divide':
                return val1 // val2
            case 'power':
                return val1 **val2
            case _:
                return 'Invalid operation'
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"
    except Exception:
        return 'something went wrong' 

def  data_type_conversion(value, data_type): 
    try:
        if data_type == 'float':
            return float(value)
        elif data_type == 'int':
            return int(value)
        elif data_type == 'str':
            return str(value)
    except:
        return f"You can't convert {value} into a {data_type}."

def grade(*args):
    try:
        average = sum(args) / len(args)
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'
    except:
        return  "Invalid data was provided."

def repeat(string, count):
    solution = ""
    for _ in range(count):
        solution += string
    return solution

def student_scores(method, **kwargs):
    try:
        if method == 'best':
            return max(kwargs, key=kwargs.get)
        elif method == 'mean':
            return sum(kwargs.values())  / len(kwargs) 
    except:
        'Invalid Method'

def titleize(string):
    little_words = [ "a", "on", "an", "the", "of", "and", "is", "in"]
    words = string.lower().split()
    solution = []
    for i, word in enumerate(words):
        if i == 0 or i == len(word) -1:
            solution.append(word.capitalize())
        elif word in little_words:
            solution.append(word)
        else:
            solution.append(word.capitalize())
    return " ".join(solution) 

def hangman(secret, guess):
    solution = ""
    for letter in secret:
        if letter in guess:
            solution += letter
        else:
            solution += '_'
    return solution 

def pig_latin(sentence):
    vowels = 'aeiou'
    words = sentence.split()
    result = []

    for word in words:
        if word[0] in vowels:
            result.append(word + 'ay')
        elif word.startswith('qu'):
            result.append(word[2:] + 'quay')
        else:
            i = 0
            while i < len(word)  and word[i] not in vowels:
                if word[i] == 'q' and i + 1 < len(word) and word[i + 1] == 'u':
                    i += 2
                    break
                i += 1
            result.append(word[i:] + word[:i] + "ay")
    
    return " ".join(result)

                                           


        
        







