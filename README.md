# Placement-Management-System

The Placement Management System (PMS) is a web application designed to streamline the process of managing candidate details and placement confirmations. Candidates can register for the placement drive by using their credentials and verifying the information displayed in the webpage. It also allows employers to enter a unique User ID and a corresponding company code to view detailed user information fetched from backend files. Employers can then confirm placement details, including role and package type, which are stored and managed in a results file. The application provides a user-friendly interface for both viewing candidate details and confirming placements, enhancing efficiency in placement management tasks.


## Prerequisites

List any prerequisites or dependencies needed to run your project. Include instructions for installing them if necessary.

- Python 3.x
- Flask
- Pandas

## Installation

Guide users through installing your project locally. Provide step-by-step instructions.

1. Clone the repository:
   ```
   git clone https://github.com/Pradeesh-Saravanan/Placement-Management-System.git
   cd Placement-Management-System
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up CSV files:
   - Ensure files needed are placed in the project directory.

## Usage

Explain how to use your application. Include details on how to run the Flask server and navigate the application.

1. Start the Flask server:
   ```
   python app.py
   ```

2. Open a web browser and go to `http://localhost:5000/` to access the application.

3. Enter a valid `User ID` and `Code` to view user details and confirm placement.

## Project Structure

Explain the structure of your project's directory and important files.

```
Registration/
│
├── app.py               # Main Flask application file
├── Engineering.csv      # CSV file containing user details
├── static/              # Directory for static assets (CSS, JS)
│   └── styles.css       # Stylesheet for HTML templates
├── templates/           # Directory for HTML templates
│   ├── index.html       # Template for entering User ID and Code
│   ├── details.html     # Template for displaying user details and inputting placement details
│   └── thank.html       # Template for displaying a thank you message
└── results.csv          # CSV file to store placement confirmation details
```
```
Recruitment/
│
├── app.py               # Main Flask application file
├── Engineering.csv      # CSV file containing user details
├── Empolyer_preprocessed.csv  # CSV file containing company details
├── static/              # Directory for static assets (CSS, JS)
│   └── styles.css       # Stylesheet for HTML templates
├── templates/           # Directory for HTML templates
│   ├── index.html       # Template for entering User ID and Code
│   ├── details.html     # Template for displaying user details and inputting placement details
│   └── thank.html       # Template for displaying a thank you message
└── results.csv          # CSV file to store placement confirmation details
```

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests for any enhancements, bug fixes, or new features.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or feedback, please contact [Pradeesh Saravanan](mailto:pradeeshpradeesh7040@gmail.com).
