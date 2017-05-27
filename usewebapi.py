import webapp2
import simplejson as json
import urllib2

urla = "https://www.zipwise.com/webservices/distance.php?key=u5dzfpv55x6oi3ae&zip1="
urlb = "&zip2="
urlc = "&format=json"

class MainPage(webapp2.RequestHandler):

    def get(self):
        # Create the FORM
        self.response.write('<html><body><h1>Use API example to Find Great Circle Distance</h1>')
        self.response.write(""" <hr> <form method="post">
        Enter the first zip code:
        <input type="textarea" name="zip1"></input><br><br>
        Enter the second zip code:
        <input type="textarea" name="zip2"></input><br><br>
        (Note: Allowable ZIPs are US 5-digits only (do not include the space))
        <br><br>
        <input type="submit" name="Find Great Circle Distance"></input>
        </form>""")
        self.response.write('</body></html>')

    def post(self):
        # get what the user entered in the FORM
        symbol_entered = self.request.get('zip1')
        symbol_entered1 = self.request.get('zip2')

        # Prepare the url request
        url = urllib2.urlopen(urla + symbol_entered + urlb + symbol_entered1 + urlc)
        ld_json = json.loads(url.read())

        # get the reply contents from the Web Service Server 
        
        # Print out REPLY
        zip1 = ld_json['results']['zip1']
        zip2 = ld_json['results']['zip2']
        distance = ld_json['results']['distance']
        self.response.write('<html><body> ')
        self.response.write(' <b>Zip1 = </b>%s' % (zip1))
        self.response.write('<p> <b>Zip2 = </b>%s' % (zip2))
        self.response.write('<p> <b>Distance = </b>%s' % (distance))
        self.response.write('</body></html>')

application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True) 
