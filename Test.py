from selenium import webdriver

# Set the path to the ChromeDriver executable (change this path to the location of your ChromeDriver)
driver_path = "path/to/chromedriver"

# Create a Chrome driver instance
driver = webdriver.Chrome(executable_path=driver_path)

# Navigate to Amazon.com
driver.get("https://www.amazon.com/")

# Close the browser
driver.quit()
