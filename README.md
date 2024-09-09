# To-Do-app
This is a simple To-Do application built with Flet, a Python framework for building interactive web, mobile, and desktop apps. The app allows users to add tasks, view them in a list, and keep track of what's completed. Tasks are saved using Python's pickle module, ensuring that your task list is persistent between sessions.

Features
Add Tasks: Easily add new tasks with a text input field and a floating action button.
Task Persistence: Tasks are saved locally in a file (tasks.pkl), so you won't lose your list when you close the app.
Task Management: Tasks are displayed as checkboxes, allowing you to keep track of completed and pending tasks.
Responsive Design: The app is designed to run in a web browser, providing a responsive and user-friendly interface.
Installation
Clone the Repository:

bash
Kodu kopyala
git clone https://github.com/yourusername/todo-app.git
cd todo-app
Install Dependencies: Make sure you have Python installed, then install Flet using pip:

bash
Kodu kopyala
pip install flet
Run the App: Start the app by running:

bash
Kodu kopyala
python main.py
Usage
Start the app using the steps above.
Use the text input to enter the name of a task and click the + button to add it to your list.
Your tasks will be saved automatically, so you can resume where you left off next time you run the app.
File Structure
main.py: The main file that contains the app's code.
tasks.pkl: A file where tasks are saved using the pickle module.
Contributing
If you'd like to contribute to this project, feel free to fork the repository and submit a pull request with your improvements.

License
This project is open-source and available under the MIT License.

