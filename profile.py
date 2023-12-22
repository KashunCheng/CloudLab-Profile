"""This is a trivial example of a gitrepo-based profile; The profile source code and other software, documentation, etc. are stored in in a publicly accessible GIT repository (say, github.com). When you instantiate this profile, the repository is cloned to all of the nodes in your experiment, to `/local/repository`.

This particular profile is a simple example of using a single raw PC. It can be instantiated on any cluster; the node will boot the default operating system, which is typically a recent version of Ubuntu.

Instructions:
Wait for the profile instance to start, then click on the node in the topology and choose the `shell` menu item.
"""

# Import the Portal object.
import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as pg

# Create a portal context.
pc = portal.Context()

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()

phystype = 'c6525-25g'
# Add a raw PC to the request.
router = request.RawPC("router")
clients = [
    request.RawPC("node0"),
    request.RawPC("node1")
]

router.hardware_type = phystype
clients[0].hardware_type = phystype
clients[1].hardware_type = phystype

router_node0 = request.Link()
router_node0.addInterface(router.addInterface("eth1"))
router_node0.addInterface(clients[0].addInterface("eth1"))
router_node1 = request.Link()
router_node1.addInterface(router.addInterface("eth2"))
router_node1.addInterface(clients[1].addInterface("eth2"))

# Print the RSpec to the enclosing page.
pc.printRequestRSpec(request)
