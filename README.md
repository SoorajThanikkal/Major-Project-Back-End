# Major-Project-Back-End

This repository contains the backend server for the Major Project. It is built using Django Rest Framework for creating RESTful APIs.

## Getting Started

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/your-username/Major-Project-Back-End.git
    ```

2. **Set Up Virtual Environment (Optional):**
    ```bash
    cd Major-Project-Back-End
    python -m venv venv
    ```

3. **Activate the Virtual Environment:**
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5. **Apply Initial Migrations:**
    ```bash
    python manage.py migrate
    ```

6. **Run the Development Server:**
    ```bash
    python manage.py runserver
    ```

The server will be running at [http://localhost:8000/](http://localhost:8000/).

## Front-End Development

The front-end for this project is being developed in ReactJS. You can find the repository [here](https://github.com/thamir0022/Major-Project-Front-End). Make sure to follow the setup instructions in the front-end repository to integrate it with this backend.

## Next Steps

- Start building your API endpoints in the `views.py` file.
- Define your data models in the `models.py` file.
- Customize the project settings in the `settings.py` file.

Happy coding!
