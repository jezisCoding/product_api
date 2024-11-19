*** Settings *** 
Library            requests
Library            OperatingSystem
Library            Process
Variables          variables.py
Suite Setup        Start Django Server
Suite Teardown     Stop Django Server


*** Variables ***
${HOSTNAME}    127.0.0.1
${PORT}        8000
${SERVER}      http://${HOSTNAME}:${PORT}/


*** Test Cases ***
Api test Post import - wrong data type
    ${resp} =    requests.Post    url=http://127.0.0.1:8000/import    data=sdadassda
    Should Be Equal    ${resp.status_code}    ${415}    

Api test Get AttributeName list - empty list
    ${resp} =    requests.Get    url=http://127.0.0.1:8000/detail/AttributeName
    Should Be Equal    ${resp.status_code}    ${200}

# get aj na list, nie len na konkretny zaznam
Api test Get AttributeName - record does not exist
    ${resp}    requests.Get    url=http://127.0.0.1:8000/detail/AttributeName/1
    Should Be Equal    ${resp.status_code}    ${404}

Api test Post import - valid import
    ${resp} =    requests.Post    url=http://127.0.0.1:8000/import    json=${ATTRNAME1}
    Should Be Equal    ${resp.status_code}    ${200}
    Should Be Equal    ${resp.json()}    ${ATTRNAME11} #REST API should return inserted data on successful Post

Api test Get AttributeName - valid get
    ${resp} =    requests.Get    url=http://127.0.0.1:8000/detail/AttributeName/1
    Should Be Equal    ${resp.status_code}    ${200}
    Should Be Equal    ${resp.json()}    ${ATTRNAME11}

Api test Get Attributename list - valid get
    ${resp} =    requests.Get    url=http://127.0.0.1:8000/detail/AttributeName
    Should Be Equal    ${resp.json()}    ${ATTRNAME11LIST}

*** Keywords ***
Start Django Server
    OperatingSystem.Remove File    apina/db.sqlite3
    ${out}    Run    venv/bin/python3 apina/manage.py migrate
    Log    ${out}
    ${process}    Process.Start Process    venv/bin/python3    apina/manage.py    runserver
    Set Suite Variable    $RUNSERVER    ${process}    # escaped variable name
    Sleep    3    # wait for server to startup

Stop Django Server
    ${process}    Get Variable Value    $RUNSERVER    # escaped variable name
    ${result}    Process.Terminate Process    ${process}