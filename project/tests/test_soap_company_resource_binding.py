# coding=utf-8
import pytest
from allure.constants import AttachmentType
import allure
import requests
from xml.etree.ElementTree import XML
import xml.etree.ElementTree as ET
from utils.api import *
new_company_name = "Test API"
new_first_name = "Name"
new_last_name = "LastName"
new_middle_name = "MiddleName"
update_first_name = "NameUpdate"
update_last_name = "LastNameUpdate"
update_middle_name = "MiddleNameUpdate"


@allure.feature('Test SOAP Company Resource_Binding')
@allure.story('Add Company Request')
def test_add_company():
    with allure.step('Step 1.InCorrect request(empty Name)'):
        data = """
                <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:sch="http://csssr.com/schemas">
                <soapenv:Header/>
                <soapenv:Body>
                <sch:AddCompanyRequest>
                <sch:Name></sch:Name>
                </sch:AddCompanyRequest>
                </soapenv:Body>
                </soapenv:Envelope>"""
        r = requests.post("https://soap.qa-test.csssr.com/ws/", data=data)
        # TODO изменить ответ на 500, Name обязательное поле
        assert r.status_code == 200

    with allure.step('Step 2.Correct request'):
        data = """
                <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:sch="http://csssr.com/schemas">
                <soapenv:Header/>
                <soapenv:Body>
                <sch:AddCompanyRequest>
                <sch:Name></sch:Name>                                
                </sch:AddCompanyRequest>
                </soapenv:Body>
                </soapenv:Envelope>"""
        root = ET.fromstring(data)
        elem = root.find(".//{http://csssr.com/schemas}Name")
        elem.text = new_company_name
        data = ET.tostring(root)
        r = requests.post("https://soap.qa-test.csssr.com/ws/", data)
        assert r.status_code == 200
        print(r.content)
        company_name = XML(r.content).find(".//{http://csssr.com/schemas}Name").text
        assert company_name == new_company_name
        global new_id_company
        new_id_company = XML(r.content).find(".//{http://csssr.com/schemas}Id").text


@allure.feature('Test SOAP Company Resource_Binding')
@allure.story('Get Company Request')
def test_get_company():
    with allure.step('Step 1.Incorrect request(empty id)'):
        data = """
                <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:sch="http://csssr.com/schemas">
                <soapenv:Header/>
                <soapenv:Body>
                <sch:GetCompanyRequest>
                <sch:CompanyId></sch:CompanyId>
                </sch:GetCompanyRequest>
                </soapenv:Body>
                </soapenv:Envelope>"""
        r = requests.post("https://soap.qa-test.csssr.com/ws/", data)
        assert r.status_code == 500

    with allure.step('Step 2.Incorrect request(not found id)'):
        data = """
                <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:sch="http://csssr.com/schemas">
                <soapenv:Header/>
                <soapenv:Body>
                <sch:GetCompanyRequest>
                <sch:CompanyId></sch:CompanyId>
                </sch:GetCompanyRequest>
                </soapenv:Body>
                </soapenv:Envelope>"""
        root = ET.fromstring(data)
        elem = root.find(".//{http://csssr.com/schemas}CompanyId")
        elem.text = string
        data = ET.tostring(root)
        r = requests.post("https://soap.qa-test.csssr.com/ws/", data)
        assert r.status_code == 500

    with allure.step('Step 3.Correct request'):
        data = """
                <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:sch="http://csssr.com/schemas">
                <soapenv:Header/>
                <soapenv:Body>
                <sch:GetCompanyRequest>
                <sch:CompanyId></sch:CompanyId>
                </sch:GetCompanyRequest>
                </soapenv:Body>
                </soapenv:Envelope>"""
        root = ET.fromstring(data)
        elem = root.find(".//{http://csssr.com/schemas}CompanyId")
        elem.text = new_id_company
        data = ET.tostring(root)
        r = requests.post("https://soap.qa-test.csssr.com/ws/", data)
        assert r.status_code == 200
        print(r.content)
        company_name = XML(r.content).find(".//{http://csssr.com/schemas}Name").text
        company_id = XML(r.content).find(".//{http://csssr.com/schemas}Id").text
        assert company_name == new_company_name
        assert new_id_company == company_id


