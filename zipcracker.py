import sys
import zipfile

def brute_force(length):
    length = int(length)
    your_list = 'abcdefghijklmnopqrstuvwxyz'
    complete_list = []
    for current in xrange(length):
        a = [i for i in your_list]
        for y in xrange(current):
            a = [x+i for i in your_list for x in a]
            print a
    complete_list = complete_list+a
    return complete_list
def main():
	"""
	Zipfile password cracker using a brute-force dictionary attack
	"""
        try:       
            zipfilename = sys.argv[1]#'/home/laquicka/Downloads/Black.Panther.DVDrip.avi/Black.Panther.DVDrip.avi.zip'
            password_length = sys.argv[2]
            if not zipfilename:
                print "File name not fount"
                return
        except IndexError as e:
            print "Pass file name and length of password"
            return
        
        zip_file = zipfile.ZipFile(zipfilename)
        passwords = brute_force(password_length)
	for password in passwords:
            try:
                print "Trying pass: %s" % password
                zip_file.extractall(pwd=password)
                print "==================================="
                print 'Password found: %s' % password
                print "=================================="
                return
            except Exception as e:
                pass

if __name__ == '__main__':
	main()
