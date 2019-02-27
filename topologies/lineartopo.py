from mininet.topo import Topo 
from mininet.net import Mininet 
from mininet.util import dumpNodeConnections 
from mininet.log import setLogLevel 

#class for Linear Topology
class LinearTopo(Topo):
	def __init__(self,n=10, **opts):
		Topo.__init__(self, **opts)

		#Adding Hosts
		h1 = self.addHost('h1')
		h2 = self.addHost('h2')
		h3 = self.addHost('h3')
		h4 = self.addHost('h4')
		h5 = self.addHost('h5')
		h6 = self.addHost('h6')
		h7 = self.addHost('h7')
		h8 = self.addHost('h8')
		h9 = self.addHost('h9')
		h10 = self.addHost('h10')

		#Adding switches
		s1 = self.addSwitch('s1')
		s2 = self.addSwitch('s2')
		s3 = self.addSwitch('s3')
		s4 = self.addSwitch('s4')
		s5 = self.addSwitch('s5')
		s6 = self.addSwitch('s6')
		s7 = self.addSwitch('s7')
		s8 = self.addSwitch('s8')
		s9 = self.addSwitch('s9')
		s10 = self.addSwitch('s10')

		#Adding links
		self.addLink(h1,s1)
		self.addLink(h2,s2)
		self.addLink(h3,s3)
		self.addLink(h4,s4)
		self.addLink(h5,s5)
		self.addLink(h6,s6)
		self.addLink(h7,s7)
		self.addLink(h8,s8)
		self.addLink(h9,s9)
		self.addLink(h10,s10)

		self.addLink(s1,s2)
		self.addLink(s2,s3)
		self.addLink(s3,s4)
		self.addLink(s4,s5)
		self.addLink(s5,s6)
		self.addLink(s6,s7)
		self.addLink(s7,s8)
		self.addLink(s8,s9)
		self.addLink(s9,s10)

def simpleTest():
	topo = LinearTopo(n=10)
	net = Mininet(topo)
	net.start()
	print "Dumping host connections"    
	dumpNodeConnections(net.hosts)    
	print "Testing network connectivity"    
	net.pingAll()    
	net.stop()

if __name__ == '__main__':
	setLogLevel('info')
	simpleTest()
