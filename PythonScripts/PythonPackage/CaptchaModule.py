'''
Created on Mar 17, 2022

@author: Cristina
'''

from selenium import webdriver
#from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time

def solve():
    import sys
    from twocaptcha import TwoCaptcha
    result = None

    sitekey = '7dfYFy8oTNKqALueUX11sH9/f38AAAAAAAAAAVgvpSXNLDv7ntPSA8VL7O+Lx2YCODwXYhpBDqanP6TLMg3oyO0CkIFsIZoGiz0TAOB8KXtHfAresFmh1BTiEVskU5/3PWzuPUXYhSon0E6h+VVTZL/sBuWYCZ990wHM2Qu5MBf9AZ10mibr0R/Y18o4Y4HBJ5t29w5xvnFGeMSRey0pSieXYtdHpCL+K8qCYc2DTTxSuij+bZxZUifJEJKgRdXjaySYNqQ3xBgEIrxcQXcWENEZZCaScXIE+gDlYk4TMDg1ONrXD4drKZPJzCp1G8O9C6x1uQRnnZcPntd+7oAVdVbhHSST0UOkZ6VTZKu4KRz8JxqySA+e1uc0aQs='
    api_key = 'a15b0816291ec68a7e27e07efd855901'
    solver = TwoCaptcha(api_key)
    try:
        result = solver.recaptcha(
            sitekey=sitekey,
            url='https://portal.aws.amazon.com/billing/signup?refid=6b3c2524-1f32-42dc-881e-bada4380a9af&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation#/identityverification'
        )

    except Exception as e:
        sys.exit(e)

    return result

driver = webdriver.Chrome(executable_path='C:\\Users\\Cristina\\Downloads\\chromedriver_win32\\chromedriver_99.0.4844.51.exe')

#driver.get('https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=*all&awsf.Free%20Tier%20Categories=categories%23compute&trk=33ffcbe8-beac-4ead-b902-a91ced7f226f&sc_channel=ps&sc_campaign=acquisition&sc_medium=ACQ-P|PS-GO|Brand|Desktop|SU|Compute|Solution|EEM|EN|Text|EU&s_kwcid=AL!4422!3!495118606976!e!!g!!amazon%20cloud&ef_id=Cj0KCQiAybaRBhDtARIsAIEG3kmEDKgPp0YVVMsFG96FN-fNdsB-kK2jS-AktqhIkHvkBVrs47_iv7saApUTEALw_wcB:G:s&s_kwcid=AL!4422!3!495118606976!e!!g!!amazon%20cloud')


textarea = driver.find_element_by_id('g-recaptcha-response')
solution = solve()
code = solution['code']
driver.execute_script(f"var ele=arguments[0]; ele.innerHTML = '{code}';", textarea)
time.sleep(1) # waiting is mandatory
textarea = driver.find_element_by_xpath('//*[@id="login-btn"]/button').click()


if __name__ == '__main__':
    pass