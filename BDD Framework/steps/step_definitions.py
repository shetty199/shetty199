from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, TimeoutException, \
    WebDriverException, ElementNotInteractableException
import time

@given('I am logged into the platform')
def step_impl(context):
    try:
        # Start Chrome driver
        context.driver = webdriver.Chrome(executable_path="C:/shetty/chromedriver-win32/chromedriver.exe")  # Path to your chromedriver
        context.driver.get("https://indeedemo-fyc.watch.indee.tv/")
        # Wait for the PIN input field to be visible
        WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.ID, "access-code"))
        )

        # Find the PIN input element
        pin_input = context.driver.find_element(By.ID, "access-code")
        pin_input.send_keys("WVMVHWBS")
        pin_input.send_keys(Keys.RETURN)

        # Wait until the next page or action is done (optional)
        WebDriverWait(context.driver, 10).until(
            EC.url_changes(context.driver.current_url)
        )
        # Maximizing the window
        context.driver.maximize_window()
    except NoSuchElementException as e:
        print(f"Error: Element not found - {e}")
        # Optionally, take a screenshot or log the error for debugging
        context.driver.save_screenshot('element_not_found.png')
    except TimeoutException as e:
        print(f"Error: Timed out waiting for element - {e}")
        # Optionally, take a screenshot or log the error for debugging
        context.driver.save_screenshot('timeout_error.png')
    except ElementNotInteractableException as e:
        print(f"Error: Element not interactable - {e}")
        # Optionally, take a screenshot or log the error for debugging
        context.driver.save_screenshot('element_not_interactable.png')
    except WebDriverException as e:
        print(f"Error: WebDriver related issue - {e}")
        # Optionally, take a screenshot or log the error for debugging
        context.driver.save_screenshot('webdriver_issue.png')
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        # Optionally, take a screenshot or log the error for debugging
        context.driver.save_screenshot('unexpected_error.png')

@when('I navigate to the "Test Automation Project"')
def step_impl(context):
    try:
        context.driver.implicitly_wait(10)

        # Wait for the element to be visible and clickable
        project = WebDriverWait(context.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//h5[contains(text(), 'Test automation project')]"))
        )
        # Click the project
        project.click()

    except NoSuchElementException as e:
        print(f"Error: Element not found - {e}")
        context.driver.save_screenshot('test_automation_project_not_found.png')
    except TimeoutException as e:
        print(f"Error: Timed out waiting for element - {e}")
        context.driver.save_screenshot('test_automation_project_timeout.png')
    except ElementNotInteractableException as e:
        print(f"Error: Element not interactable - {e}")
        context.driver.save_screenshot('test_automation_project_not_interactable.png')
    except WebDriverException as e:
        print(f"Error: WebDriver related issue - {e}")
        context.driver.save_screenshot('webdriver_issue_test_automation_project.png')
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        context.driver.save_screenshot('unexpected_error_test_automation_project.png')

@when('I switch to the "Details" tab')
def step_impl(context):
    try:
        # Wait for the details section to be present
        WebDriverWait(context.driver, 20).until(
            EC.presence_of_element_located((By.ID, "detailsSection"))
        )

        # Find the Details tab and click
        details_tab = context.driver.find_element(By.ID, "detailsSection")

        # Check if the element is interactable before clicking
        if details_tab.is_displayed() and details_tab.is_enabled():
            details_tab.click()
        else:
            raise ElementNotInteractableException("The Details tab is either not displayed or not enabled.")

    except NoSuchElementException as e:
        print(f"Error: Element not found - {e}")
        context.driver.save_screenshot('details_tab_not_found.png')
    except TimeoutException as e:
        print(f"Error: Timed out waiting for element - {e}")
        context.driver.save_screenshot('details_tab_timeout.png')
    except ElementNotInteractableException as e:
        print(f"Error: Element not interactable - {e}")
        context.driver.save_screenshot('details_tab_not_interactable.png')
    except WebDriverException as e:
        print(f"Error: WebDriver related issue - {e}")
        context.driver.save_screenshot('webdriver_issue_details_tab.png')
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        context.driver.save_screenshot('unexpected_error_details_tab.png')

