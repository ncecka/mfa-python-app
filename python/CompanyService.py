import requests
from Constants import Constant
from CompanyTokenUtil import CompanyToken

class CompanyService():
       companyToken = CompanyToken()

       def addAccount(self, username, accountowner, grouplist):
           url = "%s/%s/addaccount?username=%s&accountowner=%s&grouplist=%s&token=%s" % (Constant.API_URL, Constant.COMPANY_KEY, username, accountowner, grouplist, self.companyToken.get())
           response = requests.get(url)
           if response.status_code == 'EXPIRED_TOKEN':
               self.companyToken.invalidate()
               self.addAccount(username, accountowner, grouplist)
           else:
               response.json()
           return response.json()

       def verifyAccount(self, username, accountowner, isadaccount):
           url = "%s/%s/verifyaccount?username=%s&accountowner=%s&isadaccount=%s&token=%s" % (Constant.API_URL, Constant.COMPANY_KEY, username, accountowner, isadaccount, self.companyToken.get())
           response = requests.get(url)
           if response.status_code == 'EXPIRED_TOKEN':
               self.companyToken.invalidate()
               self.verifyAccount(username, accountowner, isadaccount)
           else:
               response.json()
           return response.json()

       def removeAccount(self, username):
           url = "%s/%s/removeaccount?username=%s&token=%s" % (Constant.API_URL, Constant.COMPANY_KEY, username, self.companyToken.get())
           response = requests.get(url)
           if response.status_code == 'EXPIRED_TOKEN':
               self.companyToken.invalidate()
               self.removeAccount(username)
           else:
               response.json()
           return response.json()

companyService = CompanyService()