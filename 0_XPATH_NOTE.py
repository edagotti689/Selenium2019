## What is XPath?
1. XPath is defined as XML path.
2. It is a syntax or language for finding any element on the web page using XML path expression.
3. XPath is used to find the location of any element on a webpage using HTML DOM structure.


## Syntax for XPath:

1. XPath contains the path of the element situated at the web page. 

    # syntax:- Xpath=//tagname[@attributename='value']
    //             ==> Select current node.
    Tagname        ==> Tagname of the particular node.
    @              ==> Select attribute.
    Attributename  ==> Attribute name of the node.
    Value          ==> Value of the attribute


## D/B find element and elements ?

    # FindElement() method
    1. We need to use findElement method frequently in our webdriver software test case because this is the only way to locate any element in webdriver software testing tool.
    2. findElement method is useful to locating targeted single element.
    3. If targeted element is not found on the page then it will throw NoSuchElementException.
    # FindElements() method
    1. We are using findElements method just occasionally.
    2. findElements method will return list of all the matching elements from current page as per given element locator mechanism.
    3. If not found any element on current page as per given element locator mechanism, it will return empty list.

## Types of X-paths
    # Absolute XPath:
    1. It is the direct way to find the element, but the disadvantage of the absolute XPath is that if there are any changes made in the path of the element then that XPath gets failed.

    2. The key characteristic of XPath is that it begins with the single forward slash(/) ,which means you can select the element from the root node.
    # Example:- html/body/div[1]/section/div[1]/div/div/div[3]/div[1]/div/h4[1]/b

    # Relative xpath:
    1. For Relative Xpath the path starts from the middle of the HTML DOM structure. 
    2. It starts with the double forward slash (//), which means it can search the element anywhere at the webpage.
    3. You can start from the middle of the HTML DOM structure and no need to write long xpath.
    # Example:- //*[@class='featured-box']//*[text()='Testing']

## Waits in python selenium
1. These days most of the web apps are using AJAX techniques and angular. 
2. When a page is loaded by the browser, the elements within that page may load at different time intervals.
3. This makes locating elements difficult if an element is not yet present in the DOM, a locate function will raise an ElementNotVisibleException exception.
4. Using waits, we can solve this issue.

## Wait types:
    1. Implicitly Wait
    2. Explicity wait
# Implicitly wait
1. Implicitly wait is one of the way to request selenium not throw any exception until provided time.
2. Default wait time of the selenium is 500 milli-seconds.
3. Implicit wait tries to find the element in first go, if element is not present implicit wait tries to find the element after 500ms of first polling, if element is not available on second time also then implicit wait tries third time after 500 ms of second try and it goes on till the time reaches the given time.

# Explicity wait
1. The explicit wait is used to tell the Web Driver to wait for certain conditions or the maximum time limit before throwing an Exception .
2. We can reuse the WebdriverWait object once we create it.Explicit wait will be applicable for only one line, we have to use it with ExpectedConditions class.
3. WebDriverWait by default calls the ExpectedCondition every 500 milliseconds until it returns successfully.
