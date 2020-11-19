# QAautomationTest
Repo consisting of 5 automated tests that verify the proper functionality of the Login page from PrinterLogic

## Getting It Running

You will need

- Python 3.8
- ChromeDriver 86.0.4240.22
- selenium 3.141.0
- html-testRunner 1.2.1
- remember to get the **secrets.py** content from creator

### 1. Run the tests

Main testing archive is **login.py**, and starting from "Project" directory type:
  ```sh
  python login.py
  ```

### 2. Test descriptions

  #### Test 01: valid login
  This test checks if the input given for the login page is correct and gives access to the home page. Furthermore, checks if the title of the personal menu contains the username. Finally, the test performs a logout from the page.
  #### Test 02: invalid login
  Verifies that the user cannot enter the home page with an erroneous password, and does it by waiting for a unique homepage web-element to appear.  
  #### Test 03: empty login
  Without any information given, the login attempt must display a unique message that this test asserts and confirms its functionality.
  #### Test 04: forgot password access
  Simply verifies that the "forgot password" button takes you to the corresponding site and verifies that the name coincides with that of the option.
  #### Test 05: privacy policy link
  Checks the functionality of the privacy policy link by assessing the number of handles after the option is selected. This tests limits just to check that the link is working as intended. 
