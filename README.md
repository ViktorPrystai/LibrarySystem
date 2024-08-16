## Installation

1. Clone repo

```bash
git clone https://github.com/ViktorPrystai/LibrarySystem.git librarysys
```

2. Move into library directory

```bash
cd librarysys
```

3. Create python virtual environment in librarysys directory

```bash
python -m venv .env
```

4. Activating python virtual environment

    - For Windows

    ```pwsh
    .\.env\Scripts\activate
    ```
    - For Unix-like (Mac OS, Linux, BSD)
    ```bash
    source .env/bin/activate
    ```

    In order to deactivate python virtual environment

    ```bash
    deactivate
    ```

5. Install requirements for the project

```bash
pip install -r requirements.txt
```

## Run project

1. Go to the library folder with manage.py
```bash
cd library
```

2. Run migrations

```bash
python manage.py migrate
```

3. Start the local server

```bash
python manage.py runserver
```
