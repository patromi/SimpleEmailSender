# Simple Email Sender

**Simple Email Sender** is a tool for automatically sending emails based on data from a CSV file. This script is created for the AKAI group.

## Requirements


Install the required libraries with:

```bash
pip install -r req.txt
```

**Configuration**

Environment Variables
Set up a .env file in the project root directory with the following variables:


LOGIN=your_email@example.com         # Your email for SMTP login 

PASSWORD=your_password               # Your email password

SUBJECT=Email Subject                # Subject line for emails

CSV_PATH=path/to/input.csv           # Path to the input recrutation CSV file

MODE=template | custom_template      # Template for default csv recrutation file or custom for custom mail body without csv file

TEMPLATE_PATH==path/to/template.html # Path to the custom template file

