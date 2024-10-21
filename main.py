# main.py

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import json

from csharp_tutorial import CsharpTutorialAgent
from python_tutorial import PythonTutorialAgent
class TutorialGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Programming Tutorial Agent")
        self.master.geometry("700x500")
        self.python_agent = None
        self.csharp_agent = None
        self.current_agent = None
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

        # Welcome message
        self.welcome_label = ttk.Label(self.main_frame, text="Welcome to the Programming Tutorial Agent!", font=("Arial", 16))
        self.welcome_label.grid(row=0, column=0, columnspan=6, pady=20)

        # Language selection
        self.language_label = ttk.Label(self.main_frame, text="Please select a tutorial:")
        self.language_label.grid(row=1, column=0, columnspan=6, pady=10)

        self.language_var = tk.StringVar(value="Python")
        self.language_menu = ttk.OptionMenu(self.main_frame, self.language_var, "Python", "Python", "C#")
        self.language_menu.grid(row=2, column=0, columnspan=6, pady=10)

        # Start button
        self.start_button = ttk.Button(self.main_frame, text="Start Tutorial", command=self.start_tutorial)
        self.start_button.grid(row=3, column=0, columnspan=6, pady=20)

        # Chat display (hidden initially)
        self.chat_display = scrolledtext.ScrolledText(self.main_frame, wrap=tk.WORD, width=80, height=20)
        self.chat_display.grid(row=4, column=0, columnspan=6, padx=10, pady=10, sticky="nsew")
        self.chat_display.grid_remove()
        self.chat_display.config(state=tk.DISABLED)

        # User input (hidden initially)
        self.user_input = ttk.Entry(self.main_frame, width=70)
        self.user_input.grid(row=5, column=0, columnspan=5, padx=10, pady=10, sticky="ew")
        self.user_input.grid_remove()
        self.user_input.bind("<Return>", self.send_message)

        # Send button (hidden initially)
        self.send_button = ttk.Button(self.main_frame, text="Send", command=self.send_message)
        self.send_button.grid(row=5, column=5, padx=5, pady=10)
        self.send_button.grid_remove()

        # Action buttons (hidden initially)
        self.action_buttons = []
        actions = ["Help", "Topics", "Next", "Quiz", "Progress"]
        for i, action in enumerate(actions):
            button = ttk.Button(self.main_frame, text=action, command=lambda a=action: self.perform_action(a))
            button.grid(row=6, column=i, padx=2, pady=10)
            button.grid_remove()
            self.action_buttons.append(button)

        # Dark mode toggle
        self.dark_mode_var = tk.BooleanVar(value=self.dark_mode)
        self.dark_mode_check = ttk.Checkbutton(self.main_frame, text="Dark Mode",
                                               command=self.toggle_dark_mode,
                                               variable=self.dark_mode_var)
        self.dark_mode_check.grid(row=7, column=0, columnspan=6, pady=10)

        # Configure grid
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(4, weight=1)

    def start_tutorial(self):
        selected_language = self.language_var.get()
        if selected_language == "Python":
            self.current_agent = PythonTutorialAgent()
        else:
            self.current_agent = CsharpTutorialAgent()

        # Hide welcome screen elements
        self.welcome_label.grid_remove()
        self.language_label.grid_remove()
        self.language_menu.grid_remove()
        self.start_button.grid_remove()

        # Show tutorial elements
        self.chat_display.grid()
        self.user_input.grid()
        self.send_button.grid()
        for button in self.action_buttons:
            button.grid()

        # Display initial tutorial message
        self.display_message(f"Starting {selected_language} Tutorial\n\nAgent: " + self.current_agent.start_tutorial())

    def send_message(self, event=None):
        user_message = self.user_input.get()
        self.display_message("You: " + user_message)
        self.user_input.delete(0, tk.END)

        response = self.current_agent.handle_input(user_message)
        self.display_message("Agent: " + response)

        if self.current_agent.is_exit_command(user_message):
            self.master.after(1000, self.master.quit)

    def display_message(self, message):
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.insert(tk.END, message + "\n\n")
        self.chat_display.see(tk.END)
        self.chat_display.config(state=tk.DISABLED)

    def perform_action(self, action):
        if action == "Help":
            self.display_message(
                "Agent: You can ask me about programming topics, or use the buttons to navigate. Type 'topics' to see available topics, 'next' to move to the next subtopic, or 'quiz' to start a quiz on the current topic.")
        elif action == "Topics":
            self.display_message("Agent: " + self.current_agent.list_topics())
        elif action == "Next":
            response = self.current_agent.next_subtopic()
            self.display_message("Agent: " + response)
        elif action == "Quiz":
            response = self.current_agent.start_quiz()
            self.display_message("Agent: " + response)
        elif action == "Progress":
            progress_report = self.current_agent.show_progress()
            self.display_message("Agent: " + progress_report)

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

def main():
    root = tk.Tk()
    gui = TutorialGUI(root)
    root.protocol("WM_DELETE_WINDOW", root.quit)  # Ensure clean exit
    root.mainloop()

if __name__ == "__main__":
    main()