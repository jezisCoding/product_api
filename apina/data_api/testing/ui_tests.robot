*** Settings ***
Library    Browser

*** Test Cases ***
Open google
    New Browser   browser=    headless=${False}
    New page     https://www.google.com
    Type Text    selector=<zisti selector na search input field>   txt=cute kittens
    Click      selector=button[name="btnK"]   # This is CSS selector
    Click      selector="Search"    # This is Text selector
    Wait For Elements State     selector=button >> "search"    state=visible
    Wait For Elements State     selector=h3 >> "Implicit selector strategy"

