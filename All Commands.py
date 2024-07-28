from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.get("URL") //get the url
driver.title //to get the tiltle of the page
driver.current_url  //current url of the current webpage
length = len(count) // length of the element
driver.maximize_window()
src = driver.page_source //pagesource

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver.implicitly_wait(5) // Implict wait
wait = WebDriverWait(driver,5) // Explicit wait
element = wait.until(EC.element_to_be_clickable(By.XPATH,"Path of it"))
element.click()
element = wait.until(EC.presence_of_element_located(By.XPATH,"Path of it"))
element.click()

driver.find_element(By.ID,"Id Value") // submit the text contents
driver.find_element(By.NAME,"Name of it") //to find the element with name and clear the name of it
driver.find_element(By.CSS_SELECTOR,"Value").text //to get the text from the element using css selector
driver.find_element(By.CLASS_NAME,"Name of class").click() // click the button or checkbox using class name of the element
driver.find_element(By.TAG_NAME,"p") //locates the element using html tag
driver.find_element(By.LINK_TEXT,"text of the link").click() // locates a link using the link text
driver.find_element(By.PARTIAL_LINK_TEXT,"some text of the link") //locates a some text of the link using the Partial link text 
driver.find_element(By.XPATH,"//input[@id='txtSearchText']").get_attribute('value') //locates an element using xpath query

driver.find_element(By.ID,"Id Value").send_keys("test") //method is used to input text in an edit box,text area,fields. 
driver.find_element(By.NAME,"Name of it").clear() //method is used to clear the text from an editbox,text area.
driver.find_element(By.CSS_SELECTOR,"Value").value_of_css_selector("color") //method is used to get the value of css property
driver.find_element(By.CLASS_NAME,"Name of class").click() //method is used to click on a link,button.
driver.find_element(By.LINK_TEXT,"text of the link").text //method is used to get the text displayed of an element
driver.find_element(By.TAG_NAME,"p").submit() //method is used with any element within the form
driver.find_element(By.XPATH,"//input[@id='txtSearchText']").get_attribute('value') //method is used to get the attribute value /property value of an element.
element = driver.find_element(By.ID,"ID Value").send_keys("text/value") //to find the element with ID and send the value into it
element = element.size // to get the size of this element
element = element.is_displayed() // check element/page is displayed or not
element = element.is_enabled() // check the textfield/checkbox is enabled or not
element = element.is_selected() // check the field/button is selected or not
element = element.location // cmnd to get the location of the element in form of X and Y coordinates
element = element.tag_name //cmnd to gives the tag used in particular element and returns its string value

driver.refresh() // referesh/reload the webpage 
driver.back() // navigate the browsing page backward
driver.forward() // navigate the browsing page forward/next page

driver.switch_to.window("window name") // move to the window which we need
driver.switch_to.frame(name/id/index) // move from one frame to another frame using name/id/index_number
driver.switch_to.default_content() //switch to homepage

drp = Select(driver.find_element(By.ID,"ID name")) // by using Select class we can handle the Drop down 
drp.select_by_visible_text("visible text")
drp.select_by_value("value")
drp.select_by_index("index number")

src = driver.find_element(By.ID,"SRC Value") //using actionchains we can drag and drop the elements
tgt = driver.find_element(By.ID,"TGT Value")
action = ActionChains(driver)
action.drag_and_drop(src,tgt).perform()

from selenium.webdriver.common.alert import Alert
driver.window_handles[1] //handles popup window 
driver.switch_to.window("window name") // move to the window which we need
driver.switch_to.alert.accept() // closes the alert window after clicking OK
driver.switch_to.alert.dismiss() // closes the alert window after clicking Cancel

driver.close()
driver.quit()

