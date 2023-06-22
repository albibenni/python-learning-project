def decorator_function(original_function):
    def modified_function(*args, **kwargs):
        # Add extra functionality before invoking the original function
        print("Decorator added some functionality")
        result = original_function(*args, **kwargs)  # Invoke the original function
        # Add extra functionality after invoking the original function
        return result

    return modified_function


@decorator_function
def my_function():
    print("Original function")


my_function()
