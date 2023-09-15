# Subdomain enumeration

## Description

The Subdomain Extractor is a Python-based tool designed to simplify the process of discovering subdomains associated with a target domain. Whether you are a cybersecurity professional, a web developer, or a curious enthusiast, this tool provides an efficient way to enumerate subdomains and gather valuable information about your target.

## Key Features

- **Subdomain Enumeration:**
  Automatically scans and extracts subdomains associated with the target domain.

- **Parallel Processing:**
  Utilizes multi-threading to enhance the speed of subdomain discovery.

- **Custom DNS Resolution:**
  Supports custom DNS server configurations for precise domain resolution.

- **Verbose Mode:**
  Enable verbose output for detailed information about the enumeration process.

- **Threads Mode:**
  Enable threads mode for efficient processing of a large number of subdomains.

- **Wildcard Detection:**
  It has the ability to detect wildcard DNS entries.


## Installation

1. **Clone this repository:**

     git clone https://github.com/yourusername/subdomain-extractor.git
2. **Install dependencies:**

     pip install -r requirements.txt


## Usage

Run the subenum.py  file with target domain and provide output file  path if you'll not provide output path then it will generate output in same directory.

**python subdomain_extractor.py -u example.com -o /path/output.txt**

or,

**python subenum.py -u examole.com -o target.txt**


## Contributing

Explain how others can contribute to your project if it's open-source.