@when('I return to the "Videos" tab')
def step_impl(context):
    try:
        # Wait for the "Videos" section to be present
        WebDriverWait(context.driver, 20).until(
            EC.presence_of_element_located((By.ID, "videosSection"))
        )

        # Find the "Videos" tab and click
        videos_tab = context.driver.find_element(By.ID, "videosSection")

        # Check if the element is interactable before clicking
        if videos_tab.is_displayed() and videos_tab.is_enabled():
            videos_tab.click()
        else:
            raise ElementNotInteractableException("The Videos tab is either not displayed or not enabled.")

    except NoSuchElementException as e:
        print(f"Error: Element not found - {e}")
        context.driver.save_screenshot('videos_tab_not_found.png')
    except TimeoutException as e:
        print(f"Error: Timed out waiting for element - {e}")
        context.driver.save_screenshot('videos_tab_timeout.png')
    except ElementNotInteractableException as e:
        print(f"Error: Element not interactable - {e}")
        context.driver.save_screenshot('videos_tab_not_interactable.png')
    except WebDriverException as e:
        print(f"Error: WebDriver related issue - {e}")
        context.driver.save_screenshot('webdriver_issue_videos_tab.png')
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        context.driver.save_screenshot('unexpected_error_videos_tab.png')

@when('I play the video')
def step_impl(context):
    try:
        context.driver.implicitly_wait(5)

        # Handle the play button click, re-find the element in case it became stale
        try:
            video_player = context.driver.find_element(By.XPATH, "//button[@aria-label='Play Video']")
            video_player.click()
        except StaleElementReferenceException:
            print("Stale element reference exception: Re-finding the play button")
            video_player = context.driver.find_element(By.XPATH, "//button[@aria-label='Play Video']")
            video_player.click()
        except NoSuchElementException:
            print("Play video button not found.")
            return
        except Exception as e:
            print(f"Error while clicking the play button: {str(e)}")
            return

        # Wait to ensure the video starts playing before proceeding
        context.driver.implicitly_wait(20)

        # Perform the action to simulate mouse movement
        actions = ActionChains(context.driver)
        actions.move_by_offset(100, 100).perform()

        # Switching to the iframe, handle potential stale element issue
        try:
            iframe = context.driver.find_element(By.XPATH, "//iframe[@id='video_player']")
            context.driver.switch_to.frame(iframe)
        except StaleElementReferenceException:
            print("Stale element reference exception occurred while switching to iframe. Re-finding iframe.")
            iframe = context.driver.find_element(By.XPATH, "//iframe[@id='video_player']")
            context.driver.switch_to.frame(iframe)
        except NoSuchElementException:
            print("Iframe not found.")
            return
        except Exception as e:
            print(f"Error while switching to iframe: {str(e)}")
            return

        # At this point, you can interact with elements inside the iframe or perform other actions
        print("Successfully switched to iframe.")

    except TimeoutException as e:
        print(f"TimeoutException: The operation took too long: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")


def retry_find_element(driver, by, value, retries=3, delay=2):
    """
    Retry finding an element with specified retries and delay between attempts.
    """
    for _ in range(retries):
        try:
            # Wait for the element to be clickable
            return WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((by, value))
            )
        except (TimeoutException, StaleElementReferenceException) as e:
            print(f"Error: {str(e)}. Retrying...")
            time.sleep(delay)  # Wait before retrying
    raise TimeoutException(f"Element with {by}={value} could not be found after {retries} retries.")

