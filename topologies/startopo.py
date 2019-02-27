from mininet.topo import Topo 
from mininet.net import Mininet 
from mininet.util import dumpNodeConnections 
from mininet.log import setLogLevel 
from mininet.node import RemoteController, OVSSwitch
from mininet.cli import CLI


#class for Star Topology
class StarTopo(Topo):
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

		#Adding switch
		s = self.addSwitch('s1')
		#Adding Links
		self.addLink(s,h1)
		self.addLink(s,h2)
		self.addLink(s,h3)
		self.addLink(s,h4)
		self.addLink(s,h5)
		self.addLink(s,h6)
		self.addLink(s,h7)
		self.addLink(s,h8)
		self.addLink(s,h9)
		self.addLink(s,h10)

def simpleTest():
	topo = StarTopo(n=10)
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


