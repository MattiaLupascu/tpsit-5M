# Ajax Name Filter

This project is a simple Flask application that demonstrates how to use AJAX to filter a list of names based on user input.

## Project Structure

```
Ajax
├── app.py                # Main Flask application
├── static
│   └── js
│       └── script.js     # JavaScript for handling AJAX requests
├── templates
│   └── index.html        # HTML template with input and display elements
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## Setup Instructions

1. **Clone the repository** or download the project files.

2. **Navigate to the project directory**:
   ```
   cd Ajax
   ```

3. **Create a virtual environment** (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. **Install the required dependencies**:
   ```
   pip install -r requirements.txt
   ```

5. **Run the Flask application**:
   ```
   python app.py
   ```

6. **Open your web browser** and go to `http://127.0.0.1:5000` to access the application.

## Usage

- Enter letters of a first name in the textbox.
- The list of names will be filtered and displayed in real-time below the textbox based on your input.

## License

This project is open-source and available under the MIT License.