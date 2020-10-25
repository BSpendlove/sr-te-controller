### SR-TE Controller

This project is a slow attempt to craft a half-working open source SR-TE controller without using PCEP/PCE (because I'm lazy)... I would like to involve PCEP/PCE in the future but currently I have opt'd to use BGP labelled unicast to send engineered label stacks  to existing routes learned via neighbors that directly peer with the controller.

Initial idea topology/container configuration:
![exabgp and API Example](/img/exabgp-sdn-controller.JPG)

Above is an example of the idea I had in my head when I first begun the project. The initial idea went something like this:

Use BGP-LS between a router/application running as a Docker container to pull in the information regarding the link-state protocol and other information such as SR labels/TE options. At first I was going to simply run IS-IS on FRR and poll the LSDB locally, build some local application that can run through all the LSPs and convert it to useful JSON data but then thought no, what about if we use BGP-LS? FRR/Quagga currently doesn't support BGP-LS (there is example code but hasn't been fully implemented) so Exabgp appeared after a few searches on the Internet.

Exabgp done a fair amount of work for me already because BGP Messages can be taken from the stdin as JSON and can either be used by a local python script attached to the exabgp process (or however that works...) or what I have currently opt'd to do is to constantly read the stdin and send it to a Flask API to centralize all the functions such as data processing, maintain the network topology (and potentially display via vis.js the segment adjacencies/labels and potentially perform basic traffic engineering for segment routing)

BGP-LS will scale/make it easier in the future if I ever want to actually start to implement multi-IGP domains and draw separate topologies/maintain separate IGP networks instead of having a local controller per IGP domain. We can use iBGP or eBGP with BGP-LS and potentially can even implement multiple controllers along with the ability to efficently parse/handle multiple BGP-LS neighbors within the same domain to multiple controllers for redundancy purposes but this isn't a product, it's a project so don't expect it to work if you pull it and try running it yourself!

Implementation Rant:
- Firstly, this project is not considered production ready and I'm not entirely sure if it will get to that state within the next year. This is a journey to improve my Python abilities and also gives me a reason to study more BGP topics.
- The controller is typically tested with Cisco XR and Juniper vMX however versions may differ. I have had multiple problems with XR images not correctly implementing BGP-LS or accepting modified routes with a label stack larger than 2 labels.
- The GUI part of displaying the topology and giving the option to push a label stack doesn't work properly and is more focused towards me improving my front end design skills.
- If you just peer towards this controller, the API in most cases should be 100% functional and you'll have a working state of the link-state topology within the local SQLite database that is used.
- Everything is stored within a local database, this application doesn't record any useful data that couldn't easily be obtained by restarting the container or peering with a new neighbor. I have designed the API to update the database and remove/update any existing nodes/links/prefixes learned via BGP-LS.
- There is little documentation on this project until I get in the later state however I have tried to comment code when required and provided example dumps of data I am working with in the root directory of the project. (folder called "examples")
- Projects will require ENV files to be setup, please copy the respective "env-example" or "example-env" folder as "env" in the same directory and fill out the details which should be self-explanatory.

The main part I want to work in is how to get the data nicely into the database and ensure the data is very easy to manipulate/use. and then I'll focus my efforts on how to maintain the network state (which should essentially let me write a very basic network topology GUI with vis.js with minimal effort)

![IS-IS SDN Controller Example](/img/isis-sdn-controller-example.JPG)

### Flask Route diagram

![Frontend Views](/img/exabgp_flask_routes.JPG)
