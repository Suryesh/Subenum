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

     git clone https://github.com/Suryesh/Subenum.git
2. **Go to Subenum directory:**
   
   cd Subenum
   
3. **Install dependencies:**

     pip install -r requirements.txt
   
4. **Give Executable permision**
   
   chmod +x subenum.py

## Usage

Run the subenum.py  file with target domain and provide output file  path otherwise it will generate output in same directory.

**python subenum.py -u example.com -o /path/output.txt**

or,

**python subenum.py -u example.com -o target.txt**

or,

**python subenum.py -u example.com** 
- This command will save output automatically in same directory

**we can use this tool in windows as well as in all LInux distribution**

## Example Output
 - subdomain1.example.com
 - subdomain2.example.com
 - ...............

## Screenshots

- **Result 1:**
  
  ![Result 1](Screenshots/result1.png)

- **Result 2:**

  ![Result 2](Screenshots/result2.png)

- **Result 3:**

  ![Result 3](Screenshots/result3.png)

- **Result 4:**

  ![Result 3](Screenshots/result4.png)
  
## Contributer's

Thank you to the following contributors for their valuable contributions to this project:

- [Raushan Kumar](https://github.com/eryadav9955)


