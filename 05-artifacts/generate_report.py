def generate_report() -> None:
    """Creates a file called report.txt with some text in it."""
    try:
        with open("report.txt", "w") as f:
            f.write("This is a generated report row 1.\nThis is a generated report row 2.\n")
    except:
        print("Failed to generate report.")
        return
    
    print("Report generated.")


if __name__ == "__main__":
    generate_report()
