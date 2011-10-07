from javax.swing import *

def hello(event):
	print "Hello. I'm an event."

def main():
	frame = JFrame("Hello Jython")
	button = JButton("Hello", actionPerformed = hello)
	frame.add(button)
	frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
	frame.setSize(300, 300)
	frame.show()

# This doesn't actually get called when running from the jar
# it is useful when calling jython in dev though ;)
if __name__ == "__main__":
	main()
