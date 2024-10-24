# main.py

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import json

from csharp_tutorial import CsharpTutorialAgent
from python_tutorial import PythonTutorialAgent
from cpp_tutorial import CppTutorialAgent
class TutorialGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Programming Tutorial Agent")
        self.master.geometry("700x500")
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
        self.welcome_label = ttk.Label(
            self.main_frame,
            text="Welcome to the Programming Tutorial Agent!",
            font=("Arial", 16, "bold")
        )
        self.welcome_label.grid(row=0, column=0, columnspan=6, pady=20)

        # Language selection with improved styling
        self.language_frame = ttk.LabelFrame(self.main_frame, text="Select Your Tutorial", padding="10")
        self.language_frame.grid(row=1, column=0, columnspan=6, pady=10, padx=20, sticky="ew")

        self.language_var = tk.StringVar(value="Python")

        # Radio buttons for language selection
        languages = [("Python Tutorial", "Python"),
                     ("C# Tutorial", "C#"),
                     ("C++ Tutorial", "C++")]

        for i, (text, value) in enumerate(languages):
            radio = ttk.Radiobutton(
                self.language_frame,
                text=text,
                value=value,
                variable=self.language_var
            )
            radio.pack(pady=5)

        # Language descriptions
        descriptions = {
            "Python": "• Beginner-friendly\n• Great for web, data science, and automation",
            "C#": "• Microsoft's powerful language\n• Excellent for Windows and game development",
            "C++": "• High-performance language\n• Perfect for system and game programming"
        }

        self.desc_label = ttk.Label(
            self.language_frame,
            text=descriptions["Python"],
            justify=tk.LEFT,
            padding="10"
        )
        self.desc_label.pack(pady=10)

        # Update description when language changes
        def update_description(*args):
            self.desc_label.config(text=descriptions[self.language_var.get()])

        self.language_var.trace('w', update_description)

        # Start button with improved styling
        self.start_button = ttk.Button(
            self.main_frame,
            text="Start Tutorial",
            command=self.start_tutorial,
            style="Accent.TButton"
        )
        self.start_button.grid(row=3, column=0, columnspan=6, pady=30)

        # Chat display (hidden initially)
        self.chat_display = scrolledtext.ScrolledText(
            self.main_frame,
            wrap=tk.WORD,
            width=80,
            height=20,
            font=("Arial", 10)
        )
        self.chat_display.grid(row=4, column=0, columnspan=6, padx=10, pady=10, sticky="nsew")
        self.chat_display.grid_remove()
        self.chat_display.config(state=tk.DISABLED)

        # Create bottom frame for input and buttons
        self.bottom_frame = ttk.Frame(self.main_frame)
        self.bottom_frame.grid(row=5, column=0, columnspan=6, sticky="ew", pady=5)
        self.bottom_frame.grid_remove()

        # User input (hidden initially)
        self.user_input = ttk.Entry(self.bottom_frame, width=70)
        self.user_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        self.user_input.bind("<Return>", self.send_message)

        # Send button (hidden initially)
        self.send_button = ttk.Button(self.bottom_frame, text="Send", command=self.send_message)
        self.send_button.pack(side=tk.RIGHT, padx=5)

        # Action buttons frame (hidden initially)
        self.action_frame = ttk.Frame(self.main_frame)
        self.action_frame.grid(row=6, column=0, columnspan=6, pady=10)
        self.action_frame.grid_remove()

        # Action buttons with tooltips
        self.action_buttons = []
        actions = [
            ("Help", "Get help with using the tutorial"),
            ("Topics", "View all available topics"),
            ("Next", "Move to the next subtopic"),
            ("Quiz", "Take a quiz on the current topic"),
            ("Progress", "View your learning progress"),
            ("Main Menu", "Return to the language selection")
        ]

        for i, (action, tooltip) in enumerate(actions):
            button = ttk.Button(
                self.action_frame,
                text=action,
                command=lambda a=action: self.perform_action(a)
            )
            button.pack(side=tk.LEFT, padx=5)
            self.create_tooltip(button, tooltip)
            self.action_buttons.append(button)

        # Dark mode toggle with improved styling
        self.theme_frame = ttk.Frame(self.main_frame)
        self.theme_frame.grid(row=7, column=0, columnspan=6, pady=10)

        self.dark_mode_var = tk.BooleanVar(value=self.dark_mode)
        self.dark_mode_check = ttk.Checkbutton(
            self.theme_frame,
            text="Dark Mode",
            command=self.toggle_dark_mode,
            variable=self.dark_mode_var
        )
        self.dark_mode_check.pack()

        # Configure grid
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(4, weight=1)

    def create_tooltip(self, widget, text):
        def enter(event):
            tooltip = tk.Toplevel()
            tooltip.wm_overrideredirect(True)
            tooltip.wm_geometry(f"+{event.x_root + 10}+{event.y_root + 10}")

            label = ttk.Label(tooltip, text=text, justify=tk.LEFT,
                              background="#ffffe0", relief=tk.SOLID, borderwidth=1)
            label.pack()

            widget.tooltip = tooltip

        def leave(event):
            if hasattr(widget, 'tooltip'):
                widget.tooltip.destroy()
                del widget.tooltip

        widget.bind('<Enter>', enter)
        widget.bind('<Leave>', leave)

    def back_to_menu(self):
        # Reset agents
        self.current_agent = None

        # Show welcome screen elements
        self.welcome_label.grid()
        self.language_frame.grid()
        self.start_button.grid()

        # Hide tutorial elements
        self.chat_display.grid_remove()
        self.bottom_frame.grid_remove()
        self.action_frame.grid_remove()

        # Clear chat display
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.delete(1.0, tk.END)
        self.chat_display.config(state=tk.DISABLED)

    def start_tutorial(self):
        selected_language = self.language_var.get()
        if selected_language == "Python":
            self.current_agent = PythonTutorialAgent()
        elif selected_language == "C#":
            self.current_agent = CsharpTutorialAgent()
        else:  # C++
            self.current_agent = CppTutorialAgent()

        # Hide welcome screen elements
        self.welcome_label.grid_remove()
        self.language_frame.grid_remove()
        self.start_button.grid_remove()

        # Show tutorial elements
        self.chat_display.grid()
        self.bottom_frame.grid()
        self.action_frame.grid()

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
        if action == "Main Menu":
            if messagebox.askyesno("Confirm",
                                   "Are you sure you want to return to the main menu? Your progress will be saved."):
                self.back_to_menu()
            return

        if action == "Help":
            self.display_message(
                "Agent: You can ask me about programming topics, or use the buttons to navigate:\n\n"
                "• Topics - View all available topics\n"
                "• Next - Move to the next subtopic\n"
                "• Quiz - Test your knowledge\n"
                "• Progress - Track your learning\n"
                "• Main Menu - Return to language selection"
            )
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
            # Configure dark theme colors
            bg_color = "#2b2b2b"
            fg_color = "white"
            button_bg = "#4a4a4a"
            button_fg = "white"

            self.style.configure(".", background=bg_color, foreground=fg_color)
            self.style.configure("TButton", background=button_bg, foreground=button_fg)
            self.style.configure("Accent.TButton", background="#007acc", foreground="white")
            self.style.map("TButton", background=[('active', '#666666')])
            self.style.configure("TCheckbutton", background=bg_color, foreground=fg_color)
            self.style.configure("TLabelframe", background=bg_color, foreground=fg_color)
            self.style.configure("TLabelframe.Label", background=bg_color, foreground=fg_color)
            self.style.configure("TRadiobutton", background=bg_color, foreground=fg_color)

            self.chat_display.config(bg=bg_color, fg=fg_color)
            self.user_input.config(style="Dark.TEntry")
            self.style.configure("Dark.TEntry", fieldbackground=button_bg, foreground=fg_color)
        else:
            self.style.theme_use('clam')
            # Configure light theme colors
            bg_color = "white"
            fg_color = "black"
            button_bg = "#e1e1e1"
            button_fg = "black"

            self.style.configure(".", background=bg_color, foreground=fg_color)
            self.style.configure("TButton", background=button_bg, foreground=button_fg)
            self.style.configure("Accent.TButton", background="#0078d4", foreground="white")
            self.style.map("TButton", background=[('active', '#d1d1d1')])
            self.style.configure("TCheckbutton", background=bg_color, foreground=fg_color)
            self.style.configure("TLabelframe", background=bg_color, foreground=fg_color)
            self.style.configure("TLabelframe.Label", background=bg_color, foreground=fg_color)
            self.style.configure("TRadiobutton", background=bg_color, foreground=fg_color)

            self.chat_display.config(bg=bg_color, fg=fg_color)
            self.user_input.config(style="TEntry")
            self.style.configure("TEntry", fieldbackground=bg_color, foreground=fg_color)

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
