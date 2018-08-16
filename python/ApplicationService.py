import requests
from Constants import Constant
from flask_api import status
from ApplicationTokenUtil import ApplicationToken

class ApplicationService():
       appT = ApplicationToken()

       def login(self, username, otp):
           url = "%s/applications/%s/otpchecks?username=%s&otp=%s&token=%s" % (Constant.API_URL, Constant.APP_API_KEY, username, otp, self.appT.get())
           response = requests.get(url)
           if response.status_code == 'EXPIRED_TOKEN':
               self.appT.invalidate()
               appService.login(username,otp)
           else:
               response
           return response if response.status_code == 200 else response.json()

       def registration(self, username, id, otp):
           url = "%s/applications/%s/registerbyuser?username=%s&saaspassid=%s&otp=%s&token=%s" \
                    % (Constant.API_URL, Constant.APP_API_KEY, username, id, otp, self.appT.get())
           response = requests.get(url)
           if response.status_code == 'EXPIRED_TOKEN':
               self.appT.invalidate()
               self.registration(username, id, otp)
           else:
               response.json()
           return response.json()

       def registerAccountByAdmin(self, username, accountowner, isadaccount):
           url = "%s/applications/%s/registerbyadmin?username=%s&accountowner=%s&isadaccount=%s&token=%s" % (Constant.API_URL, Constant.APP_API_KEY, username, accountowner, isadaccount, self.appT.get())
           response = requests.get(url)
           if response.status_code == 'EXPIRED_TOKEN':
               self.appT.invalidate()
               self.registerAccountByAdmin(username, accountowner, isadaccount)
           else:
               response.json()
           return response.json()

       def unregister(self, username):
           url = "%s/applications/%s/unregister?username=%s&token=%s" % (Constant.API_URL, Constant.APP_API_KEY, username, self.appT.get())
           response = requests.get(url)
           if response.status_code == 'EXPIRED_TOKEN':
               self.appT.invalidate()
               self.unregister(username)
           else:
               response.json()
           return response.json()

       def getbarcodeimage(self, sessionId):
           type = "IL"
           BarcodeURL = "%s/applications/%s/barcodes?session=%s&token=%s&type=%s" % (Constant.API_URL, Constant.APP_API_KEY, sessionId, self.appT.get(), type)
           barcode_image = requests.get(BarcodeURL)
           response = barcode_image.json()['barcodeimage']
           if barcode_image.status_code == 'EXPIRED_TOKEN':
               self.appT.invalidate()
               self.trackerValidation(trackerid, username)
           else:
               response
           return response

       def trackerValidation(self, trackerid, username):
           url = "%s/applications/%s/trackers/%s?&token=%s&account=%s" % (Constant.API_URL, Constant.APP_API_KEY, trackerid, self.appT.get(), username)
           response = requests.get(url)
           if response.status_code == 'EXPIRED_TOKEN':
               self.appT.invalidate()
               self.trackerValidation(trackerid, username)
           else:
               response
           return response.status_code == 200

appService = ApplicationService()