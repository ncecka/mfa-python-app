import requests
from Constants import Constant
class ApplicationToken():
      appToken = None
      def get(self):
          return self.getToken() if self.appToken == None else self.appToken

      def getToken(self):
          url = '%s/applications/%s/tokens?password=%s' % (Constant.API_URL, Constant.APP_API_KEY, Constant.APP_PASSWORD)
          response = requests.get(url).json()['token']
          self.appToken = response
          return self.appToken

      def invalidate(self):
          self.appToken = None

appToken = ApplicationToken()