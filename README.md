# TutorialAgent
# Programming Tutorial Agent

## Overview

The Programming Tutorial Agent is an interactive learning tool designed to help users learn programming languages. This application provides a user-friendly graphical interface where learners can engage with a virtual tutor, ask questions, and progress through various programming topics at their own pace.

## Features

- **Multi Programming Language Support**: Option to choose various tutorials.
- **Interactive Chat Interface**: Engage in a conversation-like learning experience with the tutorial agent.
- **Topic Navigation**: Explore different programming concepts organized by topics and subtopics.
- **Quiz Mode**: Test your knowledge with built-in quizzes for each topic.
- **Progress Tracking**: Keep track of your learning progress across different topics.
- **Dark Mode**: Toggle between light and dark themes for comfortable viewing.
- **Customizable**: Easily extendable to add more programming languages or topics.

## Prerequisites

- Python 3.7 or higher
- Tkinter (usually comes pre-installed with Python)
- NLTK library
- scikit-learn library

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/programming-tutorial-agent.git
   cd programming-tutorial-agent
   ```

2. Install the required dependencies:
   ```
   pip install nltk scikit-learn
   ```

3. Download required NLTK data:
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   nltk.download('wordnet')
   ```

## Usage

1. Run the main script:
   ```
   python main.py
   ```

2. Select your preferred programming language  from the dropdown menu.

3. Click "Start Tutorial" to begin.

4. Interact with the tutorial agent by typing questions or commands in the input box.

5. Use the action buttons (Help, Topics, Next, Quiz, Progress) for quick navigation and additional features.

## Project Structure

- `main.py`: The main script that runs the GUI and manages the tutorial agents.
- `python_tutorial.py`: Contains the Python tutorial agent logic and content.
- `csharp_tutorial.py`: Contains the C# tutorial agent logic and content.
- ˋcpp_tutorial.py´:Contains he c++ tutorial agnt logic and content.
- `settings.json`: Stores user preferences (e.g., dark mode setting).

## Customization

To add new topics or modify existing ones, edit the `topics` and `knowledge_base` dictionaries in the respective tutorial agent files (`python_tutorial.py` or `csharp_tutorial.py`).

## Contributing

Contributions to improve the tutorial content, add new features, or fix bugs are welcome. Please feel free to submit pull requests or open issues for any enhancements you'd like to see.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with love for learning and teaching programming.
- Special thanks to the open-source community for the invaluable libraries and tools that made this project possible.
