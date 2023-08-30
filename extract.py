import time
print(" ____        ____")
print("|  _ \__  __/ ___| _ __   ___ _ __")
print("| | | \ \/ /\___ \| '_ \ / _ \ '__|")
print("| |_| |>  <  ___) | |_) |  __/ |")
print("|____//_/\_\|____/| .__/ \___|_|")
print("                  |_|")

print("\nWelcome to Extractor \nThis program filters email:pass from DB \n")

def filter_emails(input_file, output_file, search_config, split_config):
    configsplit = ""
    with open(split_config, 'r') as f:
        lines = f.readlines()
    for lines in lines:
        configsplit = lines

    search_entries = []
    config = ""
    with open(search_config, 'r') as f:
        lines = f.readlines()
    for line in lines:
        search_entries.append(line.strip())
    for entries in search_entries:
        config += "\n"
        config += entries
    print('Your config is:','\n\nSearch:', config,"\n\nSplit -> ", configsplit)
    print('\nIndexing...')
    fr_emails = []

    start_time = time.time()

    with open(input_file, 'r') as f:
        lines = f.readlines()

    total_emails = len(lines)
    
    for index, line in enumerate(lines, 1):
        parts = line.strip().split(configsplit)
        email = parts[0]
        for entry in search_entries:
            if email.endswith(entry):
                fr_emails.append(line)

            
            if index % 1000 == 0:
                elapsed_time = time.time() - start_time
                emails_per_second = index / elapsed_time
                emails_per_minute = emails_per_second * 60
                progress_message = (
                    f"Progress: {index}/{total_emails} - "
                    f"Emails/second: {emails_per_second:.2f} - "
                    f"Emails/minute: {emails_per_minute:.2f}"
                )
                print(f"\r{progress_message}", end='', flush=True)

    with open(output_file, 'w') as f:
        for email in fr_emails:
            f.write(email)  

    end_time = time.time()  
    elapsed_time = end_time - start_time  

    print(f"\nFiltering was completed in {elapsed_time:.4f} seconds.")


input_file = 'db_input.txt'
output_file = 'db_extracted.txt'
search_config = 'search_config.txt'
split_config = 'split_config.txt'
filter_emails(input_file, output_file, search_config, split_config)