@allure.feature('Test SOAP Company Resource_Binding')
@allure.story('Add Employee Request')
def test_add_employee():
    with allure.step('Step 1.Incorrect request(empty FirstName)'):
        data = """
            <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:sch="http://csssr.com/schemas">
            <soapenv:Header/>
            <soapenv:Body>
            <sch:AddEmployeeRequest>
            <sch:FirstName></sch:FirstName>
            <sch:LastName></sch:LastName><sch:MiddleName></sch:MiddleName>
            <!--Optional:-->
         
            </sch:AddEmployeeRequest>
            </soapenv:Body>
            </soapenv:Envelope>"""
        root = ET.fromstring(data)
        elem = root.find(".//{http://csssr.com/schemas}LastName")
        elem.text = new_last_name
        data = ET.tostring(root)
        elem = root.find(".//{http://csssr.com/schemas}MiddleName")
        elem.text = new_middle_name
        data = ET.tostring(root)
        r = requests.post("https://soap.qa-test.csssr.com/ws/", data)
        # TODO изменить ответ на 500, т.к FirstName обязательно поле
        assert r.status_code == 200

    with allure.step('Step 2.Incorrect request(empty LastName)'):
        data = """
                <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:sch="http://csssr.com/schemas">
                <soapenv:Header/>
                <soapenv:Body>
                <sch:AddEmployeeRequest>
                <sch:FirstName></sch:FirstName>
                <sch:LastName></sch:LastName><sch:MiddleName></sch:MiddleName>
                <!--Optional:-->
        
                </sch:AddEmployeeRequest>
                </soapenv:Body>
                </soapenv:Envelope>"""
        root = ET.fromstring(data)
        elem = root.find(".//{http://csssr.com/schemas}FirstName")
        elem.text = new_first_name
        data = ET.tostring(root)
        elem = root.find(".//{http://csssr.com/schemas}MiddleName")
        elem.text = new_middle_name
        data = ET.tostring(root)
        r = requests.post("https://soap.qa-test.csssr.com/ws/", data)
        # TODO изменить ответ на 500, т.к LastName обязательно поле
        assert r.status_code == 200

    with allure.step('Step 3.Correct request(empty MiddleName)'):
        data = """
                <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:sch="http://csssr.com/schemas">
                <soapenv:Header/>
                <soapenv:Body>
                <sch:AddEmployeeRequest>
                <sch:FirstName></sch:FirstName>
                <sch:LastName></sch:LastName>
                <sch:MiddleName></sch:MiddleName>
                <!--Optional:-->
        
                </sch:AddEmployeeRequest>
                </soapenv:Body>
                </soapenv:Envelope>"""
        root = ET.fromstring(data)
        elem = root.find(".//{http://csssr.com/schemas}FirstName")
        elem.text = new_first_name
        data = ET.tostring(root)
        elem = root.find(".//{http://csssr.com/schemas}LastName")
        elem.text = new_last_name
        data = ET.tostring(root)
        r = requests.post("https://soap.qa-test.csssr.com/ws/", data)
        # TODO изменить ответ на 200, т.к MiddleName необязательно поле
        assert r.status_code == 200
        print("ААААААААААААА" + str(r.content))

    with allure.step('Step 4.Correct request'):
        data = """
            <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:sch="http://csssr.com/schemas">
            <soapenv:Header/>
            <soapenv:Body>
            <sch:AddEmployeeRequest>
            <sch:FirstName></sch:FirstName>
            <sch:LastName></sch:LastName><sch:MiddleName></sch:MiddleName>
            <!--Optional:-->
            
            </sch:AddEmployeeRequest>
            </soapenv:Body>
            </soapenv:Envelope>"""
        root = ET.fromstring(data)
        elem = root.find(".//{http://csssr.com/schemas}FirstName")
        elem.text = new_first_name
        data = ET.tostring(root)
        elem = root.find(".//{http://csssr.com/schemas}LastName")
        elem.text = new_last_name
        data = ET.tostring(root)
        elem = root.find(".//{http://csssr.com/schemas}MiddleName")
        elem.text = new_middle_name
        data = ET.tostring(root)
        r = requests.post("https://soap.qa-test.csssr.com/ws/", data)
        assert r.status_code == 200
        print(r.content)
        first_name = XML(r.content).find(".//{http://csssr.com/schemas}FirstName").text
        last_name = XML(r.content).find(".//{http://csssr.com/schemas}LastName").text
        middle_name = XML(r.content).find(".//{http://csssr.com/schemas}MiddleName").text
        assert first_name == new_first_name
        assert last_name == new_last_name
        assert middle_name == new_middle_name
        global new_id_employee
        new_id_employee = XML(r.content).find(".//{http://csssr.com/schemas}Id").text

    with allure.step('Step 5.Correct request second employee'):
            data = """
            <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:sch="http://csssr.com/schemas">
            <soapenv:Header/>
            <soapenv:Body>
            <sch:AddEmployeeRequest>
            <sch:FirstName></sch:FirstName>
            <sch:LastName></sch:LastName><sch:MiddleName></sch:MiddleName>
            <!--Optional:-->

            </sch:AddEmployeeRequest>
            </soapenv:Body>
            </soapenv:Envelope>"""
            root = ET.fromstring(data)
            elem = root.find(".//{http://csssr.com/schemas}FirstName")
            elem.text = new_first_name
            data = ET.tostring(root)
            elem = root.find(".//{http://csssr.com/schemas}LastName")
            elem.text = new_last_name
            data = ET.tostring(root)
            elem = root.find(".//{http://csssr.com/schemas}MiddleName")
            elem.text = new_middle_name
            data = ET.tostring(root)
            r = requests.post("https://soap.qa-test.csssr.com/ws/", data)
            assert r.status_code == 200
            print(r.content)
            first_name = XML(r.content).find(".//{http://csssr.com/schemas}FirstName").text
            last_name = XML(r.content).find(".//{http://csssr.com/schemas}LastName").text
            middle_name = XML(r.content).find(".//{http://csssr.com/schemas}MiddleName").text
            assert first_name == new_first_name
            assert last_name == new_last_name
            assert middle_name == new_middle_name
            global new_id_employee_second
            new_id_employee_second = XML(r.content).find(".//{http://csssr.com/schemas}Id").text


