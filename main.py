# To do app R Projects
import flet as ft
import pickle
import os

def main(page: ft.Page):
    # Path to the file where tasks will be saved
    tasks_file = "tasks.pkl"

    # Function to load tasks from the file
    def load_tasks():
        if os.path.exists(tasks_file):
            with open(tasks_file, "rb") as file:
                return pickle.load(file)
        return []

    # Function to save tasks to the file
    def save_tasks():
        with open(tasks_file, "wb") as file:
            pickle.dump([checkbox.label for checkbox in tasks_view.controls], file)

    def add_clicked(e):
        if new_task.value.strip():  # Check if the text field is not empty
            tasks_view.controls.append(ft.Checkbox(label=new_task.value))
            new_task.value = ""
            save_tasks()  # Save tasks to the file
            page.update()  # Refresh the page to show the new task

    new_task = ft.TextField(hint_text="What's needs to be done?", expand=True)
    tasks_view = ft.Column()

    # Load the existing tasks and add them to the tasks_view
    for task in load_tasks():
        tasks_view.controls.append(ft.Checkbox(label=task))

    view = ft.Column(width=600, controls=[
        ft.Row(controls=[new_task,
                        ft.FloatingActionButton(icon=ft.icons.ADD, on_click=add_clicked),],),
        tasks_view,
    ])

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(view)

# Run the app with the main function
ft.app(target=main, view=ft.WEB_BROWSER)
