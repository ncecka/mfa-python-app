import requests
from Constants import Constant
class CompanyToken():
      companyToken = None
      def get(self):
          return self.getToken() if self.companyToken == None else self.companyToken

      def getToken(self):
          url = '%s/%s/tokens?companysecret=%s' % (Constant.API_URL, Constant.COMPANY_KEY, Constant.COMPANY_PASSWORD)
          response = requests.get(url).json()['token']
          self.companyToken = response
          return self.companyToken

      def invalidate(self):
          self.companyToken = None

companyToken = CompanyToken()