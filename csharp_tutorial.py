import nltk
from nltk import WordNetLemmatizer, word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)


class CsharpTutorialAgent:
    def __init__(self):
        self.topics = {
            "basics": ["variables", "data types", "operators", "control structures", "input and output"],

            "data structures": [
                "arrays",
                "lists (List<T>)",
                "dictionaries (Dictionary<TKey, TValue>)",
                "hash sets (HashSet<T>)",
                "queues (Queue<T>)",
                "stacks (Stack<T>)"
            ],

            "functions and methods": [
                "defining methods",
                "method overloading",
                "params keyword",
                "lambda expressions",
                "extension methods"
            ],

            "object-oriented programming": [
                "classes",
                "objects",
                "inheritance",
                "polymorphism",
                "encapsulation",
                "abstraction",
                "interfaces",
                "abstract classes"
            ],

            "exception handling": [
                "exceptions",
                "try-catch blocks",
                "finally block",
                "throwing exceptions",
                "custom exceptions"
            ],

            "file handling": [
                "file operations",
                "reading and writing files",
                "working with directories",
                "file streams"
            ],

            "advanced concepts": [
                "delegates",
                "events",
                "LINQ",
                "async and await",
                "attributes",
                "reflection",
                "dependency injection"
            ],

            "testing": [
                "unit testing",
                "integration testing",
                "mocking",
                "test-driven development"
            ],

            "performance optimization": [
                "memory management",
                "time complexity",
                "space complexity",
                "profiling",
                "caching"
            ],

            "databases": [
                "ADO.NET",
                "Entity Framework",
                "LINQ to SQL",
                "database transactions"
            ],

            "modules and packages": [
                "using directives",
                "creating libraries",
                "NuGet packages"
            ]
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
            "basics": [
                {
                    "variables": "Variables are used to store data. In C#, variables must be declared with a type (e.g., int, string) before they can be used."
                    },
                {"data types": "C# supports various data types, including int, float, double, char, string, and bool."
                 },
                {
                    "operators": "C# has several operators: arithmetic (+, -, *, /), comparison (==, !=, <, >), logical (&&, ||, !), and assignment (=)."
                    },
                {
                    "control structures": "Control structures include if statements, switch statements, and loops (for, while, do-while) for controlling the flow of execution."
                    },
                {
                    "input and output": "Input and output can be handled using Console.ReadLine() for input and Console.WriteLine() for output."
                    }
            ],

            "data structures": [
                {
                    "arrays": "Arrays are fixed-size collections of elements of the same type, defined with square brackets (e.g., int[] numbers = new int[5])."
                    },
                {
                    "lists (List<T>)": "Lists are dynamic collections that can grow and shrink, defined in System.Collections.Generic namespace (e.g., List<int> numbers = new List<int>())."
                    },
                {
                    "dictionaries (Dictionary<TKey, TValue>)": "Dictionaries are collections of key-value pairs, allowing for fast lookups by key (e.g., Dictionary<string, int> dict = new Dictionary<string, int>())."
                    },
                {
                    "hash sets (HashSet<T>)": "Hash sets are collections of unique elements (e.g., HashSet<int> set = new HashSet<int>())."},
                {
                    "queues (Queue<T>)": "Queues are first-in, first-out collections (e.g., Queue<int> queue = new Queue<int>())."},
                {
                    "stacks (Stack<T>)": "Stacks are last-in, first-out collections (e.g., Stack<int> stack = new Stack<int>())."
                    }],

            "functions and methods": [
                {
                    "defining methods": "Methods are blocks of code that perform a specific task. They are defined using the return type, name, and parameters (e.g., void MyMethod(int x))."},
                {
                    "method overloading": "Method overloading allows multiple methods with the same name but different parameters (e.g., void MyMethod(int x) and void MyMethod(string y))."},
                {
                    "params keyword": "The params keyword allows you to pass a variable number of arguments to a method (e.g., void MyMethod(params int[] numbers))."},
                {
                    "lambda expressions": "Lambda expressions are anonymous functions that can contain expressions and statements (e.g., (x, y) => x + y)."},
                {
                    "extension methods": "Extension methods allow you to add new methods to existing types without modifying them (e.g., public static class MyExtensions { public static int Square(this int number) { return number * number; }})."}
            ],

            "object-oriented programming": [
                {
                    "classes": "Classes are blueprints for creating objects. They encapsulate data and behavior (e.g., class MyClass { public int MyProperty { get; set; }})."},
                {
                    "objects": "Objects are instances of classes. They can have properties and methods (e.g., MyClass obj = new MyClass();)."},
                {
                    "inheritance": "Inheritance allows a class to inherit members (fields, methods) from another class (e.g., class DerivedClass : BaseClass {})."},
                {
                    "polymorphism": "Polymorphism allows objects of different classes to be treated as instances of a common base class, enabling method overriding."},
                {
                    "encapsulation": "Encapsulation restricts access to certain components of an object and protects the integrity of the data (e.g., private fields with public properties)."},
                {
                    "abstraction": "Abstraction hides the complex implementation details and exposes only the necessary parts of an object."},
                {
                    "interfaces": "Interfaces define contracts that implementing classes must follow (e.g., interface IMyInterface { void MyMethod(); })."},
                {
                    "abstract classes": "Abstract classes cannot be instantiated and can contain abstract methods that must be implemented by derived classes."}
            ],

            "exception handling": [
                {
                    "exceptions": "Exceptions are errors that occur during execution. They can be handled to prevent crashes."},
                {
                    "try-catch blocks": "Try-catch blocks allow you to catch and handle exceptions (e.g., try { /* code */ } catch (Exception ex) { /* handle error */ })."},
                {
                    "finally block": "The finally block executes code after try-catch, regardless of whether an exception was thrown."},
                {
                    "throwing exceptions": "You can throw exceptions manually using the throw keyword (e.g., throw new Exception('Error message'))."},
                {"custom exceptions": "Custom exceptions can be created by inheriting from the System.Exception class."
                 }],

            "file handling": [
                {
                    "file operations": "Basic file operations include creating, reading, writing, and deleting files (e.g., File.Create, File.ReadAllText)."},
                {
                    "reading and writing files": "Files can be read and written using FileStream, StreamReader, and StreamWriter."},
                {
                    "working with directories": "You can create, delete, and navigate directories using the Directory class (e.g., Directory.CreateDirectory, Directory.Delete)."},
                {"file streams": "File streams allow for reading and writing bytes to and from files."}
            ],

            "advanced concepts": [
                {
                    "delegates": "Delegates are type-safe function pointers that allow methods to be passed as parameters (e.g., delegate int MyDelegate(string s);)."},
                {
                    "events": "Events are a way for a class to provide notifications to clients when something happens (e.g., public event EventHandler MyEvent;)."},
                {
                    "LINQ": "Language Integrated Query (LINQ) allows querying collections in a concise and readable way (e.g., var result = myList.Where(x => x > 5);)."},
                {
                    "async and await": "Async and await keywords enable asynchronous programming, allowing non-blocking calls to be made (e.g., async Task MyAsyncMethod())."},
                {
                    "attributes": "Attributes provide metadata about code elements (e.g., [Obsolete] attribute marks methods as deprecated)."},
                {
                    "reflection": "Reflection allows inspection of types, methods, and properties at runtime (e.g., Type.GetType, MethodInfo.Invoke)."},
                {
                    "dependency injection": "Dependency injection is a design pattern that allows the decoupling of classes by providing their dependencies externally."}
            ],

            "testing": [
                {
                    "unit testing": "Unit testing involves testing individual components in isolation, typically using frameworks like MSTest or NUnit."},
                {
                    "integration testing": "Integration testing checks the interactions between different components to ensure they work together as expected."},
                {
                    "mocking": "Mocking is a technique used in testing to simulate the behavior of complex objects (e.g., using Moq library)."},
                {
                    "test-driven development": "Test-driven development (TDD) is a software development process where tests are written before the code."}
            ],

            "performance optimization": [{
                "memory management": "Memory management involves the efficient allocation and deallocation of memory to optimize performance."},
                {
                    "time complexity": "Time complexity measures how the runtime of an algorithm changes as the size of the input increases."},
                {
                    "space complexity": "Space complexity measures the amount of memory an algorithm uses as the input size grows."},
                {
                    "profiling": "Profiling involves analyzing a program's runtime behavior to identify bottlenecks and optimize performance."},
                {
                    "caching": "Caching stores frequently accessed data in memory to improve performance and reduce database calls."}
            ],

            "databases": [
                {"ADO.NET": "ADO.NET is a set of classes for interacting with databases in .NET applications."},
                {
                    "Entity Framework": "Entity Framework is an Object-Relational Mapper (ORM) that allows developers to work with databases using .NET objects."},
                {"LINQ to SQL": "LINQ to SQL is a component that allows querying databases using LINQ syntax."},
                {
                    "database transactions": "Database transactions ensure that a series of operations are executed as a single unit of work, maintaining data integrity."
                    }],

            "modules and packages": [
                {
                    "using directives": "Using directives allow you to use types from namespaces without needing to specify their fully qualified names (e.g., using System.Collections.Generic;)."},
                {
                    "creating libraries": "You can create reusable libraries in C# by compiling classes into a DLL (Dynamic Link Library)."},
                {
                    "NuGet packages": "NuGet is a package manager for .NET, allowing developers to share and consume libraries and tools."}
            ]
        }

        return knowledge_base
        pass
    def init_quiz_questions(self):

        return {
            "basics": [
                ("What keyword is used to declare a variable in C#?", "var"),
                ("What is the data type for a true or false value in C#?", "bool"),
                ("Which operator is used for string concatenation?", "+"),
                ("How do you read input from the console in C#?", "Console.ReadLine()"),
                ("What control structure is used for conditional execution?", "if")
            ],

            "data structures": [
                ("What type is used to store a fixed-size collection of elements of the same type?", "array"),
                ("Which collection allows dynamic resizing in C#?", "List<T>"),
                ("What collection type is used for key-value pairs?", "Dictionary<TKey, TValue>"),
                ("How do you ensure that all elements in a HashSet are unique?", "HashSet<T>"),
                ("Which data structure follows FIFO order?", "Queue<T>")
            ],

            "functions and methods": [
                ("How do you define a method in C#?", "returnType MethodName(parameters)"),
                ("What is it called when two methods have the same name but different parameters?",
                 "method overloading"),
                ("What keyword allows passing a variable number of arguments to a method?", "params"),
                ("What symbol is used for lambda expressions?", "=>"),
                ("What allows adding new methods to existing types without modifying them?", "extension methods")
            ],

            "object-oriented programming": [
                ("What is a blueprint for creating objects in C#?", "class"),
                ("What is an instance of a class called?", "object"),
                ("What allows a class to inherit members from another class?", "inheritance"),
                ("What keyword is used to create an interface?", "interface"),
                ("What hides the implementation details and shows only essential features?", "abstraction")
            ],

            "exception handling": [
                ("What is the base class for exceptions in C#?", "System.Exception"),
                ("What keyword is used to catch exceptions?", "catch"),
                ("What block executes regardless of whether an exception was thrown?", "finally"),
                ("How do you throw an exception manually?", "throw"),
                ("What is the technique of creating your own exception classes called?", "custom exceptions")
            ],

            "file handling": [
                ("Which class is used to perform file operations in C#?", "File"),
                ("How do you read all text from a file?", "File.ReadAllText()"),
                ("What method is used to create a new directory?", "Directory.CreateDirectory()"),
                ("How do you open a file for reading and writing?", "FileStream"),
                ("Which namespace is commonly used for file operations?", "System.IO")
            ],

            "advanced concepts": [
                ("What allows methods to be passed as parameters in C#?", "delegates"),
                ("What keyword is used to declare an event?", "event"),
                ("What feature allows querying collections in a readable way?", "LINQ"),
                ("What is the purpose of the async keyword?", "to enable asynchronous programming"),
                ("What allows you to inspect types and members at runtime?", "reflection")
            ],

            "testing": [
                ("What framework is commonly used for unit testing in C#?", "MSTest or NUnit"),
                ("What is the practice of writing tests before code called?", "test-driven development"),
                ("What technique simulates the behavior of complex objects in testing?", "mocking"),
                ("What type of testing checks the interaction between different components?", "integration testing"),
                ("Which attribute is used to mark a test method in MSTest?", "[TestMethod]")
            ],

            "performance optimization": [
                ("What is the process of analyzing runtime behavior called?", "profiling"),
                ("What keyword is used to manage memory allocation and deallocation?", "GC (Garbage Collection)"),
                ("What measures how an algorithm's runtime grows with input size?", "time complexity"),
                ("What measures the amount of memory used by an algorithm?", "space complexity"),
                ("What technique stores frequently accessed data to improve performance?", "caching")
            ],

            "databases": [
                ("What class is used for database operations in ADO.NET?", "SqlConnection"),
                ("What is the primary ORM framework for C#?", "Entity Framework"),
                ("What does LINQ to SQL allow you to do?", "query databases using LINQ"),
                ("What ensures that a series of database operations are executed as a single unit?", "transactions"),
                ("Which keyword is used to define a data model class in Entity Framework?", "DbSet<T>")
            ],

            "modules and packages": [
                ("What keyword allows you to include namespaces in your code?", "using"),
                ("How do you create a reusable library in C#?", "by compiling it into a DLL"),
                ("What is the name of the package manager for .NET?", "NuGet"),
                ("What type of projects can be shared as NuGet packages?", "libraries and tools"),
                ("What is the purpose of the Package Manager Console?", "to manage NuGet packages in Visual Studio")
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
        return "Hello! I'm your C# Tutorial Agent. How can I help you today? You can ask me about specific topics or type 'topics' to see what I can teach you."

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
        print("Welcome to the C# Tutorial!")
        return self.greet()
