

# try:
#     result = 10 / 0  # This will raise a ZeroDivisionError
# except:
#     print("An error occurred!")


# try:
#     result = 10 / 2  
#     print(result)
# except:
#     print("An error occurred!")


# try:
#     result = 10 / 0  # This will raise a ZeroDivisionError

# except ZeroDivisionError:
#     print("Cannot Divide by Zero")

# except:
#     print("An error occurred!")



# try:
#     result = "10" / 2  # This will raise a TypeError

# except ZeroDivisionError:
#     print("Cannot Divide by Zero")

# except TypeError:
#     print("Type Error: Cannot Add a String and An Integer")

# except:
#     print("An error occurred!")


# try:
#     result = 10 / 2
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# else:
#     print(f"Division successful. Result: {result}")


# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# finally:
#     print("This will always execute.")

# try:
#     result = 10 / 2
# except ZeroDivisionError:
#     print("Cannot divide by zero!")

# else:
#     print(f"Division successful. Result: {result}")

# finally:
#     print("This will always execute.")



# def divide_numbers(a, b):
#     try:
#         result = a / b  # Test this block for errors
#     except ZeroDivisionError:
#         print("Error: Cannot divide by zero!")
#     except TypeError:
#         print("Error: Invalid input type. Numbers required.")
#     else:
#         print(f"Division successful. Result: {result}")
#     finally:
#         print("Operation complete.\n")

# # Test cases
# divide_numbers(10, 2)  # Successful division
# divide_numbers(10, 0)  # ZeroDivisionError
# divide_numbers(10, "2")  # TypeError


try:
    # result = "10" / 2 
    # print(result)
    raise ValueError("This is a custom error message.")

# except ZeroDivisionError:
#     print("Cannot Divide by Zero")

# except TypeError:
#     print("Type Error: Cannot Add a String and An Integer")

except Exception as e:
    print("An error occurred!")
    print("Error Details: ", str(e))