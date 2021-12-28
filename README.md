# UI Automation Courses
Testing scope:
1. Search for an existing course, check that the titles of the found courses contain the searched data
2. Search for a non-existing course, check that the “No Result Found” message is visible

Test Data:
1. cred.json
    * user_name
        1. test_email
        2. test_pass
        3. test_remember_checkbox
2. testdata\testdata.py
    * url - Application for testing
    * words_for_search - Courses keywords for search during testing
    * user_names - Users which used during testing
    * first_name and last_name - Necessary for registration cases

Tests:
1. tests\test_file.py
    * test_main(get_driver, config_name, user_name)
        1. config_name necessary for 'check_result_case()'
        2. user_name necessary for 'login()' and 'registration()'
      1. For correct work of 'registration()' case, comment @pytest.mark.parametrize("config_name"...
      Because of registration process must be single for each user.
      2. 'Login()' and 'Registration()' can't work together.

    * test_no_result_case(get_driver, user_name)
        1. user_name necessary for 'login()'
    
    'non_exist_case()' case keep unchangeable text for search non-exist course ('NON_EXISTING_COURSE_NAME')

Pages:
1. pages\login_page.py
    * login(get_driver, user)
    Load credentials from 'cred.json', fill the required fields and click 'Sign In'
    There are 2 asserts for errors:
         1. For Invalid email or password
         2. For Unsuccessful login (the page hasn't changed)
    Allure is present.
2. pages\main_page.py
    * find_page_elements(get_driver)
    Check the page for courses and save it to the list, then return it
    * check_result_case(get_driver, config_name)
    Search keyword (config_name) in course title, change pages if exist more than one
    There are one assert:
        1. For Keyword not in a course title
    * search_course(get_driver, text)
    Search course name by (text)
    Allure is present.
3. pages\registration_page.py
    * registration(get_driver, user)
    Load credentials from 'cred.json' and 'testdata\testdata.py', fill the required fields and click 'Sign Up'
    There are 3 asserts for errors:
        1. For Already taken email
        2. For Invalid format email
        3. For Unsuccessful register (the page hasn't changed)
   Allure is present.
4. pages\search_page.py
    * non_exist_case(get_driver)
    Search for non-exist course by entering unchangeable text ('NON_EXISTING_COURSE_NAME')

Libs:
1. libs\basic.py
    Keep the basic commands for launch tests and better interacting with ui elements

Requirements:
    * pytest
    * allure
    * selenium
    * json

Comments:
    You can mash up registration/login functionality with main scope functions like check_result_case and non_exist_case
    Create new users and add new words_for_search for extending negative and positive test results.

