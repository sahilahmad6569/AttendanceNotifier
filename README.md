# Daily Attendance Notifier

This project automates the process of checking and reporting daily attendance using web scraping and email notifications. The script logs into a specified attendance portal, retrieves the attendance data, and sends a summary via email.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Workflow](#workflow)
- [Contributing](#contributing)
- [License](#license)

## Features

- Automatically logs into the attendance portal.
- Scrapes attendance data.
- Sends daily attendance reports via email.
- Supports headless operation for background execution.

## Technologies Used

- **Python 3.12.3**: The programming language used for the script.
- **Selenium**: For web scraping and browser automation.
- **BeautifulSoup**: For parsing HTML and XML documents.
- **SMTP**: For sending email notifications.
- **GitHub Actions**: For automating the attendance check workflow.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/sahilahmad6569/AttendanceNotifier.git
   cd AttendanceNotifier
   ```

2. Set up a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

To run the project, you need to set up several environment variables. Create a `.env` file in the root directory with the following variables:

```env
USERNAME=your_username
PASSWORD=your_password
URL=https://your_attendance_portal.com/login
ATTENDANCE_URL=https://your_attendance_portal.com/attendance
SMTP_SERVER=smtp.your_email_provider.com
SMTP_PORT=587
SENDER_EMAIL=your_email@example.com
SENDER_PASSWORD=your_email_password
RECEIVER_EMAIL=receiver_email@example.com
SUBJECT="Daily Attendance Report"
```

Make sure to replace the placeholders with your actual information.

## Usage

1. **Run the script manually**:

   ```bash
   python main.py
   ```

2. **Automate with GitHub Actions**: This project includes a GitHub Actions workflow that runs the attendance script daily at 6 PM UTC. You can manually trigger it through the GitHub Actions interface.

## Workflow

The GitHub Actions workflow is defined in `.github/workflows/main.yml`. It performs the following steps:

1. Checks out the code from the repository.
2. Sets up the Python environment.
3. Installs required dependencies.
4. Executes the `main.py` script with the configured environment variables.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have suggestions or find bugs.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---