import nltk
from nltk import WordNetLemmatizer, word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)


class PythonTutorialAgent:

    def __init__(self):
        self.topics = {
            "Basics": ["variables", "data types", "operators", "control structures", "type casting",
                              "input and output"],
            "data structures": ["lists", "tuples", "dictionaries", "sets", "list comprehensions",
                                "dictionary comprehensions"],
            "functions": ["defining functions", "arguments", "return values", "lambda functions", "function scope"],
            "object-oriented programming": ["classes", "objects", "inheritance", "polymorphism", "encapsulation",
                                            "abstraction", "magic methods"],
            "file handling": ["file operations", "reading and writing files", "working with CSV", "JSON handling",
                              "context managers", "binary file handling"],
            "advanced concepts": ["decorators", "generators", "recursion", "regular expressions", "iterators",
                                  "multithreading", "multiprocessing", "asynchronous programming"],
            "error handling": ["exceptions", "try-except blocks", "raising exceptions", "custom exceptions",
                               "debugging techniques", "assertions"],
            "functional programming": ["first-class functions", "higher-order functions", "map, filter, reduce",
                                       "closures", "partial functions", "anonymous functions"],
            "modules and packages": ["importing modules", "creating modules", "Python Standard Library",
                                     "third-party packages"],
            "testing": ["unit testing", "pytest", "mocking", "test-driven development"],
            "databases": ["SQLite", "MySQL", "PostgreSQL", "ORM"],
            "performance optimization": ["profiling code", "algorithm optimization", "memory optimization","memory management", "time complexity", "space complexity"
                                         "multithreading vs multiprocessing", "caching with functools.lru_cache",
                                         "efficient loops", "NumPy and vectorization", "compiling with Cython",
                                         "using concurrent.futures", "database indexing"]
        }

        self.exit_commands = ["exit", "quit", "stop", "bye", "goodbye"]
        self.knowledge_base = self.init_knowledge_base()
        self.current_topic = None
        self.current_subtopic = None
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))
        self.vectorizer = TfidfVectorizer()
        self.knowledge_base = self.init_knowledge_base()
        self.mode = "tutorial"  # Can be "tutorial" or "quiz"
        self.progress = {topic: {subtopic: False for subtopic in subtopics}
                         for topic, subtopics in self.topics.items()}
        self.quiz_questions = self.init_quiz_questions()
        self.showing_menu = False
    def init_knowledge_base(self):
        knowledge_base = {
            "basics": [
                {
                    "variables": {
                        "description": "Named references to values in memory",
                        "examples": {
                            "basic_variables": "# Variable assignment\nname = 'John'           # String\nage = 25               # Integer\nheight = 1.75         # Float\nis_student = True      # Boolean\n\n# Multiple assignment\nx, y, z = 1, 2, 3\n\n# Multiple references to same value\na = b = c = 0\n\n# Variable naming conventions\nstudent_name = 'Alice'    # Snake case (recommended)\nstudentName = 'Bob'       # Camel case (not recommended)\n_private = 'Hidden'       # Protected variable convention\nPI = 3.14159             # Constant convention",
                            "variable_scope": "# Global and local scope\nglobal_var = 'I am global'\n\ndef show_scope():\n    local_var = 'I am local'\n    print(global_var)    # Can access global\n    print(local_var)     # Can access local\n    \n    # Modifying global\n    global global_var\n    global_var = 'Modified'"
                        },
                        "best_practices": [
                            "Use descriptive names",
                            "Follow PEP 8 naming conventions",
                            "Use snake_case for variables",
                            "Use UPPERCASE for constants",
                            "Avoid global variables when possible"
                        ]
                    }
                },
                {
                    "data_types": {
                        "description": "Built-in types for storing different kinds of data",
                        "examples": {
                            "numeric_types": "# Integers\ncount = 42\nbig_num = 1_000_000    # Underscore for readability\n\n# Floating point\nprice = 19.99\nscientific = 1.23e-4\n\n# Complex numbers\ncomplex_num = 3 + 4j",
                            "strings": "# String creation\nsingle_quotes = 'Hello'\ndouble_quotes = \"Python\"\nmulti_line = '''Multiple\nline string'''\n\n# String operations\nname = 'Python'\nprint(name[0])      # First character: P\nprint(name[-1])     # Last character: n\nprint(name[2:4])    # Slice: th\nprint(f'I love {name}')  # f-string",
                            "collections": "# Lists (ordered, mutable)\nfruits = ['apple', 'banana', 'orange']\nnumbers = [1, 2, 3, 4, 5]\n\n# Tuples (ordered, immutable)\ncoords = (10, 20)\nsingle_item = (1,)  # Note the comma\n\n# Sets (unordered, unique)\nunique_nums = {1, 2, 3, 3}  # {1, 2, 3}\n\n# Dictionaries (key-value pairs)\nperson = {\n    'name': 'Aryan',\n    'age': 24,\n    'city': 'New York'\n}"
                        },
                        "best_practices": [
                            "Use appropriate type for data",
                            "Consider immutability when choosing types",
                            "Use list comprehensions for lists",
                            "Use sets for unique collections",
                            "Use dictionaries for key-value mappings"
                        ]
                    }
                },
                {
                    "operators": {
                        "description": "Symbols that perform operations on operands",
                        "examples": {
                            "arithmetic": "# Basic arithmetic\nx = 10\ny = 3\n\naddition = x + y        # 13\nsubtraction = x - y     # 7\nmultiplication = x * y  # 30\ndivision = x / y        # 3.3333...\nfloor_div = x // y      # 3\nmodulus = x % y         # 1\npower = x ** y          # 1000",
                            "comparison": "# Comparison operators\nx = 5\ny = 10\n\nequal = x == y           # False\nnot_equal = x != y       # True\ngreater = x > y          # False\nless = x < y             # True\ngreater_equal = x >= y    # False\nless_equal = x <= y      # True",
                            "logical": "# Logical operators\nx = True\ny = False\n\nand_result = x and y     # False\nor_result = x or y       # True\nnot_result = not x       # False"
                        },
                        "best_practices": [
                            "Use parentheses for complex expressions",
                            "Be careful with operator precedence",
                            "Use 'is' for None comparisons",
                            "Use 'in' for membership tests",
                            "Consider short-circuit evaluation"
                        ]
                    }
                },
                {
                    "control_structures": {
                        "description": "Statements that control the flow of program execution",
                        "examples": {
                            "if_statements": "# If-elif-else\nage = 18\n\nif age < 13:\n    print('Child')\nelif age < 20:\n    print('Teenager')\nelse:\n    print('Adult')\n\n# Conditional expression (ternary)\nstatus = 'Adult' if age >= 18 else 'Minor'",
                            "loops": "# For loop\nfor i in range(5):\n    print(i)    # 0 to 4\n\n# While loop\ncount = 0\nwhile count < 5:\n    print(count)\n    count += 1\n\n# Loop control\nfor i in range(10):\n    if i == 5:\n        continue    # Skip 5\n    if i == 8:\n        break       # Stop at 8\n    print(i)"
                        },
                        "best_practices": [
                            "Prefer for loops over while when possible",
                            "Use enumerate() for counting in loops",
                            "Keep indentation consistent",
                            "Use meaningful loop variables",
                            "Avoid deep nesting"
                        ]
                    }
                },
                {
                    "type_casting": {
                        "description": "Converting values from one type to another",
                        "examples": {
                            "explicit_casting": "# Type conversion functions\nint_num = int('123')       # String to int\nfloat_num = float('12.34')  # String to float\nstr_num = str(123)         # Number to string\n\n# List conversion\ntuple_to_list = list((1, 2, 3))\nset_to_list = list({1, 2, 3})\n\n# Other conversions\nbin_num = bin(10)          # To binary: '0b1010'\nhex_num = hex(16)          # To hex: '0x10'\noct_num = oct(8)           # To octal: '0o10'",
                            "implicit_casting": "# Automatic type conversion\nx = 5 + 2.0    # Result is float (7.0)\ny = 2 * 3.0    # Result is float (6.0)\nz = True + 1    # Result is int (2)"
                        },
                        "best_practices": [
                            "Use explicit casting when intention matters",
                            "Handle potential conversion errors",
                            "Be aware of precision loss in float conversions",
                            "Use appropriate numeric types",
                            "Validate string inputs before conversion"
                        ]
                    }
                },
                {
                    "input_and_output": {
                        "description": "Reading input and displaying output",
                        "examples": {
                            "basic_io": "# Basic input/output\nname = input('Enter your name: ')\nprint('Hello,', name)\n\n# Formatted output\nage = 25\nprint(f'Age: {age}')\nprint('Age: {}'.format(age))\nprint('Age: %d' % age)",
                            "file_io": "# File operations\n# Writing to file\nwith open('example.txt', 'w') as f:\n    f.write('Hello, World!')\n\n# Reading from file\nwith open('example.txt', 'r') as f:\n    content = f.read()\n\n# Appending to file\nwith open('example.txt', 'a') as f:\n    f.write('\\nNew line')"
                        },
                        "best_practices": [
                            "Use f-strings for string formatting",
                            "Always use context managers (with) for files",
                            "Handle file operation exceptions",
                            "Close files properly",
                            "Validate user input"
                        ]
                    }
                }
            ],

            "data structures": [
                {
                    "lists": {
                        "description": "Ordered, mutable sequences of elements",
                        "examples": {
                            "creation_and_basic_ops": """
            # List creation
            numbers = [1, 2, 3, 4, 5]
            mixed = [1, "hello", 3.14, True]
            empty = []
            list_from_range = list(range(5))    # [0, 1, 2, 3, 4]

            # Accessing elements
            first = numbers[0]      # First element
            last = numbers[-1]      # Last element
            slice = numbers[1:3]    # Elements from index 1 to 2
            reverse = numbers[::-1] # Reverse the list

            # Modifying lists
            numbers.append(6)       # Add to end
            numbers.insert(0, 0)    # Insert at beginning
            numbers.extend([7, 8])  # Add multiple items
            numbers.remove(3)       # Remove first occurrence of 3
            popped = numbers.pop()  # Remove and return last item
            numbers[0] = 10         # Modify element
            """,
                            "advanced_operations": """
            # List methods
            numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
            numbers.sort()                # Sort in place
            numbers.reverse()            # Reverse in place
            count = numbers.count(1)     # Count occurrences
            index = numbers.index(5)     # Find first occurrence
            numbers.clear()              # Remove all items

            # List operations
            list1 = [1, 2, 3]
            list2 = [4, 5, 6]
            combined = list1 + list2     # Concatenation
            repeated = list1 * 3         # Repetition
            sublist = list1[::2]        # Step slicing

            # Nested lists
            matrix = [[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]]
            element = matrix[1][1]      # Accessing nested elements
            """
                        },
                        "best_practices": [
                            "Use list methods instead of manual operations",
                            "Consider memory usage for large lists",
                            "Use clear() instead of reassigning empty list",
                            "Use list comprehensions for transformations",
                            "Be careful with shallow vs deep copying"
                        ]
                    }
                },
                {
                    "tuples": {
                        "description": "Ordered, immutable sequences of elements",
                        "examples": {
                            "creation_and_usage": """
            # Tuple creation
            point = (3, 4)
            singleton = (1,)            # Note the comma
            empty = ()
            tuple_from_list = tuple([1, 2, 3])

            # Accessing elements
            x = point[0]               # First element
            y = point[1]               # Second element
            subset = point[0:2]        # Slicing works too

            # Tuple operations
            coordinates = (1, 2, 3)
            more_coords = coordinates + (4, 5, 6)  # Concatenation
            repeated = coordinates * 2             # Repetition

            # Tuple unpacking
            x, y = point               # Basic unpacking
            a, *rest, b = (1, 2, 3, 4) # Extended unpacking
            """,
                            "advanced_features": """
            # Tuple methods
            numbers = (1, 2, 2, 3, 4, 2)
            count = numbers.count(2)    # Count occurrences
            index = numbers.index(3)    # Find first occurrence

            # Tuples as dictionary keys
            locations = {
                (0, 0): 'origin',
                (1, 0): 'right',
                (0, 1): 'up'
            }

            # Named tuples
            from collections import namedtuple
            Point = namedtuple('Point', ['x', 'y'])
            p = Point(3, 4)
            print(p.x, p.y)            # Access by name
            """
                        },
                        "best_practices": [
                            "Use tuples for immutable sequences",
                            "Use named tuples for clarity",
                            "Consider tuples for dictionary keys",
                            "Use tuple unpacking for multiple returns",
                            "Prefer tuples over lists for fixed sequences"
                        ]
                    }
                },
                {
                    "dictionaries": {
                        "description": "Key-value pair collections",
                        "examples": {
                            "basic_operations": """
            # Dictionary creation
            person = {
                'name': 'John',
                'age': 30,
                'city': 'New York'
            }
            empty = {}
            dict_from_items = dict([('a', 1), ('b', 2)])

            # Accessing and modifying
            name = person['name']           # Direct access
            age = person.get('age', 0)     # Access with default
            person['email'] = 'j@mail.com' # Add new key-value
            person.update({'phone': '123'}) # Add multiple items
            del person['city']             # Remove key-value
            """,
                            "advanced_features": """
            # Dictionary methods
            keys = person.keys()           # Get all keys
            values = person.values()       # Get all values
            items = person.items()         # Get all key-value pairs

            # Dictionary comprehension
            squares = {x: x**2 for x in range(5)}

            # Nested dictionaries
            company = {
                'department1': {
                    'name': 'Engineering',
                    'employees': ['John', 'Jane']
                },
                'department2': {
                    'name': 'Sales',
                    'employees': ['Bob', 'Alice']
                }
            }

            # Default dictionaries
            from collections import defaultdict
            word_count = defaultdict(int)
            for word in ['apple', 'banana', 'apple']:
                word_count[word] += 1
            """
                        },
                        "best_practices": [
                            "Use get() to handle missing keys",
                            "Consider defaultdict for automatic defaults",
                            "Use dict comprehensions for transformations",
                            "Be careful with mutable dictionary values",
                            "Use clear() to empty a dictionary"
                        ]
                    }
                },
                {
                    "sets": {
                        "description": "Unordered collections of unique elements",
                        "examples": {
                            "basic_operations": """
            # Set creation
            numbers = {1, 2, 3, 4, 5}
            unique = set([1, 2, 2, 3, 3, 4])  # Creates {1, 2, 3, 4}
            empty = set()                      # Empty set

            # Modifying sets
            numbers.add(6)             # Add single element
            numbers.update([7, 8, 9])  # Add multiple elements
            numbers.remove(1)          # Remove element (raises error if missing)
            numbers.discard(10)        # Remove if present
            popped = numbers.pop()     # Remove and return arbitrary element
            """,
                            "set_operations": """
            # Set operations
            set1 = {1, 2, 3, 4}
            set2 = {3, 4, 5, 6}

            union = set1 | set2             # Union
            intersection = set1 & set2      # Intersection
            difference = set1 - set2        # Difference
            symmetric_diff = set1 ^ set2    # Symmetric difference

            # Set predicates
            is_subset = set1 <= set2        # Subset
            is_superset = set1 >= set2      # Superset
            is_disjoint = set1.isdisjoint(set2)

            # Frozen sets (immutable)
            frozen = frozenset([1, 2, 3])
            """
                        },
                        "best_practices": [
                            "Use sets for unique collections",
                            "Consider frozenset for immutable sets",
                            "Use set operations for efficient comparisons",
                            "Use discard() instead of remove() when unsure",
                            "Consider sets for membership testing"
                        ]
                    }
                },
                {
                    "list_comprehensions": {
                        "description": "Concise way to create lists based on existing iterables",
                        "examples": {
                            "basic_comprehensions": """
            # Simple list comprehension
            squares = [x**2 for x in range(10)]
            evens = [x for x in range(10) if x % 2 == 0]

            # With conditional logic
            numbers = [-4, -2, 0, 2, 4]
            abs_values = [abs(x) for x in numbers]
            pos_neg = ['pos' if x > 0 else 'neg' if x < 0 else 'zero' 
                       for x in numbers]

            # Nested list comprehension
            matrix = [[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]]
            flattened = [x for row in matrix for x in row]
            """,
                            "advanced_patterns": """
            # Multiple if conditions
            filtered = [x for x in range(100) 
                       if x % 2 == 0 if x % 3 == 0]

            # Nested comprehensions
            matrix_transpose = [[row[i] for row in matrix] 
                               for i in range(len(matrix[0]))]

            # With functions
            def is_prime(n):
                return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

            primes = [x for x in range(100) if is_prime(x)]
            """
                        },
                        "best_practices": [
                            "Use for readability over complex loops",
                            "Avoid too many nested comprehensions",
                            "Consider generator expressions for large sequences",
                            "Keep logic simple and readable",
                            "Don't overuse conditional logic"
                        ]
                    }
                },
                {
                    "dictionary_comprehensions": {
                        "description": "Concise way to create dictionaries based on iterables",
                        "examples": {
                            "basic_comprehensions": """
            # Simple dictionary comprehension
            squares = {x: x**2 for x in range(5)}
            even_squares = {x: x**2 for x in range(5) if x % 2 == 0}

            # From two lists
            keys = ['a', 'b', 'c']
            values = [1, 2, 3]
            mapping = {k: v for k, v in zip(keys, values)}

            # Inverting a dictionary
            original = {'a': 1, 'b': 2, 'c': 3}
            inverted = {v: k for k, v in original.items()}
            """,
                            "advanced_patterns": """
            # Conditional dictionary comprehension
            numbers = range(-5, 6)
            sign_dict = {x: ('positive' if x > 0 else 'negative' if x < 0 else 'zero')
                         for x in numbers}

            # Nested dictionary comprehension
            matrix = {i: {j: i*j for j in range(3)}
                     for i in range(3)}

            # Filtering with multiple conditions
            filtered = {k: v for k, v in original.items()
                       if v > 0 and k.isalpha()}
            """
                        },
                        "best_practices": [
                            "Use for creating dictionaries from iterables",
                            "Keep logic simple and readable",
                            "Consider regular loops for complex transformations",
                            "Be careful with memory usage for large dictionaries",
                            "Use when transforming existing dictionaries"
                        ]
                    }
                }
            ],

            "functions": [
                {
                    "defining_functions": {
                        "description": "Creating reusable blocks of code",
                        "examples": {
                            "basic_functions": """
            # Basic function definition
            def greet():
                print("Hello, World!")

            # Function with docstring
            def calculate_area(length, width):
                \"\"\"
                Calculate the area of a rectangle.

                Args:
                    length (float): The length of the rectangle
                    width (float): The width of the rectangle

                Returns:
                    float: The area of the rectangle
                \"\"\"
                return length * width

            # Function with default values
            def increment(number, by=1):
                return number + by

            # Function with type hints (Python 3.5+)
            def get_full_name(first_name: str, last_name: str) -> str:
                return f"{first_name} {last_name}"
            """,
                            "advanced_definitions": """
            # Function with variable arguments
            def print_all(*args):
                for arg in args:
                    print(arg)

            # Function with keyword arguments
            def print_info(**kwargs):
                for key, value in kwargs.items():
                    print(f"{key}: {value}")

            # Function with both
            def mixed_args(*args, **kwargs):
                print(f"Args: {args}")
                print(f"Kwargs: {kwargs}")

            # Function with annotations
            def process_data(data: list, 
                            threshold: float = 0.5, 
                            debug: bool = False) -> dict:
                '''Process data with given parameters'''
                # Function implementation
                pass
            """
                        },
                        "best_practices": [
                            "Use clear and descriptive function names",
                            "Include docstrings for documentation",
                            "Use type hints for better code clarity",
                            "Keep functions focused and single-purpose",
                            "Follow the DRY (Don't Repeat Yourself) principle"
                        ]
                    }
                },
                {
                    "arguments": {
                        "description": "Different ways to pass data to functions",
                        "examples": {
                            "argument_types": """
            # Positional arguments
            def greet(name, age):
                print(f"Hello {name}, you are {age} years old")

            greet("John", 25)  # Standard call
            greet(age=25, name="John")  # Keyword arguments

            # Default arguments
            def connect(host="localhost", port=3306):
                print(f"Connecting to {host}:{port}")

            connect()  # Uses defaults
            connect("example.com", 8080)  # Override defaults

            # Variable positional arguments
            def sum_all(*numbers):
                return sum(numbers)

            print(sum_all(1, 2, 3, 4, 5))  # Any number of arguments

            # Variable keyword arguments
            def user_info(**info):
                for key, value in info.items():
                    print(f"{key}: {value}")

            user_info(name="John", age=30, city="New York")
            """,
                            "advanced_arguments": """
            # Positional-only parameters (Python 3.8+)
            def divide(x, y, /):
                return x / y

            # Keyword-only arguments
            def process(*, filename, mode="r"):
                with open(filename, mode) as f:
                    return f.read()

            # Mixed argument types
            def hybrid_function(pos_only, /, standard, *, kw_only):
                print(pos_only, standard, kw_only)

            # Unpacking arguments
            def point(x, y):
                return x, y

            coords = [3, 4]
            print(point(*coords))  # Unpacking list

            params = {"x": 3, "y": 4}
            print(point(**params))  # Unpacking dict
            """
                        },
                        "best_practices": [
                            "Use positional-only for implementation details",
                            "Use keyword-only for clearer function calls",
                            "Provide default values for optional parameters",
                            "Be careful with mutable default arguments",
                            "Document parameter requirements clearly"
                        ]
                    }
                },
                {
                    "return_values": {
                        "description": "Ways functions can return data",
                        "examples": {
                            "basic_returns": """
            # Single return value
            def square(x):
                return x * x

            # Multiple return values
            def divide_and_remainder(x, y):
                return x // y, x % y

            quotient, remainder = divide_and_remainder(10, 3)

            # Conditional returns
            def get_grade(score):
                if score >= 90:
                    return 'A'
                elif score >= 80:
                    return 'B'
                else:
                    return 'C'

            # Early returns
            def find_index(items, target):
                for i, item in enumerate(items):
                    if item == target:
                        return i
                return -1  # Not found
            """,
                            "advanced_returns": """
            # Returning functions
            def create_multiplier(factor):
                def multiplier(x):
                    return x * factor
                return multiplier

            double = create_multiplier(2)
            print(double(5))  # 10

            # Returning multiple values as data structures
            def get_stats(numbers):
                return {
                    'min': min(numbers),
                    'max': max(numbers),
                    'avg': sum(numbers) / len(numbers)
                }

            # Generator functions
            def fibonacci(n):
                a, b = 0, 1
                for _ in range(n):
                    yield a
                    a, b = b, a + b

            # Optional returns with None
            def find_user(user_id):
                # Simulated database lookup
                if user_id == 1:
                    return {"id": 1, "name": "John"}
                return None
            """
                        },
                        "best_practices": [
                            "Be consistent with return types",
                            "Use meaningful return values",
                            "Consider using named tuples for multiple returns",
                            "Document return types and values",
                            "Use early returns to simplify logic"
                        ]
                    }
                },
                {
                    "lambda_functions": {
                        "description": "Small anonymous functions",
                        "examples": {
                            "basic_lambda": """
            # Simple lambda functions
            square = lambda x: x ** 2
            add = lambda x, y: x + y

            # Using with built-in functions
            numbers = [1, 2, 3, 4, 5]
            squares = list(map(lambda x: x**2, numbers))
            evens = list(filter(lambda x: x % 2 == 0, numbers))

            # Sorting with lambda
            points = [(1, 2), (3, 1), (2, 5)]
            sorted_points = sorted(points, key=lambda p: p[1])

            # Lambda in list comprehension
            transform = [(lambda x: x*2)(x) for x in range(5)]
            """,
                            "advanced_lambda": """
            # Lambda with multiple conditions
            compare = lambda x: 'positive' if x > 0 else 'zero' if x == 0 else 'negative'

            # Lambda with dictionaries
            users = [{'name': 'John', 'age': 30}, 
                     {'name': 'Jane', 'age': 25}]
            sorted_users = sorted(users, key=lambda u: u['age'])

            # Immediate lambda execution
            (lambda x: print(f"Value is {x}"))(42)

            # Lambda in higher-order functions
            def apply_operation(x, operation):
                return operation(x)

            result = apply_operation(5, lambda x: x * x)
            """
                        },
                        "best_practices": [
                            "Use for simple operations only",
                            "Prefer regular functions for complex logic",
                            "Use descriptive names when assigning lambdas",
                            "Consider readability over conciseness",
                            "Use with built-in functions like map/filter/sort"
                        ]
                    }
                },
                {
                    "function_scope": {
                        "description": "Variable visibility and lifetime in functions",
                        "examples": {
                            "scope_basics": """
            # Local and global scope
            global_var = "I am global"

            def show_scope():
                local_var = "I am local"
                print(local_var)    # Access local
                print(global_var)   # Access global

            # Modifying global variables
            counter = 0

            def increment():
                global counter
                counter += 1

            # Nonlocal variables
            def outer():
                x = "outer"
                def inner():
                    nonlocal x
                    x = "modified"
                inner()
                print(x)  # "modified"
            """,
                            "advanced_scope": """
            # Closure example
            def create_counter():
                count = 0
                def increment():
                    nonlocal count
                    count += 1
                    return count
                return increment

            # Variable lifetime
            def demonstrate_scope():
                # Local variable
                x = 1

                def inner():
                    # Creates a new local x
                    x = 2
                    print('Inner x:', x)

                inner()
                print('Outer x:', x)

            # Class-level scope
            class Example:
                class_var = "I am class-level"

                def method(self):
                    self.instance_var = "I am instance-level"
                    local_var = "I am method-local"
            """
                        },
                        "best_practices": [
                            "Avoid global variables when possible",
                            "Use function parameters instead of globals",
                            "Be explicit with global and nonlocal",
                            "Understand variable lifetime",
                            "Keep scope as narrow as possible"
                        ]
                    }
                }
            ],

            "object-oriented programming": [
                {
                    "classes": {
                        "description": "Blueprint for creating objects that bundle data and functionality",
                        "examples": {
                            "basic_class": """
        # Basic class definition
        class Person:
            def __init__(self, name, age):
                self.name = name
                self.age = age

            def introduce(self):
                return f"Hi, I'm {self.name} and I'm {self.age} years old."

        # Class with class variables
        class Employee:
            company = "Tech Corp"  # Class variable
            employee_count = 0

            def __init__(self, name, role):
                self.name = name  # Instance variable
                self.role = role
                Employee.employee_count += 1

            @classmethod
            def get_company_info(cls):
                return f"Company: {cls.company}, Employees: {cls.employee_count}"

            @staticmethod
            def is_workday(day):
                return day.weekday() < 5
        """,
                            "advanced_class": """
        # Class with property decorators
        class BankAccount:
            def __init__(self, initial_balance=0):
                self._balance = initial_balance
                self._transactions = []

            @property
            def balance(self):
                return self._balance

            @balance.setter
            def balance(self, value):
                if value < 0:
                    raise ValueError("Balance cannot be negative")
                self._balance = value
                self._transactions.append(value)

            @property
            def transaction_history(self):
                return tuple(self._transactions)  # Immutable copy

        # Class with slots for memory optimization
        class Point:
            __slots__ = ['x', 'y']

            def __init__(self, x, y):
                self.x = x
                self.y = y
        """
                        },
                        "best_practices": [
                            "Use clear and descriptive class names",
                            "Initialize all instance variables in __init__",
                            "Use properties instead of direct attribute access",
                            "Document classes with docstrings",
                            "Use slots for memory optimization when appropriate"
                        ]
                    }
                },
                {
                    "objects": {
                        "description": "Instances of classes that contain data and code",
                        "examples": {
                            "object_creation": """
        # Creating and using objects
        class Car:
            def __init__(self, make, model, year):
                self.make = make
                self.model = model
                self.year = year
                self._mileage = 0

            def drive(self, distance):
                self._mileage += distance
                return f"Drove {distance} miles"

            def get_info(self):
                return f"{self.year} {self.make} {self.model}"

        # Creating objects
        my_car = Car("Toyota", "Corolla", 2020)
        other_car = Car("Honda", "Civic", 2019)

        # Using objects
        print(my_car.get_info())
        my_car.drive(100)
        """,
                            "object_relationships": """
        # Objects containing other objects
        class Engine:
            def __init__(self, horsepower):
                self.horsepower = horsepower
                self.running = False

            def start(self):
                self.running = True

            def stop(self):
                self.running = False

        class Car:
            def __init__(self, make, model, engine_hp):
                self.make = make
                self.model = model
                self.engine = Engine(engine_hp)  # Composition

            def start_engine(self):
                self.engine.start()
                return "Engine started"

        # Object relationships
        sports_car = Car("Ferrari", "F40", 478)
        sports_car.start_engine()
        """
                        },
                        "best_practices": [
                            "Initialize objects with all required data",
                            "Use meaningful object relationships",
                            "Implement proper cleanup if needed",
                            "Consider object lifecycle",
                            "Use composition over inheritance when possible"
                        ]
                    }
                },
                {
                    "inheritance": {
                        "description": "Mechanism for code reuse and establishing relationships between classes",
                        "examples": {
                            "basic_inheritance": """
        # Single inheritance
        class Animal:
            def __init__(self, name):
                self.name = name

            def speak(self):
                raise NotImplementedError("Subclass must implement")

        class Dog(Animal):
            def speak(self):
                return f"{self.name} says Woof!"

        class Cat(Animal):
            def speak(self):
                return f"{self.name} says Meow!"

        # Method overriding and super()
        class Vehicle:
            def __init__(self, brand):
                self.brand = brand

            def start(self):
                return "Vehicle starting"

        class ElectricCar(Vehicle):
            def __init__(self, brand, battery_capacity):
                super().__init__(brand)
                self.battery_capacity = battery_capacity

            def start(self):
                return f"{super().start()} silently"
        """,
                            "advanced_inheritance": """
        # Multiple inheritance
        class Flyable:
            def fly(self):
                return "Flying..."

        class Swimmable:
            def swim(self):
                return "Swimming..."

        class Duck(Animal, Flyable, Swimmable):
            def speak(self):
                return f"{self.name} says Quack!"

        # Abstract base classes
        from abc import ABC, abstractmethod

        class Shape(ABC):
            @abstractmethod
            def area(self):
                pass

            @abstractmethod
            def perimeter(self):
                pass

        class Rectangle(Shape):
            def __init__(self, width, height):
                self.width = width
                self.height = height

            def area(self):
                return self.width * self.height

            def perimeter(self):
                return 2 * (self.width + self.height)

        # Mixin classes
        class LoggerMixin:
            def log(self, message):
                print(f"[{self.__class__.__name__}]: {message}")

        class User(LoggerMixin):
            def __init__(self, username):
                self.username = username
                self.log(f"Created user {username}")
        """
                        },
                        "best_practices": [
                            "Use inheritance for 'is-a' relationships",
                            "Keep inheritance hierarchies shallow",
                            "Use composition for 'has-a' relationships",
                            "Implement all abstract methods",
                            "Be careful with multiple inheritance"
                        ]
                    }
                },
                {
                    "polymorphism": {
                        "description": "Ability of objects to take multiple forms",
                        "examples": {
                            "basic_polymorphism": """
        # Method polymorphism
        def process_shape(shape):
            print(f"Area: {shape.area()}")
            print(f"Perimeter: {shape.perimeter()}")

        class Circle:
            def __init__(self, radius):
                self.radius = radius

            def area(self):
                return 3.14 * self.radius ** 2

            def perimeter(self):
                return 2 * 3.14 * self.radius

        class Square:
            def __init__(self, side):
                self.side = side

            def area(self):
                return self.side ** 2

            def perimeter(self):
                return 4 * self.side

        # Using polymorphism
        shapes = [Circle(5), Square(4)]
        for shape in shapes:
            process_shape(shape)
        """,
                            "advanced_polymorphism": """
        # Operator overloading
        class Vector:
            def __init__(self, x, y):
                self.x = x
                self.y = y

            def __add__(self, other):
                return Vector(self.x + other.x, self.y + other.y)

            def __mul__(self, scalar):
                return Vector(self.x * scalar, self.y * scalar)

            def __str__(self):
                return f"Vector({self.x}, {self.y})"

        # Duck typing
        class Database:
            def execute(self, query):
                pass

        class MySQLDB(Database):
            def execute(self, query):
                return "MySQL: " + query

        class PostgresDB(Database):
            def execute(self, query):
                return "Postgres: " + query

        def run_query(db, query):
            # Works with any object that has execute method
            return db.execute(query)
        """
                        },
                        "best_practices": [
                            "Design for polymorphism through interfaces",
                            "Use duck typing when appropriate",
                            "Keep interface methods consistent",
                            "Document expected method behavior",
                            "Use abstract base classes to enforce interfaces"
                        ]
                    }
                },
                {
                    "encapsulation": {
                        "description": "Bundling of data and methods that operate on that data within a single unit",
                        "examples": {
                            "basic_encapsulation": """
        # Private and protected attributes
        class Account:
            def __init__(self, balance):
                self.__balance = balance  # Private
                self._transactions = []   # Protected

            def deposit(self, amount):
                if amount > 0:
                    self.__balance += amount
                    self._transactions.append(('deposit', amount))
                    return True
                return False

            def get_balance(self):
                return self.__balance

        # Name mangling demonstration
        class Person:
            def __init__(self, name):
                self.__name = name  # Creates _Person__name

            def get_name(self):
                return self.__name
        """,
                            "advanced_encapsulation": """
        # Property decorators for encapsulation
        class Temperature:
            def __init__(self, celsius):
                self._celsius = celsius

            @property
            def celsius(self):
                return self._celsius

            @celsius.setter
            def celsius(self, value):
                if value < -273.15:
                    raise ValueError("Temperature below absolute zero")
                self._celsius = value

            @property
            def fahrenheit(self):
                return self._celsius * 9/5 + 32

            @fahrenheit.setter
            def fahrenheit(self, value):
                self.celsius = (value - 32) * 5/9

        # Descriptor protocol
        class Validator:
            def __init__(self, minimum=None, maximum=None):
                self.minimum = minimum
                self.maximum = maximum

            def __set_name__(self, owner, name):
                self.name = f"_{name}"

            def __get__(self, instance, owner):
                if instance is None:
                    return self
                return getattr(instance, self.name)

            def __set__(self, instance, value):
                if self.minimum is not None and value < self.minimum:
                    raise ValueError(f"Value must be ≥ {self.minimum}")
                if self.maximum is not None and value > self.maximum:
                    raise ValueError(f"Value must be ≤ {self.maximum}")
                setattr(instance, self.name, value)

        class Person:
            age = Validator(0, 150)
            def __init__(self, age):
                self.age = age
        """
                        },
                        "best_practices": [
                            "Use properties for controlled attribute access",
                            "Keep internal representation private",
                            "Provide clear public interfaces",
                            "Use name mangling when needed",
                            "Document public interfaces thoroughly"
                        ]
                    }
                },
                {
                    "abstraction": {
                        "description": "Hiding complex implementation details and showing only necessary features",
                        "examples": {
                            "basic_abstraction": """
        # Abstract base class
        from abc import ABC, abstractmethod

        class PaymentProcessor(ABC):
            @abstractmethod
            def process_payment(self, amount):
                pass

            @abstractmethod
            def refund(self, amount):
                pass

        class CreditCardProcessor(PaymentProcessor):
            def process_payment(self, amount):
                return f"Processing ${amount} via Credit Card"

            def refund(self, amount):
                return f"Refunding ${amount} to Credit Card"
        """,
                            "advanced_abstraction": """
        # Interface segregation
        class Printable(ABC):
            @abstractmethod
            def print_document(self):
                pass

        class Scannable(ABC):
            @abstractmethod
            def scan_document(self):
                pass

        class Printer(Printable):
            def print_document(self):
                return "Printing..."

        class Scanner(Scannable):
            def scan_document(self):
                return "Scanning..."

        class AllInOnePrinter(Printable, Scannable):
            def print_document(self):
                return "Printing..."

            def scan_document(self):
                return "Scanning..."
        """
                        },
                        "best_practices": [
                            "Use abstract base classes to define interfaces",
                            "Keep interfaces minimal and focused",
                            "Hide implementation details",
                            "Provide clear documentation",
                            "Follow interface segregation principle"
                        ]
                    }
                },
                {
                    "magic_methods": {
                        "description": "Special methods that customize object behavior",
                        "examples": {
                            "basic_magic_methods": """
        # Common magic methods
        class Vector:
            def __init__(self, x, y):
                self.x = x
                self.y = y

            def __str__(self):
                return f"Vector({self.x}, {self.y})"

            def __repr__(self):
                return f"Vector(x={self.x}, y={self.y})"

            def __eq__(self, other):
                return self.x == other.x and self.y == other.y

            def __add__(self, other):
                return Vector(self.x + other.x, self.y + other.y)

            def __len__(self):
                return int((self.x ** 2 + self.y ** 2) ** 0.5)
        """,
                            "advanced_magic_methods": """
        # Container and descriptor protocol
        class DataList:
            def __init__(self):
                self._data = []

            def __getitem__(self, index):
                return self._data[index]

            def __setitem__(self, index, value):
                self._data[index] = value

            def __delitem__(self, index):
                del self._data[index]

            def __iter__(self):
                return iter(self._data)

            def __contains__(self, item):
                return item in self._data

        # Context manager protocol
        class Resource:
            def __init__(self, name):
                self.name = name

            def __enter__(self):
                print(f"Acquiring {self.name}")
                return self

            def __exit__(self, exc_type, exc_val, exc_tb):
                print(f"Releasing {self.name}")
                if exc_type is not None:
                    print(f"Error: {exc_val}")
                    return False  # Propagate exception

        # Callable objects
        class Multiplier:
            def __init__(self, factor):
                self.factor = factor

            def __call__(self, x):
                return x * self.factor

        double = Multiplier(2)
        result = double(10)  # result = 20
        """
                        },
                        "best_practices": [
                            "Implement __str__ and __repr__",
                            "Make objects behave like built-in types when appropriate",
                            "Use context managers for resource management",
                            "Implement container protocol completely",
                            "Document magic method behavior"
                        ]
                    }
                }
            ],

            "file handling": [
                {
                    "file_operations": {
                        "description": "Basic file operations including opening, closing, and modes",
                        "examples": {
                            "basic_operations": """
            # Opening and closing files
            file = open('example.txt', 'r')  # Open for reading
            content = file.read()
            file.close()

            # Using context manager (recommended)
            with open('example.txt', 'r') as file:
                content = file.read()

            # Different file modes
            with open('file.txt', 'w') as f:   # Write mode (overwrites)
                f.write('Hello')

            with open('file.txt', 'a') as f:   # Append mode
                f.write('World')

            with open('file.txt', 'r+') as f:  # Read and write mode
                content = f.read()
                f.write('New content')

            # Checking if file exists
            import os
            if os.path.exists('file.txt'):
                print('File exists')
            """,
                            "file_management": """
            # File and directory operations
            import os
            import shutil

            # Create directory
            os.makedirs('new_directory', exist_ok=True)

            # List directory contents
            files = os.listdir('.')
            files_with_path = [os.path.join('.', f) for f in files]

            # Get file info
            file_stats = os.stat('example.txt')
            size = file_stats.st_size
            modified_time = file_stats.st_mtime

            # Copy, move, and delete
            shutil.copy('source.txt', 'destination.txt')
            os.rename('old_name.txt', 'new_name.txt')
            os.remove('file_to_delete.txt')

            # Walking directory tree
            for root, dirs, files in os.walk('.'):
                print(f'Directory: {root}')
                print(f'Files: {files}')
            """
                        },
                        "best_practices": [
                            "Always use context managers (with)",
                            "Close files explicitly if not using context managers",
                            "Check file existence before operations",
                            "Use appropriate file modes",
                            "Handle permissions and exceptions"
                        ]
                    }
                },
                {
                    "reading_and_writing_files": {
                        "description": "Methods for reading from and writing to text files",
                        "examples": {
                            "reading_files": """
            # Different ways to read
            with open('example.txt', 'r') as f:
                # Read entire file
                content = f.read()

                # Read specific number of characters
                f.seek(0)  # Reset file pointer
                chunk = f.read(10)

                # Read line by line
                f.seek(0)
                line = f.readline()

                # Read all lines into list
                f.seek(0)
                lines = f.readlines()

            # Iterating over file
            with open('example.txt', 'r') as f:
                for line in f:
                    print(line.strip())

            # Reading with encoding
            with open('example.txt', 'r', encoding='utf-8') as f:
                content = f.read()
            """,
                            "writing_files": """
            # Different ways to write
            with open('output.txt', 'w') as f:
                # Write string
                f.write('Hello, World\\n')

                # Write multiple lines
                lines = ['Line 1\\n', 'Line 2\\n', 'Line 3\\n']
                f.writelines(lines)

                # Write with print
                print('Using print', file=f)

            # Appending to file
            with open('output.txt', 'a') as f:
                f.write('Appended text\\n')

            # Writing with encoding
            with open('output.txt', 'w', encoding='utf-8') as f:
                f.write('Special characters: äöü')
            """
                        },
                        "best_practices": [
                            "Specify encoding explicitly",
                            "Use appropriate line endings",
                            "Handle large files in chunks",
                            "Buffer writes when appropriate",
                            "Clean up resources properly"
                        ]
                    }
                },
                {
                    "working_with_CSV": {
                        "description": "Reading and writing CSV (Comma-Separated Values) files",
                        "examples": {
                            "basic_csv": """
            import csv

            # Writing CSV
            data = [
                ['Name', 'Age', 'City'],
                ['John', 30, 'New York'],
                ['Alice', 25, 'London']
            ]

            with open('data.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(data)

            # Reading CSV
            with open('data.csv', 'r', newline='') as f:
                reader = csv.reader(f)
                for row in reader:
                    print(row)
            """,
                            "advanced_csv": """
            import csv

            # Using DictReader and DictWriter
            data = [
                {'name': 'John', 'age': 30, 'city': 'New York'},
                {'name': 'Alice', 'age': 25, 'city': 'London'}
            ]

            # Writing CSV with headers
            with open('data.csv', 'w', newline='') as f:
                fieldnames = ['name', 'age', 'city']
                writer = csv.DictWriter(f, fieldnames=fieldnames)

                writer.writeheader()
                writer.writerows(data)

            # Reading CSV as dictionaries
            with open('data.csv', 'r', newline='') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    print(row['name'], row['age'])

            # Handling different dialects
            csv.register_dialect('pipes', delimiter='|')

            with open('data.csv', 'w', newline='') as f:
                writer = csv.writer(f, dialect='pipes')
                writer.writerows(data)

            # Custom dialect
            csv.register_dialect('custom',
                delimiter=';',
                quoting=csv.QUOTE_ALL,
                escapechar='\\'
            )
            """
                        },
                        "best_practices": [
                            "Use newline='' parameter",
                            "Handle different CSV dialects",
                            "Use DictReader/DictWriter for structured data",
                            "Validate CSV data",
                            "Handle encoding properly"
                        ]
                    }
                },
                {
                    "JSON_handling": {
                        "description": "Working with JSON (JavaScript Object Notation) files",
                        "examples": {
                            "basic_json": """
            import json

            # Writing JSON
            data = {
                'name': 'John',
                'age': 30,
                'city': ['New York', 'London']
            }

            with open('data.json', 'w') as f:
                json.dump(data, f, indent=4)

            # Reading JSON
            with open('data.json', 'r') as f:
                loaded_data = json.load(f)

            # Converting to/from JSON strings
            json_string = json.dumps(data)
            parsed_data = json.loads(json_string)
            """,
                            "advanced_json": """
            import json
            from datetime import datetime

            # Custom JSON encoder
            class DateTimeEncoder(json.JSONEncoder):
                def default(self, obj):
                    if isinstance(obj, datetime):
                        return obj.isoformat()
                    return super().default(obj)

            data = {
                'name': 'Event',
                'date': datetime.now()
            }

            # Using custom encoder
            with open('event.json', 'w') as f:
                json.dump(data, f, cls=DateTimeEncoder)

            # Custom JSON decoder
            def datetime_decoder(dct):
                for k, v in dct.items():
                    if isinstance(v, str):
                        try:
                            dct[k] = datetime.fromisoformat(v)
                        except ValueError:
                            pass
                return dct

            # Using custom decoder
            with open('event.json', 'r') as f:
                loaded_data = json.load(f, object_hook=datetime_decoder)

            # Pretty printing JSON
            print(json.dumps(data, cls=DateTimeEncoder, 
                            indent=4, sort_keys=True))
            """
                        },
                        "best_practices": [
                            "Handle JSON encoding errors",
                            "Use custom encoders for complex types",
                            "Validate JSON structure",
                            "Use appropriate indentation",
                            "Consider JSON schema validation"
                        ]
                    }
                },
                {
                    "context_managers": {
                        "description": "Using and creating context managers for file handling",
                        "examples": {
                            "using_context_managers": """
            # Basic context manager usage
            with open('file.txt', 'r') as f:
                content = f.read()

            # Multiple context managers
            with open('input.txt', 'r') as in_file, \
                 open('output.txt', 'w') as out_file:
                content = in_file.read()
                out_file.write(content.upper())
            """,
                            "creating_context_managers": """
            # Class-based context manager
            class FileManager:
                def __init__(self, filename, mode):
                    self.filename = filename
                    self.mode = mode
                    self.file = None

                def __enter__(self):
                    self.file = open(self.filename, self.mode)
                    return self.file

                def __exit__(self, exc_type, exc_val, exc_tb):
                    if self.file:
                        self.file.close()
                    return False  # Don't suppress exceptions

            # Function-based context manager
            from contextlib import contextmanager

            @contextmanager
            def file_manager(filename, mode):
                try:
                    f = open(filename, mode)
                    yield f
                finally:
                    f.close()

            # Using custom context managers
            with FileManager('file.txt', 'r') as f:
                content = f.read()

            with file_manager('file.txt', 'r') as f:
                content = f.read()
            """
                        },
                        "best_practices": [
                            "Always use context managers for file operations",
                            "Handle exceptions properly in __exit__",
                            "Clean up resources in finally block",
                            "Document context manager behavior",
                            "Keep context managers focused"
                        ]
                    }
                },
                {
                    "binary_file_handling": {
                        "description": "Working with binary files",
                        "examples": {
                            "basic_binary": """
            # Reading and writing binary files
            with open('binary.dat', 'wb') as f:
                # Write bytes
                f.write(b'Hello World')

                # Write bytearray
                data = bytearray([65, 66, 67])  # ABC
                f.write(data)

            with open('binary.dat', 'rb') as f:
                # Read all bytes
                content = f.read()

                # Read specific number of bytes
                f.seek(0)
                chunk = f.read(5)
            """,
                            "advanced_binary": """
            import struct

            # Writing structured binary data
            data = struct.pack('if', 42, 3.14)  # int and float
            with open('data.bin', 'wb') as f:
                f.write(data)

            # Reading structured binary data
            with open('data.bin', 'rb') as f:
                data = f.read()
                number, pi = struct.unpack('if', data)

            # Working with memory views
            with open('data.bin', 'rb') as f:
                mv = memoryview(f.read())
                # Access individual bytes
                first_byte = mv[0]
                # Create slice
                slice_view = mv[1:4]

            # Memory-mapped files
            import mmap

            with open('large_file.bin', 'rb') as f:
                mm = mmap.mmap(f.fileno(), 0, 
                               access=mmap.ACCESS_READ)
                # Use like a string/bytes object
                data = mm[10:20]
                mm.close()
            """
                        },
                        "best_practices": [
                            "Use appropriate binary modes ('rb', 'wb')",
                            "Handle endianness in structured data",
                            "Use memory mapping for large files",
                            "Consider buffering for performance",
                            "Validate binary data structure"
                        ]
                    }
                }
            ],

            "advanced concepts": [
                {
                    "decorators": {
                        "description": "Functions that modify other functions or classes",
                        "examples": {
                            "function_decorators": """
            # Basic decorator
            def timing_decorator(func):
                from time import time
                def wrapper(*args, **kwargs):
                    start = time()
                    result = func(*args, **kwargs)
                    end = time()
                    print(f"{func.__name__} took {end-start:.2f} seconds")
                    return result
                return wrapper

            @timing_decorator
            def slow_function():
                from time import sleep
                sleep(1)
                return "Done"

            # Decorator with arguments
            def repeat(times):
                def decorator(func):
                    def wrapper(*args, **kwargs):
                        for _ in range(times):
                            result = func(*args, **kwargs)
                        return result
                    return wrapper
                return decorator

            @repeat(times=3)
            def greet(name):
                print(f"Hello {name}")""",
                            "class_decorators": """
            # Class decorator
            class CountCalls:
                def __init__(self, func):
                    self.func = func
                    self.count = 0

                def __call__(self, *args, **kwargs):
                    self.count += 1
                    print(f"Call {self.count} of {self.func.__name__}")
                    return self.func(*args, **kwargs)

            @CountCalls
            def say_hello():
                print("Hello!")

            # Property decorator
            class Temperature:
                def __init__(self, celsius):
                    self._celsius = celsius

                @property
                def fahrenheit(self):
                    return (self._celsius * 9/5) + 32

                @fahrenheit.setter
                def fahrenheit(self, value):
                    self._celsius = (value - 32) * 5/9"""
                        },
                        "best_practices": [
                            "Use functools.wraps to preserve function metadata",
                            "Keep decorators simple and focused",
                            "Handle all possible arguments",
                            "Preserve function signatures",
                            "Document decorator behavior"
                        ]
                    },
                    "generators": {
                        "description": "Functions that generate a sequence of values over time",
                        "examples": {
                            "basic_generators": """
            # Simple generator
            def number_generator(n):
                for i in range(n):
                    yield i

            # Generator with state
            def fibonacci():
                a, b = 0, 1
                while True:
                    yield a
                    a, b = b, a + b

            # Generator expression
            squares = (x**2 for x in range(10))""",
                            "advanced_generators": """
            # Generator with send
            def counter():
                count = 0
                while True:
                    val = yield count
                    if val is not None:
                        count = val
                    else:
                        count += 1

            # Generator pipeline
            def read_file(filename):
                with open(filename, 'r') as f:
                    for line in f:
                        yield line.strip()

            def grep(pattern, lines):
                for line in lines:
                    if pattern in line:
                        yield line

            # Using in pipeline
            file_lines = read_file('example.txt')
            matched_lines = grep('python', file_lines)"""
                        },
                        "best_practices": [
                            "Use generators for large sequences",
                            "Implement cleanup in finally block",
                            "Use send() carefully",
                            "Consider memory usage",
                            "Document generator behavior"
                        ]
                    },
                    "recursion": {
                        "description": "Functions that call themselves to solve problems",
                        "examples": {
                            "basic_recursion": """
            # Factorial calculation
            def factorial(n):
                if n <= 1:
                    return 1
                return n * factorial(n - 1)

            # Fibonacci sequence
            def fibonacci(n):
                if n <= 1:
                    return n
                return fibonacci(n-1) + fibonacci(n-2)""",
                            "advanced_recursion": """
            # Tree traversal
            class Node:
                def __init__(self, value, left=None, right=None):
                    self.value = value
                    self.left = left
                    self.right = right

            def traverse(node):
                if node is None:
                    return
                traverse(node.left)
                print(node.value)
                traverse(node.right)

            # Tail recursion optimization
            def factorial_tail(n, accumulator=1):
                if n <= 1:
                    return accumulator
                return factorial_tail(n - 1, n * accumulator)"""
                        },
                        "best_practices": [
                            "Consider stack depth limitations",
                            "Use tail recursion when possible",
                            "Consider iterative alternatives",
                            "Handle base cases properly",
                            "Document recursive conditions"
                        ]
                    },
                    "regular_expressions": {
                        "description": "Pattern matching and text manipulation",
                        "examples": {
                            "basic_regex": """
            import re

            # Pattern matching
            pattern = r'\\b\\w+@\\w+\\.\\w+\\b'
            text = "Contact us at info@example.com"
            matches = re.findall(pattern, text)

            # Search and replace
            text = "Hello, World!"
            new_text = re.sub(r'World', 'Python', text)

            # Pattern validation
            def is_email(email):
                pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$'
                return bool(re.match(pattern, email))""",
                            "advanced_regex": """
            # Named groups
            pattern = r'(?P<name>\\w+)\\s+(?P<age>\\d+)'
            match = re.search(pattern, "John 30")
            if match:
                print(match.group('name'))
                print(match.group('age'))

            # Lookahead and lookbehind
            text = "password123"
            has_number = bool(re.search(r'(?=.*\\d)', text))

            # Compile patterns for reuse
            email_pattern = re.compile(r'\\b\\w+@\\w+\\.\\w+\\b')
            emails = email_pattern.findall(text)"""
                        },
                        "best_practices": [
                            "Compile patterns for reuse",
                            "Use raw strings for patterns",
                            "Consider performance implications",
                            "Test patterns thoroughly",
                            "Document pattern components"
                        ]
                    },
                    "iterators": {
                        "description": "Objects that implement iteration protocol",
                        "examples": {
                            "basic_iterators": """
            # Custom iterator
            class CountUpTo:
                def __init__(self, max_value):
                    self.max_value = max_value
                    self.current = 0

                def __iter__(self):
                    return self

                def __next__(self):
                    if self.current >= self.max_value:
                        raise StopIteration
                    self.current += 1
                    return self.current""",
                            "advanced_iterators": """
            # Iterator with context management
            class DatabaseIterator:
                def __init__(self, connection):
                    self.connection = connection
                    self.cursor = None

                def __iter__(self):
                    self.cursor = self.connection.cursor()
                    return self

                def __next__(self):
                    row = self.cursor.fetchone()
                    if row is None:
                        self.cursor.close()
                        raise StopIteration
                    return row"""
                        },
                        "best_practices": [
                            "Implement both __iter__ and __next__",
                            "Handle StopIteration properly",
                            "Clean up resources",
                            "Consider memory usage",
                            "Document iterator behavior"
                        ]
                    },
                    "multithreading": {
                        "description": "Concurrent execution using threads",
                        "examples": {
                            "basic_threading": """
            import threading

            def worker(number):
                print(f"Worker {number} starting")
                # Do some work
                print(f"Worker {number} finished")

            threads = []
            for i in range(5):
                t = threading.Thread(target=worker, args=(i,))
                threads.append(t)
                t.start()

            for t in threads:
                t.join()""",
                            "advanced_threading": """
            # Thread synchronization
            class SafeCounter:
                def __init__(self):
                    self._counter = 0
                    self._lock = threading.Lock()

                def increment(self):
                    with self._lock:
                        self._counter += 1

                @property
                def value(self):
                    with self._lock:
                        return self._counter

            # Thread pool
            from concurrent.futures import ThreadPoolExecutor

            def process_item(item):
                # Process item
                return item * 2

            with ThreadPoolExecutor(max_workers=4) as executor:
                results = list(executor.map(process_item, range(10)))"""
                        },
                        "best_practices": [
                            "Use thread-safe data structures",
                            "Avoid global variables",
                            "Handle thread synchronization",
                            "Consider the GIL",
                            "Clean up threads properly"
                        ]
                    },
                    "multiprocessing": {
                        "description": "Parallel execution using processes",
                        "examples": {
                            "basic_multiprocessing": """
            from multiprocessing import Process

            def worker(number):
                print(f"Process {number} starting")
                # Do some work
                print(f"Process {number} finished")

            if __name__ == '__main__':
                processes = []
                for i in range(5):
                    p = Process(target=worker, args=(i,))
                    processes.append(p)
                    p.start()

                for p in processes:
                    p.join()""",
                            "advanced_multiprocessing": """
            from multiprocessing import Pool, Queue, Manager

            def process_chunk(chunk):
                return [x * 2 for x in chunk]

            if __name__ == '__main__':
                # Process pool
                with Pool(4) as pool:
                    data = range(100)
                    results = pool.map(process_chunk, 
                                     [data[i:i+10] for i in range(0, 100, 10)])

                # Shared memory
                with Manager() as manager:
                    shared_dict = manager.dict()
                    shared_list = manager.list()"""
                        },
                        "best_practices": [
                            "Use Process Pool for CPU-bound tasks",
                            "Handle process communication properly",
                            "Consider serialization overhead",
                            "Protect the main module",
                            "Clean up processes properly"
                        ]
                    },
                    "asynchronous_programming": {
                        "description": "Cooperative multitasking using coroutines",
                        "examples": {
                            "basic_async": """
            import asyncio

            async def say_hello(name, delay):
                await asyncio.sleep(delay)
                print(f"Hello, {name}")

            async def main():
                await asyncio.gather(
                    say_hello("Alice", 1),
                    say_hello("Bob", 2),
                    say_hello("Charlie", 3)
                )

            asyncio.run(main())""",
                            "advanced_async": """
            import aiohttp
            import asyncio

            async def fetch_url(session, url):
                async with session.get(url) as response:
                    return await response.text()

            async def main():
                urls = [
                    'http://example.com',
                    'http://example.org',
                    'http://example.net'
                ]

                async with aiohttp.ClientSession() as session:
                    tasks = [fetch_url(session, url) for url in urls]
                    results = await asyncio.gather(*tasks)

                return results

            # Event loop and tasks
            loop = asyncio.get_event_loop()
            tasks = [
                loop.create_task(say_hello("Alice", 1)),
                loop.create_task(say_hello("Bob", 2))
            ]
            loop.run_until_complete(asyncio.wait(tasks))"""
                        },
                        "best_practices": [
                            "Use asyncio for I/O-bound tasks",
                            "Avoid blocking operations",
                            "Handle exceptions properly",
                            "Use context managers",
                            "Clean up resources properly"
                        ]
                    }
                }
            ],

            "error handling": [
                {
                    "exceptions": "Exceptions are Python's way of handling errors during program execution. They include built-in types like TypeError, ValueError, and IndexError.",
                    "examples": [
                        "# Handling multiple exception types",
                        "try:",
                        "    result = '2' + 2  # TypeError",
                        "    numbers = [1, 2, 3]",
                        "    value = numbers[10]  # IndexError",
                        "except TypeError as e:",
                        "    print(f'Type mismatch: {e}')",
                        "except IndexError as e:",
                        "    print(f'Invalid index: {e}')"
                    ]
                },
                {
                    "try-except blocks": "Control structures for handling exceptions, including optional else and finally clauses for additional control flow.",
                    "examples": [
                        "# Complete try-except structure",
                        "try:",
                        "    file = open('data.txt')",
                        "except FileNotFoundError:",
                        "    print('File not found')",
                        "else:",
                        "    content = file.read()",
                        "finally:",
                        "    file.close()"
                    ]
                },
                {
                    "raising exceptions": "Mechanism to trigger exceptions manually when invalid conditions are detected in code.",
                    "examples": [
                        "def validate_age(age):",
                        "    if not isinstance(age, int):",
                        "        raise TypeError('Age must be an integer')",
                        "    if age < 0:",
                        "        raise ValueError('Age cannot be negative')",
                        "    return age"
                    ]
                },
                {
                    "custom exceptions": "User-defined exception classes that inherit from the base Exception class for specific error cases.",
                    "examples": [
                        "class ValidationError(Exception):",
                        "    def __init__(self, message, code=None):",
                        "        self.message = message",
                        "        self.code = code",
                        "    def __str__(self):",
                        "        return f'Error {self.code}: {self.message}'"
                    ]
                },
                {
                    "debugging techniques": "Methods for finding and fixing errors in code, including print debugging, logging, and using debuggers.",
                    "examples": [
                        "import logging",
                        "logging.basicConfig(level=logging.DEBUG)",
                        "logger = logging.getLogger(__name__)",
                        "",
                        "def process_data(data):",
                        "    logger.debug(f'Processing: {data}')",
                        "    try:",
                        "        result = perform_operation(data)",
                        "        logger.info('Operation successful')",
                        "        return result",
                        "    except Exception as e:",
                        "        logger.error(f'Error: {e}')",
                        "        raise"
                    ]
                },
                {
                    "assertions": "Debug-time checks that verify conditions and assumptions in code.",
                    "examples": [
                        "def calculate_average(numbers):",
                        "    assert len(numbers) > 0, 'List cannot be empty'",
                        "    assert all(isinstance(x, (int, float)) for x in numbers),",
                        "           'All elements must be numbers'",
                        "    return sum(numbers) / len(numbers)"
                    ]
                }
            ],

            "functional programming": [
                {
                    "first-class functions": "In Python, functions are first-class objects that can be assigned to variables, passed as arguments, and returned from other functions.",
                    "examples": [
                        "# Assigning functions to variables",
                        "def greet(name):",
                        "    return f'Hello, {name}!'",
                        "",
                        "say_hello = greet",
                        "print(say_hello('Alice'))  # Hello, Alice!",
                        "",
                        "# Passing functions as arguments",
                        "def apply_function(func, value):",
                        "    return func(value)",
                        "",
                        "def double(x):",
                        "    return x * 2",
                        "",
                        "result = apply_function(double, 5)  # 10"
                    ]
                },
                {
                    "higher-order functions": "Functions that take other functions as arguments or return functions as results.",
                    "examples": [
                        "# Function returning a function",
                        "def create_multiplier(factor):",
                        "    def multiplier(x):",
                        "        return x * factor",
                        "    return multiplier",
                        "",
                        "double = create_multiplier(2)",
                        "triple = create_multiplier(3)",
                        "print(double(5))  # 10",
                        "print(triple(5))  # 15",
                        "",
                        "# Function taking a function as argument",
                        "def process_list(items, processor):",
                        "    return [processor(item) for item in items]",
                        "",
                        "numbers = [1, 2, 3, 4]",
                        "squared = process_list(numbers, lambda x: x**2)  # [1, 4, 9, 16]"
                    ]
                },
                {
                    "map, filter, reduce": "Built-in functions for functional-style operations on iterables.",
                    "examples": [
                        "from functools import reduce",
                        "",
                        "# map: Apply function to every item",
                        "numbers = [1, 2, 3, 4, 5]",
                        "squared = list(map(lambda x: x**2, numbers))  # [1, 4, 9, 16, 25]",
                        "",
                        "# filter: Keep items that satisfy condition",
                        "evens = list(filter(lambda x: x % 2 == 0, numbers))  # [2, 4]",
                        "",
                        "# reduce: Aggregate items to single value",
                        "product = reduce(lambda x, y: x * y, numbers)  # 120",
                        "",
                        "# Using with list comprehension alternatives",
                        "squared_comp = [x**2 for x in numbers]",
                        "evens_comp = [x for x in numbers if x % 2 == 0]"
                    ]
                },
                {
                    "closures": "Functions that capture and carry references to variables from their enclosing scope.",
                    "examples": [
                        "def create_counter():",
                        "    count = 0",
                        "    def counter():",
                        "        nonlocal count",
                        "        count += 1",
                        "        return count",
                        "    return counter",
                        "",
                        "c1 = create_counter()",
                        "print(c1())  # 1",
                        "print(c1())  # 2",
                        "",
                        "# Closure with parameters",
                        "def create_power_function(exponent):",
                        "    def power(base):",
                        "        return base ** exponent",
                        "    return power",
                        "",
                        "square = create_power_function(2)",
                        "cube = create_power_function(3)",
                        "print(square(4))  # 16",
                        "print(cube(4))    # 64"
                    ]
                },
                {
                    "partial functions": "Creating new functions with some arguments fixed.",
                    "examples": [
                        "from functools import partial",
                        "",
                        "# Basic partial function",
                        "def multiply(x, y):",
                        "    return x * y",
                        "",
                        "double = partial(multiply, y=2)",
                        "triple = partial(multiply, y=3)",
                        "print(double(5))  # 10",
                        "print(triple(5))  # 15",
                        "",
                        "# Practical example with sorting",
                        "pairs = [(1, 'one'), (2, 'two'), (3, 'three')]",
                        "get_second = partial(lambda x, i: x[i], i=1)",
                        "sorted_pairs = sorted(pairs, key=get_second)  # Sort by string"
                    ]
                },
                {
                    "anonymous functions": "Small one-time-use functions created with lambda syntax.",
                    "examples": [
                        "# Basic lambda functions",
                        "square = lambda x: x**2",
                        "print(square(5))  # 25",
                        "",
                        "# Lambda with multiple arguments",
                        "add = lambda x, y: x + y",
                        "print(add(3, 4))  # 7",
                        "",
                        "# Lambda in sorting",
                        "pairs = [(1, 'b'), (2, 'a'), (3, 'c')]",
                        "sorted_pairs = sorted(pairs, key=lambda x: x[1])",
                        "",
                        "# Lambda with conditional expression",
                        "classify = lambda x: 'even' if x % 2 == 0 else 'odd'",
                        "print(classify(4))  # 'even'",
                        "print(classify(5))  # 'odd'"
                    ]
                }
            ],

            "modules and packages": [
                {
                    "importing_modules": "Methods for importing and using code from other Python files.",
                    "examples": [
                        "# Basic imports",
                        "import math",
                        "print(math.pi)  # 3.141592...",
                        "",
                        "# Import specific items",
                        "from datetime import datetime, timedelta",
                        "current_time = datetime.now()",
                        "",
                        "# Import with alias",
                        "import numpy as np",
                        "arr = np.array([1, 2, 3])",
                        "",
                        "# Import all (not recommended)",
                        "from math import *",
                        "",
                        "# Relative imports",
                        "from .utils import helper",
                        "from ..constants import config"
                    ]
                },
                {
                    "creating_modules": "Creating your own Python modules for code organization.",
                    "examples": [
                        "# math_utils.py",
                        "def add(a, b):",
                        "    return a + b",
                        "",
                        "def multiply(a, b):",
                        "    return a * b",
                        "",
                        "PI = 3.14159",
                        "",
                        "class Calculator:",
                        "    def __init__(self):",
                        "        self.value = 0",
                        "",
                        "    def add_value(self, x):",
                        "        self.value += x",
                        "",
                        "if __name__ == '__main__':",
                        "    # Code that runs when module is executed directly",
                        "    print('Running math_utils module')",
                        "",
                        "# Using the module",
                        "import math_utils",
                        "result = math_utils.add(5, 3)"
                    ]
                },
                {
                    "python_standard_library": "Built-in modules that come with Python installation.",
                    "examples": [
                        "# Common standard library modules",
                        "import os",
                        "current_dir = os.getcwd()",
                        "files = os.listdir('.')",
                        "",
                        "import sys",
                        "python_path = sys.path",
                        "version = sys.version",
                        "",
                        "import json",
                        "data = json.dumps({'name': 'John', 'age': 30})",
                        "",
                        "import datetime",
                        "today = datetime.date.today()",
                        "",
                        "import random",
                        "random_number = random.randint(1, 10)",
                        "",
                        "import collections",
                        "counter = collections.Counter(['a', 'b', 'a'])",
                        "",
                        "import itertools",
                        "combinations = itertools.combinations([1, 2, 3], 2)"
                    ]
                },
                {
                    "third_party_packages": "External packages installed using pip and package managers.",
                    "examples": [
                        "# Installing packages",
                        "# pip install package_name",
                        "# pip install -r requirements.txt",
                        "",
                        "# Popular third-party packages",
                        "import requests",
                        "response = requests.get('https://api.example.com')",
                        "",
                        "import pandas as pd",
                        "df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})",
                        "",
                        "import numpy as np",
                        "array = np.array([1, 2, 3])",
                        "",
                        "# Virtual environments",
                        "# python -m venv myenv",
                        "# source myenv/bin/activate  # Unix",
                        "# myenv\\Scripts\\activate    # Windows",
                        "",
                        "# Requirements file (requirements.txt)",
                        "# numpy==1.21.0",
                        "# pandas>=1.3.0",
                        "# requests~=2.26.0"
                    ]
                },
                {
                    "package_structure": "Organizing code into packages with multiple modules.",
                    "examples": [
                        "# Package structure",
                        "mypackage/",
                        "    __init__.py",
                        "    module1.py",
                        "    module2.py",
                        "    subpackage/",
                        "        __init__.py",
                        "        module3.py",
                        "",
                        "# __init__.py example",
                        "from .module1 import function1",
                        "from .module2 import function2",
                        "",
                        "__all__ = ['function1', 'function2']",
                        "",
                        "# Using the package",
                        "from mypackage import function1",
                        "from mypackage.subpackage import module3",
                        "",
                        "# Setup.py for distribution",
                        "from setuptools import setup, find_packages",
                        "",
                        "setup(",
                        "    name='mypackage',",
                        "    version='0.1',",
                        "    packages=find_packages(),",
                        "    install_requires=[",
                        "        'requests>=2.22.0',",
                        "        'pandas>=1.0.0',",
                        "    ],",
                        ")"
                    ]
                },
                {
                    "namespace_packages": "Splitting packages across multiple directories.",
                    "examples": [
                        "# Namespace package structure",
                        "project1/",
                        "    mynamespace/",
                        "        __init__.py",
                        "        module1.py",
                        "",
                        "project2/",
                        "    mynamespace/",
                        "        __init__.py",
                        "        module2.py",
                        "",
                        "# Using namespace packages",
                        "from mynamespace import module1",
                        "from mynamespace import module2",
                        "",
                        "# Creating namespace package",
                        "# __init__.py can be empty or contain:",
                        "__import__('pkg_resources').declare_namespace(__name__)"
                    ]
                }
            ],

            "testing": [
                {
                    "unit_testing": "Testing individual components of code using Python's unittest framework",
                    "examples": [
                        "# Basic unit test",
                        "import unittest",
                        "",
                        "class Calculator:",
                        "    def add(self, a, b):",
                        "        return a + b",
                        "",
                        "class TestCalculator(unittest.TestCase):",
                        "    def setUp(self):",
                        "        self.calc = Calculator()",
                        "",
                        "    def test_add(self):",
                        "        result = self.calc.add(3, 5)",
                        "        self.assertEqual(result, 8)",
                        "",
                        "    def test_add_negative(self):",
                        "        result = self.calc.add(-1, -1)",
                        "        self.assertEqual(result, -2)",
                        "",
                        "    def tearDown(self):",
                        "        pass",
                        "",
                        "if __name__ == '__main__':",
                        "    unittest.main()"
                    ],
                    "assertions": [
                        "# Common assertions",
                        "self.assertEqual(x, y)      # x == y",
                        "self.assertNotEqual(x, y)   # x != y",
                        "self.assertTrue(x)          # bool(x) is True",
                        "self.assertFalse(x)         # bool(x) is False",
                        "self.assertIs(x, y)         # x is y",
                        "self.assertIsNone(x)        # x is None",
                        "self.assertIn(x, y)         # x in y",
                        "self.assertIsInstance(x, y)  # isinstance(x, y)",
                        "self.assertRaises(Exception, func, args)"
                    ]
                },
                {
                    "pytest": "Popular Python testing framework with simpler syntax and powerful features",
                    "examples": [
                        "# Basic pytest example",
                        "# test_calculator.py",
                        "def test_addition():",
                        "    assert 1 + 1 == 2",
                        "",
                        "# Fixtures",
                        "import pytest",
                        "",
                        "@pytest.fixture",
                        "def calculator():",
                        "    return Calculator()",
                        "",
                        "def test_add(calculator):",
                        "    assert calculator.add(2, 3) == 5",
                        "",
                        "# Parameterized testing",
                        "@pytest.mark.parametrize('a,b,expected', [",
                        "    (2, 3, 5),",
                        "    (-1, 1, 0),",
                        "    (0, 0, 0)",
                        "])",
                        "def test_add_params(calculator, a, b, expected):",
                        "    assert calculator.add(a, b) == expected",
                        "",
                        "# Testing exceptions",
                        "def test_divide_by_zero(calculator):",
                        "    with pytest.raises(ZeroDivisionError):",
                        "        calculator.divide(1, 0)"
                    ]
                },
                {
                    "mocking": "Replacing parts of the system with mock objects for testing",
                    "examples": [
                        "# Using unittest.mock",
                        "from unittest.mock import Mock, patch",
                        "",
                        "class UserService:",
                        "    def get_user(self, user_id):",
                        "        # Actual API call here",
                        "        pass",
                        "",
                        "# Mock object",
                        "def test_get_user():",
                        "    service = UserService()",
                        "    service.get_user = Mock(return_value={'id': 1, 'name': 'John'})",
                        "    result = service.get_user(1)",
                        "    assert result['name'] == 'John'",
                        "",
                        "# Patching",
                        "@patch('requests.get')",
                        "def test_api_call(mock_get):",
                        "    mock_get.return_value.status_code = 200",
                        "    mock_get.return_value.json.return_value = {'data': 'test'}",
                        "    # Test code here",
                        "",
                        "# Mock with side effects",
                        "def side_effect_func(arg):",
                        "    if arg == 1:",
                        "        return 'one'",
                        "    raise ValueError('Invalid arg')",
                        "",
                        "mock_func = Mock(side_effect=side_effect_func)"
                    ]
                },
                {
                    "test-driven_development": "Writing tests before implementing functionality",
                    "examples": [
                        "# TDD Cycle Example",
                        "# 1. Write failing test",
                        "def test_user_creation():",
                        "    user = User('John', 'john@example.com')",
                        "    assert user.name == 'John'",
                        "    assert user.email == 'john@example.com'",
                        "    assert user.is_active == True",
                        "",
                        "# 2. Implement minimal code to pass",
                        "class User:",
                        "    def __init__(self, name, email):",
                        "        self.name = name",
                        "        self.email = email",
                        "        self.is_active = True",
                        "",
                        "# 3. Refactor",
                        "class User:",
                        "    def __init__(self, name, email):",
                        "        self.name = self._validate_name(name)",
                        "        self.email = self._validate_email(email)",
                        "        self.is_active = True",
                        "",
                        "    def _validate_name(self, name):",
                        "        if not name or not isinstance(name, str):",
                        "            raise ValueError('Invalid name')",
                        "        return name.strip()",
                        "",
                        "    def _validate_email(self, email):",
                        "        if not '@' in email:",
                        "            raise ValueError('Invalid email')",
                        "        return email.lower()"
                    ]
                },
                {
                    "test_organization": "Best practices for organizing and structuring tests",
                    "examples": [
                        "# Directory structure",
                        "project/",
                        "    src/",
                        "        module.py",
                        "    tests/",
                        "        __init__.py",
                        "        test_module.py",
                        "        conftest.py",
                        "",
                        "# conftest.py for shared fixtures",
                        "import pytest",
                        "",
                        "@pytest.fixture(scope='session')",
                        "def database():",
                        "    # Setup database",
                        "    db = Database()",
                        "    yield db",
                        "    # Teardown database",
                        "    db.close()",
                        "",
                        "# Test categories",
                        "@pytest.mark.slow",
                        "def test_slow_operation():",
                        "    pass",
                        "",
                        "@pytest.mark.integration",
                        "def test_integration():",
                        "    pass"
                    ]
                },
                {
                    "testing_best_practices": "Guidelines for writing effective tests",
                    "concepts": [
                        "# Test Isolation",
                        "- Each test should be independent",
                        "- Use fixtures for setup and teardown",
                        "- Avoid test interdependence",
                        "",
                        "# Test Coverage",
                        "- Use coverage.py to measure test coverage",
                        "- Aim for high coverage but don't obsess",
                        "- Test edge cases and error conditions",
                        "",
                        "# Test Organization",
                        "- One test file per module",
                        "- Clear test names describing behavior",
                        "- Group related tests in classes",
                        "- Use appropriate fixtures",
                        "",
                        "# Test Performance",
                        "- Keep tests fast",
                        "- Use appropriate scopes for fixtures",
                        "- Mock expensive operations",
                        "- Use test categories for slow tests"
                    ]
                }
            ],

            "databases": [
                {
                    "SQLite": "Lightweight, serverless database included with Python",
                    "examples": [
                        "# Basic SQLite operations",
                        "import sqlite3",
                        "",
                        "# Connect to database",
                        "conn = sqlite3.connect('example.db')",
                        "cursor = conn.cursor()",
                        "",
                        "# Create table",
                        "cursor.execute('''",
                        "    CREATE TABLE IF NOT EXISTS users (",
                        "        id INTEGER PRIMARY KEY AUTOINCREMENT,",
                        "        name TEXT NOT NULL,",
                        "        email TEXT UNIQUE",
                        "    )",
                        "''')",
                        "",
                        "# Insert data",
                        "def add_user(name, email):",
                        "    cursor.execute('''",
                        "        INSERT INTO users (name, email)",
                        "        VALUES (?, ?)",
                        "    ''', (name, email))",
                        "    conn.commit()",
                        "",
                        "# Query data",
                        "def get_user(user_id):",
                        "    cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))",
                        "    return cursor.fetchone()",
                        "",
                        "# Using context manager",
                        "with sqlite3.connect('example.db') as conn:",
                        "    cur = conn.cursor()",
                        "    cur.execute('SELECT * FROM users')",
                        "    users = cur.fetchall()"
                    ]
                },
                {
                    "MySQL": "Popular open-source relational database",
                    "examples": [
                        "# Using MySQL Connector",
                        "import mysql.connector",
                        "",
                        "# Connect to MySQL",
                        "db = mysql.connector.connect(",
                        "    host='localhost',",
                        "    user='username',",
                        "    password='password',",
                        "    database='mydatabase'",
                        ")",
                        "",
                        "# Create table",
                        "cursor = db.cursor()",
                        "cursor.execute('''",
                        "    CREATE TABLE IF NOT EXISTS products (",
                        "        id INT AUTO_INCREMENT PRIMARY KEY,",
                        "        name VARCHAR(255),",
                        "        price DECIMAL(10, 2)",
                        "    )",
                        "''')",
                        "",
                        "# Using connection pool",
                        "from mysql.connector import pooling",
                        "",
                        "dbconfig = {",
                        "    'pool_name': 'mypool',",
                        "    'pool_size': 5,",
                        "    'host': 'localhost',",
                        "    'user': 'username',",
                        "    'password': 'password',",
                        "    'database': 'mydatabase'",
                        "}",
                        "",
                        "pool = mysql.connector.pooling.MySQLConnectionPool(**dbconfig)",
                        "connection = pool.get_connection()"
                    ]
                },
                {
                    "PostgreSQL": "Advanced open-source relational database",
                    "examples": [
                        "# Using psycopg2",
                        "import psycopg2",
                        "from psycopg2 import pool",
                        "",
                        "# Connect to PostgreSQL",
                        "conn = psycopg2.connect(",
                        "    dbname='mydatabase',",
                        "    user='username',",
                        "    password='password',",
                        "    host='localhost'",
                        ")",
                        "",
                        "# Create table with advanced features",
                        "with conn.cursor() as cur:",
                        "    cur.execute('''",
                        "        CREATE TABLE IF NOT EXISTS employees (",
                        "            id SERIAL PRIMARY KEY,",
                        "            name VARCHAR(100),",
                        "            department VARCHAR(50),",
                        "            salary NUMERIC(10,2),",
                        "            hire_date DATE,",
                        "            CONSTRAINT unique_name UNIQUE (name)",
                        "        )",
                        "    ''')",
                        "",
                        "# Connection pool",
                        "postgreSQL_pool = pool.SimpleConnectionPool(",
                        "    1, 20,",
                        "    database='mydatabase',",
                        "    user='username',",
                        "    password='password',",
                        "    host='localhost'",
                        ")"
                    ]
                },
                {
                    "ORM_SQLAlchemy": "Python SQL toolkit and Object-Relational Mapping",
                    "examples": [
                        "# Basic SQLAlchemy setup",
                        "from sqlalchemy import create_engine, Column, Integer, String",
                        "from sqlalchemy.ext.declarative import declarative_base",
                        "from sqlalchemy.orm import sessionmaker",
                        "",
                        "# Create engine",
                        "engine = create_engine('sqlite:///example.db')",
                        "Base = declarative_base()",
                        "",
                        "# Define models",
                        "class User(Base):",
                        "    __tablename__ = 'users'",
                        "    ",
                        "    id = Column(Integer, primary_key=True)",
                        "    name = Column(String)",
                        "    email = Column(String, unique=True)",
                        "",
                        "# Create tables",
                        "Base.metadata.create_all(engine)",
                        "",
                        "# Create session",
                        "Session = sessionmaker(bind=engine)",
                        "session = Session()",
                        "",
                        "# CRUD operations",
                        "def create_user(name, email):",
                        "    user = User(name=name, email=email)",
                        "    session.add(user)",
                        "    session.commit()",
                        "",
                        "def get_user(user_id):",
                        "    return session.query(User).filter_by(id=user_id).first()",
                        "",
                        "def update_user(user_id, new_name):",
                        "    user = get_user(user_id)",
                        "    if user:",
                        "        user.name = new_name",
                        "        session.commit()",
                        "",
                        "def delete_user(user_id):",
                        "    user = get_user(user_id)",
                        "    if user:",
                        "        session.delete(user)",
                        "        session.commit()"
                    ]
                },
                {
                    "database_best_practices": "Guidelines for database programming",
                    "concepts": [
                        "# Connection Management",
                        "- Use connection pools for better performance",
                        "- Always close connections properly",
                        "- Use context managers when possible",
                        "",
                        "# Security",
                        "- Use parameterized queries to prevent SQL injection",
                        "- Never store plain text passwords",
                        "- Use appropriate user permissions",
                        "",
                        "# Performance",
                        "- Index frequently queried columns",
                        "- Use batch operations for bulk updates",
                        "- Optimize queries for large datasets",
                        "",
                        "# Error Handling",
                        "- Handle database exceptions properly",
                        "- Implement proper transaction management",
                        "- Add retry logic for failed connections"
                    ],
                    "examples": [
                        "# Transaction management",
                        "from sqlalchemy import create_engine",
                        "from sqlalchemy.orm import sessionmaker",
                        "",
                        "engine = create_engine('postgresql://user:pass@localhost/db')",
                        "Session = sessionmaker(bind=engine)",
                        "",
                        "def transfer_money(from_account, to_account, amount):",
                        "    session = Session()",
                        "    try:",
                        "        from_acc = session.query(Account).get(from_account)",
                        "        to_acc = session.query(Account).get(to_account)",
                        "        ",
                        "        from_acc.balance -= amount",
                        "        to_acc.balance += amount",
                        "        ",
                        "        session.commit()",
                        "    except Exception as e:",
                        "        session.rollback()",
                        "        raise",
                        "    finally:",
                        "        session.close()"
                    ]
                },
                {
                    "database_migrations": "Managing database schema changes",
                    "examples": [
                        "# Using Alembic with SQLAlchemy",
                        "# alembic.ini configuration",
                        "sqlalchemy.url = driver://user:pass@localhost/dbname",
                        "",
                        "# Migration script",
                        "from alembic import op",
                        "import sqlalchemy as sa",
                        "",
                        "def upgrade():",
                        "    op.create_table(",
                        "        'account',",
                        "        sa.Column('id', sa.Integer, primary_key=True),",
                        "        sa.Column('name', sa.String(50), nullable=False),",
                        "        sa.Column('description', sa.Unicode(200))",
                        "    )",
                        "",
                        "def downgrade():",
                        "    op.drop_table('account')"
                    ]
                }
            ],
            "performance optimization": [
    {
      "profiling_code": "Techniques to measure and analyze code performance",
      "examples": [
        "# Using cProfile",
        "import cProfile",
        "import pstats",
        "",
        "def profile_func(func):",
        "    profiler = cProfile.Profile()",
        "    profiler.enable()",
        "    func()",
        "    profiler.disable()",
        "    stats = pstats.Stats(profiler).sort_stats('cumulative')",
        "    stats.print_stats()",
        "",
        "# Time measurement",
        "from timeit import timeit",
        "",
        "def measure_time():",
        "    setup = 'x = list(range(1000))'",
        "    stmt = 'sorted(x)'",
        "    time = timeit(stmt, setup, number=1000)",
        "    print(f'Average time: {time/1000} seconds')",
        "",
        "# Memory profiling",
        "from memory_profiler import profile",
        "",
        "@profile",
        "def memory_intensive_function():",
        "    large_list = [i for i in range(1000000)]",
        "    return sum(large_list)"
      ]
    },
    {
      "algorithm_optimization": "Improving algorithmic efficiency",
      "examples": [
        "# Optimizing loops",
        "# Bad practice",
        "def slow_append():",
        "    result = []",
        "    for i in range(1000):",
        "        result = result + [i]  # Creates new list each time",
        "",
        "# Better practice",
        "def fast_append():",
        "    result = []",
        "    for i in range(1000):",
        "        result.append(i)  # In-place append",
        "",
        "# List comprehension vs loop",
        "# Slower",
        "squares = []",
        "for i in range(1000):",
        "    squares.append(i**2)",
        "",
        "# Faster",
        "squares = [i**2 for i in range(1000)]",
        "",
        "# Using generators for memory efficiency",
        "def generate_squares(n):",
        "    for i in range(n):",
        "        yield i**2"
      ]
    },
    {
      "memory_optimization": "Techniques for reducing memory usage",
      "examples": [
        "# Using __slots__",
        "class OptimizedClass:",
        "    __slots__ = ['name', 'value']  # Restricts attributes",
        "    ",
        "    def __init__(self, name, value):",
        "        self.name = name",
        "        self.value = value",
        "",
        "# Generator vs List",
        "def read_large_file(filename):",
        "    with open(filename) as f:",
        "        for line in f:  # Generator-based iteration",
        "            yield line.strip()",
        "",
        "# Using array instead of list for numerical data",
        "from array import array",
        "numbers = array('i', [1, 2, 3, 4])  # More memory efficient",
        "",
        "# Weak references",
        "import weakref",
        "class Cache:",
        "    def __init__(self):",
        "        self._cache = weakref.WeakValueDictionary()"
      ]
    },
    {
      "concurrent_execution": "Utilizing multiple cores and threads",
      "examples": [
        "# Multiprocessing for CPU-bound tasks",
        "from multiprocessing import Pool",
        "",
        "def cpu_intensive_task(x):",
        "    return x * x",
        "",
        "def parallel_processing():",
        "    with Pool(4) as p:",
        "        result = p.map(cpu_intensive_task, range(1000))",
        "",
        "# Threading for I/O-bound tasks",
        "import threading",
        "import queue",
        "",
        "def worker(queue):",
        "    while True:",
        "        item = queue.get()",
        "        if item is None:",
        "            break",
        "        process_item(item)",
        "        queue.task_done()",
        "",
        "# Asyncio for concurrent I/O",
        "import asyncio",
        "",
        "async def async_task(name):",
        "    await asyncio.sleep(1)",
        "    return f'Task {name} completed'",
        "",
        "async def main():",
        "    tasks = [async_task(i) for i in range(10)]",
        "    results = await asyncio.gather(*tasks)"
      ]
    },
    {
      "caching": "Storing computed results for reuse",
      "examples": [
        "# Function result caching",
        "from functools import lru_cache",
        "",
        "@lru_cache(maxsize=128)",
        "def fibonacci(n):",
        "    if n < 2:",
        "        return n",
        "    return fibonacci(n-1) + fibonacci(n-2)",
        "",
        "# Custom caching",
        "class SimpleCache:",
        "    def __init__(self):",
        "        self._cache = {}"
        "",
        "    def get(self, key, default=None):",
        "        return self._cache.get(key, default)",
        "",
        "    def set(self, key, value):",
        "        self._cache[key] = value",
        "",
        "# Memoization decorator",
        "def memoize(func):",
        "    cache = {}"
        "",
        "    def memoized(*args):",
        "        if args not in cache:",
        "            cache[args] = func(*args)",
        "        return cache[args]",
        "    return memoized"
      ]
    },
    {
      "numpy_vectorization": "Using NumPy for efficient numerical operations",
      "examples": [
        "# NumPy arrays vs lists",
        "import numpy as np",
        "",
        "# Slow list operation",
        "def list_operation(lst):",
        "    return [x**2 for x in lst]",
        "",
        "# Fast NumPy operation",
        "def numpy_operation(arr):",
        "    return arr**2",
        "",
        "# Vectorized functions",
        "def vectorized_calc(x, y):",
        "    return np.multiply(x, y) + np.sin(x)",
        "",
        "# Broadcasting",
        "def efficient_broadcasting():",
        "    a = np.array([[1, 2, 3], [4, 5, 6]])",
        "    b = np.array([10, 20, 30])",
        "    return a + b  # Broadcasting happens automatically"
      ]
    },
    {
      "code_optimization_techniques": "General techniques for better performance",
      "examples": [
        "# Use built-in functions",
        "# Slower",
        "sum_squares = sum([x*x for x in range(1000)])",
        "",
        "# Faster",
        "from operator import mul",
        "sum_squares = sum(map(mul, range(1000), range(1000)))",
        "",
        "# String concatenation",
        "# Slow",
        "s = ''",
        "for i in range(1000):",
        "    s += str(i)",
        "",
        "# Fast",
        "s = ''.join(str(i) for i in range(1000))",
        "",
        "# Set operations for lookups",
        "# Slow",
        "def check_common_items(list1, list2):",
        "    return any(item in list2 for item in list1)",
        "",
        "# Fast",
        "def check_common_items_fast(list1, list2):",
        "    return bool(set(list1) & set(list2))"
      ]
    },
    {
      "database_optimization": "Optimizing database operations",
      "examples": [
        "# Batch processing",
        "from sqlalchemy.orm import Session",
        "",
        "def batch_insert(items, batch_size=1000):",
        "    session = Session()",
        "    for i in range(0, len(items), batch_size):",
        "        batch = items[i:i + batch_size]",
        "        session.bulk_insert_mappings(Model, batch)",
        "        session.commit()",
        "",
        "# Connection pooling",
        "from sqlalchemy import create_engine",
        "",
        "engine = create_engine('postgresql:///',",
        "                      pool_size=20,",
        "                      max_overflow=0)",
        "",
        "# Efficient querying",
        "def efficient_query():",
        "    return (session.query(User)",
        "            .filter(User.active == True)",
        "            .options(selectinload(User.posts))",
        "            .limit(100)",
        "            .all())"
      ]
    }
  ]

        }

        return knowledge_base
        pass
    def init_quiz_questions(self):

        return {
    "Basics": [
        ("What keyword is used to define a function in Python?", "def"),
        ("Which of these is not a valid variable name: my_var, 2nd_var, _private, camelCase?", "2nd_var"),
        ("What is the result of 3 * 'abc'?", "abcabcabc"),
        ("What type of operator is 'in'?", "membership"),
        ("How do you import a module named 'mymodule' in Python?", "import mymodule")
    ],
    "data structures": [
        ("What data structure in Python is ordered and mutable?", "list"),
        ("What method would you use to add an element to a set?", "add"),
        ("What is the syntax to create an empty dictionary?", "{}"),
        ("Which of these is not mutable: list, tuple, set, dictionary?", "tuple"),
        ("What is the output of [1, 2, 3] + [4, 5, 6]?", "[1, 2, 3, 4, 5, 6]")
    ],
    "object-oriented programming": [
        ("What keyword is used to define a class in Python?", "class"),
        ("What method is called when an object is created?", "__init__"),
        ("What is it called when a class inherits properties from another class?", "inheritance"),
        ("What does the 'self' keyword refer to?", "the instance of the class"),
        ("What is it called when a method in a subclass overrides a method in its superclass?", "method overriding")
    ],
    "file handling": [
        ("What function is used to open a file in Python?", "open"),
        ("What mode should you use to open a file for reading?", "r"),
        ("What method reads all lines of a file into a list?", "readlines"),
        ("What module is commonly used for working with CSV files?", "csv"),
        ("What is the advantage of using a 'with' statement when working with files?", "it automatically closes the file")
    ],
    "advanced concepts": [
        ("What character is used to define a lambda function?", ":"),
        ("What type of object does a generator function return?", "iterator"),
        ("What decorator is used to define a static method?", "@staticmethod"),
        ("What is the purpose of the 'yield' keyword?", "to define a generator function"),
        ("What module is used for working with regular expressions in Python?", "re")
    ],
    "error handling": [
        ("What keyword is used to handle exceptions in Python?", "except"),
        ("What clause is used to define code that should run regardless of whether an exception occurred?", "finally"),
        ("What built-in exception is raised when trying to divide by zero?", "ZeroDivisionError"),
        ("How do you define a custom exception class?", "inherit from Exception"),
        ("What function can be used to raise an exception manually?", "raise")
    ],
    "functional programming": [
        ("What built-in function applies a function to all items in an input list?", "map"),
        ("What is a function called that takes another function as an argument?", "higher-order function"),
        ("What is the output of filter(lambda x: x > 5, [2, 4, 6, 8, 10])?", "[6, 8, 10]"),
        ("What is a function that returns another function called?", "closure"),
        ("What module provides the 'reduce' function in Python 3?", "functools")
    ],
    "modules and packages": [
        ("How do you import all contents of a module named 'mymodule'?", "from mymodule import *"),
        ("What command installs third-party packages in Python?", "pip install package_name"),
        ("What built-in module provides access to operating system functionality?", "os"),
        ("How can you check for installed packages in your Python environment?", "pip list"),
        ("What method can be used to reload a module?", "importlib.reload")
    ],
    "testing": [
        ("What module is commonly used for unit testing in Python?", "unittest"),
        ("What is the command to run a test case file in Python?", "python -m unittest test_file.py"),
        ("Which function is used to assert equality in unit tests?", "assertEqual"),
        ("What is the purpose of mocking in tests?", "to simulate the behavior of objects and methods"),
        ("What is Pytest used for?", "writing and executing test cases in Python")
    ],
    "performance optimization": [
                ("What does Python use for automatic memory management?", "Garbage collection"),
                ("Which Python module is used to interact with the garbage collector?", "gc"),
                ("What is the purpose of time complexity in algorithms?",
                 "To analyze the time an algorithm takes to run as a function of the input size"),
                ("What notation is commonly used to describe time complexity?", "Big O notation"),
                ("What is the time complexity of searching for an element in a balanced binary search tree?",
                 "O(log n)"),
                ("What is space complexity?",
                 "The amount of memory required by an algorithm relative to the input size"),
                ("Which data structure is more memory efficient for iterating over large datasets: list or generator?",
                 "Generator"),
                ("How does Python handle memory deallocation for unused objects?",
                 "Through reference counting and garbage collection"),
                ("What is the time complexity of accessing an element in a Python list?", "O(1)"),
                ("What is the advantage of using a generator over a list for large datasets?",
                 "Generators are more memory efficient as they generate items on-the-fly instead of storing them in memory.")
            ],
    "asynchronous programming": [
        ("What keyword defines an asynchronous function?", "async"),
        ("What is used to pause execution in async functions?", "await"),
        ("Which library in Python is primarily used for async programming?", "asyncio"),
        ("What is the event loop?", "a core mechanism to run asynchronous tasks"),
        ("What is a coroutine?", "a function that can pause and resume its execution")
    ]
}
    pass
    def preprocess_text(self, text):
        tokens = word_tokenize(text.lower())
        return " ".join(
            [self.lemmatizer.lemmatize(word) for word in tokens if word not in self.stop_words and word.isalnum()])

    def is_exit_command(self, user_input):
        return any(cmd in user_input for cmd in self.exit_commands)

    def get_most_similar_subtopic(self, query):
        preprocessed_query = self.preprocess_text(query)
        subtopics = list(self.knowledge_base.keys())
        corpus = [self.preprocess_text(subtopic) for subtopic in subtopics]
        corpus.append(preprocessed_query)

        tfidf_matrix = self.vectorizer.fit_transform(corpus)
        cosine_similarities = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1]).flatten()
        most_similar_index = cosine_similarities.argmax()

        return subtopics[most_similar_index]

    def greet(self):
        return "Hello! I'm your Python Tutorial Agent. How can I help you today? Type 'topics' to see what I can teach you."

    def list_topics(self):
        topics_list = "\nAvailable Python Topics:\n"
        for i, topic in enumerate(self.topics.keys(), 1):
            topics_list += f"{i}. {topic.capitalize()}\n"
        topics_list += "\nWhich topic would you like to explore? (Type the topic name or number)"
        return topics_list

    def handle_input(self, user_input):
        user_input = user_input.lower().strip()

        if self.is_exit_command(user_input):
            return "Thank you for using the Python Tutorial Agent. Goodbye!"

        # Handle quiz mode
        if self.mode == "quiz":
            return self.handle_quiz_answer(user_input)

        # Handle post-tutorial menu choices
        if hasattr(self, 'showing_menu') and self.showing_menu:
            if user_input == "1":
                self.showing_menu = False
                return self.start_quiz()
            elif user_input == "2":
                self.showing_menu = False
                self.current_topic = None
                self.current_subtopic = None
                return "Sure, let's choose a new topic.\n" + self.list_topics()
            elif user_input == "3":
                return self.show_progress()

        # Handle progress request
        if "progress" in user_input:
            return self.show_progress()

        # Handle topics list request
        if "topic" in user_input:
            return self.list_topics()

        # Handle topic selection by number when no current topic
        if user_input.isdigit():
            topic_number = int(user_input)
            # If we're not showing a menu, treat as topic selection
            if not hasattr(self, 'showing_menu') or not self.showing_menu:
                topic_list = list(self.topics.keys())
                if 1 <= topic_number <= len(topic_list):
                    self.current_topic = topic_list[topic_number - 1]
                    self.current_subtopic = None
                    return f"Great! Let's learn about {self.current_topic}. We'll cover: {', '.join(self.topics[self.current_topic])}.\nType 'start' when you're ready to begin, or ask me anything about {self.current_topic}."
                else:
                    return f"Please enter a number between 1 and {len(topic_list)}."

        # Handle current topic actions
        if self.current_topic:
            if user_input == "start" or user_input == "next":
                return self.next_subtopic()
            elif user_input == "quiz":
                self.showing_menu = False
                return self.start_quiz()

        # Check for topic name matches
        matching_topics = [topic for topic in self.topics if topic.lower() in user_input]
        if matching_topics:
            self.current_topic = matching_topics[0]
            self.current_subtopic = None
            return f"Great! Let's learn about {self.current_topic}. We'll cover: {', '.join(self.topics[self.current_topic])}.\nType 'start' when you're ready to begin, or ask me anything about {self.current_topic}."

        # Default to most similar subtopic if no other matches
        most_similar_subtopic = self.get_most_similar_subtopic(user_input)
        subtopic_info = self.get_subtopic_info(most_similar_subtopic)
        return f"Based on your question, I think you might be interested in {most_similar_subtopic}. Here's what I know:\n\n{subtopic_info}\n\nDo you want to know more about this, or shall we move to the next topic? Type 'next' to continue or ask me anything else."

    def next_subtopic(self):
        if not self.current_topic:
            return "Please choose a topic first. " + self.list_topics()

        if not self.current_subtopic:
            self.current_subtopic = self.topics[self.current_topic][0]
        else:
            current_topics = self.topics[self.current_topic]
            try:
                current_index = current_topics.index(self.current_subtopic)
                if current_index < len(current_topics) - 1:
                    self.current_subtopic = current_topics[current_index + 1]
                else:
                    self.current_subtopic = None
                    self.showing_menu = True  # Set flag when showing menu
                    return ("We've covered all subtopics in this area. Great job!\n"
                            "Would you like to:\n"
                            "1. Take a quiz on this topic\n"
                            "2. Choose a new topic to learn about\n"
                            "3. See your overall progress\n"
                            "Type the number of your choice or ask me anything!")
            except ValueError:
                self.current_subtopic = current_topics[0]

        # Mark current subtopic as completed
        if self.current_subtopic:
            self.progress[self.current_topic][self.current_subtopic] = True
            subtopic_info = None
            for item in self.knowledge_base[self.current_topic]:
                if self.current_subtopic in item:
                    subtopic_info = item[self.current_subtopic]
                    break

            if subtopic_info:
                return (f"Let's learn about {self.current_subtopic}:\n\n"
                        f"{subtopic_info}\n\n"
                        f"What would you like to know more about {self.current_subtopic}, or type 'next' to continue?")
            else:
                return f"Information about {self.current_subtopic} is not available at the moment. Type 'next' to continue."

        return "Please choose a topic first. " + self.list_topics()

    def start_quiz(self):
        self.mode = "quiz"
        self.current_question = 0
        self.quiz_questions = self.get_quiz_questions()
        if not self.quiz_questions:
            self.mode = "tutorial"
            return "Sorry, there are no quiz questions available for this topic."
        return self.get_next_question()

    def get_next_question(self):
        if self.current_question < len(self.quiz_questions):
            question, _ = self.quiz_questions[self.current_question]
            return f"Quiz Question {self.current_question + 1}: {question}"
        else:
            self.mode = "tutorial"
            return "Quiz completed! Well done! Type 'next' to continue with the tutorial or choose a new topic."

    def handle_quiz_answer(self, user_answer):
        _, correct_answer = self.quiz_questions[self.current_question]
        if user_answer.lower() == correct_answer.lower():
            response = "Correct!"
        else:
            response = f"Sorry, the correct answer is: {correct_answer}"

        self.current_question += 1
        next_question = self.get_next_question()
        return f"{response}\n\n{next_question}"



    def get_subtopic_info(self, subtopic):
        try:
            # First try to find the subtopic in the knowledge base
            for topic_data in self.knowledge_base.values():
                for item in topic_data:
                    if subtopic in item:
                        return item[subtopic]

            # If not found, return a generic message
            return "Information not available for this subtopic."
        except Exception as e:
            print(f"Error in get_subtopic_info: {e}")
            return "Information not available at the moment."
    def show_progress(self):
        progress_report = "Here's your learning progress:\n"
        for topic, subtopics in self.progress.items():
            completed = sum(subtopics.values())
            total = len(subtopics)
            percentage = (completed / total) * 100
            progress_report += f"{topic.capitalize()}: {completed}/{total} subtopics completed ({percentage:.0f}%)\n"
        return progress_report

    def get_quiz_questions(self):
        if self.current_topic in self.quiz_questions:
            return self.quiz_questions[self.current_topic]
        else:
            return []

    def start_tutorial(self):
        print("Welcome to the Python Tutorial!")
        return self.greet()
