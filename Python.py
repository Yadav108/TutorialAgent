import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import json

import nltk
from nltk import WordNetLemmatizer, word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)


class TutorialAgent:
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
        self.progress = {topic: {subtopic: False for subtopic in subtopics} for topic, subtopics in self.topics.items()}
        self.quiz_questions = self.init_quiz_questions()

    def init_knowledge_base(self):
        knowledge_base = {
            "Basics": [
                {
                    "variables": "Variables are containers for storing data values. Python uses dynamic typing, so you don't need to declare a variable's type explicitly."
                },
                {
                    "data types": "Python has several built-in data types including integers, floating-point numbers, strings, booleans, lists, tuples, sets, and dictionaries."
                },
                {
                    "operators": "Python supports various operators: arithmetic (+, -, *, /, %, **), comparison (==, !=, <, >), logical (and, or, not), identity (is, is not), and membership (in, not in)."
                },
                {
                    "control structures": "Control structures include if-else statements, for and while loops, and try-except blocks for handling errors."
                },
                {
                    "type casting": "Type casting allows you to convert variables from one data type to another (e.g., int to float)."
                },
                {
                    "input and output": "Use input() to take user input and print() to display output in Python."
                }
            ],

            "data structures": [
                {
                    "lists": "Lists are ordered, mutable sequences. You can add, remove, and modify elements. Lists are defined with square brackets []."
                },
                {
                    "tuples": "Tuples are ordered, immutable sequences. Once created, their values cannot be changed. They are defined with parentheses ()."
                },
                {
                    "dictionaries": "Dictionaries are unordered collections of key-value pairs. They are defined with curly braces {} and allow for fast lookup of values by keys."
                },
                {
                    "sets": "Sets are unordered collections of unique elements. They are defined with curly braces {} or by using the set() function."
                },
                {
                    "list comprehensions": "List comprehensions provide a concise way to create lists based on existing lists using a single line of code."
                },
                {
                    "dictionary comprehensions": "Similar to list comprehensions but used for creating dictionaries."
                }
            ],

            "functions": [
                {
                    "defining functions": "Functions are defined using the def keyword, followed by the function name and parentheses containing parameters."
                },
                {
                    "arguments": "Functions can have positional, keyword, default, or variable-length arguments (*args, **kwargs)."
                },
                {
                    "return values": "The return statement specifies the value that a function returns to the caller."
                },
                {
                    "lambda functions": "Lambda functions are small, anonymous functions created with the lambda keyword."
                },
                {
                    "function scope": "Variables defined inside a function have local scope. Global and nonlocal keywords can be used to modify scope."
                }
            ],

            "object-oriented programming": [
                {
                    "classes": "Classes are blueprints for creating objects. A class is defined using the class keyword."
                },
                {
                    "objects": "Objects are instances of a class, containing data (attributes) and methods (functions)."
                },
                {
                    "inheritance": "Inheritance allows one class to inherit the properties and methods of another class."
                },
                {
                    "polymorphism": "Polymorphism allows different objects to be treated as instances of the same class through common interfaces."
                },
                {
                    "encapsulation": "Encapsulation restricts access to some of an object's components, using private variables and methods."
                },
                {
                    "abstraction": "Abstraction hides the complexity of the implementation from the user and shows only essential details."
                },
                {
                    "magic methods": "Special methods (dunder methods) like __init__, __str__, and __repr__ define the behavior of Python objects."
                }
            ],

            "file handling": [
                {
                    "file operations": "Basic file operations in Python include open(), read(), write(), and close()."
                },
                {
                    "reading and writing files": "Files can be read using read(), readline(), and readlines(). Files can be written using write() and writelines()."
                },
                {
                    "working with CSV": "The csv module allows reading and writing CSV files, which are simple text files with comma-separated values."
                },
                {
                    "JSON handling": "The json module helps convert Python objects to JSON format and parse JSON strings into Python objects."
                },
                {
                    "context managers": "Context managers (using the with statement) provide a cleaner way to open files and ensure that resources are properly released."
                },
                {
                    "binary file handling": "Binary file handling deals with reading and writing binary data using 'rb' or 'wb' modes."
                }
            ],

            "advanced concepts": [
                {
                    "decorators": "Decorators are a way to modify the behavior of a function or class method. They are defined using the @decorator syntax."
                },
                {
                    "generators": "Generators are functions that return an iterator. They use the yield keyword to produce a sequence of results lazily."
                },
                {
                    "recursion": "Recursion is a technique where a function calls itself in order to solve a problem."
                },
                {
                    "regular expressions": "Regular expressions (regex) allow for pattern matching in strings. Python's re module provides regex functionality."
                },
                {
                    "iterators": "Iterators are objects that allow you to traverse through all the elements of a collection, using the __iter__() and __next__() methods."
                },
                {
                    "multithreading": "Multithreading allows concurrent execution of threads in a program, improving performance for I/O-bound tasks."
                },
                {
                    "multiprocessing": "Multiprocessing enables parallel execution using multiple CPU cores."
                },
                {
                    "asynchronous programming": "Asyncio is a Python library used for writing concurrent code using async/await syntax."
                }
            ],

            "error handling": [
                {
                    "exceptions": "Exceptions are errors that occur during execution. They are handled using try-except blocks."
                },
                {
                    "try-except blocks": "Use try to wrap code that might raise an exception, and use except to handle the error if it occurs."
                },
                {
                    "raising exceptions": "You can manually raise exceptions using the raise keyword."
                },
                {
                    "custom exceptions": "Custom exceptions can be created by inheriting from Python's built-in Exception class."
                },
                {
                    "debugging techniques": "Common debugging techniques include using print statements, assert statements, and Python’s built-in pdb debugger."
                },
                {
                    "assertions": "Assertions are checks in the code to ensure that certain conditions hold true during execution."
                }
            ],

            "functional programming": [
                {
                    "first-class functions": "In Python, functions are first-class citizens, meaning they can be passed around as arguments, returned from other functions, and assigned to variables."
                },
                {
                    "higher-order functions": "Higher-order functions are functions that take other functions as arguments or return them as results."
                },
                {
                    "map, filter, reduce": "These functions apply a function to a sequence: map() applies a function to all items, filter() filters elements, and reduce() applies a cumulative function to items."
                },
                {
                    "closures": "A closure is a function object that remembers values in enclosing scopes even if they are not present in memory."
                },
                {
                    "partial functions": "Partial functions allow you to fix a few arguments of a function and generate a new function with fewer parameters."
                },
                {
                    "anonymous functions": "Anonymous functions (lambdas) are small, unnamed functions created using the lambda keyword."
                }
            ],

            "modules and packages": [
                {
                    "importing modules": "Modules are files containing Python code. They can be imported using the import statement."
                },
                {
                    "creating modules": "You can create your own modules by saving Python functions and variables in a .py file."
                },
                {
                    "Python Standard Library": "Python comes with a large standard library that provides many useful modules and functions (e.g., math, datetime, os)."
                },
                {
                    "third-party packages": "Packages can be installed from external sources using pip, the Python package installer."
                }
            ],

            "testing": [
                {
                    "unit testing": "Unit testing involves testing individual components of the code in isolation. Python’s unittest module provides a framework for writing and running tests."
                },
                {
                    "pytest": "Pytest is an advanced testing framework used to write simple as well as scalable test cases."
                },
                {
                    "mocking": "Mocking simulates the behavior of objects or functions during testing to focus on the part of the code being tested."
                },
                {
                    "test-driven development (TDD)": "TDD is a software development process where tests are written before the code, ensuring that the code passes all the tests."
                }
            ],

            "databases": [
                {
                    "SQLite": "SQLite is a lightweight, file-based database included in Python's standard library. You can interact with it using the sqlite3 module."
                },
                {
                    "PostgreSQL": "PostgreSQL is a powerful, open-source database system. You can use the psycopg2 or SQLAlchemy libraries to interact with it."
                },
                {
                    "MySQL": "MySQL is another popular relational database, and MySQL Connector or SQLAlchemy can be used to connect to it."
                },
                {
                    "ORM": "ORM-Object Relational Mapping frameworks like SQLAlchemy allow you to interact with databases using Python classes"
            }
        ],
            "performance optimization": [
                {
                    "profiling code": "Profiling involves analyzing your code's performance to identify bottlenecks. Python provides tools like cProfile and timeit for measuring execution time and performance."
                },
                {
                    "algorithm optimization": "Choosing efficient algorithms and data structures can significantly improve performance. For example, using a set instead of a list for membership checks."
                },
                {
                    "memory optimization": "Efficient use of memory can boost performance. Techniques include using generators instead of lists for large data processing and leveraging the sys.getsizeof() function to monitor memory usage."
                },
                {
                    "multithreading vs multiprocessing": "Use multithreading for I/O-bound tasks (e.g., file operations, network requests) and multiprocessing for CPU-bound tasks to better utilize system resources."
                },
                {
                    "caching with functools.lru_cache": "Caching frequently used results can save computation time. functools.lru_cache can be used to cache results of function calls."
                },
                {
                    "efficient loops": "Avoid unnecessary looping or repetitive calculations inside loops. Use built-in functions and libraries like map(), zip(), or list comprehensions for optimized loops."
                },
                {
                    "NumPy and vectorization": "Use libraries like NumPy for operations on large datasets. Vectorization with NumPy is often faster than using standard Python loops."
                },
                {
                    "compiling with Cython": "Cython converts Python code to C to improve performance for CPU-bound tasks, making it faster than regular Python execution."
                },
                {
                    "using concurrent.futures": "The concurrent.futures module provides an easier way to handle threading and multiprocessing, allowing you to distribute work across multiple CPU cores."
                },
                {
                    "database indexing": "For database operations, use proper indexing to speed up query execution and avoid unnecessary full table scans."
                },
                {
                    "memory management": "Memory management in Python is handled by the Python memory manager. Python automatically allocates and deallocates memory through garbage collection for objects that are no longer in use. You can manually control memory allocation using libraries like `gc` and handle large datasets using efficient structures such as generators."
                },
                {

                    "time complexity": "Time complexity refers to the computational complexity that describes the amount of time it takes to run an algorithm as a function of the length of the input. Understanding time complexity (using Big O notation) helps in optimizing code to run faster, especially with large data inputs."
                },
                {
                    "space complexity": "Space complexity measures the total amount of memory space that an algorithm or function needs to run relative to the size of the input. Efficient algorithms minimize both time and space usage to improve overall performance."
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
        return "Hello! I'm your Python Tutorial Agent. How can I help you today? You can ask me about specific topics or type 'topics' to see what I can teach you."

    def list_topics(self):
        return "I can teach you about: " + ", ".join(self.topics.keys()) + ". Which topic would you like to explore?"

    def handle_input(self, user_input):
        print(f"Handling input: {user_input}")
        user_input = user_input.lower().strip()

        if self.is_exit_command(user_input):
            return "Thank you for using the C# Tutorial Agent. Goodbye!"

        if user_input == "3" or "progress" in user_input:
            return self.show_progress()

        if "topic" in user_input:
            return self.list_topics()

        if self.mode == "quiz":
            return self.handle_quiz_answer(user_input)

        # Check for partial matches in topics
        matching_topics = [topic for topic in self.topics if topic.lower() in user_input]
        if matching_topics:
            self.current_topic = matching_topics[0]
            self.current_subtopic = None
            return f"Great! Let's learn about {self.current_topic}. We'll cover: {', '.join(self.topics[self.current_topic])}. Type 'start' when you're ready to begin, or ask me anything about {self.current_topic}."

        if self.current_topic:
            if user_input == "start" or "next" in user_input:
                return self.next_subtopic()
            elif user_input in ["1", "quiz"]:
                return self.start_quiz()
            elif user_input in ["2", "new topic"]:
                self.current_topic = None
                self.current_subtopic = None
                return "Sure, let's choose a new topic. " + self.list_topics()

        # If no specific topic is identified, try to find the most relevant information
        most_similar_subtopic = self.get_most_similar_subtopic(user_input)
        subtopic_info = self.get_subtopic_info(most_similar_subtopic)
        return f"Based on your question, I think you might be interested in {most_similar_subtopic}. Here's what I know:\n\n{subtopic_info}\n\nDo you want to know more about this, or shall we move to the next topic? Type 'next' to continue or ask me anything else."

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
        print(f"Getting info for subtopic: {subtopic}")
        for topic, subtopics in self.knowledge_base.items():
            for item in subtopics:
                if subtopic in item:
                    return item[subtopic]
        return "Information not available."

    def next_subtopic(self):
        if self.current_topic:
            if not self.current_subtopic:
                self.current_subtopic = self.topics[self.current_topic][0]
            else:
                current_index = self.topics[self.current_topic].index(self.current_subtopic)
                if current_index < len(self.topics[self.current_topic]) - 1:
                    self.current_subtopic = self.topics[self.current_topic][current_index + 1]
                else:
                    return ("We've covered all subtopics in this area. Great job!\n"
                            "Would you like to:\n"
                            "1. Take a quiz on this topic\n"
                            "2. Choose a new topic to learn about\n"
                            "3. See your overall progress\n"
                            "Type the number of your choice or ask me anything!")

            self.progress[self.current_topic][self.current_subtopic] = True

            subtopic_info = self.get_subtopic_info(self.current_subtopic)

            return (f"Let's learn about {self.current_subtopic}:\n\n"
                    f"{subtopic_info}\n\n"
                    f"What would you like to know more about {self.current_subtopic}, or type 'next' to continue?")
        else:
            return "Please choose a topic first. " + self.list_topics()

    def list_topics(self):
        return "I can teach you about: " + ", ".join(self.topics.keys()) + ". Which topic would you like to explore?"

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

    def show_progress(self):
        progress_report = "Here's your learning progress:\n"
        for topic, subtopics in self.progress.items():
            completed = sum(subtopics.values())
            total = len(subtopics)
            percentage = (completed / total) * 100
            progress_report += f"{topic.capitalize()}: {completed}/{total} subtopics completed ({percentage:.0f}%)\n"
        return progress_report


class TutorialGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Python Tutorial Agent")
        self.master.geometry("700x500")
        self.agent = TutorialAgent()
        self.quiz_in_progress = False
        self.current_question = 0
        self.quiz_questions = []

        self.dark_mode = self.load_dark_mode_setting()
        self.create_widgets()
        self.apply_theme()

    def create_widgets(self):
        self.style = ttk.Style()

        # Main frame
        self.main_frame = ttk.Frame(self.master, padding="10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Chat display
        self.chat_display = scrolledtext.ScrolledText(self.main_frame, wrap=tk.WORD, width=80, height=20)
        self.chat_display.grid(row=0, column=0, columnspan=6, padx=10, pady=10, sticky="nsew")
        self.chat_display.config(state=tk.DISABLED)

        # User input
        self.user_input = ttk.Entry(self.main_frame, width=70)
        self.user_input.grid(row=1, column=0, columnspan=5, padx=10, pady=10, sticky="ew")
        self.user_input.bind("<Return>", self.send_message)

        # Send button
        self.send_button = ttk.Button(self.main_frame, text="Send", command=self.send_message)
        self.send_button.grid(row=1, column=5, padx=5, pady=10)

        # Action buttons
        actions = ["Help", "Topics", "Next", "Quiz", "Progress"]
        for i, action in enumerate(actions):
            button = ttk.Button(self.main_frame, text=action, command=lambda a=action: self.perform_action(a))
            button.grid(row=2, column=i, padx=2, pady=10)

        # Dark mode toggle
        self.dark_mode_var = tk.BooleanVar(value=self.dark_mode)
        self.dark_mode_check = ttk.Checkbutton(self.main_frame, text="Dark Mode",
                                               command=self.toggle_dark_mode,
                                               variable=self.dark_mode_var)
        self.dark_mode_check.grid(row=2, column=5, padx=2, pady=10)

        # Menu
        self.menu_bar = tk.Menu(self.master)
        self.master.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Save Chat", command=self.save_chat)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.master.quit)

        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="About", command=self.show_about)

        # Configure grid
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(0, weight=1)

        self.display_message("Agent: " + self.agent.greet())

    def send_message(self, event=None):
        user_message = self.user_input.get()
        self.display_message("You: " + user_message)
        self.user_input.delete(0, tk.END)

        response = self.agent.handle_input(user_message)
        self.display_message("Agent: " + response)

        if self.agent.is_exit_command(user_message):
            self.master.after(1000, self.master.quit)

    def display_message(self, message):
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.insert(tk.END, message + "\n\n")
        self.chat_display.see(tk.END)
        self.chat_display.config(state=tk.DISABLED)

    def perform_action(self, action):
        if action == "Help":
            self.display_message(
                "Agent: You can ask me about Python topics, or use the buttons to navigate. Type 'topics' to see available topics, 'next' to move to the next subtopic, or 'quiz' to start a quiz on the current topic.")
        elif action == "Topics":
            self.display_message("Agent: " + self.agent.list_topics())
        elif action == "Next":
            response = self.agent.next_subtopic()
            self.display_message("Agent: " + response)
        elif action == "Quiz":
            response = self.agent.next_subtopic()
            self.display_message("Agent: " + response)
        elif action == "Progress":
            progress_report = self.agent.show_progress()
            self.display_message("Agent: " + progress_report)

    def start_quiz(self):
        self.quiz_questions = self.agent.get_quiz_questions()
        if not self.quiz_questions:
            self.display_message("Agent: Sorry, there are no quiz questions available for this topic.")
            return
        self.quiz_in_progress = True
        self.current_question = 0
        self.display_message("Agent: Starting the quiz. Type 'stop' or 'exit' at any time to end the quiz.")
        self.display_next_question()

    def display_next_question(self):
        if self.current_question < len(self.quiz_questions):
            question, _ = self.quiz_questions[self.current_question]
            self.display_message(f"Agent: Quiz Question {self.current_question + 1}: {question}")
        else:
            self.display_message("Agent: Quiz completed! Well done!")
            self.quiz_in_progress = False

    def handle_quiz_answer(self, user_answer):
        _, correct_answer = self.quiz_questions[self.current_question]
        if user_answer.lower() == correct_answer.lower():
            self.display_message("Agent: Correct!")
        else:
            self.display_message(f"Agent: Sorry, the correct answer is: {correct_answer}")

        self.current_question += 1
        self.display_next_question()

    def toggle_dark_mode(self):
        self.dark_mode = self.dark_mode_var.get()
        self.apply_theme()
        self.save_dark_mode_setting()

    def apply_theme(self):
        if self.dark_mode:
            self.style.theme_use('clam')
            self.style.configure(".", background="#2b2b2b", foreground="white")
            self.style.configure("TButton", background="#4a4a4a", foreground="white")
            self.style.map("TButton", background=[('active', '#666666')])
            self.style.configure("TCheckbutton", background="#2b2b2b", foreground="white")
            self.chat_display.config(bg="#2b2b2b", fg="white")
            self.user_input.config(style="Dark.TEntry")
            self.style.configure("Dark.TEntry", fieldbackground="#4a4a4a", foreground="white")
        else:
            self.style.theme_use('clam')
            self.style.configure(".", background="white", foreground="black")
            self.style.configure("TButton", background="#e1e1e1", foreground="black")
            self.style.map("TButton", background=[('active', '#d1d1d1')])
            self.style.configure("TCheckbutton", background="white", foreground="black")
            self.chat_display.config(bg="white", fg="black")
            self.user_input.config(style="TEntry")
            self.style.configure("TEntry", fieldbackground="white", foreground="black")

    def load_dark_mode_setting(self):
        try:
            with open("settings.json", "r") as f:
                settings = json.load(f)
                return settings.get("dark_mode", False)
        except (FileNotFoundError, json.JSONDecodeError):
            return False

    def save_dark_mode_setting(self):
        settings = {"dark_mode": self.dark_mode}
        with open("settings.json", "w") as f:
            json.dump(settings, f)

    def save_chat(self):
        chat_content = self.chat_display.get("1.0", tk.END)
        try:
            with open("chat_log.txt", "w", encoding="utf-8") as f:
                f.write(chat_content)
            messagebox.showinfo("Save Chat", "Chat log has been saved to chat_log.txt")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save chat log: {str(e)}")

    def show_about(self):
        about_text = "Python Tutorial Agent\nVersion 2.0\nCreated with ❤️ for learning Python\nAryan Yadav"
        messagebox.showinfo("About", about_text)

def main():
                root = tk.Tk()
                gui = TutorialGUI(root)
                root.protocol("WM_DELETE_WINDOW", root.quit)  # Ensure clean exit
                root.mainloop()

if __name__ == "__main__":
                main()