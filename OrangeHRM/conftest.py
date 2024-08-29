#configuration file or we can say properties file


import pytest
from datetime import datetime
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
baseurl="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
Username="Admin"
Password="admin123"

@pytest.fixture(scope="class",autouse=True)
def browser_setup(request):
    chrome_options=Options()
    chrome_options.add_experimental_option("detach",True)
    # driver_path=ChromeDriverManager.install()
    # request.cls.driver=webdriver.Chrome(driver_path,options=chrome_options)
    serv_obj=Service(r"C:\Test_Drivers\chromedriver-win32\chromedriver-win32\chromedriver.exe")
    request.cls.driver=webdriver.Chrome(service=serv_obj,options=chrome_options)

#HTML REPORT AUTO GENERATE SETUP
# @pytest.hookimpl(tryfirst=True)
# def pytest_configure(config):
#     today=datetime.now()
#     report_dir=Path("hrmreports", today.strftime("%Y%m%d"))
#     report_dir.mkdir(parents=True, exist_ok=True)
#     pytest_html=report_dir / f"Report_{'%Y%m%d%h%m'}.html"
#     config.option.htmlpath= report_dir
#     config.option.self_contained_html= True

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    today = datetime.now()
    report_dir = Path("hrmreports", today.strftime("%Y%m%d"))
    report_dir.mkdir(parents=True, exist_ok=True)
    report_file = report_dir / f"Report_{today.strftime('%Y%m%d_%H%M')}.html"
    config.option.htmlpath = str(report_file)  # Convert Path to string
    config.option.self_contained_html = True

#TITILE FOR REPORT
def pytest_html_report_title(report):
    report.title="HRM TEST REPORT"