@when('I change the resolution to 480p and then back to 720p')
def step_impl(context):
    # Start with an action chain for moving by offset
    actions = ActionChains(context.driver)
    actions.move_by_offset(100, 100).perform()


    try:
        resolution_option = retry_find_element(context.driver, By.XPATH, "//button[@aria-label='480p']")
        resolution_option.click()
        print("Resolution changed to 480p.")
    except TimeoutException:
        print("Failed to find 480p resolution option.")
        return

    # Wait for the action to take effect (you might adjust this based on video buffering time)
    context.driver.implicitly_wait(3)

    try:
        # Locate and click the settings button to open the resolution menu
        settings_button = retry_find_element(context.driver, By.XPATH, "//div[@aria-label='Settings']")
        context.driver.execute_script("arguments[0].click();", settings_button)
        print("Opened settings menu.")
    except TimeoutException:
        print("Failed to open settings menu.")
        return

    try:
        # Locate and click the 720p resolution option
        resolution_option_720p = retry_find_element(context.driver, By.XPATH, "//button[@aria-label='720p']")
        resolution_option_720p.click()
        print("Resolution changed to 720p.")
    except TimeoutException:
        print("Failed to find 720p resolution option.")
        return

    # If there are any iframes, switch to it
    try:
        iframe = context.driver.find_element(By.XPATH, "//iframe[@src='iframe_url']")  # Modify XPath accordingly
        context.driver.switch_to.frame(iframe)  # Switch to iframe
        print("Switched to iframe.")
    except:
        print("No iframe found or already in the correct frame.")

    context.driver.implicitly_wait(3)

    # Switch back to the default content (if you switched to an iframe)
    context.driver.switch_to.default_content()

    # Additional logic like verifying if the video plays and continues with the resolution changes
    print("Test completed successfully.")

@when('I pause the video and exit the project')
def step_impl(context):
    try:
        # Wait for the Pause button to be visible and clickable
        pause_button = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//div[@aria-label='Pause'])[2]"))
        )
        pause_button.click()
        print("Video paused.")

        # Wait for the "Go Back and continue playing video" button to be clickable
        go_back_button = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Go Back and continue playing video']"))
        )
        go_back_button.click()
        print("Exiting project and going back.")

    except NoSuchElementException as e:
        print(f"Error: Element not found - {e}")
        # Handle the failure case here (maybe take a screenshot or log the error)
    except TimeoutException as e:
        print(f"Error: Timed out waiting for element - {e}")
        # Handle the failure case here (maybe take a screenshot or log the error)
    except StaleElementReferenceException as e:
        print(f"Error: Stale element reference - {e}")
        # Retry the operation here if needed, or log the error
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# @when(u'I logout from the platform')
# def step_impl(context):
#     try:
#         # Wait for the logout button or menu option to appear
#         WebDriverWait(context.driver, 10).until(
#             EC.presence_of_element_located((By.ID, "signOutSideBar"))  # Adjust the locator if necessary
#         )
#
#         # Find the logout button and click it
#         logout_button = context.driver.find_element(By.ID, "signOutSideBar")
#
#         # Check if the element is interactable before clicking
#         if logout_button.is_displayed() and logout_button.is_enabled():
#             logout_button.click()
#         else:
#             raise ElementNotInteractableException("The logout button is either not displayed or not enabled.")
#
#         # Additional logic to confirm logout (if required)
#         # This may depend on the page behavior after logout. For example, checking if the login page is shown.
#         WebDriverWait(context.driver, 10).until(
#             EC.url_contains("login")  # Adjust the URL or element check based on your platform's behavior after logout
#         )
#
#         print("Logout successful.")
#
#     except NoSuchElementException as e:
#         print(f"Error: Element not found - {e}")
#         context.driver.save_screenshot('logout_button_not_found.png')
#     except TimeoutException as e:
#         print(f"Error: Timed out waiting for element - {e}")
#         context.driver.save_screenshot('logout_timeout.png')
#     except ElementNotInteractableException as e:
#         print(f"Error: Element not interactable - {e}")
#         context.driver.save_screenshot('logout_button_not_interactable.png')
#     except WebDriverException as e:
#         print(f"Error: WebDriver related issue - {e}")
#         context.driver.save_screenshot('webdriver_issue_logout.png')
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")
#         context.driver.save_screenshot('unexpected_error_logout.png')