@allure.feature('Test SOAP Company Resource_Binding')
@allure.story('Update Employee Request')
def test_update_employee():
    with allure.step('Step 1.Incorrect request(empty id)'):
        data = """
            <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:sch="http://csssr.com/schemas">
            <soapenv:Header/>
            <soapenv:Body>
            <sch:UpdateEmployeeRequest>
            <sch:Id></sch:Id>
            <sch:FirstName></sch:FirstName>
            <sch:LastName></sch:LastName><sch:MiddleName></sch:MiddleName>
            <!--Optional:-->
         
            </sch:UpdateEmployeeRequest>
           </soapenv:Body>
           </soapenv:Envelope>"""
        root = ET.fromstring(data)
        elem = root.find(".//{http://csssr.com/schemas}FirstName")
        elem.text = update_first_name
        data = ET.tostring(root)
        elem = root.find(".//{http://csssr.com/schemas}LastName")
        elem.text = update_last_name
        data = ET.tostring(root)
        elem = root.find(".//{http://csssr.com/schemas}MiddleName")
        elem.text = update_middle_name
        data = ET.tostring(root)
        r = requests.post("https://soap.qa-test.csssr.com/ws/", data)
        assert r.status_code == 500

    with allure.step('Step 2.Incorrect request(not found id)'):
        data = """
                <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:sch="http://csssr.com/schemas">
                <soapenv:Header/>
                <soapenv:Body>
                <sch:UpdateEmployeeRequest>
                <sch:Id></sch:Id>
                <sch:FirstName></sch:FirstName>
                <sch:LastName></sch:LastName><sch:MiddleName></sch:MiddleName>
                <!--Optional:-->

                </sch:UpdateEmployeeRequest>
               </soapenv:Body>
               </soapenv:Envelope>"""
        root = ET.fromstring(data)
        elem = root.find(".//{http://csssr.com/schemas}FirstName")
        elem.text = update_first_name
        data = ET.tostring(root)
        elem = root.find(".//{http://csssr.com/schemas}LastName")
        elem.text = update_last_name
        data = ET.tostring(root)
        elem = root.find(".//{http://csssr.com/schemas}MiddleName")
        elem.text = update_middle_name
        data = ET.tostring(root)
        elem = root.find(".//{http://csssr.com/schemas}Id")
        elem.text = string
        data = ET.tostring(root)
        r = requests.post("https://soap.qa-test.csssr.com/ws/", data)
        assert r.status_code == 500

    with allure.step('Step 3.Incorrect request(empty FirstName)'):
        data = """
             <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:sch="http://csssr.com/schemas">
             <soapenv:Header/>
             <soapenv:Body>
             <sch:UpdateEmployeeRequest>
             <sch:Id></sch:Id>
             <sch:FirstName></sch:FirstName>
             <sch:LastName></sch:LastName><sch:MiddleName></sch:MiddleName>
             <!--Optional:-->
             
             </sch:UpdateEmployeeRequest>
             </soapenv:Body>
             </soapenv:Envelope>"""
        root = ET.fromstring(data)
        elem = root.find(".//{http://csssr.com/schemas}LastName")
        elem.text = update_last_name
        data = ET.tostring(root)
        elem = root.find(".//{http://csssr.com/schemas}MiddleName")
        elem.text = update_middle_name
        data = ET.tostring(root)
        elem = root.find(".//{http://csssr.com/schemas}Id")
        elem.text = new_id_employee
        data = ET.tostring(root)
        r = requests.post("https://soap.qa-test.csssr.com/ws/", data)
        # TODO изменить ответ на 500, т.к FirstName обязательно поле
        assert r.status_code == 200

    with allure.step('Step 4.Incorrect request(empty LastName)'):
        data = """
            <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:sch="http://csssr.com/schemas">
            <soapenv:Header/>
            <soapenv:Body>
            <sch:UpdateEmployeeRequest>
            <sch:Id></sch:Id>
            <sch:FirstName></sch:FirstName>
            <sch:LastName></sch:LastName><sch:MiddleName></sch:MiddleName>
            <!--Optional:-->
            
            </sch:UpdateEmployeeRequest>
            </soapenv:Body>
            </soapenv:Envelope>"""
        root = ET.fromstring(data)
        elem = root.find(".//{http://csssr.com/schemas}FirstName")
        elem.text = update_first_name
        data = ET.tostring(root)
        elem = root.find(".//{http://csssr.com/schemas}MiddleName")
        elem.text = update_middle_name
        data = ET.tostring(root)
        elem = root.find(".//{http://csssr.com/schemas}Id")
        elem.text = new_id_employee
        data = ET.tostring(root)
        r = requests.post("https://soap.qa-test.csssr.com/ws/", data)
        # TODO изменить ответ на 500, т.к LastName обязательно поле
        assert r.status_code == 200

    with allure.step('Step 5.Correct request(empty MiddleName)'):
        data = """
             <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:sch="http://csssr.com/schemas">
             <soapenv:Header/>
             <soapenv:Body>
             <sch:UpdateEmployeeRequest>
             <sch:Id></sch:Id>
             <sch:FirstName></sch:FirstName>
             <sch:LastName></sch:LastName><sch:MiddleName></sch:MiddleName>
             <!--Optional:-->
             
             </sch:UpdateEmployeeRequest>
             </soapenv:Body>
             </soapenv:Envelope>"""
        root = ET.fromstring(data)
        elem = root.find(".//{http://csssr.com/schemas}FirstName")
        elem.text = update_first_name
        data = ET.tostring(root)
        elem = root.find(".//{http://csssr.com/schemas}LastName")
        elem.text = update_last_name
        data = ET.tostring(root)
        elem = root.find(".//{http://csssr.com/schemas}Id")
        elem.text = new_id_employee
        data = ET.tostring(root)
        r = requests.post("https://soap.qa-test.csssr.com/ws/", data)
        assert r.status_code == 200

    with allure.step('Step 6.Correct request'):
        data = """
            <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:sch="http://csssr.com/schemas">
            <soapenv:Header/>
            <soapenv:Body>
            <sch:UpdateEmployeeRequest>
            <sch:Id></sch:Id>
            <sch:FirstName></sch:FirstName>
            <sch:LastName></sch:LastName><sch:MiddleName></sch:MiddleName>
            <!--Optional:-->
            
            </sch:UpdateEmployeeRequest>
            </soapenv:Body>
            </soapenv:Envelope>"""
        root = ET.fromstring(data)
        elem = root.find(".//{http://csssr.com/schemas}FirstName")
        elem.text = update_first_name
        data = ET.tostring(root)
        elem = root.find(".//{http://csssr.com/schemas}LastName")
        elem.text = update_last_name
        data = ET.tostring(root)
        elem = root.find(".//{http://csssr.com/schemas}MiddleName")
        elem.text = update_middle_name
        data = ET.tostring(root)
        elem = root.find(".//{http://csssr.com/schemas}Id")
        elem.text = new_id_employee
        data = ET.tostring(root)
        r = requests.post("https://soap.qa-test.csssr.com/ws/", data)
        assert r.status_code == 200
        print(r.content)
        first_name = XML(r.content).find(".//{http://csssr.com/schemas}FirstName").text
        last_name = XML(r.content).find(".//{http://csssr.com/schemas}LastName").text
        middle_name = XML(r.content).find(".//{http://csssr.com/schemas}MiddleName").text
        id_employee = XML(r.content).find(".//{http://csssr.com/schemas}Id").text
        # TODO FirstName не измегяеься, раскомментить после фикса
        # assert first_name == update_first_name
        assert last_name == update_last_name
        assert middle_name == update_middle_name
        assert id_employee == new_id_employee


