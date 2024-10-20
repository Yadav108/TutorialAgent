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
            "python basics": ["variables", "data types", "operators", "control structures"],
            "data structures": ["lists", "tuples", "dictionaries", "sets"],
            "functions": ["defining functions", "arguments", "return values", "lambda functions"],
            "object-oriented programming": ["classes", "objects", "inheritance", "polymorphism"],
            "file handling": ["file operations", "reading and writing files", "working with CSV", "JSON handling",
                              "context managers"],
            "advanced concepts": ["decorators", "generators", "lambda functions", "recursion", "regular expressions"],
            "error handling": ["exceptions", "try-except blocks", "raising exceptions", "custom exceptions",
                               "debugging techniques"],
            "functional programming": ["first-class functions", "higher-order functions", "map, filter, reduce",
                                       "closures", "partial functions"]
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
            "variables": "In Python, variables are containers for storing data values. They are created the moment you first assign a value to them. Python uses dynamic typing, meaning you don't need to declare the type of a variable explicitly.",
            "data types": "Python has several built-in data types including integers, floating-point numbers, strings, booleans, lists, tuples, sets, and dictionaries. Each type has its own characteristics and use cases.",
            "operators": "Python supports various types of operators: arithmetic (+, -, *, /, //, %, **), comparison (==, !=, <, >, <=, >=), logical (and, or, not), identity (is, is not), and membership (in, not in) operators.",
            "control structures": "Control structures in Python include if-else statements for conditional execution, for and while loops for iteration, and try-except blocks for error handling.",
            "lists": "Lists are ordered, mutable sequences in Python. They can contain elements of different types and are defined using square brackets [].",
            "tuples": "Tuples are ordered, immutable sequences in Python. They are defined using parentheses () and can contain elements of different types.",
            "dictionaries": "Dictionaries in Python are unordered collections of key-value pairs. They are defined using curly braces {} with colons : separating keys and values.",
            "sets": "Sets are unordered collections of unique elements in Python. They are defined using curly braces {} or the set() function.",
            "defining functions": "Functions in Python are defined using the 'def' keyword, followed by the function name and parameters in parentheses.",
            "arguments": "Function arguments in Python can be positional, keyword, default, or variable-length (*args and **kwargs).",
            "return values": "The 'return' statement is used in Python functions to specify the value to be returned to the caller.",
            "lambda functions": "Lambda functions are small, anonymous functions in Python, defined using the 'lambda' keyword.",
            "classes": "Classes in Python are blueprints for creating objects. They are defined using the 'class' keyword.",
            "objects": "Objects are instances of classes in Python, created from class definitions.",
            "inheritance": "Inheritance in Python allows a class to inherit attributes and methods from another class.",
            "polymorphism": "Polymorphism in Python allows objects of different classes to be treated as objects of a common base class.",
            "file operations": "Python provides built-in functions for file operations such as open(), close(), read(), and write().",
            "reading and writing files": "Reading files in Python can be done using methods like read(), readline(), or readlines(). Writing to files is achieved using the write() method.",
            "working with CSV": "Python's csv module provides functionality to read from and write to CSV (Comma Separated Values) files.",
            "JSON handling": "Python's json module allows you to encode Python objects as JSON strings and decode JSON strings into Python objects.",
            "context managers": "Context managers in Python (used with the 'with' statement) provide a convenient way to manage resources like file handles.",
            "decorators": "Decorators in Python are functions that modify other functions. They are defined using the @decorator syntax.",
            "generators": "Generators are functions that return an iterator. They are defined like normal functions but use the 'yield' keyword instead of 'return'.",
            "recursion": "Recursion is a programming technique where a function calls itself to solve a problem.",
            "regular expressions": "Regular expressions (regex) are powerful tools for pattern matching and text manipulation. Python's re module provides support for regular expressions.",
            "exceptions": "Exceptions in Python are events that occur during the execution of a program that disrupt the normal flow of instructions.",
            "try-except blocks": "Try-except blocks are used for exception handling in Python. Code that might raise an exception is placed in the 'try' block, and the code to handle the exception is placed in the 'except' block.",
            "raising exceptions": "In Python, you can raise exceptions using the 'raise' keyword.",
            "custom exceptions": "Python allows you to create your own exception classes by inheriting from the built-in Exception class or its subclasses.",
            "debugging techniques": "Debugging in Python can be done using print statements, assertions, and the built-in pdb module for interactive debugging.",
            "first-class functions": "In Python, functions are first-class citizens, meaning they can be assigned to variables, passed as arguments to other functions, and returned from functions.",
            "higher-order functions": "Higher-order functions are functions that can take other functions as arguments or return functions as results.",
            "map, filter, reduce": "map(), filter(), and reduce() are built-in functions in Python that operate on iterables.",
            "closures": "A closure is a function object that remembers values in enclosing scopes even if they are not present in memory.",
            "partial functions": "Partial functions allow you to fix a certain number of arguments of a function and generate a new function."
        }
        return knowledge_base
    def init_quiz_questions(self):
        # Quiz questions content (same as before)
        return {
            "python basics": [
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
                ("What is it called when a method in a subclass overrides a method in its superclass?",
                 "method overriding")
            ],
            "file handling": [
                ("What function is used to open a file in Python?", "open"),
                ("What mode should you use to open a file for reading?", "r"),
                ("What method reads all lines of a file into a list?", "readlines"),
                ("What module is commonly used for working with CSV files?", "csv"),
                ("What is the advantage of using a 'with' statement when working with files?",
                 "it automatically closes the file")
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
                ("What clause is used to define code that should run regardless of whether an exception occurred?",
                 "finally"),
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
            ]
            # ... (rest of the topics)
        }

    def preprocess_text(self, text):
        tokens = word_tokenize(text.lower())
        return " ".join(
            [self.lemmatizer.lemmatize(word) for word in tokens if word not in self.stop_words and word.isalnum()])

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
        user_input = user_input.lower().strip()

        if self.is_exit_command(user_input):
            return "Thank you for using the Python Tutorial Agent. Goodbye!"

        if user_input == "3" or "progress" in user_input:
            return self.show_progress()

        if "topic" in user_input:
            return self.list_topics()
        elif any(topic in user_input for topic in self.topics):
            for topic in self.topics:
                if topic in user_input:
                    self.current_topic = topic
                    self.current_subtopic = None
                    return f"Great! Let's learn about {topic}. We'll cover: {', '.join(self.topics[topic])}. Type 'start' when you're ready to begin, or ask me anything about {topic}."
        elif self.current_topic and user_input == "start":
            return self.next_subtopic()
        elif self.current_topic and "next" in user_input:
            return self.next_subtopic()
        elif user_input in ["1", "quiz"]:
            self.mode = "quiz"
            return "Great! Let's start a quiz. Type 'stop' or 'exit' at any time to end the quiz."
        elif user_input in ["2", "new topic"]:
            self.current_topic = None
            self.current_subtopic = None
            return "Sure, let's choose a new topic. " + self.list_topics()
        else:
            most_similar_subtopic = self.get_most_similar_subtopic(user_input)
            return f"Based on your question, I think you might be interested in {most_similar_subtopic}. Here's what I know:\n\n{self.knowledge_base[most_similar_subtopic]}\n\nDo you want to know more about this, or shall we move to the next topic? Type 'next' to continue or ask me anything else."

    def is_exit_command(self, user_input):
        return any(cmd in user_input for cmd in self.exit_commands)

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
            return (f"Let's learn about {self.current_subtopic}:\n\n"
                    f"{self.knowledge_base[self.current_subtopic]}\n\n"
                    f"What would you like to know more about {self.current_subtopic}, or type 'next' to continue?")
        else:
            return "Please choose a topic first. " + self.list_topics()

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
            self.start_quiz()
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