// create an array with nodes
//console.log(nodes)
console.log(topology_details)
/*
var all_nodes = [];
var all_links = [];

for(var i=0; i < nodes.nodes.length; i++) {
    var node_details = nodes.nodes[i];
    var node_data = {
        id: node_details.id,
        label: node_details["node_details"]["node_attributes"]["bgp-ls"]["local-te-router-ids"]
    };
    console.log(node_details);
    all_nodes.push(node_data);
    for(var x=0; x < nodes.nodes[i]["node_details"]["links"].length; x++)
    {
        var link_details = node_details.node_details.links[x];
        var link_data = {
            from: link_details.node_id,
            to: 1,
            label: link_details.link["interface-address"]["interface-address"]
        };
        console.log(link_details);
        all_links.push(link_data)
    }
}

console.log(all_nodes);
console.log(all_links);
*/
//var nodes = new vis.DataSet([
//  { id: 1, label: "Node 1" },
//  { id: 2, label: "Node 2" },
//  { id: 3, label: "Node 3" },
//  { id: 4, label: "Node 4" },
//  { id: 5, label: "Node 5" }
//]);


var display_nodes = new vis.DataSet(topology_details["nodes"]);
  
var edges = new vis.DataSet(topology_details["edges"])

// create a network
var container = document.getElementById("topology");
var data = {
  nodes: display_nodes,
  edges: edges
};

var options = {};
var network = new vis.Network(container, data, options);
