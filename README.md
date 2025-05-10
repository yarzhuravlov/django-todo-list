# django-todo-list
## Overview

This is a simple Django-based To-Do List application that allows users to manage their tasks efficiently. Users can create, update, delete, and mark tasks as completed.

## Features

- Add new tasks with a title and description.
- Mark tasks as completed or pending.
- Edit existing tasks.
- Delete tasks.
- Assign tags to tasks for better organization.
- Manage tags through the user interface, including adding, editing, and deleting tags.
- Tags can be reused across multiple tasks for consistency.

## Installation

1. Clone the repository:
  ```bash
  git clone https://github.com/your-username/django-todo-list.git
  cd django-todo-list
  ```

2. Create and activate a virtual environment:
  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
  ```

3. Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

4. Apply migrations:
  ```bash
  python manage.py migrate
  ```

5. Run the development server:
  ```bash
  python manage.py runserver
  ```

6. Open your browser and navigate to `http://127.0.0.1:8000`.

## Loading Initial Data

You can preload the application with initial data using Django's `loaddata` command. This is useful for setting up default tasks or testing data.

1. Create a fixture file in JSON or YAML format and place it in the `fixtures` directory of your app (e.g., `app_name/fixtures/initial_data.json`).

2. Load the data into the database:
  ```bash
  python manage.py loaddata initial_data
  ```

3. Verify that the data has been loaded by checking the application or querying the database.

For more details, refer to the [Django documentation on fixtures](https://docs.djangoproject.com/en/stable/howto/initial-data/).

## Usage

1. Navigate to the homepage to view your task list.
2. Use the "Add Task" button to create a new task.
3. Click on a task to edit or mark it as completed.
4. Use the delete button to remove tasks.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push the branch.
4. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Django documentation: [https://docs.djangoproject.com](https://docs.djangoproject.com)
- Bootstrap for styling: [https://getbootstrap.com](https://getbootstrap.com)
- Inspiration from various to-do list applications.