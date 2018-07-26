from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

WEBSERVER_PORT = 8080
PUB_KEY_PATH = './pubkey'

# This function verifies the signature of the message
# https://gist.github.com/lkdocs/6519372
def verify_sign(public_key_loc, signature, data):
    '''
    Verifies with a public key from whom the data came that it was indeed
    signed by their private key
    param: public_key_loc Path to public key
    param: signature String signature to be verified
    return: Boolean. True if the signature is valid; False otherwise.
    '''
    from Crypto.PublicKey import RSA
    from Crypto.Signature import PKCS1_v1_5
    from Crypto.Hash import SHA224
    from base64 import b64decode
    pub_key = open(public_key_loc, "r").read()
    rsakey = RSA.importKey(pub_key)
    signer = PKCS1_v1_5.new(rsakey)
    digest = SHA224.new()
    # Assumes the data is base64 encoded to begin with
    digest.update(data)
    if signer.verify(digest, b64decode(signature)):
        return True
    return False

# This class will handles any incoming request sent to it, but we want to validate they come from Messagemedia
class secureWebHookHandler(BaseHTTPRequestHandler):

	#Handler for the GET requests
	def do_POST(self):

		self.send_response(200)
		self.send_header('Content-type','application/json')
		self.end_headers()

		signature = self.headers['X-Messagemedia-Signature']
		date = self.headers['Date']

		content_length = int(self.headers['Content-Length'])
		body = self.rfile.read(content_length)


		data = self.requestline + date + body
		print data


		sign = verify_sign(PUB_KEY_PATH, signature, data)
		print sign

		# Send a response
		self.wfile.write("{\"verified\":\""+str(sign)+"\"}")
		return

try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer(('', WEBSERVER_PORT), secureWebHookHandler)
	print 'Started WebSocket Server: ' , WEBSERVER_PORT

	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the WebSocket Web Server'
	server.socket.close()
