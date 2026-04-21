from scan.scanner import scan_folder
from database.operations import (
    get_largest_files,
    get_file_types,
    total_size,
    search_file,
    clear_table
)
from convert.cnvrt import format_size
from convert.chart import show_pie_chart


def menu():
    while True:
        print("\n Disk Analyzer Menu")
        print("1. Scan Folder")
        print("2. Show Largest Files")
        print("3. Show File Types")
        print("4. Search File") 
        print("5. Total Size")
        print("6. Clear Database")
        print("7. Show Chart")
        print("8. Exit")

        choice = input("Enter choice ")

        if choice == "1":
            path = input("Enter folder path ")
            scan_folder(path)

        elif choice == "2":
            files = get_largest_files()
            if files:
                for name, size in files:
                    print(f"{name} -> {format_size(size)}")
            else:
                print("No data found, Please scan first.")

        elif choice == "3":
            types = get_file_types()
            for t, count in types:
                print(f"{t} -> {count} files")

        elif choice == "4":
            name = input("Enter file name ")
            results = search_file(name)

            if results:
                for file_name, path in results:
                    print(f"{file_name} -> {path}")
            else:
                print("No matching files found")

        elif choice == "5":
            size = total_size()
            print(f"Total Size----{format_size(size)}")

        elif choice == "6":
            confirm = input("Are you sure you want to clear database?(y/n)")
            if confirm.lower() == "y":
                clear_table()
                print("Database cleared")
            else:
                print("Cancelled")

        elif choice == "7":
            data = get_file_types()
            show_pie_chart(data)
            
        elif choice == "8":
            print("Exiting")
            break

        else:
            print("Invalid choice,Try again")


if __name__ == "__main__":
    menu()