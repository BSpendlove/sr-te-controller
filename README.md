### ISIS SDN Controller

This is a fairly slow attempt in making some kind of python API that allows you to interact with the IS-IS network. The initial idea of this project was something like this:


Have a container run exabgp and run BGP-LS AFI between the required routers in a network and the container, have a local flask API to query the exabgp API and display the IS-IS topology along with the ability to perform basic traffic engineering tasks (and even act as a simple dumb application for SR-TE instead of using PCEP)

or have a container run FRR and peer with an IS-IS router (inter-domain/inter-IGP view will be limited) and the FRR container may struggle if it needs to keep working hard to keep up with the readers IS-IS network. The reason is because FRR still doesn't have official support for BGP-LS

However, to make a start on this project... I've opted for the easier way (and lazy way) which does take out some of the excitement of the overall idea but I need to look into a more reliable way of obtaining BGP-LS information from exabgp. So currently, we're stuck with basic CLI scraping that only works with Cisco XR... The purpose of exabgp was to also eliminate the need to CLI scraping, so this basic application can be introduced into any network/vendor configuration that supports BGP-LS at a minimum. Currently, I've only found simple stdin/stdout python scripts to scrap the container for when exabgp reads a BGP UPDATE message but again, I'm lazy and just went with this manual way which will:

- Use Netmiko to SSH to a device
- Interact with the device based on Flask API calls such as pull all the IS-IS neighborship information, ISIS LSP basic database view, and the full-on detailed LSDB view which will be used at a later date to potentially display on the index of the app using vis.js...

I'm currently just using the TextFSM module to pull data along with some pre-made (and custom made) textFSM regex templates. This TextFSM should at least return somewhat, "structured" JSON data to make it easier to work with the returned data from an API call... Netmiko is slow and I'm hoping within the next few months to get the BGP-LS idea working at a minimum with a clean way to access the exabgp API.

The container side of this project won't be done until I get to a decent size of API calls so I currently just run this as a flask app in a python virtual environment... Here is a diagram of what I want to achieve in the following months:

![IS-IS SDN Controller Example](/img/isis-sdn-controller-example.JPG)