from mininet.topo import Topo 
from mininet.net import Mininet 
from mininet.util import dumpNodeConnections 
from mininet.log import setLogLevel , info
from mininet.cli import CLI
from mininet.node import RemoteController, OVSSwitch

#class for Ring Topology
def RingTopo():

    net = Mininet( topo=None, build=False )

    info( '*** Adding controller\n' )
    net.addController('c0', controller=RemoteController,ip="127.0.0.1",port=6633)
    h1 = net.addHost('h1', ip='10.0.2.1')
    h2 = net.addHost('h2', ip='10.0.2.2')
    h3 = net.addHost('h3', ip='10.0.2.3')
    h4 = net.addHost('h4', ip='10.0.2.4')
    h5 = net.addHost('h5', ip='10.0.2.5')
    h6 = net.addHost('h6', ip='10.0.2.6')
    h7 = net.addHost('h7', ip='10.0.2.7')
    h8 = net.addHost('h8', ip='10.0.2.8')
    h9 = net.addHost('h9', ip='10.0.2.9')
    h10 = net.addHost('h10', ip='10.0.2.10')

    

    info( '*** Adding switch\n' )
    s1 = net.addSwitch( 's1', cls=OVSSwitch )
    s2 = net.addSwitch( 's2', cls=OVSSwitch )
    s3 = net.addSwitch( 's3', cls=OVSSwitch )
    s4 = net.addSwitch( 's4', cls=OVSSwitch )
    s5 = net.addSwitch( 's5', cls=OVSSwitch )
    s6 = net.addSwitch( 's6', cls=OVSSwitch )
    s7 = net.addSwitch( 's7', cls=OVSSwitch )
    s8 = net.addSwitch( 's8', cls=OVSSwitch )
    s9 = net.addSwitch( 's9', cls=OVSSwitch )
    s10 = net.addSwitch( 's10', cls=OVSSwitch )

    info( '*** Creating links\n' )
    ## controller 
    net.addLink(h1,s1)
    net.addLink(h2,s2)
    net.addLink(h3,s3)
    net.addLink(h4,s4)
    net.addLink(h5,s5)
    net.addLink(h6,s6)
    net.addLink(h7,s7)
    net.addLink(h8,s8)
    net.addLink(h9,s9)
    net.addLink(h10,s10)

    # ## switches
    # s = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10]
    # for i in range (0, len(s)-1):
    #     net.addLink(s[i], s[i+1])



    net.addLink(s1, s2)
    net.addLink(s2, s3)
    net.addLink(s3, s4)
    net.addLink(s4, s5)
    net.addLink(s5, s6)
    net.addLink(s6, s7)
    net.addLink(s7, s8)
    net.addLink(s8, s9)
    net.addLink(s9, s10)
    net.addLink(s10, s1)


    # net.addLink(s[0], s[9])

    info( '*** Starting network\n')
    net.start()

    info('*** Set ip address to switch\n')
    s1.cmd('ifconfig switch1 10.0.1.1')
    s2.cmd('ifconfig switch2 10.0.1.1')
    s3.cmd('ifconfig switch3 10.0.1.1')
    s4.cmd('ifconfig switch4 10.0.1.1')
    s5.cmd('ifconfig switch5 10.0.1.1')
    s6.cmd('ifconfig switch6 10.0.1.1')
    s7.cmd('ifconfig switch7 10.0.1.1')
    s8.cmd('ifconfig switch8 10.0.1.1')
    s9.cmd('ifconfig switch9 10.0.1.1')
    s10.cmd('ifconfig switch10 10.0.1.1')

    info('*** Enable spanning tree\n')                    
    s1.cmd('ovs-vsctl set bridge switch1 stp-enable=true')
    s2.cmd('ovs-vsctl set bridge switch2 stp-enable=true')
    s3.cmd('ovs-vsctl set bridge switch3 stp-enable=true')
    s4.cmd('ovs-vsctl set bridge switch4 stp-enable=true')
    s5.cmd('ovs-vsctl set bridge switch5 stp-enable=true')
    s6.cmd('ovs-vsctl set bridge switch6 stp-enable=true')
    s7.cmd('ovs-vsctl set bridge switch7 stp-enable=true')
    s8.cmd('ovs-vsctl set bridge switch8 stp-enable=true')
    s9.cmd('ovs-vsctl set bridge switch9 stp-enable=true')
    s10.cmd('ovs-vsctl set bridge switch10 stp-enable=true')

    info( '*** Running CLI\n' )
    CLI( net )

    info( '*** Stopping network' )
    net.stop()



if __name__ == '__main__':
    setLogLevel('info')
    RingTopo()
