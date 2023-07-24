import webbrowser



def open_all_urls(urls):

    for url in urls:

        url = url.strip()

        webbrowser.get("firefox").open(url)



def open_one_by_one(urls):

    for i, url in enumerate(urls):

        url = url.strip()

        input(f"Press Enter to open URL {i+1}: {url}")

        webbrowser.get("firefox").open(url)



if __name__ == "__main__":

    file_path = input("Enter the path of the text file containing URLs: ")



    try:

        with open(file_path, 'r') as file:

            urls = file.readlines()

    except Exception as e:

        print(f"Error: {e}")

        exit(1)



    num_urls = len(urls)

    print(f"{num_urls} URLs found in the file.")



    while True:

        choice = input("Do you want to open all URLs directly (1) or open one by one (2)? Enter '1' or '2': ")

        if choice == '1':

            open_all_urls(urls)

            break

        elif choice == '2':

            open_one_by_one(urls)

            break

        else:

            print("Invalid choice. Please enter '1' or '2'.")



    print("Task completed!")

