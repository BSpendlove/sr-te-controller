### SR-TE Controller

This is a fairly slow attempt in making some kind of python API that allows you to interact with the IGP (IS-IS/OSPF) network. The initial idea of this project is for the learning experience both for in-depth networking and developing my python skills.

Initial idea topology/container configuration:
![exabgp and API Example](/img/exabgp-sdn-controller-example.JPG)

Above is an example of the idea I had in my head when I first begun the project. The initial idea went something like this:

Use BGP-LS between a router/application running as a Docker container to pull in the information regarding the link-state protocol and other information such as SR labels/TE options. At first I was going to simply run IS-IS on FRR and poll the LSDB locally, build some local application that can run through all the LSPs and convert it to useful JSON data but then thought no, what about if we use BGP-LS? FRR/Quagga currently doesn't support BGP-LS (there is example code but hasn't been fully implemented) so Exabgp appeared after a few searches on the Internet.

Exabgp done a fair amount of work for me already because BGP Messages can be taken from the stdin as JSON and can either be used by a local python script attached to the exabgp process (or however that works...) or what I have currently opt'd to do is to constantly read the stdin and send it to a Flask API to centralize all the functions such as data processing, maintain the network topology (and potentially display via vis.js the segment adjacencies/labels and potentially perform basic traffic engineering for segment routing)

BGP-LS will scale/make it easier in the future if I ever want to actually start to implement multi-IGP domains and draw separate topologies/maintain separate IGP networks instead of having a local controller per IGP domain. We can use iBGP or eBGP with BGP-LS and potentially can even implement multiple controllers along with the ability to efficently parse/handle multiple BGP-LS neighbors within the same domain to multiple controllers for redundancy purposes but this isn't a product, it's a project so don't expect it to work if you pull it and try running it yourself!

Here is what I currently have in my brain as of 25/07/2020 to implement (not in order) to get a basic working 'SDN' controller for BGP-LS/Segment Routing TE:
- Firstly, how to handle the network topology information? If I want to support all the above (redundancy within local and remote IGP domains) then I need to do it correct from the start otherwise I'll end up having to rewrite the majority of the core code again and again and I'll lose motiviation. How do I identify per IGP area? When the neighborship comes up, I need to ensure is the network topology already built from this same IGP domain with a redundant neighbor? or is this a completely new neighbor/IGP domain that I need to begin to start implementing logic to create the "initial topology" and store this somewhere like a database. How do I ensure the database is in-sync with the current network state at the exact momement of performing a change? (such as a basic SR-TE instruction) but a link goes down as soon as a tunnel is configured...
- How do I encode/decode the JSON data I receive from the Exabgp API? Should I just dump the JSON into MongoDB or use Flask SQLAlchemy and OOP/Model based classes per address family? What if I want to also implement L3VPN/L2VPN topology?
- How do I ensure that when a neighbor goes down, the  topology is updated to reflect that? Should I completely delete the initial topology if no other neighbors exist for that IGP domain? or should I cache it for a few minutes in case it was just a BGP flap?
- Do I build it all based on event driven events (eg. when we receive a BGP neighbor update?, listen to all BGP updates for that specific neighbor and once we receive an EOR message, we build the initial topology?)
- Do I just build the OOP models manually and use something like PostgreSQL or MySQL?
- What happens if the container dies? I have a database with the initial topology but is that now considered invalid data and I should just manually rebuild the topology when the container comes back up and BGP neighborship state informs the API it's up again?

Implementation:
- Basic frontend GUI to display the network topology with information such as SR labels, BGP peer sessions, IGP domain map
- Database Modelling/structure
- Which database??? So far I don't like MongoDB or SQLite... I don't want to fall into bad habits and use SQLAlchemy for the OOP database models but it's so tempting, however it won't be scalable...? But it's just a little personal project right??!!
- Basic traffic engineering interaction, eg. Route X network over Tunnel with a,b,z labels
- Purely Python based (as much as I can) with BGP-LS (no use of PCE/PCEP
- Documentation... Exabgp has meh documentation, in future versions anything can just break and take ages to fix because eg. a change in config syntax...

The main part I want to work in is how to get the data nicely into the database and ensure the data is very easy to manipulate/use. and then I'll focus my efforts on how to maintain the network state (which should essentially let me write a very basic network topology GUI with vis.js with minimal effort)

![IS-IS SDN Controller Example](/img/isis-sdn-controller-example.JPG)

