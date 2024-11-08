*** Settings *** 
Library    requests

*** Test Cases ***
Api test get AttributeName - response status code
    ${resp} =    requests.Get    url=http://127.0.0.1:8000/detail/AttributeName
    Should Be Equal    ${resp.status_code}    ${200}

Api test get AttributeName - response body
    ${resp} =    requests.Get    url=http://127.0.0.1:8000/detail/AttributeName/1
    ${resp_json} =    ${resp.json()}
    Should Be Equal    ${resp_json}    ${ATTRNAME1}

Api test post import - response status code
    ${resp} =    requests.Post    url=http://127.0.0.1:8000/import    json=${ATTRNAME1}
    Should Be Equal    ${resp.status_code}    ${200}

Api test post import - wrong data type
    ${resp} =    requests.Post    url=http://127.0.0.1:8000/import    data=sdadassda
    Should Be Equal    ${resp.status_code}    ${415}    