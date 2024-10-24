import nltk
from nltk import WordNetLemmatizer, word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)


class CppTutorialAgent:

    def __init__(self):
        self.topics = {
    "Basics": [
        "variables",
        "data types",
        "operators",
        "control structures",
        "type casting",
        "input and output",
        "constants",
        "namespaces"
    ],

    "data structures": [
        "arrays",
        "pointers",
        "references",
        "structs",
        "enums",
        "classes",
        "STL containers (vectors, lists, maps, sets)",
        "iterators"
    ],

    "functions": [
        "defining functions",
        "arguments",
        "return values",
        "inline functions",
        "default arguments",
        "function overloading",
        "function templates",
        "recursion",
        "lambda expressions",
        "function scope (local, global variables)",
        "passing by reference vs value"
    ],

    "object-oriented programming": [
        "classes",
        "objects",
        "constructors",
        "destructors",
        "inheritance",
        "polymorphism",
        "encapsulation",
        "abstraction",
        "virtual functions",
        "pure virtual functions",
        "friend functions",
        "operator overloading"
    ],

    "file handling": [
        "file streams (ifstream, ofstream, fstream)",
        "reading and writing files",
        "binary file handling",
        "file error handling",
        "working with CSV",
        "random access in files"
    ],

    "advanced concepts": [
        "pointers and dynamic memory",
        "smart pointers",
        "move semantics",
        "rvalue references",
        "STL algorithms",
        "iterators",
        "multithreading",
        "concurrency with threads",
        "mutexes and condition variables",
        "atomic operations",
        "templates",
        "metaprogramming",
        "asynchronous programming"
    ],

    "error handling": [
        "exceptions",
        "try-catch blocks",
        "throwing exceptions",
        "custom exceptions",
        "standard exception classes (std::exception)",
        "assertions",
        "error codes"
    ],

    "functional programming": [
        "function pointers",
        "lambda functions",
        "std::function",
        "higher-order functions",
        "map, filter, reduce (functional-style operations in C++)",
        "closures",
        "partial functions"
    ],

    "modules and packages": [
        "header files",
        "source files",
        "linking and compiling",
        "C++ Standard Library",
        "third-party libraries",
        "cmake",
        "modular programming (C++20 modules)"
    ],

    "testing": [
        "unit testing",
        "assertions",
        "Google Test",
        "mocking",
        "test-driven development",
        "benchmarking"
    ],

    "databases": [
        "connecting to databases (ODBC, SQL)",
        "SQLite",
        "MySQL",
        "PostgreSQL",
        "ORM libraries for C++",
        "database connection management"
    ],

    "performance optimization": [
        "profiling code",
        "algorithm optimization",
        "memory management",
        "time complexity",
        "space complexity",
        "multithreading vs multiprocessing",
        "move semantics",
        "efficient loops",
        "inline functions",
        "copy elision",
        "compiling with optimization flags",
        "memory alignment",
        "cache optimization",
        "using concurrent containers",
        "lock-free data structures"
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
        self.progress = {topic: {subtopic: False for subtopic in subtopics}
                         for topic, subtopics in self.topics.items()}
        self.quiz_questions = self.init_quiz_questions()
        self.showing_menu = False
    def init_knowledge_base(self):
        knowledge_base = {
            "Basics": [
                {
                    "variables": "Variables store data values, and in C++, you need to explicitly declare their types (e.g., int, float, char).\n\nExample:\nint x = 10; \nfloat y = 5.5;"
                },
                {
                    "data types": "C++ has several built-in data types, including int, float, char, bool, and void.\n\nExample:\nint age = 21; \nchar grade = 'A';"
                },
                {
                    "operators": "C++ supports arithmetic (+, -, *, /), comparison (==, !=, <, >), logical (&&, ||, !), bitwise (&, |, ^), and other operators.\n\nExample:\nint result = a + b;"
                },
                {
                    "control structures": "C++ control structures include if-else statements, for/while loops, and switch-case statements for decision making.\n\nExample:\nif (x > 10) { \n  cout << 'Greater'; \n}"
                },
                {
                    "type casting": "Type casting allows conversion between different data types, such as from float to int.\n\nExample:\nint a = static_cast<int>(3.14);"
                },
                {
                    "input and output": "C++ uses cin for input and cout for output.\n\nExample:\nint x;\ncin >> x;\ncout << x;"
                }
            ],

            "data structures": [
                {
                    "lists": "C++ doesn't have built-in lists, but you can use vectors from the STL (Standard Template Library) which are dynamic arrays.\n\nExample:\n#include <vector>\nstd::vector<int> myVector = {1, 2, 3};"
                },
                {
                    "tuples": "C++ tuples allow grouping different types of data into one object.\n\nExample:\n#include <tuple>\nauto myTuple = std::make_tuple(1, 'A', 3.14);"
                },
                {
                    "dictionaries (maps)": "In C++, dictionaries are implemented using maps from the STL, where keys are associated with values.\n\nExample:\n#include <map>\nstd::map<std::string, int> ageMap;"
                },
                {
                    "sets": "Sets in C++ are collections of unique elements, and they can be implemented using the STL set.\n\nExample:\n#include <set>\nstd::set<int> mySet = {1, 2, 3};"
                },
                {
                    "list comprehensions (not available)": "C++ does not have list comprehensions like Python, but you can achieve similar results using loops or the STL algorithms."
                },
                {
                    "dictionary comprehensions (not available)": "Similar to list comprehensions, C++ does not support dictionary comprehensions, but you can use map operations and loops to achieve similar functionality."
                }
            ],

            "functions": [
                {
                    "defining functions": "Functions in C++ are declared with a return type, a name, and parameters. Functions must be defined before use.\n\nExample:\nint sum(int a, int b) { return a + b; }"
                },
                {
                    "arguments": "C++ functions can accept arguments, which are passed by value or by reference.\n\nExample:\nvoid add(int a, int& b) { b = a + b; }"
                },
                {
                    "return values": "Functions return a value of the declared type. If no value is returned, the function is declared with the void type.\n\nExample:\nreturn x * 2;"
                },
                {
                    "lambda functions": "C++ supports anonymous functions or lambda expressions, useful for short functions passed as arguments.\n\nExample:\nauto sum = [](int a, int b) { return a + b; };"
                },
                {
                    "function scope": "C++ variables declared inside functions have local scope, and those outside functions have global scope."
                }
            ],

            "object-oriented programming": [
                {
                    "classes": "A class in C++ is a blueprint for creating objects, bundling data (attributes) and methods (functions).\n\nExample:\nclass Car { public: int speed; void drive(); };"
                },
                {
                    "objects": "Objects are instances of classes in C++.\n\nExample:\nCar myCar;\nmyCar.drive();"
                },
                {
                    "inheritance": "C++ supports inheritance, where a class can inherit attributes and methods from another class.\n\nExample:\nclass SportsCar : public Car {};"
                },
                {
                    "polymorphism": "Polymorphism in C++ allows objects of different classes to be treated as objects of a common base class.\n\nExample:\nvirtual void drive();"
                },
                {
                    "encapsulation": "Encapsulation is the bundling of data with methods that operate on the data, restricting access through public, private, and protected keywords."
                },
                {
                    "abstraction": "Abstraction is the concept of hiding complex implementation details and showing only the necessary features.\n\nExample:\nclass Shape { virtual void draw() = 0; };"
                },
                {
                    "magic methods": "In C++, magic methods (or special member functions) include constructors, destructors, and operator overloading.\n\nExample:\n~Car() // Destructor"
                }
            ],

            "file handling": [
                {
                    "file operations": "C++ allows file I/O through streams like ifstream and ofstream.\n\nExample:\n#include <fstream>\nstd::ofstream file('example.txt');\nfile << 'Hello!';"
                },
                {
                    "reading and writing files": "Use ifstream to read from files and ofstream to write to files."
                },
                {
                    "working with CSV": "To work with CSV files in C++, you can read line by line using getline()."
                },
                {
                    "JSON handling": "JSON handling is not built-in in C++ but can be done using libraries like nlohmann/json.\n\nExample:\n#include <nlohmann/json.hpp>\njson j = { { 'name', 'John' }, { 'age', 30 } };"
                },
                {
                    "context managers (not available)": "C++ does not have context managers like Python, but RAII (Resource Acquisition Is Initialization) patterns can be used to manage resources."
                },
                {
                    "binary file handling": "Use ios::binary mode when working with binary files in C++.\n\nExample:\nstd::ofstream file('data.bin', std::ios::binary);"
                }
            ],

            "advanced concepts": [
                {
                    "pointers and dynamic memory": "Raw pointers allow direct memory manipulation and dynamic memory allocation in C++. Use new/delete for allocation/deallocation.\n\nExample:\nint* ptr = new int(42);\n// Use the pointer\ndelete ptr; // Free the memory\n\n// Dynamic array\nint* arr = new int[5];\n// Use the array\ndelete[] arr; // Free array memory"
                },
                {
                    "smart pointers": "Modern C++ provides smart pointers (unique_ptr, shared_ptr, weak_ptr) for automatic memory management and avoiding memory leaks.\n\nExample:\n#include <memory>\n\nstd::unique_ptr<int> uptr = std::make_unique<int>(42);\n// No need to delete - automatically managed\n\nstd::shared_ptr<int> sptr = std::make_shared<int>(100);\nstd::shared_ptr<int> sptr2 = sptr; // Reference count = 2"
                },
                {
                    "move semantics": "Move semantics allows the transfer of resources from one object to another without copying, improving performance.\n\nExample:\nstd::vector<int> source{1, 2, 3};\nstd::vector<int> dest = std::move(source); // Moves data instead of copying\n// source is now in valid but unspecified state"
                },
                {
                    "rvalue references": "Rvalue references (&&) enable move semantics and perfect forwarding, distinguishing between lvalue and rvalue expressions.\n\nExample:\nvoid process(int&& x) { // Takes only rvalue\n    // Process x\n}\nint temp = 42;\nprocess(std::move(temp)); // Convert lvalue to rvalue"
                },
                {
                    "STL algorithms": "The Standard Template Library provides powerful algorithms for container manipulation, searching, sorting, and transforming data.\n\nExample:\n#include <algorithm>\nstd::vector<int> vec{3, 1, 4, 1, 5};\nstd::sort(vec.begin(), vec.end());\nstd::transform(vec.begin(), vec.end(), vec.begin(),\n    [](int x) { return x * 2; }); // Double each element"
                },
                {
                    "iterators": "Iterators provide a uniform way to access elements in containers, supporting different traversal patterns.\n\nExample:\nstd::vector<int> vec{1, 2, 3, 4, 5};\nfor (auto it = vec.begin(); it != vec.end(); ++it) {\n    std::cout << *it << ' ';\n}\n\n// Reverse iterator\nfor (auto rit = vec.rbegin(); rit != vec.rend(); ++rit) {\n    std::cout << *rit << ' ';\n}"
                },
                {
                    "multithreading": "C++11 introduced built-in support for multithreading, allowing concurrent execution of code.\n\nExample:\n#include <thread>\n\nvoid worker(int id) {\n    std::cout << \"Thread \" << id << \" working\\n\";\n}\n\nstd::thread t1(worker, 1);\nstd::thread t2(worker, 2);\nt1.join();\nt2.join();"
                },
                {
                    "concurrency with threads": "Thread management and synchronization mechanisms for handling concurrent operations.\n\nExample:\nstd::vector<std::thread> threads;\nfor(int i = 0; i < 5; ++i) {\n    threads.emplace_back([i]() {\n        std::cout << \"Thread \" << i << \" executing\\n\";\n    });\n}\nfor(auto& t : threads) t.join();"
                },
                {
                    "mutexes and condition variables": "Synchronization primitives for thread safety and coordination.\n\nExample:\nstd::mutex mtx;\nstd::condition_variable cv;\nbool ready = false;\n\nvoid worker() {\n    std::unique_lock<std::mutex> lock(mtx);\n    cv.wait(lock, [] { return ready; });\n    // Do work\n}\n\n// In another thread\n{\n    std::lock_guard<std::mutex> lock(mtx);\n    ready = true;\n    cv.notify_one();\n}"
                },
                {
                    "atomic operations": "Thread-safe operations on single variables without explicit locking.\n\nExample:\n#include <atomic>\nstd::atomic<int> counter{0};\n\nvoid increment() {\n    ++counter; // Atomic increment\n    counter.fetch_add(1); // Alternative syntax\n}\n\nbool compare_exchange() {\n    int expected = 2;\n    return counter.compare_exchange_strong(expected, 3);\n}"
                },
                {
                    "templates": "Generic programming constructs for creating type-independent code.\n\nExample:\n// Function template\ntemplate<typename T>\nT max(T a, T b) {\n    return (a > b) ? a : b;\n}\n\n// Class template\ntemplate<typename T>\nclass Container {\n    T data;\npublic:\n    Container(T d) : data(d) {}\n    T getValue() { return data; }\n};"
                },
                {
                    "metaprogramming": "Template metaprogramming allows computation at compile-time rather than runtime.\n\nExample:\ntemplate<unsigned N>\nstruct Factorial {\n    static constexpr unsigned value = N * Factorial<N-1>::value;\n};\n\ntemplate<>\nstruct Factorial<0> {\n    static constexpr unsigned value = 1;\n};\n\nconstexpr unsigned fact5 = Factorial<5>::value; // Computed at compile-time"
                },
                {
                    "asynchronous programming": "Mechanisms for handling asynchronous operations using futures and promises.\n\nExample:\n#include <future>\n\nstd::future<int> fut = std::async(std::launch::async, []() {\n    // Simulating long computation\n    std::this_thread::sleep_for(std::chrono::seconds(2));\n    return 42;\n});\n\n// Do other work while computation is running\nint result = fut.get(); // Wait for result"
                }
            ],

            "error_handling": [
                {
                    "exceptions": {
                        "description": "Core mechanism for handling runtime errors in C++",
                        "example": "// Basic exception handling\nvoid processData(const std::vector<int>& data) {\n    try {\n        if(data.empty()) {\n            throw std::runtime_error(\"Empty data set\");\n        }\n        \n        // Process data\n        for(int value : data) {\n            if(value < 0) {\n                throw std::invalid_argument(\n                    \"Negative values not allowed\");\n            }\n        }\n    } catch(const std::exception& e) {\n        std::cerr << \"Error: \" << e.what() << std::endl;\n        throw; // Re-throw the exception\n    }\n}\n\n// Function try block\nclass Resource {\npublic:\n    Resource() try : data(new int[1000000]) {\n        // Constructor code\n    } catch(const std::bad_alloc& e) {\n        std::cerr << \"Memory allocation failed: \" \n                  << e.what() << std::endl;\n        throw;\n    }\n\nprivate:\n    int* data;\n};"
                    }
                },
                {
                    "try-catch blocks": {
                        "description": "Syntax for handling exceptions and implementing error recovery",
                        "example": "// Multiple catch blocks\nvoid complexOperation() {\n    try {\n        // Risky operation\n        throw std::runtime_error(\"Something went wrong\");\n        \n    } catch(const std::invalid_argument& e) {\n        // Handle invalid arguments\n        std::cerr << \"Invalid argument: \" << e.what() << std::endl;\n        \n    } catch(const std::runtime_error& e) {\n        // Handle runtime errors\n        std::cerr << \"Runtime error: \" << e.what() << std::endl;\n        \n    } catch(...) {\n        // Handle all other exceptions\n        std::cerr << \"Unknown error occurred\" << std::endl;\n        throw; // Re-throw unknown exceptions\n    }\n}\n\n// Nested try-catch blocks\nvoid nestedErrorHandling() {\n    try {\n        try {\n            throw std::runtime_error(\"Inner error\");\n        } catch(const std::exception& e) {\n            std::cerr << \"Inner catch: \" << e.what() << std::endl;\n            throw std::runtime_error(\"Outer error\");\n        }\n    } catch(const std::exception& e) {\n        std::cerr << \"Outer catch: \" << e.what() << std::endl;\n    }\n}"
                    }
                },
                {
                    "throwing exceptions": {
                        "description": "Various ways to throw and propagate exceptions",
                        "example": "// Basic throw statements\nvoid validateAge(int age) {\n    if(age < 0) {\n        throw std::invalid_argument(\"Age cannot be negative\");\n    }\n    if(age > 150) {\n        throw std::out_of_range(\"Age value too high\");\n    }\n}\n\n// Throwing in constructors\nclass Person {\npublic:\n    Person(int age) {\n        if(age < 0) {\n            throw std::invalid_argument(\"Age cannot be negative\");\n        }\n        age_ = age;\n    }\nprivate:\n    int age_;\n};\n\n// Re-throwing exceptions\nvoid processUserData() {\n    try {\n        Person person(-5);\n    } catch(const std::exception& e) {\n        // Log error\n        std::cerr << \"Error creating person: \" << e.what() << std::endl;\n        throw; // Re-throw the same exception\n    }\n}"
                    }
                },
                {
                    "custom exceptions": {
                        "description": "Creating custom exception classes for specific error scenarios",
                        "example": "// Basic custom exception\nclass DatabaseError : public std::runtime_error {\npublic:\n    explicit DatabaseError(const std::string& message)\n        : std::runtime_error(message) {}\n};\n\n// Advanced custom exception with additional information\nclass NetworkError : public std::exception {\npublic:\n    NetworkError(const std::string& message, int errorCode)\n        : message_(message), errorCode_(errorCode) {}\n    \n    const char* what() const noexcept override {\n        return message_.c_str();\n    }\n    \n    int getErrorCode() const noexcept {\n        return errorCode_;\n    }\n\nprivate:\n    std::string message_;\n    int errorCode_;\n};\n\n// Using custom exceptions\nvoid connectToDatabase() {\n    try {\n        throw DatabaseError(\"Failed to connect to database\");\n    } catch(const DatabaseError& e) {\n        std::cerr << \"Database error: \" << e.what() << std::endl;\n    }\n    \n    try {\n        throw NetworkError(\"Connection timeout\", 408);\n    } catch(const NetworkError& e) {\n        std::cerr << \"Network error (\" << e.getErrorCode() \n                  << \"): \" << e.what() << std::endl;\n    }\n}"
                    }
                },
                {
                    "standard exception classes": {
                        "description": "Built-in exception classes provided by the C++ Standard Library",
                        "example": "// Common standard exceptions\n#include <stdexcept>\n#include <new>\n#include <typeinfo>\n\nvoid demonstrateStandardExceptions() {\n    // logic_error and its derived classes\n    try {\n        throw std::invalid_argument(\"Invalid input\");\n    } catch(const std::logic_error& e) {}\n    \n    try {\n        throw std::out_of_range(\"Index out of bounds\");\n    } catch(const std::logic_error& e) {}\n    \n    // runtime_error and its derived classes\n    try {\n        throw std::overflow_error(\"Arithmetic overflow\");\n    } catch(const std::runtime_error& e) {}\n    \n    try {\n        throw std::underflow_error(\"Arithmetic underflow\");\n    } catch(const std::runtime_error& e) {}\n    \n    // Other standard exceptions\n    try {\n        throw std::bad_alloc(); // Memory allocation failure\n    } catch(const std::bad_alloc& e) {}\n    \n    try {\n        throw std::bad_cast(); // Failed dynamic cast\n    } catch(const std::bad_cast& e) {}\n}"
                    }
                },
                {
                    "assertions": {
                        "description": "Debug-time validation of assumptions and invariants",
                        "example": "// Using assert\n#include <cassert>\n\nvoid processArray(int* arr, size_t size) {\n    // Verify preconditions\n    assert(arr != nullptr && \"Array pointer cannot be null\");\n    assert(size > 0 && \"Array size must be positive\");\n    \n    // Process array...\n}\n\n// Static assertions (compile-time)\nstatic_assert(sizeof(int) >= 4, \n              \"Int must be at least 4 bytes\");\n\n// Custom assertions\n#define ASSERT_MSG(cond, msg) \\\n    do { \\\n        if (!(cond)) { \\\n            std::cerr << \"Assertion failed: \" << msg << std::endl; \\\n            std::abort(); \\\n        } \\\n    } while(0)\n\nvoid validateData(const std::vector<int>& data) {\n    ASSERT_MSG(!data.empty(), \"Data vector cannot be empty\");\n}"
                    }
                },
                {
                    "error codes": {
                        "description": "Traditional error handling using return values and error codes",
                        "example": "// Error code enumeration\nenum class ErrorCode {\n    Success = 0,\n    InvalidInput = 1,\n    FileNotFound = 2,\n    NetworkError = 3,\n    DatabaseError = 4\n};\n\n// Function returning error code\nErrorCode processFile(const std::string& filename) {\n    if(filename.empty()) {\n        return ErrorCode::InvalidInput;\n    }\n    \n    // Process file...\n    return ErrorCode::Success;\n}\n\n// Using std::error_code\n#include <system_error>\n\nclass FileSystem {\npublic:\n    std::error_code readFile(const std::string& path, \n                            std::string& content) {\n        if(path.empty()) {\n            return std::make_error_code(\n                std::errc::invalid_argument);\n        }\n        \n        // Read file...\n        return std::error_code();\n    }\n};\n\n// Combining error codes with output parameters\nstruct Result {\n    ErrorCode error;\n    std::string message;\n};\n\nResult validateUser(const std::string& username) {\n    if(username.empty()) {\n        return {ErrorCode::InvalidInput, \n                \"Username cannot be empty\"};\n    }\n    return {ErrorCode::Success, \"\"};\n}"
                    }
                }
            ],

            "functional_programming": [
                {
                    "function pointers": {
                        "description": "Pointers that store addresses of functions, enabling runtime function selection and callback mechanisms.",
                        "example": "// Function pointer basics\ntypedef int (*Operation)(int, int);\n\nint add(int a, int b) { return a + b; }\nint multiply(int a, int b) { return a * b; }\n\n// Usage example\nOperation op = add;\nint result = op(5, 3);  // calls add(5, 3)\n\n// Array of function pointers\nOperation operations[] = {add, multiply};\nint result2 = operations[1](4, 2);  // calls multiply(4, 2)\n\n// As class member\nclass Calculator {\n    Operation operation;\npublic:\n    Calculator(Operation op) : operation(op) {}\n    int calculate(int a, int b) { return operation(a, b); }\n};"
                    }
                },
                {
                    "lambda functions": {
                        "description": "Anonymous function objects that can capture variables from their enclosing scope.",
                        "example": "// Basic lambda\nauto greet = []() { std::cout << \"Hello World!\\n\"; };\n\n// Lambda with parameters\nauto add = [](int a, int b) { return a + b; };\n\n// Lambda with capture\nint multiplier = 10;\nauto multiply = [multiplier](int x) { return x * multiplier; };\n\n// Mutable lambda\nauto counter = [count = 0]() mutable { return ++count; };\n\n// Generic lambda (C++14)\nauto genericAdd = [](auto a, auto b) { return a + b; };\n\n// Capturing by reference\nint value = 42;\nauto modifyValue = [&value]() { value *= 2; };\n\n// With algorithms\nstd::vector<int> nums = {1, 2, 3, 4, 5};\nstd::transform(nums.begin(), nums.end(), nums.begin(),\n               [](int n) { return n * n; });"
                    }
                },
                {
                    "std::function": {
                        "description": "A general-purpose polymorphic function wrapper that can store, copy, and invoke any callable target.",
                        "example": "// Basic std::function\nstd::function<int(int, int)> operation;\n\n// Storing regular function\nint add(int a, int b) { return a + b; }\noperation = add;\n\n// Storing lambda\noperation = [](int a, int b) { return a + b; };\n\n// Member function with bind\nclass Calculator {\npublic:\n    int add(int a, int b) { return a + b; }\n};\n\nCalculator calc;\nstd::function<int(int, int)> memberFunc = \n    std::bind(&Calculator::add, calc, std::placeholders::_1, std::placeholders::_2);\n\n// Function object storage\nclass Multiplier {\npublic:\n    int operator()(int a, int b) { return a * b; }\n};\n\noperation = Multiplier();"
                    }
                },
                {
                    "higher-order functions": {
                        "description": "Functions that take other functions as parameters or return functions as results.",
                        "example": "// Function that takes function as parameter\ntemplate<typename F>\nvoid applyToRange(std::vector<int>& vec, F func) {\n    for(auto& item : vec) {\n        item = func(item);\n    }\n}\n\n// Function that returns function\nauto makeMultiplier(int factor) {\n    return [factor](int x) { return x * factor; };\n}\n\n// Function composition\ntemplate<typename F, typename G>\nauto compose(F f, G g) {\n    return [=](auto x) { return f(g(x)); };\n}\n\n// Usage examples\nstd::vector<int> numbers = {1, 2, 3, 4, 5};\nauto double_numbers = makeMultiplier(2);\napplyToRange(numbers, double_numbers);\n\nauto square = [](int x) { return x * x; };\nauto addOne = [](int x) { return x + 1; };\nauto squarePlusOne = compose(addOne, square);"
                    }
                },
                {
                    "map, filter, reduce": {
                        "description": "Functional-style operations for transforming and processing collections.",
                        "example": "// Map (transform)\nstd::vector<int> numbers = {1, 2, 3, 4, 5};\nstd::vector<int> squared;\nstd::transform(numbers.begin(), numbers.end(),\n               std::back_inserter(squared),\n               [](int x) { return x * x; });\n\n// Filter (copy_if)\nstd::vector<int> evens;\nstd::copy_if(numbers.begin(), numbers.end(),\n             std::back_inserter(evens),\n             [](int x) { return x % 2 == 0; });\n\n// Reduce (accumulate)\nint sum = std::accumulate(numbers.begin(), numbers.end(), 0);\n\n// Combining operations\nauto result = std::accumulate(numbers.begin(), numbers.end(), 0,\n    [](int acc, int val) {\n        if(val % 2 == 0) {  // Filter\n            return acc + val * val;  // Map and Reduce\n        }\n        return acc;\n    });"
                    }
                },
                {
                    "closures": {
                        "description": "Lambda functions that capture and store variables from their enclosing scope.",
                        "example": "// Basic closure\nint multiplier = 10;\nauto multiply = [multiplier](int x) { return x * multiplier; };\n\n// Closure with mutable state\nauto makeCounter() {\n    int count = 0;\n    return [count]() mutable { return ++count; };\n}\n\n// Closure capturing multiple variables\nint base = 10;\nint factor = 2;\nauto compute = [base, factor](int x) {\n    return base + x * factor;\n};\n\n// Closure with reference capture\nclass DataProcessor {\n    std::vector<int> data;\npublic:\n    auto getProcessor() {\n        return [this](int value) {\n            data.push_back(value);\n            return std::accumulate(data.begin(), data.end(), 0);\n        };\n    }\n};"
                    }
                },
                {
                    "partial functions": {
                        "description": "Creating new functions by fixing some arguments of existing functions.",
                        "example": "// Using std::bind\nint divide(int a, int b) { return a / b; }\nauto divideBy2 = std::bind(divide, std::placeholders::_1, 2);\n\n// Using lambda for partial application\nauto multiply(int a, int b, int c) { return a * b * c; }\nauto multiplyBy5 = [](int b, int c) { return multiply(5, b, c); };\n\n// Currying with lambdas\nauto curryAdd = [](int a) {\n    return [a](int b) {\n        return [a, b](int c) {\n            return a + b + c;\n        };\n    };\n};\n\n// Partial application with member functions\nclass Calculator {\npublic:\n    int add(int a, int b, int c) { return a + b + c; }\n};\n\nCalculator calc;\nauto addPartial = std::bind(&Calculator::add, calc,\n                            std::placeholders::_1,\n                            std::placeholders::_2,\n                            10);"
                    }
                }
            ],

            "modules_and_packages": [
                {
                    "header files": {
                        "description": "Interface declarations and inline definitions",
                        "examples": {
                            "basic_header": "// math_utils.h\n#ifndef MATH_UTILS_H\n#define MATH_UTILS_H\n\nnamespace math {\n    // Function declarations\n    double add(double a, double b);\n    double subtract(double a, double b);\n    \n    // Inline function definition\n    inline double multiply(double a, double b) {\n        return a * b;\n    }\n    \n    // Class declaration\n    class Calculator {\n    public:\n        Calculator();\n        double calculate(double a, double b);\n    private:\n        double result_;\n    };\n}\n\n#endif // MATH_UTILS_H",
                            "template_header": "// template_utils.h\n#ifndef TEMPLATE_UTILS_H\n#define TEMPLATE_UTILS_H\n\nnamespace utils {\n    template<typename T>\n    class SmartContainer {\n    public:\n        SmartContainer(T value) : data_(value) {}\n        \n        T getValue() const { return data_; }\n        void setValue(T value) { data_ = value; }\n        \n    private:\n        T data_;\n    };\n    \n    // Function template\n    template<typename T>\n    T max(T a, T b) {\n        return (a > b) ? a : b;\n    }\n}\n\n#endif // TEMPLATE_UTILS_H"
                        },
                        "best_practices": [
                            "Use header guards or #pragma once",
                            "Minimize includes in headers",
                            "Use forward declarations when possible",
                            "Keep implementation details private",
                            "Use inline for small, frequently called functions"
                        ]
                    }
                },
                {
                    "source files": {
                        "description": "Implementation files containing function and class definitions",
                        "examples": {
                            "implementation": "// math_utils.cpp\n#include \"math_utils.h\"\n\nnamespace math {\n    double add(double a, double b) {\n        return a + b;\n    }\n    \n    double subtract(double a, double b) {\n        return a - b;\n    }\n    \n    Calculator::Calculator() : result_(0) {}\n    \n    double Calculator::calculate(double a, double b) {\n        result_ = add(a, b);\n        return result_;\n    }\n}",
                            "class_implementation": "// complex_class.cpp\n#include \"complex_class.h\"\n#include <stdexcept>\n\nComplex::Complex(double real, double imag)\n    : real_(real), imag_(imag) {}\n\nComplex Complex::operator+(const Complex& other) const {\n    return Complex(real_ + other.real_,\n                  imag_ + other.imag_);\n}\n\ndouble Complex::magnitude() const {\n    return std::sqrt(real_ * real_ + imag_ * imag_);\n}"
                        },
                        "best_practices": [
                            "One class implementation per file",
                            "Include necessary headers only",
                            "Use anonymous namespaces for file-local functions",
                            "Keep source files focused and cohesive",
                            "Implement error handling"
                        ]
                    }
                },
                {
                    "linking and compiling": {
                        "description": "Process of compiling source files and linking them together",
                        "examples": {
                            "manual_compilation": "# Compile individual source files\ng++ -c -std=c++17 math_utils.cpp -o math_utils.o\ng++ -c -std=c++17 main.cpp -o main.o\n\n# Link object files\ng++ math_utils.o main.o -o program",
                            "makefile": "CXX = g++\nCXXFLAGS = -std=c++17 -Wall -Wextra\n\nSRCS = main.cpp math_utils.cpp\nOBJS = $(SRCS:.cpp=.o)\nTARGET = program\n\n$(TARGET): $(OBJS)\n\t$(CXX) $(OBJS) -o $(TARGET)\n\n%.o: %.cpp\n\t$(CXX) $(CXXFLAGS) -c $< -o $@\n\nclean:\n\trm -f $(OBJS) $(TARGET)"
                        },
                        "concepts": [
                            "Object files (.o)",
                            "Static libraries (.a)",
                            "Dynamic libraries (.so/.dll)",
                            "Link-time optimization",
                            "Symbol resolution"
                        ]
                    }
                },
                {
                    "C++ Standard Library": {
                        "description": "Built-in libraries provided by C++",
                        "common_libraries": {
                            "containers": [
                                "<vector>",
                                "<list>",
                                "<map>",
                                "<unordered_map>",
                                "<set>",
                                "<queue>",
                                "<stack>"
                            ],
                            "algorithms": [
                                "<algorithm>",
                                "<numeric>"
                            ],
                            "utilities": [
                                "<string>",
                                "<memory>",
                                "<utility>",
                                "<functional>"
                            ],
                            "io": [
                                "<iostream>",
                                "<fstream>",
                                "<sstream>"
                            ],
                            "threading": [
                                "<thread>",
                                "<mutex>",
                                "<future>"
                            ]
                        },
                        "usage_example": "// Using standard library components\n#include <vector>\n#include <algorithm>\n#include <string>\n\nstd::vector<std::string> names{\"Alice\", \"Bob\", \"Charlie\"};\nstd::sort(names.begin(), names.end());\n\nstd::vector<int> numbers{3, 1, 4, 1, 5};\nauto sum = std::accumulate(numbers.begin(), numbers.end(), 0);"
                    }
                },
                {
                    "third-party libraries": {
                        "description": "External libraries integration and usage",
                        "common_libraries": {
                            "Boost": {
                                "description": "Comprehensive C++ library collection",
                                "example": "// Using Boost.Filesystem\n#include <boost/filesystem.hpp>\nnamespace fs = boost::filesystem;\n\nfs::path p(\"file.txt\");\nif(fs::exists(p)) {\n    std::cout << \"Size: \" << fs::file_size(p) << std::endl;\n}"
                            },
                            "OpenCV": {
                                "description": "Computer vision library",
                                "example": "// Using OpenCV\n#include <opencv2/opencv.hpp>\n\ncv::Mat image = cv::imread(\"image.jpg\");\ncv::GaussianBlur(image, image, cv::Size(5, 5), 1.5);"
                            }
                        },
                        "integration": {
                            "find_package": "# CMake integration\nfind_package(Boost REQUIRED COMPONENTS filesystem)\ntarget_link_libraries(${PROJECT_NAME} Boost::filesystem)",
                            "pkg_config": "# pkg-config usage\n pkg-config --cflags --libs opencv4"
                        }
                    }
                },
                {
                    "cmake": {
                        "description": "Build system generator for C++ projects",
                        "examples": {
                            "basic_cmake": "# Basic CMakeLists.txt\ncmake_minimum_required(VERSION 3.15)\nproject(MyProject)\n\nset(CMAKE_CXX_STANDARD 17)\nset(CMAKE_CXX_STANDARD_REQUIRED ON)\n\nadd_executable(${PROJECT_NAME}\n    src/main.cpp\n    src/math_utils.cpp\n)\n\ntarget_include_directories(${PROJECT_NAME}\n    PRIVATE\n        ${PROJECT_SOURCE_DIR}/include\n)",
                            "library_cmake": "# Library CMakeLists.txt\nadd_library(math_lib\n    src/math_utils.cpp\n    src/complex.cpp\n)\n\ntarget_include_directories(math_lib\n    PUBLIC\n        ${PROJECT_SOURCE_DIR}/include\n)\n\n# Create and link executable\nadd_executable(main src/main.cpp)\ntarget_link_libraries(main PRIVATE math_lib)"
                        },
                        "best_practices": [
                            "Use modern CMake practices",
                            "Specify target properties explicitly",
                            "Use proper visibility specifiers",
                            "Handle dependencies properly",
                            "Set compile features instead of flags"
                        ]
                    }
                },
                {
                    "modular programming": {
                        "description": "C++20 modules feature for better code organization",
                        "examples": {
                            "module_interface": "// math.ixx\nexport module math;\n\nexport namespace math {\n    double add(double a, double b);\n    double subtract(double a, double b);\n    \n    class Calculator {\n    public:\n        Calculator();\n        double calculate(double a, double b);\n    private:\n        double result_;\n    };\n}",
                            "module_implementation": "// math.cpp\nmodule math;\n\nnamespace math {\n    double add(double a, double b) {\n        return a + b;\n    }\n    \n    double subtract(double a, double b) {\n        return a - b;\n    }\n    \n    Calculator::Calculator() : result_(0) {}\n    \n    double Calculator::calculate(double a, double b) {\n        result_ = add(a, b);\n        return result_;\n    }\n}",
                            "module_usage": "// main.cpp\nimport math;\n\nint main() {\n    math::Calculator calc;\n    double result = calc.calculate(3.14, 2.71);\n    return 0;\n}"
                        },
                        "advantages": [
                            "Faster compilation",
                            "No header guards needed",
                            "Better encapsulation",
                            "Explicit exports",
                            "No macro problems"
                        ]
                    }
                }
            ],

            "testing": [
                {
                    "unit testing": {
                        "core_concepts": [
                            "Test fixtures - Setup and teardown of test environments",
                            "Test suites - Grouping related tests together",
                            "Test cases - Individual test functions",
                            "Assertions - Verifying expected behavior",
                            "Test runners - Executing and reporting test results",
                            "Code coverage - Measuring test coverage"
                        ],
                        "common_patterns": [
                            "Arrange-Act-Assert pattern",
                            "Given-When-Then structure",
                            "Setup and teardown methods",
                            "Parameterized tests",
                            "Exception testing"
                        ]
                    }
                },
                {
                    "assertions": {
                        "types": [
                            "Basic assertions (equality, inequality)",
                            "Boolean assertions (true/false)",
                            "Floating-point comparisons",
                            "Exception assertions",
                            "String comparisons",
                            "Custom assertions"
                        ],
                        "frameworks": [
                            "assert() macro",
                            "static_assert",
                            "Google Test assertions",
                            "Boost.Test assertions",
                            "Catch2 assertions"
                        ]
                    }
                },
                {
                    "Google Test": {
                        "features": [
                            "Test fixtures (TEST_F)",
                            "Test cases (TEST)",
                            "Parameterized tests",
                            "Type-parameterized tests",
                            "Value-parameterized tests",
                            "Death tests",
                            "Global test environment"
                        ],
                        "components": [
                            "Test assertions",
                            "Test suites",
                            "Test filters",
                            "Test listeners",
                            "XML report generation"
                        ]
                    }
                },
                {
                    "mocking": {
                        "concepts": [
                            "Mock objects",
                            "Stub methods",
                            "Fake objects",
                            "Test doubles",
                            "Behavior verification"
                        ],
                        "features": [
                            "Expect calls",
                            "Return values",
                            "Argument matching",
                            "Call counting",
                            "Sequence verification"
                        ]
                    }
                },
                {
                    "test-driven development": {
                        "principles": [
                            "Red-Green-Refactor cycle",
                            "Write test first",
                            "Minimal implementation",
                            "Refactoring",
                            "Continuous testing"
                        ],
                        "practices": [
                            "Small iterations",
                            "Clear test names",
                            "Single responsibility",
                            "Test isolation",
                            "Maintainable tests"
                        ]
                    }
                },
                {
                    "benchmarking": {
                        "metrics": [
                            "Execution time",
                            "Memory usage",
                            "CPU cycles",
                            "Cache misses",
                            "System calls"
                        ],
                        "tools": [
                            "Google Benchmark",
                            "Catch2 benchmarking",
                            "Profilers",
                            "Performance counters",
                            "System monitors"
                        ]
                    }
                }
            ],
            "databases": [
                {
                    "connecting to databases (ODBC, SQL)": "Using ODBC (Open Database Connectivity) to connect to various databases.\n\nExample:\n#include <windows.h>\n#include <sql.h>\n#include <sqlext.h>\n\nclass ODBCConnection {\n    SQLHENV env;\n    SQLHDBC dbc;\n    SQLHSTMT stmt;\n\npublic:\n    bool connect() {\n        // Allocate environment handle\n        SQLAllocHandle(SQL_HANDLE_ENV, SQL_NULL_HANDLE, &env);\n        SQLSetEnvAttr(env, SQL_ATTR_ODBC_VERSION, (void*)SQL_OV_ODBC3, 0);\n        \n        // Allocate connection handle\n        SQLAllocHandle(SQL_HANDLE_DBC, env, &dbc);\n        \n        // Connect to datasource\n        SQLCHAR* connStr = (SQLCHAR*)\"DSN=MyDataSource;UID=user;PWD=password\";\n        SQLCHAR outStr[1024];\n        SQLSMALLINT outStrLen;\n        \n        SQLRETURN ret = SQLDriverConnect(dbc, NULL, connStr, SQL_NTS,\n                                        outStr, sizeof(outStr), &outStrLen,\n                                        SQL_DRIVER_COMPLETE);\n        return SQL_SUCCEEDED(ret);\n    }\n\n    bool executeQuery(const char* query) {\n        SQLAllocHandle(SQL_HANDLE_STMT, dbc, &stmt);\n        SQLRETURN ret = SQLExecDirect(stmt, (SQLCHAR*)query, SQL_NTS);\n        return SQL_SUCCEEDED(ret);\n    }\n\n    void disconnect() {\n        SQLFreeHandle(SQL_HANDLE_STMT, stmt);\n        SQLDisconnect(dbc);\n        SQLFreeHandle(SQL_HANDLE_DBC, dbc);\n        SQLFreeHandle(SQL_HANDLE_ENV, env);\n    }\n};"
                },
                {
                    "SQLite": "Using SQLite, a lightweight, file-based database.\n\nExample:\n#include <sqlite3.h>\n#include <iostream>\n\nclass SQLiteDB {\n    sqlite3* db;\n    \n    // Callback function for queries\n    static int callback(void* data, int argc, char** argv, char** colName) {\n        for(int i = 0; i < argc; i++) {\n            std::cout << colName[i] << \": \" << (argv[i] ? argv[i] : \"NULL\") << std::endl;\n        }\n        return 0;\n    }\n\npublic:\n    bool connect(const char* dbName) {\n        int rc = sqlite3_open(dbName, &db);\n        if(rc) {\n            std::cerr << \"Can't open database: \" << sqlite3_errmsg(db) << std::endl;\n            return false;\n        }\n        return true;\n    }\n\n    bool executeQuery(const char* query) {\n        char* errMsg = 0;\n        int rc = sqlite3_exec(db, query, callback, 0, &errMsg);\n        if(rc != SQLITE_OK) {\n            std::cerr << \"SQL error: \" << errMsg << std::endl;\n            sqlite3_free(errMsg);\n            return false;\n        }\n        return true;\n    }\n\n    // Prepared statement example\n    bool insertUser(const std::string& name, int age) {\n        sqlite3_stmt* stmt;\n        const char* query = \"INSERT INTO users (name, age) VALUES (?, ?)\";\n        \n        int rc = sqlite3_prepare_v2(db, query, -1, &stmt, nullptr);\n        if(rc != SQLITE_OK) return false;\n\n        sqlite3_bind_text(stmt, 1, name.c_str(), -1, SQLITE_STATIC);\n        sqlite3_bind_int(stmt, 2, age);\n\n        rc = sqlite3_step(stmt);\n        sqlite3_finalize(stmt);\n        return rc == SQLITE_DONE;\n    }\n\n    void close() {\n        sqlite3_close(db);\n    }\n};"
                },
                {
                    "MySQL": "Connecting to MySQL databases using the MySQL C++ Connector.\n\nExample:\n#include <mysql_connection.h>\n#include <cppconn/driver.h>\n#include <cppconn/exception.h>\n#include <cppconn/resultset.h>\n#include <cppconn/statement.h>\n\nclass MySQLDB {\n    sql::Driver* driver;\n    sql::Connection* con;\n    sql::Statement* stmt;\n\npublic:\n    bool connect(const std::string& host, const std::string& user,\n                 const std::string& password, const std::string& database) {\n        try {\n            driver = get_driver_instance();\n            con = driver->connect(host, user, password);\n            con->setSchema(database);\n            stmt = con->createStatement();\n            return true;\n        } catch(sql::SQLException& e) {\n            std::cerr << \"SQLException: \" << e.what() << std::endl;\n            return false;\n        }\n    }\n\n    bool executeQuery(const std::string& query) {\n        try {\n            sql::ResultSet* res = stmt->executeQuery(query);\n            while(res->next()) {\n                // Process results\n                std::cout << res->getString(1) << std::endl;\n            }\n            delete res;\n            return true;\n        } catch(sql::SQLException& e) {\n            std::cerr << \"SQLException: \" << e.what() << std::endl;\n            return false;\n        }\n    }\n\n    // Prepared statement example\n    bool insertUser(const std::string& name, int age) {\n        try {\n            sql::PreparedStatement* pstmt = con->prepareStatement(\n                \"INSERT INTO users(name, age) VALUES (?, ?)\");\n            pstmt->setString(1, name);\n            pstmt->setInt(2, age);\n            pstmt->execute();\n            delete pstmt;\n            return true;\n        } catch(sql::SQLException& e) {\n            std::cerr << \"SQLException: \" << e.what() << std::endl;\n            return false;\n        }\n    }\n\n    void disconnect() {\n        delete stmt;\n        delete con;\n    }\n};"
                },
                {
                    "PostgreSQL": "Connecting to PostgreSQL using the libpq library.\n\nExample:\n#include <libpq-fe.h>\n#include <string>\n\nclass PostgreSQLDB {\n    PGconn* conn;\n\npublic:\n    bool connect(const std::string& conninfo) {\n        conn = PQconnectdb(conninfo.c_str());\n        if(PQstatus(conn) != CONNECTION_OK) {\n            std::cerr << \"Connection failed: \" << PQerrorMessage(conn) << std::endl;\n            return false;\n        }\n        return true;\n    }\n\n    bool executeQuery(const std::string& query) {\n        PGresult* res = PQexec(conn, query.c_str());\n        if(PQresultStatus(res) != PGRES_TUPLES_OK) {\n            std::cerr << \"Query failed: \" << PQerrorMessage(conn) << std::endl;\n            PQclear(res);\n            return false;\n        }\n\n        // Process results\n        int rows = PQntuples(res);\n        int cols = PQnfields(res);\n        for(int i = 0; i < rows; i++) {\n            for(int j = 0; j < cols; j++) {\n                std::cout << PQgetvalue(res, i, j) << \"\\t\";\n            }\n            std::cout << std::endl;\n        }\n\n        PQclear(res);\n        return true;\n    }\n\n    // Prepared statement example\n    bool insertUser(const std::string& name, int age) {\n        const char* paramValues[2];\n        char ageStr[12];\n        sprintf(ageStr, \"%d\", age);\n        \n        paramValues[0] = name.c_str();\n        paramValues[1] = ageStr;\n\n        PGresult* res = PQexecParams(conn,\n            \"INSERT INTO users(name, age) VALUES($1, $2)\",\n            2,          // number of parameters\n            nullptr,    // parameter types\n            paramValues,\n            nullptr,    // parameter lengths\n            nullptr,    // parameter formats\n            0);         // result format\n\n        bool success = PQresultStatus(res) == PGRES_COMMAND_OK;\n        PQclear(res);\n        return success;\n    }\n\n    void disconnect() {\n        PQfinish(conn);\n    }\n};"
                },
                {
                    "ORM libraries for C++": "Using Object-Relational Mapping libraries in C++.\n\nExample using ODB:\n#include <odb/core.hxx>\n#include <string>\n\n#pragma db object\nclass User {\n    #pragma db id auto\n    unsigned long id_;\n\n    std::string name_;\n    int age_;\n\npublic:\n    User(const std::string& name, int age)\n        : name_(name), age_(age) {}\n\n    const std::string& name() const { return name_; }\n    void name(const std::string& name) { name_ = name; }\n\n    int age() const { return age_; }\n    void age(int age) { age_ = age; }\n};\n\n// Usage example:\n#include <odb/database.hxx>\n#include <odb/transaction.hxx>\n#include <odb/mysql/database.hxx>\n\nint main() {\n    try {\n        odb::mysql::database db(\"test\", \"user\", \"password\", \"localhost\");\n        \n        User user(\"John Doe\", 30);\n        \n        odb::transaction t(db.begin());\n        db.persist(user);\n        t.commit();\n    } catch(const odb::exception& e) {\n        std::cerr << e.what() << std::endl;\n    }\n}"
                },
                {
                    "database connection management": "Managing database connections efficiently with connection pooling.\n\nExample:\n#include <vector>\n#include <mutex>\n#include <memory>\n\ntemplate<typename DBConnection>\nclass ConnectionPool {\n    std::vector<std::unique_ptr<DBConnection>> connections;\n    std::vector<bool> inUse;\n    std::mutex mtx;\n    size_t poolSize;\n\n    // Connection parameters\n    std::string host;\n    std::string user;\n    std::string password;\n    std::string database;\n\npublic:\n    ConnectionPool(size_t size, const std::string& h, const std::string& u,\n                  const std::string& p, const std::string& db)\n        : poolSize(size), host(h), user(u), password(p), database(db) {\n        connections.reserve(poolSize);\n        inUse.resize(poolSize, false);\n\n        // Initialize connections\n        for(size_t i = 0; i < poolSize; ++i) {\n            connections.push_back(std::make_unique<DBConnection>());\n            connections.back()->connect(host, user, password, database);\n        }\n    }\n\n    // Get available connection\n    DBConnection* getConnection() {\n        std::lock_guard<std::mutex> lock(mtx);\n        for(size_t i = 0; i < poolSize; ++i) {\n            if(!inUse[i]) {\n                inUse[i] = true;\n                return connections[i].get();\n            }\n        }\n        return nullptr; // No available connections\n    }\n\n    // Return connection to pool\n    void releaseConnection(DBConnection* conn) {\n        std::lock_guard<std::mutex> lock(mtx);\n        for(size_t i = 0; i < poolSize; ++i) {\n            if(connections[i].get() == conn) {\n                inUse[i] = false;\n                break;\n            }\n        }\n    }\n\n    // Cleanup\n    ~ConnectionPool() {\n        for(auto& conn : connections) {\n            conn->disconnect();\n        }\n    }\n};"
                }
            ],

            "performance optimization": [
                {
                    "profiling code": "Using profiling tools to identify performance bottlenecks in your code.\n\nExample using gprof:\n// Compile with: g++ -pg program.cpp\n// Run the program to generate gmon.out\n// Analyze with: gprof ./a.out gmon.out\n\n// Manual timing example:\n#include <chrono>\nauto start = std::chrono::high_resolution_clock::now();\n// Code to profile\nauto end = std::chrono::high_resolution_clock::now();\nauto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);\nstd::cout << \"Execution time: \" << duration.count() << \" microseconds\";"
                },
                {
                    "algorithm optimization": "Improving algorithm efficiency through better data structures and algorithmic approaches.\n\nExample:\n// Inefficient string concatenation\nstring result;\nfor(int i = 0; i < 1000; i++) {\n    result += \"x\";  // Creates new string each time\n}\n\n// Optimized version using reserve\nstring result;\nresult.reserve(1000);  // Pre-allocate space\nfor(int i = 0; i < 1000; i++) {\n    result += \"x\";\n}\n\n// Using StringBuilder pattern\nstringstream ss;\nfor(int i = 0; i < 1000; i++) {\n    ss << \"x\";\n}\nstring result = ss.str();"
                },
                {
                    "memory management": "Efficient memory allocation and deallocation strategies.\n\nExample:\n// Custom allocator for frequent allocations\ntemplate<typename T>\nclass PoolAllocator {\n    static constexpr size_t POOL_SIZE = 1000;\n    T* pool[POOL_SIZE];\n    size_t current = 0;\n\npublic:\n    T* allocate() {\n        if (current < POOL_SIZE)\n            return pool[current++];\n        return new T();\n    }\n    void deallocate(T* ptr) {\n        if (current > 0)\n            pool[--current] = ptr;\n        else\n            delete ptr;\n    }\n};"
                },
                {
                    "time complexity": "Understanding and optimizing algorithmic time complexity.\n\nExample:\n// O(n^2) implementation\nvoid findDuplicates(vector<int>& arr) {\n    for(size_t i = 0; i < arr.size(); i++) {\n        for(size_t j = i + 1; j < arr.size(); j++) {\n            if(arr[i] == arr[j]) cout << \"Found duplicate: \" << arr[i];\n        }\n    }\n}\n\n// O(n) implementation using hash set\nvoid findDuplicatesOptimized(vector<int>& arr) {\n    unordered_set<int> seen;\n    for(int num : arr) {\n        if(!seen.insert(num).second)\n            cout << \"Found duplicate: \" << num;\n    }\n}"
                },
                {
                    "space complexity": "Managing memory usage and reducing space requirements.\n\nExample:\n// Space inefficient: O(n) extra space\nvector<int> removeDuplicates(const vector<int>& arr) {\n    set<int> unique(arr.begin(), arr.end());\n    return vector<int>(unique.begin(), unique.end());\n}\n\n// Space efficient: O(1) extra space\n// Assumes sorted array\nint removeDuplicatesInPlace(vector<int>& arr) {\n    if (arr.empty()) return 0;\n    int writeIndex = 1;\n    for(int i = 1; i < arr.size(); i++) {\n        if(arr[i] != arr[i-1]) {\n            arr[writeIndex++] = arr[i];\n        }\n    }\n    return writeIndex;\n}"
                },
                {
                    "multithreading vs multiprocessing": "Choosing between thread-based and process-based parallelism.\n\nExample:\n// Multithreading example\nvoid threadExample() {\n    vector<thread> threads;\n    mutex mtx;\n    int shared_sum = 0;\n    \n    for(int i = 0; i < 4; i++) {\n        threads.emplace_back([&mtx, &shared_sum]() {\n            lock_guard<mutex> lock(mtx);\n            shared_sum += 1;\n        });\n    }\n    for(auto& t : threads) t.join();\n}\n\n// Multiprocessing example (Linux)\n#include <unistd.h>\nvoid processExample() {\n    pid_t pid = fork();\n    if (pid == 0) {\n        // Child process\n        exit(0);\n    } else if (pid > 0) {\n        // Parent process\n        wait(NULL);\n    }\n}"
                },
                {
                    "move semantics": "Using move operations to avoid unnecessary copying.\n\nExample:\nclass Buffer {\n    std::vector<char> data;\npublic:\n    // Move constructor\n    Buffer(Buffer&& other) noexcept \n        : data(std::move(other.data)) {}\n    \n    // Move assignment\n    Buffer& operator=(Buffer&& other) noexcept {\n        if(this != &other) {\n            data = std::move(other.data);\n        }\n        return *this;\n    }\n    \n    // Example usage\n    void transfer(Buffer&& other) {\n        data = std::move(other.data);\n    }\n};"
                },
                {
                    "efficient loops": "Optimizing loop performance through better iteration patterns.\n\nExample:\n// Cache-friendly loop (row-major order for 2D array)\nconst int SIZE = 1000;\nint matrix[SIZE][SIZE];\n\n// Efficient\nfor(int i = 0; i < SIZE; i++) {\n    for(int j = 0; j < SIZE; j++) {\n        matrix[i][j] = 0;  // Follows memory layout\n    }\n}\n\n// Loop unrolling\nfor(int i = 0; i < SIZE; i += 4) {\n    matrix[i] = 0;\n    matrix[i+1] = 0;\n    matrix[i+2] = 0;\n    matrix[i+3] = 0;\n}"
                },
                {
                    "inline functions": "Using inline functions to reduce function call overhead.\n\nExample:\n// Inline function definition\ninline int square(int x) {\n    return x * x;\n}\n\n// Class member inline function\nclass Math {\npublic:\n    inline static int cube(int x) { return x * x * x; }\n};\n\n// Force inline with attribute (compiler-specific)\n[[gnu::always_inline]] int factorial(int n) {\n    return (n <= 1) ? 1 : n * factorial(n - 1);\n}"
                },
                {
                    "copy elision": "Optimizing out unnecessary copy operations.\n\nExample:\nclass Heavy {\n    vector<int> data;\npublic:\n    Heavy(size_t size) : data(size) {}\n    \n    // Return value optimization (RVO)\n    static Heavy createHeavy() {\n        return Heavy(1000);  // No copy, directly constructed\n    }\n    \n    // Named return value optimization (NRVO)\n    static Heavy createNamed() {\n        Heavy result(1000);\n        return result;  // Copy might be elided\n    }\n};"
                },
                {
                    "compiling with optimization flags": "Using compiler optimizations to improve performance.\n\nExample:\n/*\n// Common optimization flags:\ng++ -O2 program.cpp  // Moderate optimization\ng++ -O3 program.cpp  // Aggressive optimization\ng++ -march=native program.cpp  // CPU-specific optimizations\n\n// Combined optimizations:\ng++ -O3 -march=native -flto program.cpp  // Link-time optimization\n\n// Profile-guided optimization:\ng++ -fprofile-generate program.cpp  // Step 1: Generate profile\n./a.out  // Run program to collect profile data\ng++ -fprofile-use program.cpp  // Step 2: Use profile data\n*/"
                },
                {
                    "memory alignment": "Optimizing data structure layout for better memory access.\n\nExample:\n// Poorly aligned structure\nstruct Inefficient {\n    char a;       // 1 byte\n    double b;     // 8 bytes\n    short c;      // 2 bytes\n};  // Size: 24 bytes due to padding\n\n// Optimized alignment\nstruct Efficient {\n    double b;     // 8 bytes\n    short c;      // 2 bytes\n    char a;       // 1 byte\n    // 5 bytes padding\n};  // Size: 16 bytes\n\n// Forcing alignment\nstruct alignas(16) AlignedStruct {\n    double value;\n    int data;\n};"
                },
                {
                    "cache optimization": "Improving cache utilization and reducing cache misses.\n\nExample:\n// Cache-friendly data access\nclass CacheOptimized {\n    static const size_t CACHE_LINE = 64;\n    alignas(CACHE_LINE) int frequently_accessed_data;\n    char padding[CACHE_LINE - sizeof(int)];\n    int rarely_accessed_data;\n\npublic:\n    void process_data() {\n        // Process frequently_accessed_data in tight loop\n        for(int i = 0; i < 1000; i++) {\n            frequently_accessed_data += i;\n        }\n    }\n};"
                },
                {
                    "using concurrent containers": "Thread-safe containers for concurrent access.\n\nExample:\n#include <concurrent_queue>  // Microsoft PPL or similar\n\ntemplate<typename T>\nclass ThreadSafeQueue {\n    mutable mutex mtx;\n    queue<T> data;\n    condition_variable cv;\n\npublic:\n    void push(T value) {\n        lock_guard<mutex> lock(mtx);\n        data.push(std::move(value));\n        cv.notify_one();\n    }\n\n    bool try_pop(T& value) {\n        lock_guard<mutex> lock(mtx);\n        if(data.empty()) return false;\n        value = std::move(data.front());\n        data.pop();\n        return true;\n    }\n};"
                },
                {
                    "lock-free data structures": "Data structures that avoid mutex locks for better concurrency.\n\nExample:\ntemplate<typename T>\nclass LockFreeStack {\n    struct Node {\n        T data;\n        Node* next;\n        Node(const T& d) : data(d), next(nullptr) {}\n    };\n\n    atomic<Node*> head;\n\npublic:\n    void push(T value) {\n        Node* new_node = new Node(value);\n        do {\n            new_node->next = head.load();\n        } while(!head.compare_exchange_weak(new_node->next, new_node));\n    }\n\n    bool pop(T& value) {\n        Node* old_head = head.load();\n        do {\n            if(!old_head) return false;\n        } while(!head.compare_exchange_weak(old_head, old_head->next));\n        value = old_head->data;\n        delete old_head;\n        return true;\n    }\n};"
                }
            ]
        }



        return knowledge_base
        pass
    def init_quiz_questions(self):
        return {
            "Basics": [
                ("What keyword is used to declare a variable in C++?", "int, float, char, etc."),
                ("What is the correct syntax for a single-line comment in C++?", "//"),
                ("What are the fundamental data types in C++?", "int, float, char, double, bool"),
                ("What is the result of the expression 5 % 2?", "1 (modulus operator)"),
                ("What is a namespace in C++ used for?",
                 "To organize code into logical groups and avoid name conflicts."),
                ("Which keyword is used to define a constant variable?", "const"),
                ("How do you declare input and output streams?", "cin, cout"),
                ("What type of loop runs at least once even if the condition is false?", "do-while loop"),
                ("What keyword is used to exit a loop prematurely?", "break"),
                ("How do you cast an int variable 'x' to a float?", "static_cast<float>(x)"),
            ],

            "data structures": [
                (
                "What is the default size of an array in C++ when not specified?", "Undefined, needs to be specified."),
                ("What is the difference between a pointer and a reference?",
                 "A pointer can be reassigned, a reference cannot."),
                ("What is the syntax for defining an array of 10 integers?", "int arr[10];"),
                ("Which STL container stores key-value pairs?", "map"),
                ("What function is used to allocate memory dynamically in C++?", "new"),
                ("How do you declare an iterator for a vector in C++?", "std::vector<int>::iterator it;"),
                ("What is the difference between a struct and a class in C++?",
                 "Members of a struct are public by default, members of a class are private by default."),
                ("Which STL container does not allow duplicate values?", "set"),
                ("How do you access a member of a struct in C++?", "Using the dot operator (.)."),
                ("What is the difference between a vector and an array?", "Vector is dynamic, array is static."),
            ],

            "functions": [
                ("What is the syntax to define a function that returns an integer in C++?", "int function_name() { }"),
                ("What is the purpose of an inline function in C++?",
                 "To suggest to the compiler to replace the function call with the function code itself."),
                ("What is function overloading in C++?",
                 "Defining multiple functions with the same name but different parameter lists."),
                ("What is the syntax to pass a parameter by reference?", "void func(int &x);"),
                ("What does it mean to have default arguments in a function?",
                 "You can call the function without specifying all arguments, and default values will be used."),
                ("What is a lambda function in C++?", "An anonymous function defined with the [] syntax."),
                ("What is the difference between passing by value and passing by reference?",
                 "Passing by value copies the data, passing by reference allows the function to modify the original data."),
                ("What does the return keyword do in a function?",
                 "It exits the function and optionally returns a value."),
                ("What is recursion?", "A function calling itself."),
                ("How do you declare a function template in C++?", "template<typename T> T function_name(T arg);"),
            ],

            "object-oriented programming": [
                ("What is a class in C++?", "A blueprint for creating objects."),
                ("What is the purpose of a constructor?", "To initialize an object when it is created."),
                ("What is the difference between public, private, and protected access specifiers?",
                 "Public allows access from anywhere, private restricts access to the class, and protected allows access to derived classes."),
                ("What is inheritance in C++?", "A mechanism where a class derives properties from another class."),
                ("What is polymorphism?",
                 "The ability of a function or method to work in multiple forms (e.g., method overriding or function overloading)."),
                ("What are virtual functions?", "Functions that can be overridden in derived classes."),
                ("What is the use of a destructor in C++?", "To clean up resources when an object is destroyed."),
                ("What is operator overloading?", "The ability to define new behavior for existing operators."),
                ("What is a friend function?",
                 "A function that has access to the private and protected members of a class."),
                (
                "What is a pure virtual function?", "A virtual function that must be overridden in any derived class."),
            ],

            "file handling": [
                ("What is the purpose of ifstream in C++?", "To read from a file."),
                ("What is the purpose of ofstream in C++?", "To write to a file."),
                ("How do you open a file in append mode?", "ofstream file('filename', ios::app);"),
                ("What function is used to check if a file has been opened successfully?", "is_open()"),
                ("What does the function eof() check for?", "End of file."),
                ("How do you read a single line from a file?", "getline(file, variable);"),
                ("What is the difference between text and binary files in C++?",
                 "Text files store data as readable characters, binary files store data in binary format."),
                ("What operator is used to write to a file?", "<< (output operator)"),
                ("How do you seek to a specific position in a file?",
                 "seekg() for input files, seekp() for output files."),
                ("How do you close a file in C++?", "file.close();"),
            ],

            "advanced concepts": [
                ("What is dynamic memory allocation?", "Allocating memory at runtime using new or malloc."),
                ("What is a smart pointer in C++?",
                 "A wrapper around a raw pointer that handles memory management automatically."),
                ("What is move semantics in C++?",
                 "The ability to transfer ownership of resources from one object to another."),
                ("What is a mutex used for?", "To provide synchronization between threads."),
                ("What is an rvalue reference?", "A reference that can bind to a temporary object."),
                ("What is a template in C++?",
                 "A feature that allows functions and classes to operate with generic types."),
                ("What is the purpose of std::async?", "To run tasks asynchronously in a separate thread."),
                ("What is std::future?", "An object used to retrieve the result of an asynchronous task."),
                ("What is an atomic operation?", "An operation that completes without being interrupted."),
                ("What are condition variables used for in multithreading?",
                 "To synchronize threads by blocking them until a condition is met."),
            ],

            "error handling": [
                ("What keyword is used to throw an exception?", "throw"),
                ("How do you catch an exception in C++?", "Using try-catch blocks."),
                ("What is the base class for all exceptions in C++?", "std::exception"),
                ("What is a custom exception?", "An exception class defined by the user."),
                ("What is the purpose of assertions in C++?", "To test assumptions during development."),
                ("What happens if an exception is not caught?", "The program terminates."),
                ("What function is used to display the error message from an exception?", "what()"),
                ("How do you rethrow an exception?", "Using the throw keyword inside a catch block."),
                ("What is a logic_error in C++?", "An exception thrown due to a logical error in the program."),
                ("What is a runtime_error in C++?",
                 "An exception thrown due to runtime issues such as division by zero."),
            ],

            "functional programming": [
                ("What is a lambda function in C++?", "An anonymous function defined with [] syntax."),
                ("What is std::function?", "A general-purpose wrapper for storing callable objects."),
                ("How do you define a function pointer in C++?", "ReturnType (*PointerName)(ParameterType);"),
                ("What is a closure in C++?", "A lambda function that captures variables from its enclosing scope."),
                ("What is a higher-order function?",
                 "A function that takes another function as an argument or returns one."),
                ("What library functions can be used to implement map and reduce operations?",
                 "std::transform (for map), std::accumulate (for reduce)"),
                ("How do you create a partial function in C++?",
                 "By using a lambda to bind some arguments and leave others to be provided later."),
                ("What is the purpose of std::bind?",
                 "To bind specific arguments to a function, returning a new function."),
                ("What are function pointers used for?", "To store the address of a function and call it indirectly."),
                ("What does the keyword auto do when declaring a lambda?",
                 "Automatically deduces the type of the lambda function."),
            ],

            "modules and packages": [
                ("What is the purpose of a header file?", "To declare function prototypes, classes, and constants."),
                ("What is the purpose of #include in C++?", "To include the contents of a file."),
                ("How do you prevent multiple inclusions of the same header file?",
                 "Using include guards (#ifndef, #define, #endif)."),
                ("What tool is commonly used to manage and build C++ projects?", "CMake"),
                ("What are C++20 modules?", "A feature to improve modularity and reduce compilation dependencies."),
                ("What is the purpose of linking in C++?", "To combine multiple object files into an executable."),
                ("What is the C++ Standard Library?",
                 "A collection of classes and functions providing data structures, algorithms, and utilities."),
                ("How do you declare a constant value in a header file?", "Using the const or constexpr keyword."),
                ("What is modular programming?", "Dividing a program into smaller, independent, and interchangeable modules."),
                 ("What tool is used to link third-party libraries in C++?", "Linker (using options like -l<library_name>)."),
            ],

            "testing": [
                ("What is unit testing?", "Testing individual components of a program in isolation."),
                ("Which library is commonly used for testing in C++?", "Google Test"),
                ("What is mocking?", "Simulating objects or functions to isolate and test different components."),
                ("What does test-driven development involve?", "Writing tests before writing the actual code."),
                ("How do you write an assertion in Google Test?", "Using ASSERT_EQ, ASSERT_NE, etc."),
                ("What is the purpose of benchmarking?", "To measure the performance of a program or function."),
                ("What is the purpose of assertions in testing?",
                 "To check if a condition is true during program execution."),
                ("How do you compile and run tests with Google Test?",
                 "Using g++ or CMake and running the resulting executable."),
                ("What is a test suite?", "A collection of related test cases."),
                ("What is the difference between ASSERT and EXPECT in Google Test?",
                 "ASSERT halts the test on failure, EXPECT continues."),
            ],

            "databases": [
                ("What is ODBC in C++?", "Open Database Connectivity, a standard API for accessing databases."),
                ("Which function is used to connect to a MySQL database in C++?", "mysql_real_connect()"),
                ("What library would you use to interact with SQLite in C++?", "SQLite C++ API"),
                ("What is an ORM?", "Object-Relational Mapping, a way to map classes to database tables."),
                ("How do you execute an SQL query in C++ using MySQL?", "Using the mysql_query() function."),
                ("What is a prepared statement?", "A precompiled SQL statement that can be executed multiple times."),
                ("What is the purpose of database connection management?",
                 "To efficiently manage multiple connections to a database."),
                ("How do you handle database errors in C++?", "By checking error codes and using try-catch blocks."),
                ("What is PostgreSQL?", "An open-source relational database management system."),
                ("What does SQL stand for?", "Structured Query Language."),
            ],

            "performance optimization": [
                ("What is code profiling?", "Analyzing a program to determine where it spends the most time."),
                ("What is the time complexity of a binary search?", "O(log n)"),
                ("What is the space complexity of an algorithm?",
                 "The amount of memory the algorithm uses relative to input size."),
                ("What is the purpose of move semantics?", "To avoid unnecessary copying of resources."),
                ("What is copy elision in C++?", "An optimization that eliminates unnecessary copying of objects."),
                ("What are inline functions used for?",
                 "To suggest the compiler replace the function call with the actual function code."),
                ("What is memory alignment?", "Arranging data in memory at specific boundaries for faster access."),
                ("What is a cache-friendly data structure?",
                 "A data structure optimized for access patterns that minimize cache misses."),
                ("How do you parallelize a loop in C++?", "Using OpenMP or std::thread."),
                ("What are concurrent containers?", "Data structures designed for safe access by multiple threads."),
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
        return "Hello! I'm your C++ Tutorial Agent. How can I help you today? Type 'topics' to see what I can teach you."

    def list_topics(self):
        topics_list = "\nAvailable Python Topics:\n"
        for i, topic in enumerate(self.topics.keys(), 1):
            topics_list += f"{i}. {topic.capitalize()}\n"
        topics_list += "\nWhich topic would you like to explore? (Type the topic name or number)"
        return topics_list

    def handle_input(self, user_input):
        user_input = user_input.lower().strip()

        if self.is_exit_command(user_input):
            return "Thank you for using the C++ Tutorial Agent. Goodbye!"

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
        print("Welcome to the C++ Tutorial!")
        return self.greet()