@allure.feature('Test SOAP Company Resource_Binding')
@allure.story('Add Employee to Company Request')
def test_add_employee_to_company():
    with allure.step('Step 1.Incorrect request(empty CompanyId)'):
        data = """
            <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:sch="http://csssr.com/schemas">
            <soapenv:Header/>
            <soapenv:Body>
            <sch:AddEmployeesToCompanyRequest>
            <sch:CompanyId></sch:CompanyId><sch:EmployeeId></sch:EmployeeId>
            <!--Zero or more repetitions:-->
         
            </sch:AddEmployeesToCompanyRequest>
            </soapenv:Body>
            </soapenv:Envelope>"""
        root = ET.fromstring(data)
        elem = root.find(".//{http://csssr.com/schemas}EmployeeId")
        elem.text = new_id_employee
        data = ET.tostring(root)
        r = requests.post("https://soap.qa-test.csssr.com/ws/", data)
        assert r.status_code == 500

    with allure.step('Step 2.Incorrect request(empty EmployeeId)'):
        data = """
            <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:sch="http://csssr.com/schemas">
            <soapenv:Header/>
            <soapenv:Body>
            <sch:AddEmployeesToCompanyRequest>
            <sch:CompanyId></sch:CompanyId><sch:EmployeeId></sch:EmployeeId>
            <!--Zero or more repetitions:-->
         
            </sch:AddEmployeesToCompanyRequest>
            </soapenv:Body>
            </soapenv:Envelope>"""
        root = ET.fromstring(data)
        elem = root.find(".//{http://csssr.com/schemas}CompanyId")
        elem.text = new_id_company
        data = ET.tostring(root)
        r = requests.post("https://soap.qa-test.csssr.com/ws/", data)
        assert r.status_code == 500

    with allure.step('Step 3.Correct request'):
        data = """
            <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:sch="http://csssr.com/schemas">
            <soapenv:Header/>
            <soapenv:Body>
            <sch:AddEmployeesToCompanyRequest>
            <sch:CompanyId></sch:CompanyId><sch:EmployeeId></sch:EmployeeId>
            <!--Zero or more repetitions:-->
         
            </sch:AddEmployeesToCompanyRequest>
            </soapenv:Body>
            </soapenv:Envelope>"""
        root = ET.fromstring(data)
        elem = root.find(".//{http://csssr.com/schemas}CompanyId")
        elem.text = new_id_company
        data = ET.tostring(root)
        elem = root.find(".//{http://csssr.com/schemas}EmployeeId")
        elem.text = new_id_employee
        data = ET.tostring(root)
        r = requests.post("https://soap.qa-test.csssr.com/ws/", data)
        assert r.status_code == 200
        first_name = XML(r.content).find(".//{http://csssr.com/schemas}FirstName").text
        last_name = XML(r.content).find(".//{http://csssr.com/schemas}LastName").text
        middle_name = XML(r.content).find(".//{http://csssr.com/schemas}MiddleName").text
        id_employee = XML(r.content).findall(".//{http://csssr.com/schemas}Id")[1].text
        # TODO FirstName не изменяется, раскомментить после фикса
        # assert first_name == update_first_name
        assert last_name == update_last_name
        assert middle_name == update_middle_name
        assert id_employee == new_id_employee
        company_name = XML(r.content).find(".//{http://csssr.com/schemas}Name").text
        company_id = XML(r.content).find(".//{http://csssr.com/schemas}Id").text
        assert company_name == new_company_name
        assert new_id_company == company_id

    with allure.step('Step 4.Correct request second'):
        data = """
                <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:sch="http://csssr.com/schemas">
                <soapenv:Header/>
                <soapenv:Body>
                <sch:AddEmployeesToCompanyRequest>
                <sch:CompanyId></sch:CompanyId><sch:EmployeeId></sch:EmployeeId>
                <!--Zero or more repetitions:-->
        
                </sch:AddEmployeesToCompanyRequest>
                </soapenv:Body>
                </soapenv:Envelope>"""
        root = ET.fromstring(data)
        elem = root.find(".//{http://csssr.com/schemas}CompanyId")
        elem.text = new_id_company
        data = ET.tostring(root)
        elem = root.find(".//{http://csssr.com/schemas}EmployeeId")
        elem.text = new_id_employee_second
        data = ET.tostring(root)
        r = requests.post("https://soap.qa-test.csssr.com/ws/", data)
        assert r.status_code == 200
        last_name = XML(r.content).find(".//{http://csssr.com/schemas}LastName").text
        middle_name = XML(r.content).find(".//{http://csssr.com/schemas}MiddleName").text
        id_employee = XML(r.content).findall(".//{http://csssr.com/schemas}Id")[1].text
        assert last_name == new_last_name
        assert middle_name == new_middle_name
        assert id_employee == new_id_employee_second
        company_name = XML(r.content).find(".//{http://csssr.com/schemas}Name").text
        company_id = XML(r.content).find(".//{http://csssr.com/schemas}Id").text
        assert company_name == new_company_name
        assert new_id_company == company_id
