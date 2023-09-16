import os
import socket
import concurrent.futures
import argparse
import sys
import pyfiglet

# Owner's name and Banner
owner_name = "This tool is developed by Suryesh"
font_name = "slant"
ascii_banner = pyfiglet.figlet_format("Sub enum", font=font_name)
final_banner = f"{ascii_banner}             {owner_name}"
print(final_banner)

# Wordlist file path
wordlist_path = "words.txt"

# Default output directory
DEFAULT_OUTPUT_DIRECTORY = "Output"

# Default output filename
DEFAULT_OUTPUT_FILE = os.path.join(DEFAULT_OUTPUT_DIRECTORY, "output.txt")

# Ensure the output directory exists
if not os.path.exists(DEFAULT_OUTPUT_DIRECTORY):
    os.makedirs(DEFAULT_OUTPUT_DIRECTORY)

def enumerate_subdomain(subdomain, target_domain, args, verbose=False):
    full_domain = f"{subdomain}.{target_domain}"
    try:
        # Use a custom DNS resolver if specified
        if args.dns:
            ip_address = socket.gethostbyname_ex(full_domain, args.dns)[0]
        else:
            ip_address = socket.gethostbyname(full_domain)

        result = f"{full_domain}"
        if verbose:
            print(result)
        return result
    except socket.gaierror:
        return None  # Subdomain does not exist

# Help section
def display_help():
    print("Usage: python3 subenum.py -u <target_domain>")
    print("Options:")
    print("-h, --help          Show the help message")

# Description section
description_text = f'''Discover and catalog subdomains effortlessly with this powerful Subdomain Enumeration tool.
Whether you're conducting security assessments, gathering information for your web applications,
or simply exploring an online presence, this tool streamlines the process.
Boost your cybersecurity efforts, enhance your reconnaissance tasks, and uncover hidden assets with ease.
'''

# Main function section
def main():
    parser = argparse.ArgumentParser(description=description_text)
    parser.add_argument("-u", "--url", required=True, metavar="", help="Enter the target domain for enumeration")
    parser.add_argument("-o", "--output", metavar="", help="Output file for results")
    parser.add_argument("-t", "--threads", metavar="", dest="threads", type=int, default=2000, help="Number of concurrent threads")
    parser.add_argument("-d", "--dns", metavar="", help="Specify custom DNS server")
    parser.add_argument("-w", "--wildcard", action="store_true", help="Detect wildcard DNS entries")
    parser.add_argument("-v", "--version", action="version", help="Print the Version", version="%(prog)s 1.0")
    parser.add_argument("-V", "--verbose", action="store_true", help="Enable verbose mode")
    args = parser.parse_args()
    target_domain = args.url

    if not os.path.isfile(wordlist_path):
        print(f"Error: Wordlist file '{wordlist_path}' not found.")
        sys.exit(1)

    # Determine the output file path
    if args.output:
        output_file_path = args.output
    else:
        # Use the default output file path
        output_file_path = DEFAULT_OUTPUT_FILE

    with concurrent.futures.ThreadPoolExecutor(max_workers=args.threads) as executor:
        with open(wordlist_path, 'r') as wordlist_file:
            subdomains = wordlist_file.read().splitlines()
        results = executor.map(lambda subdomain: enumerate_subdomain(subdomain, target_domain, args, args.verbose), subdomains)

        # Output results to the specified or default output file
        with open(output_file_path, 'w') as out_file:
            for result in results:
                if result:
                    out_file.write(result + '\n')
                    # Print the result to the terminal
                    print(result)

if __name__ == "__main__":
    main()
